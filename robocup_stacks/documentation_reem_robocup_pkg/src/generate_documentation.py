#! /usr/bin/env python
# -.- coding: utf-8 -.-
import roslib
roslib.load_manifest("documentation_reem_robocup_pkg")

import os
import rospkg
from rospkg import parse_manifest_file
import inspect
#from sys import stderr


class GenerateDocumentation():
    """ Generate the rst files for all packages listed on the manifest to be
    able to generate the documentation using (ros)make in this package. """
    def __init__(self):
        self.rospack = rospkg.RosPack()
        PACKAGE_NAME = rospkg.get_package_name(inspect.getfile(inspect.currentframe()))
        PACKAGE_PATH = self.rospack.get_path(PACKAGE_NAME)
        DOCUMENTATION_FOLDER = "pkg_documentation"
        self.DOCUMENTATION_PATH = os.path.join(PACKAGE_PATH, DOCUMENTATION_FOLDER)
        self.EXTENSION = '.rst'
        self.DOC = "_doc"
        self.CONFIG_FILENAME = "conf.py"
        self.MAIN_RST_FILE = os.path.join(self.DOCUMENTATION_PATH, 'pkg' + self.DOC + self.EXTENSION)
        self.CONFIG_FILE = os.path.join(PACKAGE_PATH, 'src', self.CONFIG_FILENAME)
        self.MAIN_CONF_FILE = os.path.join(PACKAGE_PATH , self.CONFIG_FILENAME )
        self.packages = parse_manifest_file(PACKAGE_PATH, "manifest.xml").depends

        self.PACKAGES_MAP = {}

    def extract_python_files(self):
        """ This is the first function that should be called.\
        Extract the python file's names from all packages listed on the manifest. """
        for pkg in self.packages:
            pkg = str(pkg)
            self.PACKAGES_MAP[pkg] = {"files": [], "dirs": {}}
            print "Extracting python files from package: " + pkg
            path = self.rospack.get_path(pkg)

            for dirpath, dirnames, filenames in os.walk(path):  # dirpath, dirnames, filenames
                dirpath = str(dirpath)
                for filename in filenames:
                    if filename.endswith(".py"):
                        self.PACKAGES_MAP[pkg]["files"].append(filename)
                        self.PACKAGES_MAP[pkg]["dirs"][dirpath] = True

    def create_rst_file(self, folder, pkg_name):
        """ Create the rst file for any package. On the generated rst file
        will be listed all python files from the package. """
        folder = str(folder)
        pkg_name = str(pkg_name)

#        try:
        fname = os.path.join(folder, pkg_name) + self.DOC + self.EXTENSION
        rst_file = open(fname, 'w')
        print "Creating rst file: " + pkg_name  + self.DOC + self.EXTENSION

        pkg_title = pkg_name.replace('_', ' ').title()
        pkg_title_doc = pkg_title  + " Documentation"

        content = (pkg_title_doc + '\n')
        content += (len(pkg_title_doc) * '=') + '\n\n'

        content += pkg_title + '\n'
        content += (len(pkg_title) * '-') + '\n\n'

        python_files = self.PACKAGES_MAP[pkg_name]["files"]
        for python_file in python_files:
            content += python_file + '\n'
            content += (len(python_file ) * '.') + '\n'
            content += '.. automodule::  ' + python_file.split('.py')[0] + '\n'
            content += '   :members:\n\n'

        rst_file.write(content)
        rst_file.close()
#        except Exception as e:
#            print >> stderr, e

    def create_package_folders(self):
        """ Create folders to the packages where the rst files will be located
        and call create_rst_file to generate the rst files. """
        packages_name = self.PACKAGES_MAP.keys()
        for pkg in packages_name:
            pkg = str(pkg)
            folder = os.path.join(self.DOCUMENTATION_PATH , pkg)
            if not os.path.exists(folder):
                os.mkdir(folder)

            self.create_rst_file(folder, pkg)

    def create_main_rst_file(self):
        """ Create the main rst file that will 'link' all packages. """
#        try:
        print "Creating main rst file: " + 'pkg' + self.DOC + self.EXTENSION
        rst_file = open(self.MAIN_RST_FILE, 'w')
        title = 'Packages Documentation'
        subtitle = 'Here you can find all the documentation that has to do with all the ROS packages that we' \
        ' have created in the last 2 years (~2011 - 2013).'

        content = title + '\n'
        content += (len(title) * '=') + '\n\n'

        content += subtitle + '\n\n'

        for pkg_name in self.PACKAGES_MAP.keys():
            pkg_title = pkg_name.replace('_', ' ').title()

            content += pkg_title + '\n'
            content += (len(pkg_title) * '-') + '\n'
            content += ':doc:`' + os.path.join(pkg_name, pkg_name + self.DOC) + '`\n\n'

        rst_file.write(content)
        rst_file.close()
#        except Exception as e:
#            print >> stderr, e

    def create_main_conf_file(self):
        """ Create the conf.py file adding to the sys.path all folders
        where the python files are located to generate the documentation. """
#        try:
        print "Creating main config file: " + self.CONFIG_FILENAME
        original_conf_content = open(self.CONFIG_FILE, 'r').read()

        new_conf_file = open(self.MAIN_CONF_FILE, 'w')
        content = original_conf_content + '\n'

        packages = self.PACKAGES_MAP.keys()
        for pkg in packages:
            for dir_path in self.PACKAGES_MAP[pkg]["dirs"]:
                content += 'sys.path.append(\'' + dir_path + '\')\n'

        new_conf_file.write(content)
        new_conf_file.close()
#        except Exception as e:
#            print >> stderr, e

    def execute(self):
        """ This is the only method the should be called at the main function. """
        self.extract_python_files()
        self.create_package_folders()
        self.create_main_rst_file()
        self.create_main_conf_file()

#    print PACKAGES_MAP

def main():

    generator = GenerateDocumentation()
    generator.execute()

if __name__ == "__main__":
    main()
DOCUMENTATION TUTORIAL
=======================


.. image:: Awake.png


Introduction
------------
In trunk you will find a directory called *documentation_reem_robocup*.
This directory is meant to house all the documentation REEM robocup@HOME project.

Installation of Sphinx
----------------------

I found two ways of doing it, choose the one that you prefer.

#. $sudo easy_install -U Sphinx
#. $sudo apt-get install python-sphinx


To test that it works correctly:

#. $mkdir whatever_name_dir
#. $cd whatever_name_dir
#. $sphinx-quickstart
#. $make html
#. $cd _build/html
#. Open index.html with your browser to see if you created your first Sphinx html.

Link to the webpages:
 
 `TUTORIAL WEB`_
 
 `ROS SPHINX`_

.. _ROS SPHINX: http://www.ros.org/wiki/Sphinx
.. _TUTORIAL WEB: http://matplotlib.org/sampledoc/getting_started.html#installing-your-doc-directory


Protocol to add your pkg documentation.
----------------------------------------
You can see two examples made with *execute.py in dancing_reem* and *math_utils.py in common/src/utils*.

1. In conf.py add --> *roslib.load_manifest('your_pkg_name')*


Note: Becarefull, because if the modules that you want to autodoc aren't in the src
directory, they won't be found. You will have to add it manually to the sys.path.

Example: To add the modules in common/utils I had to add this line to the conf.py:

*sys.path.insert(0, os.path.join(packages.get_pkg_dir('common'), 'src/utils'))*


2. Go to pkg_documentation dir. You have to
   
	I) Create here a directory with the name for example the 'your_pkg_name_dir'.
   
	
	II) Create inside, a document called 'your_pkg_name_doc.rst'.
   
	
	III) Go inside the pkg_doc.rst in pkg_documentation dir. In it add the following line:
	
	*:doc:`your_pkg_name_dir/your_pkg_name_doc`*
   
	This will add a link to the your_pkg_name_doc where you will then put the automodule system.
   
	
	IV) Go inside the your_pkg_name_doc.rst and add the following:
	
  
           *.. automodule:: name_of_module_you_want_to_create_autodoc 
   	   
	   :members:*

3. Once this is done, you just have to run a roscore ( apparently needs it to autodoc ROS-PKGs) 
and create the html in the documentation_reem_robocup directory with the command:

$make html

4. Then go to the directory _build/html and select the index.html. 

.. image:: reem_doc.jpg


Note: It will give warning that the .rst files that you added with :doc: are not included
in the tree. It just means that you didn't put it in the main index ( index.rst ) , which 
we don't want to do to maintain the html clean.


LINKS of INTEREST
-----------------

 `reST SINTAX Introduction`_
 
 `Sphinx First Steps`_
 
 `How AutoDocumentation works`_
 
 `How TOC tree works`_
 
 `Things to do with your rst files`_
 
 `How to avoid those nasty WARNINGS`_
 
 `How to show code examples`_

.. _reST SINTAX Introduction: http://sphinx-doc.org/rest.html
.. _Sphinx First Steps: http://sphinx-doc.org/tutorial.html
.. _How AutoDocumentation works: http://sphinx-doc.org/ext/autodoc.html
.. _How TOC tree works: http://sphinx-doc.org/markup/toctree.html 
.. _Things to do with your rst files: http://sphinx-doc.org/markup/inline.html
.. _How to avoid those nasty WARNINGS:  http://sphinx-doc.org/config.html#confval-exclude_patterns
.. _How to show code examples: http://sphinx-doc.org/markup/code.html

.. image:: PAL_robot_power.png

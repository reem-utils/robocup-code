#!/usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import sys
from pal_smach_utils.utils.colors import Colors

DEFAULT_FILENAME = './robocup_params_configuration.txt'
DISCLAIMER = '#File generated with the param_configurator script!'
POSSIBLE_PARAMS = ['names', 'rooms', 'pois', 'objects', 'objectfindingbehaviour', 'firelocations']
GRAMMARS = ['bring.gram', 'deliver.gram', 'room.gram', 'general.gram', 'iam.gram', 'cleanup.gram']
GRAMMARS = ['cleanup.gram']
COMPULSORY_LOCATIONS = ['drinks_location', 'exit', 'pre_exit', 'registration table', 'party_room', 'trash bin']
c = Colors()


def get_pkg_path(pkg_name):
    return roslib.packages.get_pkg_dir(pkg_name)
    #return os.popen('echo `rospack find %s`' % pkg_name).readline().strip()


coord_translator_path = get_pkg_path('coord_translator') + '/config'
grammar_path = '/mnt_flash/etc/interaction/sphinx/model/gram/en_GB/robocup'
grammar_path = '/home/gerard/Escriptori'


class ParameterConfigurator(object):
    '''
    Class that reads a parameter configurator file.
    It's created with a filename of the file. Then parse should be called.
    Then, the write method will overwrite all the files that're necessary.
    '''
    def __init__(self, filename, write_grammar):
        self.file = open(filename, 'r')
        self.names = set()  # List of names
        self.rooms = {}  # Dictionary of rooms
        self.objects = {}
        self.ofb = {}
        self.pois = {}
        self.firelocations = {}
        self.write_grammar = write_grammar
        self.loc_categories = {}
        self.obj_categories = {}
        self._line = 0
        self.any_poi_with_arm = False

    def normalize_option_line(self, line, delimiter=':'):
        return line.strip().split(delimiter)[0].lower()

    def parse(self):
        for line in self.file:
            self._line += 1
            option = self.normalize_option_line(line)  # Remove spaces, split at ':' and lowercase
            if (option == '') or (option[0] == '#'):  # It's a comment or newline, skip the line!
                continue
            elif option == 'names':
                self.parse_names()
            elif option == 'rooms':
                self.parse_pois(rooms=True)
            elif option == 'pois':
                self.parse_pois()
            elif option == 'objects':
                self.parse_objects()
            elif option == 'objectfindingbehaviour':
                self.parse_OFB()
            elif option == 'firelocations':
                self.parse_pois(fire=True)
            else:
                print "%sError in line %d: couldn't parse file because option \"%s\" was not recognized. Please, solve it and run the script again.\nNo file has been modified!%s" \
                      % (c.RED, self._line, line.strip(), c.NATIVE_COLOR)
                sys.exit(-1)
        locs = self.rooms.keys() + self.pois.keys()
        for c_loc in COMPULSORY_LOCATIONS:
            if not c_loc in locs:
                print '%sError: "%s" is a compulsory location and must be in the configuration file.\nAborting, no file has been modified!%s' \
                      % (c.RED, c_loc, c.NATIVE_COLOR)
                sys.exit(-1)
        self.file.close()

    def parse_names(self):
        print 'Reading "names" section...'
        for line in self.file:
            self._line += 1
            part = line.partition('#')  # Remove comments from line and then possible spaces
            if part[1] == '#' and part[0] == '':  # It's a comment, skip the line!
                continue
            name = part[0].strip().lower()
            if name == '':  # Blank line means we've read the whole section
                break
            self.names.add(name)

    def parse_pois(self, rooms=False, fire=False):
        print 'Reading "%s" section...' % ('rooms' if rooms else 'firelocations' if fire else 'pois')
        for line in self.file:
            self._line += 1
            lower_line = line.partition('#')
            if lower_line[1] == '#' and lower_line[0] == '':  # It's a comment, skip the line!
                continue
            lower_line = lower_line[0].strip().lower()  # Remove comments and trailing whitespaces
            if lower_line == '':  # We found the blank line, so we're at the end.
                break
            info = map(lambda x: x.strip(), lower_line.split(','))
            if info[0] in self.rooms or info[0] in self.pois:
                print '%sError in line %d: %s already defined in POIS or Rooms. Aborting!%s' % (c.RED, self._line, info[0], c.NATIVE_COLOR)
                sys.exit(-1)
            if rooms or fire:
                if len(info) != 4:
                    print '%sError in line %d: More or less information than necessary has been provided. Aborting!%s' % (c.RED, self._line, c.NATIVE_COLOR)
                    sys.exit(-1)
                for e in info[1:]:
                    try:
                        float(e)
                    except:
                        print '%sError in line %d: Unexpected type. Found "%s", expected something with a numeric type (for example float). Aborting!%s' % (c.RED, self._line, e, c.NATIVE_COLOR)
                        sys.exit(-1)
                if rooms:
                    self.rooms[info[0]] = info[1:]
                    try:
                        self.loc_categories['room'] += [info[0]]
                    except KeyError:
                        self.loc_categories['room'] = [info[0]]
                else:
                    self.firelocations[info[0]] = info[1:]
            else:
                if len(info) != 12 and len(info) != 5:  # 11 and 4 if no class is used 12 and 5 if class used
                    print '%sError in line %d: More or less information than necessary has been provided. Aborting!%s' % (c.RED, self._line, c.NATIVE_COLOR)
                    sys.exit(-1)
                for e in info[2:]:
                    try:
                        float(e)
                    except:
                        print '%sError in line %d: Unexpected type. Found "%s", expected something with a numeric type (for example float). Aborting!%s' % (c.RED, self._line, e, c.NATIVE_COLOR)
                        sys.exit(-1)
                self.pois[info[0]] = info[1:]
                try:
                    self.loc_categories[info[1]] += [info[0]]
                except KeyError:
                    self.loc_categories[info[1]] = [info[0]]

    def parse_objects(self):
        print 'Reading "objects" section...'
        for line in self.file:
            self._line += 1
            lower_line = line.partition('#')
            if lower_line[1] == '#' and lower_line[0] == '':  # It's a comment, skip the line!
                continue
            lower_line = lower_line[0].strip().lower()  # Remove comments and trailing whitespaces
            if lower_line == '':  # We found the blank line, so we're at the end.
                break
            info = map(lambda x: x.strip(), lower_line.split(','))
            if not info[2] in self.rooms and not info[2] in self.pois:
                print '%sError in line %d: Unexpected poi location. Found "%s", but it isn\'t in the rooms section nor in the pois section. Aborting!%s' % (c.RED, self._line, info[2], c.NATIVE_COLOR)
                sys.exit(-1)
            if len(info) != 4:
                print '%sError in line %d: More or less information than necessary has been provided. Aborting!%s' % (c.RED, self._line, c.NATIVE_COLOR)
                sys.exit(-1)
            self.objects[info[0]] = info[1:]
            try:
                self.obj_categories[info[1]] += [info[0]]
            except KeyError:
                self.obj_categories[info[1]] = [info[0]]

    def parse_OFB(self):
        print 'Reading "objectfindingbehaviour" section...'
        read_rooms = set()
        for line in self.file:
            self._line += 1
            lower_line = line.partition('#')
            if lower_line[1] == '#' and lower_line[0] == '':  # It's a comment, skip the line!
                continue
            lower_line = lower_line[0].strip().lower()  # Remove comments and trailing whitespaces
            if lower_line == '':  # We found the blank line, so we're at the end.
                break
            info = map(lambda x: x.strip(), lower_line.split(','))
            if len(info) != 6:
                print '%sError in line %d: More or less information than necessary has been provided. Aborting!%s' % (c.RED, self._line, c.NATIVE_COLOR)
                sys.exit(-1)
            if not info[0] in self.rooms:
                print '%sError in line %d: Unexpected room name. Found "%s" room name, but it isn\'t in the rooms section. Aborting!%s' % (c.RED, self._line, info[0], c.NATIVE_COLOR)
                sys.exit(-1)
            for e in info[2:]:
                try:
                    float(e)
                except:
                    print '%sError in line %d: Unexpected type. Found "%s", expected something with a numeric type (for example float). Aborting!%s' % (c.RED, self._line, e, c.NATIVE_COLOR)
                    sys.exit(-1)
            if info[0] in self.ofb:
                self.ofb[info[0]].append(info[1:])
            else:
                self.ofb[info[0]] = [info[1:]]
            read_rooms.add(info[0])
        for r in self.rooms.iterkeys():
            if not r in read_rooms:
                print '%sThe room "%s" has not been set in this section. Aborting!%s' % (c.RED, r, c.NATIVE_COLOR)
                sys.exit(-1)

    def write_files(self):
        print 'Writing configuration files...'
        self.mmap = open(coord_translator_path+'/'+'mmap.yaml', 'w')
        self.mmap.write(DISCLAIMER+'\n')
        self.obj_list = open(coord_translator_path+'/'+'objects_list.yaml', 'w')
        self.obj_list.write(DISCLAIMER+'\n')
        self.loc_prob = open(coord_translator_path+'/'+'locations_with_probabilities.yaml', 'w')
        self.loc_prob.write(DISCLAIMER+'\n')
        self.fire = open(coord_translator_path+'/'+'fire_locations.yaml', 'w')
        self.fire.write(DISCLAIMER+'\n')

        if len(self.objects):
            self.write_objects()
        if len(self.rooms) or len(self.pois):
            self.write_pois_and_rooms_fire()
        if len(self.ofb):
            self.write_loc_prob()

        self.mmap.close()
        self.obj_list.close()
        self.loc_prob.close()
        self.fire.close()
        if self.write_grammar:
            self.update_grammars()

    def write_pois_and_rooms_fire(self):
        submap = 'submap_0'
        self.mmap.write('poi:\n    '+submap+':\n')
        i = 1
        for (room_name, info) in self.rooms.iteritems():
            self.mmap.write('        poi_%d: ' % i)
            #values = [submap, room_name, 'room'] + map(lambda x: float(x), info)
            values = [submap, room_name] + info
            self.mmap.write(str(values).replace('\'', '')+'\n')
            i += 1
        for (poi_name, info) in self.pois.iteritems():
            self.mmap.write('        poi_%d: ' % i)
            #_class = info[0]
            #values = [submap, poi_name, _class] + map(lambda x: float(x), info[1:4]) with class in coord translator
            values = [submap, poi_name] + map(lambda x: float(x), info[1:4])  # With class but not in coord translator
            #values = [submap, poi_name] + map(lambda x: float(x), info[0:3]) without class
            self.mmap.write(str(values).replace('\'', '')+'\n')
            if len(info) > 9:
                if not self.any_poi_with_arm:
                    self.any_poi_with_arm = True
                    self.obj_list.write('#Syntax: object location name: list of (x,y,z),(x,y,z,w) move_arm object pose in base_link coord\nlocation_arm_poses:\n')
                #self.obj_list.write('    ' + poi_name + ': ' + str(info[3:]).replace('\'', '')+'\n')
                self.obj_list.write('    ' + poi_name + ': ' + str(info[4:]).replace('\'', '')+'\n')
            i += 1
        #fire
        if self.firelocations:
            self.fire.write('fire_locations:\n')
            for (i, (fire_name, info)) in enumerate(self.firelocations.iteritems()):
                self.fire.write('    poi_%d: ' % (i+1))
                values = [submap, fire_name] + info
                self.fire.write(str(values).replace('\'', '')+'\n')

    def write_objects(self):
        self.obj_list.write('# object name, object category, name of the location of the object, and the name of the location_arm_poses, databaseID\n')
        self.obj_list.write('objects_data:\n')
        for (i, (obj_name, info)) in enumerate(self.objects.iteritems()):
            self.obj_list.write('    object_%d: ' % (i+1))
            values = [obj_name.replace(' ', '_'), info[0], info[1], info[1], info[2]]
            self.obj_list.write(str(values).replace('\'', '')+'\n')
        self.obj_list.write('\n')

    def write_loc_prob(self):
        self.loc_prob.write('locations_prob: # Locations and its probabilities of having objects on top\n')
        self.loc_prob.write('    # Syntax: Name_of_room/location_in_room: [probabolity, pos.x, pos.y, angle]\n')
        for (room_name, info) in self.ofb.iteritems():
            self.loc_prob.write('    '+room_name.replace(' ', '_')+':\n')
            for i in info:
                self.loc_prob.write('        '+i[0]+': '+str(i[1:]).replace('\'', '')+'\n')

    def update_grammars(self):
        for g in GRAMMARS:
            print 'Updating grammar %s...' % g
            try:
                gram_file = open(grammar_path+'/'+g, 'r')  # We need to read the file
            except IOError:
                print '%sError: grammar file "%s" was not found in "%s". Aborting!%s' % (c.RED, g, grammar_path, c.NATIVE_COLOR)
                sys.exit(-1)
            grammar = gram_file.readlines()
            gram_file.close()
            gram_file = open(grammar_path+'/'+g, 'w')  # This ereases the file
            gram_name = g.split('.gram')[0]
            for line in grammar:
                first_word = line.split(' ')[0]
                if self.objects and (first_word in ['<objects>', '<item>']):
                    gram_file.write(first_word + ' = (')
                    objs = self.objects.keys()
                    gram_file.write(' | '.join(map(lambda p: ('('+str(p)+')') if ' ' in p else str(p), objs))+');\n')
                elif self.names and (first_word in ['<names>']):
                    _names = list(self.names)
                    gram_file.write(first_word + ' = (')
                    gram_file.write(' | '.join(map(lambda p: ('('+str(p)+')') if ' ' in p else str(p), _names))+');\n')
                elif (self.rooms or self.pois) and (first_word == '<location>'):  # FIXME pois and rooms are locations?
                    gram_file.write(first_word + ' = (')
                    locs = self.rooms.keys() + self.pois.keys()
                    gram_file.write(' | '.join(map(lambda p: ('('+str(p)+')') if ' ' in p else str(p), locs))+');\n')
                elif self.rooms and (first_word == '<room>'):
                    gram_file.write(first_word + ' = (')
                    rooms = self.rooms.keys()
                    gram_file.write(' | '.join(map(lambda p: ('('+str(p)+')') if ' ' in p else str(p), rooms))+');\n')
                elif (first_word.strip('<>') in self.obj_categories):
                    gram_file.write(first_word + ' = (')
                    vals = self.obj_categories[gram_name]
                    # gram_file.write(' | '.join(map(lambda p: ('('+str(p)+')') if ' ' in p else str(p), vals))+') {obj.put("object",$.$value);});\n')
                    gram_file.write(' | '.join(map(lambda p: ('('+str(p)+')') if ' ' in p else str(p), vals))+');\n')
                # elif (first_word == ('<%s>' % gram_name)) and (gram_name in self.loc_categories):
                #     gram_file.write(first_word + ' = ((')
                #     vals = self.loc_categories[gram_name]
                #     gram_file.write(' | '.join(map(lambda p: ('('+str(p)+')') if ' ' in p else str(p), vals))+') {obj.put("object",$.$value);});\n')
                else:
                    gram_file.write(line)
            gram_file.close()


def generate_skeleton(filename):
    f = open(filename, 'w')
    f.write('#Every section begins with SECTION_NAME:. Then the parameters, and an empty line to show the end of the section\n')
    f.write('Names: # Syntax: a name in every line\n\n')
    f.write('Rooms: # Syntax: room_name, x_coord, y_coord, angle\n\n')
    f.write('POIS:\n# Syntax: poi_name, poi_class, x_coord, y_coord, angle[,arm_pose_x, arm_pose_y, arm_pose_angle, arm_pose_rot_x, arm_pose_rot_y, arm_pose_rot_z, arm_pose_rot_w]. The arm poses are optional\n\n')
    #without class f.write('POIS:\n# Syntax: poi_name, x_coord, y_coord, angle[,arm_pose_x, arm_pose_y, arm_pose_angle, arm_pose_rot_x, arm_pose_rot_y, arm_pose_rot_z, arm_pose_rot_w]. The arm poses are optional\n\n')
    f.write('Objects: # Syntax: Object name, object class, object location name (it\'ll be a POI or Room name), database_id\n\n')
    f.write('ObjectFindingBehaviour: # Syntax: room_name, location_name, probability_of_objects, x_coord, y_coord, angle\n\n')
    f.write('FireLocations: # Syntax: fire_name, x_coord, y_coord, angle\n\n')


def print_usage():
    print 'Usage: %s [options]' % sys.argv[0]
    print 'Options:\n\th: show this message\n\tp filename: print a skeleton config file in filename\n\tfilename: configure everything using filename'
    print 'You can avoid the writing of the grammar by putting the "ng" option at the end (after the filename)'

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] == 'ng':
        print '%sNo config file set!! Using: %s%s' % (c.RED, DEFAULT_FILENAME, c.NATIVE_COLOR)
        filename = DEFAULT_FILENAME
    elif sys.argv[1] == 'h':
        print_usage()
        sys.exit(0)
    elif sys.argv[1] == 'p':
        if len(sys.argv) < 3:
            print '%sNo filename to save the skeleton set!%s' % (c.RED, c.NATIVE_COLOR)
            print_usage()
            sys.exit(-1)
        generate_skeleton(sys.argv[2])
        sys.exit(0)
    else:
        print 'Reading configuration file from: %s' % sys.argv[1]
        filename = sys.argv[1]
    write_grammar = False if sys.argv[-1] == 'ng' else True
    pc = ParameterConfigurator(filename, write_grammar)
    pc.parse()
    pc.write_files()
    print '%sEverything\'s finished correctly!%s\nRemember to stop and start the coord translator to reload the parameters!!%s' % (c.GREEN, c.YELLOW_BOLD, c.NATIVE_COLOR)
    sys.exit(0)

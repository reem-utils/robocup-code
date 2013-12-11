# -*- encoding: utf-8 -*-

import roslib; roslib.load_manifest('dancing_reem')
import os, os.path
from roslib import packages

# Word that identifies transition movements
TRANSITIONS_IDENTIFIER = "transition"

CURRENT_UPDATE_POS = 'middle'
PREV_CURRENT_UPDATE_POS = 'middle'

LINKING_STRING = '_'

PACKAGE_WHERE_TO_FIND_DANCING_MOVEMENTS = 'dancing_reem'
DANCING_DATABASE_DIR = 'dancing_movements_database'

DANCING_REEM_PKG = 'dancing_reem'
NAME_MOVEMENTS_LIBRARY_DIR = 'dancing_movements_database'


# FIXME, it seems taht this is obsolete now
def GetMovementDatabase():
    """
    It gets al the movements in the Database of tancing Reem and returns a dictionary with all the
    structure.
    """
    return None


def NameIsAStep(name):

    """
    This function returns true if the name given corresponds to a Step Name.
    False if it is a transition.
    The movement name format will be : name.xml
    The Steps will have any kind of name except starting with "transition".
    The transitions will have "transition_from_front_to_up.xml"
    """

    return not(name.startswith(TRANSITIONS_IDENTIFIER))


def NumberOfTransitions(database_dict, current_pos):

    """
    Gives the number os transitions in the current pos.
    Raises an assertion in case there are no transitions. This is because all
    the positions have to be linked by a minimum of ONE transition.
    """

    sub_database_list_transitions = filter(lambda x: x.startswith(TRANSITIONS_IDENTIFIER), database_dict.get(current_pos))
    assert (len(sub_database_list_transitions) != 0), "There are NO Transitions in this position. Its a DEAD END"
    return len(sub_database_list_transitions)


def UpdatePosition(movement_name, current_position):
    """
    Extracts from the movement name the position where it goes
    and from where it comes from. It can be a Step or a transition.
    If its a transition, the origin and destination are extracted from the name.
    If it is a Step, the position will be the same, therefore thats why we need
    as input the current position.
    The transitions will have "transition_from_name_of_pos_to_name_of_pos.xml" this structure.

    """
    print "THE MOVEMENT IS ===> " + str(movement_name)

    if NameIsAStep(movement_name):
        print "Movement is a STEP"
        print "NEW PREVIOUS POS == " + str(current_position)
        print "NEW CURRENT POS == " + str(current_position)
        return current_position, current_position
    else:
        print "Movement is a TRANSITION"
        # Now we now that the movement_name is from a transition.
        # We stripout the .xml extension from the name.
        mov_name_without_xml = movement_name.rsplit('.', 1)[0]
        # We make a list of all the words separated by '_'.
        movement_name_word_list = mov_name_without_xml.rsplit('_')
        print "MOVEMENT NAME WORD LIST == " + str(movement_name_word_list)
        # We obtain the index in the list where we first find the words 'from' and 'to'.
        from_index = movement_name_word_list.index('from')
        to_index = movement_name_word_list.index('to')
        # We then extract the info of the prev pos which is in between the 'from' and 'to' words.
        new_previous_pos = LINKING_STRING.join(movement_name_word_list[from_index + 1:to_index])
        # And we extract the destination pos that is after the 'to' word.
        new_current_pos = LINKING_STRING.join(movement_name_word_list[to_index + 1:])
        print "NEW PREVIOUS POS == " + str(new_previous_pos)
        print "NEW CURRENT POS == " + str(new_current_pos)
        return new_current_pos, new_previous_pos


def MoveNameToPath(movement_name, current_pos):

    """
    Given a movement name it returns the absolute path to that file.
    In Case it doesn't exist, it will raise an assertion.
    """

    base_package_path = packages.get_pkg_dir(PACKAGE_WHERE_TO_FIND_DANCING_MOVEMENTS)
    aux_database_dir_path = os.path.join(base_package_path, DANCING_DATABASE_DIR)
    aux_area_dir_path = os.path.join(aux_database_dir_path, current_pos)
    absolute_path_mov_name = os.path.join(aux_area_dir_path, movement_name)
    print str(absolute_path_mov_name)
    assert (os.path.exists(absolute_path_mov_name)), "The path to the movement file doesn't exist"
    return absolute_path_mov_name

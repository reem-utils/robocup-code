#! /usr/bin/env python
# -.- coding: utf-8 -.-
from roslib import packages
from rospy import logwarn
from pal_smach_utils.utils.colors import Colors
import yaml

CONFIG_FILE = packages.get_pkg_dir('cocktail_party') + '/config/cocktail_party.yaml'
CONFIG = yaml.load(open(CONFIG_FILE, 'r'))

ROBOT_GRAMMAR_PATH = "/mnt_flash/etc/interaction/sphinx/model/gram/en_US/"
LOCAL_GRAMMAR_PATH = packages.get_pkg_dir('cocktail_party') + "/config/"

colors = Colors()

class CocktailPartyVariables():
    """CocktailPartyVariables class.

    Use this class to get all variables required by the CocktailPartyStateMachine.
    """
    def __init__(self, print_variables=True):
        """Constructor for CocktailPartyVariables.

        @type print_variables: boolean
        @param print_variables: If is not False, 0 or None, all the variables of this class and its values will be printed.

        """
        self.print_variables = print_variables
        self.TOPICS = []
        self.SERVICES = []
        self.ACTIONS = []
        self.MAP_LOCATIONS = []
        self.__set_variables()
        self.__set_topics()
        self.__set_services()
        self.__set_actions()
        self.__set_map_locations()
        self.__print_variables()

    def __extract_from_gram(self, grammar_name, first_sep, second_sep):
        """ Extract from a grammar file the values between first_sep and second_sep separators
        First will try load the grammar files from the robot, if fails, will load from cocktail_party/config/
        @type grammar_name: string
        @param grammar_name: The grammar name, example: 'robocup/drinks'

        @type first_sep: string
        @param first_sep: The first separator where starts the names that you want extract, example: '<objects> ='

        @type second_sep: string
        @param second_sep: The second separator, is where ends the names to extract, example: ';'
        """

        ROBOT_GRAMMAR = ROBOT_GRAMMAR_PATH + str(grammar_name) + ".gram"
        LOCAL_GRAMMAR = LOCAL_GRAMMAR_PATH + str(grammar_name) + ".gram"

        try:
            FILE = open(ROBOT_GRAMMAR)
        except Exception as e:
            logwarn(colors.RED + '\n' + str(e) + colors.NATIVE_COLOR +
                colors.YELLOW + "\nLoading '%s'" % LOCAL_GRAMMAR + colors.NATIVE_COLOR)
            FILE = open(LOCAL_GRAMMAR)

        file_content = FILE.read()
        values = file_content.split(str(first_sep))[1]
        real_values = values.split(second_sep)[0]
        no_spaces = real_values.replace(" ", "")
        values_list = no_spaces.split('|')
        return values_list

    def __load_person_names(self):
        self.PERSONS_NAME = self.__extract_from_gram(CONFIG['people_grammar_name'], '<nameshort> =', ';')

    def __load_drink_names(self):
        """Drinks that REEM can recognize AND are allowed at the competition."""
        self.ALLOWED_DRINKS = self.__extract_from_gram( CONFIG['drinks_grammar_name'], '<objects> =', ';')

    def __set_variables(self):
        self.__load_drink_names()
        self.__load_person_names()

        self.DOOR_DISTANCE = CONFIG['door_distance']  # CocktailPartyStateMachine. meters
        #self.RECOGNIZE_CALLER_TIMEOUT = CONFIG['recognize_caller_timeout')  # seconds
        self.NUMBER_PERSONS = CONFIG['number_persons']  # TakeSeveralDrinkOrdersStateMachine, ServeOrdersStateMachine
        self.DRINKS_GRAMMAR_NAME = CONFIG['drinks_grammar_name']  # TakeSeveralDrinkOrdersStateMachine
        self.PEOPLE_GRAMMAR_NAME = CONFIG['people_grammar_name']
        self.TAKE_SINGLE_ORDER_TIMEOUT = CONFIG['take_single_order_timeout']  # TakeSeveralDrinkOrdersStateMachine. seconds
        self.ROTATE_LEFT = CONFIG['rotation_left']  # TakeSeveralDrinkOrdersStateMachine
        self.ALL_AT_A_TIME = CONFIG['all_at_a_time']  # CocktailPartyStateMachine
        self.SLEEP_MOVE_CALLER = CONFIG['sleep_move_caller']  # TakeSeveralDrinkOrdersStateMachine
        self.ASK_TO_COME = CONFIG['ask_to_come']

        #topics T_*
        self.T_USERSAID = CONFIG['topic_usersaid']
        self.T_RECOGNIZED_GESTURES = CONFIG['topic_recognized_gestures']

        #actions A_*
        self.A_MOVE_BASE = CONFIG['action_move_base']
        self.A_MOVE_BY = CONFIG['action_move_by']  # EnterRoomStateMachine
        self.A_SOUND = CONFIG['action_sound']
        self.A_FACE_RECOGNITION = CONFIG['action_face_recognition']  # LearnFaceStateMachine
        self.A_HEAD_CONTROLLER = CONFIG['action_head_controller']

        #services S_*

        #map_locations M_*
        self.M_ROOM_DRINKS = CONFIG['room_drinks']
        self.M_EXIT = CONFIG['exit']
        self.M_PARTY_ROOM = CONFIG['party_room']  # CocktailPartyStateMachine. Where the people are

    def __set_topics(self):
        for variable_name in self.__dict__.keys():
            if variable_name.startswith("T_"):
                self.TOPICS .insert(len(self.TOPICS), self.__dict__[variable_name])

    def __set_services(self):
        for variable_name in self.__dict__.keys():
            if variable_name.startswith("S_"):
                self.SERVICES.insert(len(self.SERVICES), self.__dict__[variable_name])

    def __set_actions(self):
        for variable_name in self.__dict__.keys():
            if variable_name.startswith("A_"):
                self.ACTIONS.insert(len(self.ACTIONS), self.__dict__[variable_name])

    def __set_map_locations(self):
        for variable_name in self.__dict__.keys():
            if variable_name.startswith("M_"):
                self.MAP_LOCATIONS.insert(len(self.MAP_LOCATIONS), self.__dict__[variable_name])

    def __print_variables(self):
        if not self.print_variables:
            return
        variables_name = self.__dict__.keys()
        variables_name.sort()
        _ = '- ' * 10
        print colors.BACKGROUND_GREEN + _ + " COCKTAIL_PARTY VARIABLES " + _ + colors.NATIVE_COLOR
        print
        for variable_name in variables_name:
            print colors.GREEN_BOLD + "%-25s" % variable_name + ": %s%s" % (colors.GREEN, self.__dict__[variable_name])
        print colors.NATIVE_COLOR


cocktail_party_variables  = CocktailPartyVariables(print_variables=True)

if __name__ == "__main__":
    print cocktail_party_variables
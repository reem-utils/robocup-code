#! /usr/bin/env python

import smach
import rospy
import socket
import os
import rostopic
import rosservice
import rosgraph.masterapi
from global_common import succeeded, aborted
from coord_translator.srv import LocationTranslator, ObjectTranslator, ObjectTranslatorRequest
from smach_ros import ServiceState
from subprocess import Popen, PIPE
from pal_smach_utils.utils.check_using_robot import CheckUsingRobot, ROBOTS_NAME, ROS_MASTER_URI, COMPUTERNAME
from pal_smach_utils.utils.run_command_local import RunCommandLocal
from pal_smach_utils.utils.run_command_on_robot import RunCommandOnRobot
from pal_smach_utils.utils.colors import Colors
from pal_control_msgs.msg import MotionManagerGoal, MotionManagerAction
from smach_ros import SimpleActionState
from roslib import packages

ROBOT_COMPUTER_NAME = ROS_MASTER_URI.split("http://")[1].split(":")[0]  # Assuming always http://$COMPUTER:11311
USERNAME = "root"  # SSH login robot
PASSWORD = "r"  # SSH password robot

TOPIC_LIST_NAMES = [  # Topics and Actions
                    ##################### Topics #####################
                    "/usersaid",
                    "/iri_people_tracking_rai/peopleSet",
                    "/nlp",  # sm_gpsr_apply.py
                    "/iri_moped_handler/outputOPL",  # recognize_objects.py
                    "/joint_states",  # search_objects_behaviour.py
                    "/blort_tracker/outputOPL",  # search_objects_behaviour.py
                    "/iri_door_detector/door_cloud/closed_door_marker",  # enter_door.py
                    "/followMe/result",  # go_to_exit_and_follow_checker.py
                    "/smoke_detector/smoke_percentage",
                    "/LMS1xx/LAS_00",  # enter_room.py
                    "/scan_filtered",  # enter_room.py
                    "/tf"]

SERVICES_LIST_NAMES = [  # #################### Services #####################
                    "/refresh_collision_map/refresh",  # arm_movement_to_object.py
                    "/refresh_collision_map_reset/refresh_reset",
                    "/object_translator",  # sm_give.py:
                    "/object_translator_dataBase",  # search_object_with_confidence_tabletop.py
                    "/iri_moped_handler/enable",  # search_object_with_confidence_moped.py
                    "/Peer_controller_configurator/orocos_controller_start",  # robot_controllers_activation.py
                    "/object_detection",  # detect_tabletop.py
                    "/get_next_probable_location",  # ofb_first_approach.py
                    "/alive_engine/stop",  # enter_room.py
                    "/disable_emergency_stop",  # enter_room.py
                    "/alive_engine/start",
                    "/lookupTransform",  # get_current_pos.py
                    "/pal_navigation_sm",  # navigation_state.py
                    "/loc_translator"]

ACTION_LIST_NAMES = [  # #################### Actions #####################
                    "/left_arm_controller/joint_trajectory_action",
                    "/right_arm_torso_controller/joint_trajectory_action",
                    "/iri_door_detector/door_detector_actions/find_a_door",
                    "/move_base",
                    "/move_by/move_base",
                    "/move_left_arm",
                    "/move_right_arm_torso",
                    "/move_by_unsafe/move_base",
                    "/skills/bow_detector/bow_object_detector/get_grasping_poin",  # pick_up_cloth_reem.py
                    "/motion_manager",
                    "/head_traj_controller/head_scan_snapshot_action",  # detect_tabletop.py
                    "/iri_door_detector/door_detector_action_server",
                    "/motion_manager'",  # speak_and_motion_action.py
                    "/face_recognition",
                    "/upper_body"]

COORD_TRANSLATOR_SERVICE = "/loc_translator"
OBJECT_TRANSLATOR_SERVICE = "/object_translator"
ARMS_ACTION_NAME = "/motion_manager"
MANDATORY_SERVICE_NAMES = ["/disable_emergency_stop"]
MANDATORY_ACTION_NAMES = [ARMS_ACTION_NAME]
MAP_LOCATIONS = ["exit", "kitchen"]


class UserdataHacked():
    def __init__(self):
        self.anything = "test"


class CheckDependencesState(smach.State):
    """CheckDependencesState.

    Use this state to check:
        If all actions and services that your State Machine need are running; if is some node publishing on a specifig topic that you need;
        if all locations that you need send the robot can be translated from coord_translator;

    Steps of this State:
        Add the ip of the local computer on the robot (/etc/hosts file)
        Synchonize the time between the local computer and the robot.
        Display a message warning if the robot is located.
        Check if mandatory services/actions/topics are running.
        Check specific topics required by your State Machine are being published.
        Check specifig services required by your State Machine.
        Check specifig actions required by your State Machine.
        Check if all the locations that you need were set on the map.
        Check if all objects that the robot should recognize (drinks, food, snacks) are at the database, asking the service /object_translator.
        #Send the robot arms to a position out of self colision.

    IMPORTANT:
        To use this State, you should include in your manifest the package 'coord_translator'

    This State Machine check if the topics, actions, services are running and if is possible translate locations in the map.
    """

    def __init__(self, topic_names=TOPIC_LIST_NAMES, service_names=SERVICES_LIST_NAMES, action_names=ACTION_LIST_NAMES, map_locations=MAP_LOCATIONS, object_names=None, input_keys=[], output_keys=[]):
        """Constructor for CheckDependencesState

        @type topic_names: list of strings
        @param topic_names: The topic names required by your State Machine.

        @type service_names: list of strings
        @param service_names: The service names required by your State Machine.

        @type action_names: list of strings
        @param action_names: The action names required by your State Machine.

        @type map_locations: list of strings
        @param map_locations: All the locations 'on map' that you need in your State Machine.

        @type object_names: list of strings
        @param object_names: All objects (drinks, foods, snacks) that the robot should recognize by your State Machine.

        """
        smach.State.__init__(self, input_keys=input_keys, output_keys=output_keys, outcomes=[succeeded, aborted])
        if(topic_names is not None and "list" not in str(type(topic_names))):
            raise ValueError("topic_names need be of type 'list' and the type is %s" % type(topic_names))
        if(service_names is not None and "list" not in str(type(service_names))):
            raise ValueError("service_names need be of type 'list' and the type is %s" % type(service_names))
        if(action_names is not None and "list" not in str(type(action_names))):
            raise ValueError("action_names need be of type 'list' and the type is %s" % type(action_names))
        if(map_locations is not None and "list" not in str(type(map_locations))):
            raise ValueError("map_locations need be of type 'list' and the type is %s" % type(map_locations))
        if (object_names) is not None and "list" not in str(type(object_names)):
            raise ValueError("object_names need be of type 'list' and the type is %s" % type(object_names))

        self.mandatory_service_names = MANDATORY_SERVICE_NAMES
        self.mandatory_action_names = MANDATORY_ACTION_NAMES
        self.topic_names = topic_names
        self.service_names = service_names
        self.action_names = action_names
        self.map_locations = map_locations
        self.object_names = object_names
        self.rostopic = rosgraph.masterapi.Master('/rostopic')
        self.coordinates = None  # Coordinates 'of kitchen for example', in the map.
        self.object_id = None  # Id of the objects 'coke for example' at the database.
        self.ALL_OK = True
        self.colors = Colors()
        self.MY_IPS = self.__get_my_ips()
        self.using_the_robot = CheckUsingRobot(print_checking=False).execute(UserdataHacked()) == succeeded

    def _print_title(self, title):
        l = len(title)
        title += " " if l % 2 else ""
        for i in range((60 - l) / 2):
            title = "-" + title + "-"
        rospy.loginfo(self.colors.BACKGROUND_GREEN + "%s%s" % (title, self.colors.NATIVE_COLOR))

    def _print_info(self, text):
        rospy.loginfo(self.colors.GREEN_BOLD + text + self.colors.NATIVE_COLOR)

    def _print_warning(self, text):
        rospy.logwarn(self.colors.YELLOW_BOLD + text + self.colors.NATIVE_COLOR)

    def _print_fatal(self, text):
        rospy.logfatal(self.colors.RED_BOLD + text + self.colors.NATIVE_COLOR)

    def __check_service(self, service_name):
        if rosservice.get_service_type(service_name):  # None
            self._print_info("Checking service '%s': OK" % service_name)
            return succeeded
        else:
            self.ALL_OK = False
            self._print_fatal("Checking service '%s': Failed" % service_name)
            return aborted

    def __check_topic(self, topic_name):
        topic_type, real_topic, msg_eval = rostopic.get_topic_type(topic_name)  # (None, None, None)
        if real_topic:
            self._print_info("Checking topic '%s': OK" % topic_name)
        else:
            self.ALL_OK = False
            self._print_fatal("Checking topic '%s': FAILED" % topic_name)

    def __check_action(self, action_name):
        publishers, sub, serv = rosgraph.masterapi.Master("/").getSystemState()
        for publisher in publishers:
            if publisher[0].startswith(action_name) and publisher[0].endswith("status"):
                self._print_info("Checking action '%s': OK" % action_name)
                return succeeded

        self.ALL_OK = False
        self._print_fatal("Checking action '%s': Failed" % action_name)
        return aborted

    def check_mandatory(self):
        self._print_title("CHECKING MANDATORY SERVICES/ACTIONS")

        if self.using_the_robot:
            for service in self.mandatory_service_names:
                self.__check_service(service)

            for action in self.mandatory_action_names:
                self.__check_action(action)
        else:
            self._print_warning("Not checking. ROS_MASTER_URI nor COMPUTER_NAME contains %s" % ROBOTS_NAME)

    def check_specific_topics(self):
        self._print_title("CHECKING SPECIFIC TOPICS")
        if self.topic_names:
            for topic in self.topic_names:
                self.__check_topic(topic)
        else:
            self._print_warning("Not checking. 'topic_names' is empty")

    def check_specific_services(self):
        self._print_title("CHECKING SPECIFIC SERVICES")
        if self.service_names:
            for service in self.service_names:
                self.__check_service(service)
        else:
            self._print_warning("Not checking. 'service_names' is empty")

    def check_specific_actions(self):
        self._print_title("CHECKING SPECIFIC ACTIONS")

        if self.action_names:
            for action in self.action_names:
                self.__check_action(action)
        else:
            self._print_warning("Not checking. 'action_names' is empty")

    def loc_response_cb(self, userdata, response):
        self.coordinates = None
        if response.exists:
            self.coordinates = response.coordinates
            return succeeded
        return aborted

    def check_map_locations(self):
        rospy.set_param("coord_translator_print_info", False)

        self._print_title("CHECKING MAP LOCATIONS")

        if not self.map_locations:
            self._print_warning("Not checking. 'map_locations' is empty")

        elif self.__check_service(COORD_TRANSLATOR_SERVICE) == succeeded:
            loc_translator_result = ServiceState(COORD_TRANSLATOR_SERVICE, LocationTranslator, response_cb=self.loc_response_cb, request_key='room_name')
            userdata_hacked = {}
            for place in self.map_locations:
                userdata_hacked["room_name"] = place
                if loc_translator_result.execute(userdata_hacked) == succeeded:
                    self._print_info("Translating '%s': OK (%.2f, %.2f, %.2f)" % (str(place), self.coordinates.x, self.coordinates.y, self.coordinates.z))
                else:
                    self.ALL_OK = False
                    self._print_fatal("Translating '%s': FAILED" % str(place))

        rospy.set_param("coord_translator_print_info", True)

    @smach.cb_interface(input_keys=["obj_name"])
    def obj_request_cb(self, obj_name):
        req = ObjectTranslatorRequest()
        req.objname = obj_name
        return req

    def obj_response_cb(self, userdata, response):
        if response.exists:
            if response.databaseID != 0:
                self.object_id = response.databaseID
                return succeeded
        return aborted

    def check_objects_id(self):
        rospy.set_param("coord_translator_print_info", False)

        self._print_title("CHECKING OBJECTS ID")

        if not self.object_names:
            self._print_warning("Not checking. 'object_names' is empty")

        elif self.__check_service(OBJECT_TRANSLATOR_SERVICE) == succeeded:
            obj_translator_result = ServiceState(OBJECT_TRANSLATOR_SERVICE, ObjectTranslator, request_cb=self.obj_request_cb, response_cb=self.obj_response_cb, request_key='obj_name')
            userdata_hacked = {}
            for obj_name in self.object_names:
                userdata_hacked["obj_name"] = obj_name
                if obj_translator_result.execute(userdata_hacked) == succeeded:
                    self._print_info("Translating '%s': OK (ID = %s)" % (obj_name, self.object_id))
                else:
                    self.ALL_OK = False
                    self._print_fatal("Translating '%s': FAILED (ID NOT IN '%s')" % (obj_name, OBJECT_TRANSLATOR_SERVICE))

        rospy.set_param("coord_translator_print_info", True)

    def robot_localize_warning(self):
        self._print_title("WARNING LOCALIZE ROBOT")

        if self.using_the_robot:
            path = os.path.dirname(os.path.realpath(__file__))
            command = "java -classpath %s Alert \"Is the robot located? Don't forget this step.\"" % path
            os.system(command)

            rospy.loginfo(self.colors.YELLOW_BOLD + "Is the robot located? Don't forget this step!" + self.colors.NATIVE_COLOR)
        else:
            self._print_warning("Not checking. ROS_MASTER_URI nor COMPUTER_NAME contains %s" % ROBOTS_NAME)

    def __get_my_ips(self):
        proccess = Popen("ifconfig | grep addr: | cut -d':' -f2 | cut -d' ' -f1", shell=True, stdout=PIPE, stderr=PIPE)
        out, err = proccess.communicate()
        ips = []
        for ip in out.split("\n"):
            if len(ip):
                ips.insert(len(ip), ip)
        return ips

    def add_local_dns_to_robot(self):
        self._print_title("ADDING LOCAL DNS TO ROBOT")
        rospy.loginfo("IPS FOUND:   " + str(self.MY_IPS))

        if not self.using_the_robot:
            self._print_warning("Not checking. ROS_MASTER_URI no contains " + str(ROBOTS_NAME))
            return succeeded

        for robot_name in ROBOTS_NAME:
            if robot_name in ROS_MASTER_URI.lower():

                robot_ip = socket.gethostbyname(ROBOT_COMPUTER_NAME)
                command = "ip route get %s" % str(robot_ip)
                out, err = Popen(command, shell=True, stdout=PIPE, stderr=PIPE).communicate()

                route_to_robot = out.split("\n")[0]
                my_ip = route_to_robot.split(" ")[len(route_to_robot.split(" ")) - 2]
                rospy.loginfo("SELECTED IP: %s" % my_ip)

                command = "addLocalDns -u %s -i %s " % (COMPUTERNAME, my_ip)
                status = RunCommandOnRobot(command).execute(UserdataHacked())

                if status == succeeded:
                    self._print_info("Successfully added {%s, %s}" % (COMPUTERNAME, my_ip))
                else:
                    self.ALL_OK = False
                    self._print_fatal("Failed adding {%s, %s}." % (COMPUTERNAME, my_ip))
                return status

#        self.ALL_OK = False
        self._print_warning("Not added. Running on the robot.")

    def synchronize_time(self):
        self._print_title("SYNCHRONIZING TIME")

        if not self.using_the_robot:
            self._print_warning("Not synchronizing. ROS_MASTER_URI no contains %s " % ROBOTS_NAME)
            return succeeded

        for robot_name in ROBOTS_NAME:
            if robot_name in ROS_MASTER_URI.lower():
                command = "ntpdate -u " + str(ROBOT_COMPUTER_NAME)
                if RunCommandLocal(command=command, sudo_enabled=True).execute(UserdataHacked()) == succeeded:
                    self._print_info("Synchronizing time: OK")
                else:
                    self.ALL_OK = False
                    self._print_fatal("Synchronizing time: FAILED")
                break

    def arms_out_of_self_colision(self):
        self._print_title("ARMS OUT OF SELF COLISION")

        if self.using_the_robot:
            if self.__check_action(ARMS_ACTION_NAME) == aborted:
                return aborted
        else:
            self._print_warning("Not checking. ROS_MASTER_URI nor COMPUTER_NAME contains %s" % ROBOTS_NAME)
            return aborted

        robot = os.environ.get('PAL_ROBOT')
        ros_master_uri = os.environ.get('ROS_MASTER_URI')
        remotelly_executing = ros_master_uri.rfind('localhost')
        rospy.loginfo('remotelly_executing: %s' % remotelly_executing)  # FIXME: Remove this line after test in the robot
        MOTION_FOLDER_PATH = ''
        plan = False
        checkSafety = False
        if robot == 'rh2c' or robot == 'rh2m' or robot == 'reemh3c' or robot == 'reemh3m' or robot == 'reemh3' or remotelly_executing == -1:
            check_for_door = True  # FIXME: This variable is not being used.
            MOTION_FOLDER_PATH = "/mnt_flash/stacks/reem_alive/alive_engine/config/database/Stopped/interact_1.xml"
        if remotelly_executing == -1:
            MOTION_FOLDER_PATH = packages.get_pkg_dir('pal_smach_utils') + '/config/interact_1.xml'
            plan = True
            checkSafety = False

        motion_goal = MotionManagerGoal()
        motion_goal.plan = plan
        motion_goal.filename = MOTION_FOLDER_PATH
        motion_goal.checkSafety = checkSafety
        motion_goal.repeat = False

        motion_manager_action = SimpleActionState(ARMS_ACTION_NAME, MotionManagerAction, goal=motion_goal)
        userdata_hacked = {}
        status = motion_manager_action.execute(userdata_hacked)

        if status == succeeded:
            rospy.loginfo(self.colors.GREEN_BOLD + "Arms out of self colisin: OK " + self.colors.NATIVE_COLOR)
        else:
            self.ALL_OK = False
            rospy.loginfo(self.colors.RED_BOLD + "Arms out of self colisin: Failed " + self.colors.NATIVE_COLOR)

    def execute(self, userdata):
        self.add_local_dns_to_robot()
        self.synchronize_time()
        self.robot_localize_warning()
        self.check_mandatory()
        self.check_specific_topics()
        self.check_specific_services()
        self.check_specific_actions()
        self.check_map_locations()
        self.check_objects_id()
        #self.arms_out_of_self_colision()

        return succeeded if self.ALL_OK else aborted

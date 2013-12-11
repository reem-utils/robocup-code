import roslib
import rospy
import smach
import smach_ros
import actionlib
from smach_ros import SimpleActionState, ServiceState

from pal_smach_utils.utils.global_common import *
from pal_smach_utils.utils.topic_reader import *
from pal_smach_utils.navigation.move_action import MoveActionState

try:
    from pr_msgs.msg import ObjectPoseList, ObjectPose
    from pr_msgs.srv import *
    from iri_moped_handler.srv import *
except ImportError:
    from object_recognition_mock.msg import ObjectPoseList, ObjectPose
    from object_recognition_mock.srv import *

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

""" ----------------------------------------------------------------------------
authors:

siegfried gevatter
sam pfeiffer
marti morta

11.5.2012


ALGORITHM:

SearchObjectsStateMachine
  for p in places of interest
    MoveBase(p)
    SearchObjectsInPlaceStateMachine
      for a in angles to look at
        ScanForObjectStateMachine (enable,look for objects,disable)
        Rotate(angle)

STRUCTURE:
        
1. ScanForObjectStateMachine
2. SearchObjectsInPlaceStateMachine
3. SearchObjectsStateMachine
        
---------------------------------------------------------------------------- """


""" ///////////////////////////////////////////////////////////////////////////

        SCAN FOR OBJECT SM

        - enables object recognition
        - looks for object
        - disables object recognition

/////////////////////////////////////////////////////////////////////////// """

class ScanForObjectStateMachine(smach.StateMachine):

    def __init__(self):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
        output_keys=['object_data'])

        with self:

            # RESPONSE FUNCTIONS

            def moped_enable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("ENABLE_LOOK_FOR_CLOSE_OBJECTS response: " + \
                                  str(response.correct))
                    return succeeded
                else:
                    return aborted

            def moped_disable_cb(userdata, response):
                if response.correct != None:
                    rospy.loginfo("DISABLE_LOOK_FOR_CLOSE_OBJECTS response: " + \
                                  str(response.correct))
                    return succeeded
                else:
                    return aborted

            # SM

            # ENABLE LOOK FOR OBJECTS

            smach.StateMachine.add( 'ENABLE_LOOK_FOR_CLOSE_OBJECTS',
                                    ServiceState( '/iri_moped_handler/enable',
                                                  enable,
                                                  response_cb = moped_enable_cb,
                                                  #request_key = 'object_name',
                                                  request = True),
                                    transitions = {succeeded:'LOOK_FOR_OBJECTS'})

                                                                                # FIXME: why is there a smaller ctimeout & retry on aborted?
            # LOOK FOR OBJECTS                                                  # If something goes wrong it'd rather have it fail than having
                                                                                # it keep hanging on forever... --Siegfried
            smach.StateMachine.add( 'LOOK_FOR_OBJECTS',
                                    TopicReaderState( topic_name='/iri_moped_handler/outputOPL',
                                                      msg_type=ObjectPoseList,
                                                      timeout=10),
                                    remapping   = {'message' : 'object_data'},
                                    transitions = {succeeded: 'DISABLE_CLOSE_OBJECT_SEARCH',
                                                   aborted: aborted})

            # DISABLE LOOK FOR OBJECTS

            smach.StateMachine.add( 'DISABLE_LOOK_FOR_CLOSE_OBJECTS',
                                    ServiceState( '/iri_moped_handler/enable',
                                                  enable,
                                                  response_cb = moped_disable_cb,
                                                  #request_key = 'object_name',
                                                  request = False),
                                    transitions = {succeeded: succeeded})

""" ///////////////////////////////////////////////////////////////////////////

        SEARCH OBJECTS IN PLACE SM ITERATOR

        - iterates in a set of angles
          - scan for objects SM (looking to table)
          - rotates the base to 45
          - scan for objects SM (looking to NW table)
          - rotates the base to -90
          - scan for objects SM (looking to NE table)

/////////////////////////////////////////////////////////////////////////// """

class SearchObjectsInPlaceStateMachine(smach.StateMachine):

  def __init__(self):

    smach.StateMachine.__init__(self, [succeeded, preempted, aborted],
    output_keys=['object_data'])

  with self:

    smach.StateMachine.add(
            'SCAN_FOR_OBJECT_N',
            ScanForObjectStateMachine(),
            transitions = {succeeded: succeeded, aborted: 'N2_TURN_NW'})

    pose_nw = Pose()
    pose_nw.orientation = Quaternion(*quaternion_from_euler(0, 0, 0.7854))
    smach.StateMachine.add( 'N2_TURN_NW',
                            MoveActionState("/base_link", pose_nw),
                            transitions = {succeeded: 'SCAN_FOR_OBJECT_NW'})

    smach.StateMachine.add( 'SCAN_FOR_OBJECT_NW',
                            ScanForObjectStateMachine(),
                            transitions = {succeeded: succeeded, aborted: 'N2_TURN_NE'})

    pose_ne = Pose()
    pose_ne.orientation = Quaternion(*quaternion_from_euler(0, 0, -1.5708))
    smach.StateMachine.add( 'N2_TURN_NE',
                            MoveActionState("/base_link", pose_ne),
                            transitions = {succeeded: 'SCAN_FOR_OBJECT_NE'})

    smach.StateMachine.add( 'SCAN_FOR_OBJECT_NE',
                            ScanForObjectStateMachine(),
                            transitions = {succeeded: succeeded, aborted: aborted})


""" ///////////////////////////////////////////////////////////////////////////

        SEARCH OBJECTS SM ITERATOR

        - iterates in a set of positions in the map
          - move the base to the position
          - search objects in place SM

/////////////////////////////////////////////////////////////////////////// """

class SearchObjectsStateMachine(smach.StateMachine):

  def __init__(self):

    smach.StateMachine.__init__(self, [succeeded, preempted, aborted], output_keys=['object_data'])

    with self:

      # READ PLACES OF INTEREST FROM PARAMETERS place: [x,y,th]

      raw = rospy.get_param("/places")
      self.userdata.places = []
      self.userdata.object_data = []
      pose = Pose()

      for p in places:
        pose.position = Point(p[0], p[1], 0)
        pose.orientation = Quaternion(*quaternion_from_euler(0, 0, p[2]))
        places.append(pose)

      # ITERATOR

      places_it = Iterator( outcomes = [succeeded,preempted,aborted],
                            input_keys = ['places'],
                            it = lambda: range(0, len(self.userdata.places)),
                            output_keys = ['object_data'],
                            it_label = 'index',
                            exhausted_outcome = aborted)

      with places_it:

        container_sm = StateMachine(outcomes = [succeeded,preempted,aborted,'continue'],
                                        input_keys = ['places', 'index'],
                                        output_keys = ['object_data'])

        # ITERATION CONTAINER

        with container_sm:

          smach.StateMachine.add( 'N2_GO_TO_PLACE_OF_INTEREST',
                                  MoveActionState("/base_link", places[index]),
                                  transitions = {succeeded: 'SEARCH_OBJ_IN_PLACE'})

          smach.StateMachine.add( 'SEARCH_OBJ_IN_PLACE',
                                  SearchObjectsInPlaceStateMachine(),
                                  transitions = {succeeded: succeeded, aborted: 'continue'})

        Iterator.set_contained_state( 'CONTAINER_STATE',
                                      container_sm,
                                      loop_outcomes=['continue'])

      smach.StateMachine.add( 'PLACES_IT',
                              places_it,
                              {succeeded:succeeded, aborted:aborted})






""" ///////////////////////////////////////////////////////////////////////////
                              TODO
/////////////////////////////////////////////////////////////////////////// """

# create mock and use for far object detection
# Pass its data to Goto dep of policy
# smach.StateMachine.add(
#    'LOOK_FOR_FAR_OBJECTS',
#    look_for_far_objects(),
#    transitions = {succeeded: 'N2_go_to_dep_policy'})

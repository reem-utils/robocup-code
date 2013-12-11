#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import rospy

'''
Factory function to get a state machine that implements the desired approach.
The wanted approach is passed as a parameter. The different possibilities are:
    - first: Approach that uses the next_location_provider service.
             It need the information of the locations_with_probabilities.yaml of the coord_translator in order to work.
             It goes to the locations with more probaility and looks there for objects.
    - second: Approach that uses the tabletop detection in order to select places where objects can be found. It wanders
              through the room to look for tabletops, and then looks for what's on that tabletops.
              If openCV is not being used, the file room_corners.yaml in the coord_translator must be filled for every room.
    - third: Similar to the second one, it looks for furniture to go to look for objects.
    - third_tsp: The same as third, but uses the furniture_probabilities.yaml of the coord_translator to decide what detected
                 furniture will be visited first.
The parameters of the function are the same that all the approcahes have.

Note: having every import inside the conditionals prevents having dependencies on things of other approaches that people don't use.
'''


def ObjectFindingBehaviour(approach='first', target_object_key=None, target_frame='/map'):
    if approach == 'first':
        from pal_smach_utils.object_finding_algorithms.ofb_first_approach import OFBFirstApproach
        return OFBFirstApproach(target_object_key=target_object_key, target_frame=target_frame)
    elif approach == 'second':
        from pal_smach_utils.object_finding_algorithms.ofb_second_approach import OFBSecondApproach
        return OFBSecondApproach(target_object_key=target_object_key, target_frame=target_frame)
    elif approach == 'third':
        from pal_smach_utils.object_finding_algorithms.ofb_third_approach import OFBThirdApproach
        return OFBThirdApproach(target_object_key=target_object_key, target_frame=target_frame, tsp_route=False)
    elif approach == 'third_tsp':
        from pal_smach_utils.object_finding_algorithms.ofb_third_approach import OFBThirdApproach
        return OFBThirdApproach(target_object_key=target_object_key, target_frame=target_frame, tsp_route=True)
    else:
        m1 = "Asked for an Object Finding Behaviour named '%s' but it doesn't exist." % approach
        m2 = "Available approaches are: 'first', 'second', 'third' and 'third_tsp'."
        rospy.logfatal(m1 + " " + m2)
        raise rospy.ROSException(m1 + " " + m2)

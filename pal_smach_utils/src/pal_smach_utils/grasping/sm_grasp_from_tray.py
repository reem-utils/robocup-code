import smach
import rospy
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted


class GraspFromTrayStateMachine(smach.StateMachine):
    def __init__(self, tray_position=3, tray_position_cb=None, input_keys=[], output_keys=[]):

        if(tray_position < 1 or tray_position > 3):
            raise ValueError("'tray_position' need be a value between 1 and 3. Value = %s" % str(tray_position))
        elif tray_position and tray_position_cb:
            raise ValueError("You've set both `tray_position' and `tray_position_cb'!")

        self.tray_position = tray_position

        smach.StateMachine.__init__(self, input_keys=input_keys, output_keys=[], outcomes=[aborted, succeeded, preempted])

        with self:
            #FIXME: Check if the position it's really available or not. If not, put on other position
            def announce_putting_cb(userdata, message):
                rospy.logwarn("GraspFromTrayStateMachine not implemented yet")
                return "Succes on getting object from tray."
                # return "Succes on getting object in the position %s " % self.tray_position

            smach.StateMachine.add(
                "ANNOUNCE_GETTING",
                SpeakActionState(text_cb=announce_putting_cb),
                transitions={succeeded: succeeded, aborted: "ANNOUNCE_GETTING", preempted: "ANNOUNCE_GETTING"}
                )

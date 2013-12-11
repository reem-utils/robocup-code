import smach
import rospy
from pal_smach_utils.speech.sound_action import SpeakActionState
from pal_smach_utils.utils.global_common import succeeded, aborted, preempted


class PutOnTrayStateMachine(smach.StateMachine):
    def __init__(self, tray_position=None, tray_position_cb=None, input_keys=[], output_keys=[]):

        if not tray_position and not tray_position_cb:
            raise ValueError("Neither `tray_position' nor `tray_position_cb' where set!")
        elif tray_position and tray_position_cb:
            raise ValueError("You've set both `tray_position' and `tray_position_cb'!")

        smach.StateMachine.__init__(self, input_keys=input_keys, output_keys=output_keys, outcomes=[aborted, succeeded, preempted])

        def announce_putting_cb(userdata):
            # FIXME: Check if self.tray_position is a value between 1 and 3
            # self.tray_position = tray_position_cb if tray_position else tray_position_cb(userdata)
            # rospy.logwarn("PutOnTrayStateMachine need be developed")
            return "Success on putting object in the tray1"

        with self:

            smach.StateMachine.add(
                "ANNOUNCE_PUTING",
                SpeakActionState(text_cb=announce_putting_cb),
                transitions={succeeded: succeeded, aborted: "ANNOUNCE_PUTING",  preempted: "ANNOUNCE_PUTING"}
                )

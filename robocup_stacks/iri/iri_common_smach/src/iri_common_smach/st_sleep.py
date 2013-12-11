import roslib; roslib.load_manifest('iri_common_smach')
import smach
import smach_ros
import time

class WaitSeconds(smach.State):
    def __init__(self, seconds):
        smach.State.__init__(self, outcomes=['finish'])
        self.seconds = seconds

    def execute(self, userdata):
        time.sleep(self.seconds)
        return 'finish'

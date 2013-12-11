#! /usr/bin/env python
import roslib
roslib.load_manifest('upperbody_mock')
import rospy
import actionlib
from pal_control_msgs.msg import MotionManagerAction
from pr2_controllers_msgs.msg import PointHeadAction


class MotionManager_Mock:

    def __init__(self):
        self._server1 = actionlib.SimpleActionServer('/motion_manager',
                                                     MotionManagerAction,
                                                     self._execute,
                                                     auto_start=False)
        self._server1.start()

    def _execute(self, goal):
        print "Goal MOTION MANAGER received ============"
        print goal
        print "=========================="
        self._server1.set_succeeded()


class PointHead_Mock:

    def __init__(self):
        self._server2 = actionlib.SimpleActionServer('/head_traj_controller/point_head_action',
                                                     PointHeadAction,
                                                     self._execute,
                                                     auto_start=False)
        self._server2.start()

    def _execute(self, goal):
        print "Goal POINTHEAD received ============"
        print goal
        print "=========================="
        self._server2.set_succeeded()


def upperbody_mock():
    rospy.init_node('upper_body')
    server = MotionManager_Mock()
    server = PointHead_Mock()
    print "UpperBody_Mock (MotionManager and PointHead) started... waiting for goals"
    rospy.spin()

if __name__ == '__main__':
    upperbody_mock()

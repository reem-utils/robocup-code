#! /usr/bin/env python
# -.- coding: utf-8 -.-

import roslib
roslib.load_manifest('scan_table_mock')
import rospy
from actionlib import SimpleActionServer

import random
from pr2_controllers_msgs.msg import PointHeadAction

class ScanTableActionServer:
    """
      Scan Table Mock
      Run this file to have mock to the action '/head_traj_controller/head_scan_snapshot_action '(Scan Table)
    """
    def __init__(self):
        a_scan_table = {'name': '/head_traj_controller/head_scan_snapshot_action', 'ActionSpec': PointHeadAction, 'execute_cb': self.scan_table_cb, 'auto_start': False}
        self.s  = SimpleActionServer(**a_scan_table)
        self.s.start()

    def scan_table_cb(self, req):
         rospy.loginfo('Scan Table \'/head_traj_controller/head_scan_snapshot_action was called.')
         self.s.set_succeeded() if bool(random.randint(0, 1)) else self.s.set_aborted()


if __name__ == '__main__':

      rospy.init_node('scan_table_mock')

      ScanTableActionServer()

      rospy.spin()

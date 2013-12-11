#!/usr/bin/env python
import roslib
roslib.load_manifest('object_recognition_mock')

try:
   from pr_msgs.msg import ObjectPoseList, ObjectPose
except ImportError:
   from pr_msgs.msg import ObjectPoseList, ObjectPose
try:
   from iri_moped_handler.srv import *
except ImportError:
   from object_recognition_mock.srv import *


#from pr_msgs.srv import *


from geometry_msgs.msg import Pose
from sensor_msgs.msg import Image
import rospy


def ObjectRecognitionPublisher():
    print "object_recognition_mock running..."
    pub = rospy.Publisher('/iri_moped_handler/outputOPL', ObjectPoseList)

    rate = rospy.Rate(10)  # Hz
    # change to my msg
    msg = ObjectPoseList()
    msg.header.stamp = rospy.Time.now()
    msg.header.frame_id = "/head_2_link"  # "/head_mount_xtion_optical_frame"
    msg.object_list = [None] * 7
    msg.object_list[0] = ObjectPose()
    msg.object_list[0].name = "coke-close"
    msg.object_list[0].pose = Pose()

    # 1) Old secure pose in reference to /base_link
    # msg.object_list[0].pose.position.x = 0.30
    # msg.object_list[0].pose.position.y = -0.30
    # msg.object_list[0].pose.position.z = 1.13
    # msg.object_list[0].pose.orientation.x = 0.5
    # msg.object_list[0].pose.orientation.y = -0.5
    # msg.object_list[0].pose.orientation.z = 0.5
    # msg.object_list[0].pose.orientation.w = -0.5

    # Position of hand in front in reference of /kinect_link
    # msg.object_list[0].pose.position.x = 0.222509
    # msg.object_list[0].pose.position.y = -0.551083 # was positive before
    # msg.object_list[0].pose.position.z = -0.764526
    # msg.object_list[0].pose.orientation.x = 0.081764
    # msg.object_list[0].pose.orientation.y = -0.38946
    # msg.object_list[0].pose.orientation.z = 0.714737
    # msg.object_list[0].pose.orientation.w = 0.575141

    # Real detection pose in reference to /kinect_link
    # msg.object_list[0].pose.position.x = 0.0231333337724
    # msg.object_list[0].pose.position.y = 0.0350304767489
    # msg.object_list[0].pose.position.z = 0.694000005722
    # msg.object_list[0].pose.orientation.x = 0.946857988834
    # msg.object_list[0].pose.orientation.y = -0.0297971088439
    # msg.object_list[0].pose.orientation.z = -0.295009255409
    # msg.object_list[0].pose.orientation.w = 0.12466647476

    # Manually generated pose in reference of /openni_depth_frame from
    # Asking tf to transform the 1) coords from base_link to openni_depth_frame
    msg.object_list[0].pose.position.x = 0.611990241005
    msg.object_list[0].pose.position.y = -0.317951137319
    msg.object_list[0].pose.position.z = -0.38978881074
    msg.object_list[0].pose.orientation.x = 0.946857988834
    msg.object_list[0].pose.orientation.y = -0.0297971088439
    msg.object_list[0].pose.orientation.z = -0.295009255409
    msg.object_list[0].pose.orientation.w = 0.12466647476

    #   name: coke-close
    #pose:
    #  position:
    #   x: 0.0231333337724
    #   y: 0.0350304767489
    #   z: 0.694000005722
    #orientation:
    #   x: 0.946857988834
    #   y: -0.0297971088439
    #   z: -0.295009255409
    #   w: 0.12466647476
    #pose2D:
    # x: 337.68838501
    # y: 266.798492432
    # z: 0.0

    msg.object_list[1] = ObjectPose()
    msg.object_list[1].name = "milk"
    msg.object_list[1].pose = Pose()
    msg.object_list[1].pose.position.x = 0.30
    msg.object_list[1].pose.position.y = -0.30
    msg.object_list[1].pose.position.z = 1.13
    msg.object_list[1].pose.orientation.x = 0.5
    msg.object_list[1].pose.orientation.y = -0.5
    msg.object_list[1].pose.orientation.z = 0.5
    msg.object_list[1].pose.orientation.w = -0.5
    msg.originalTimeStamp = rospy.Time.now()

    msg.object_list[2] = ObjectPose()
    msg.object_list[2].name = "redbull"
    msg.object_list[2].pose = Pose()
    msg.object_list[2].pose.position.x = 0.30
    msg.object_list[2].pose.position.y = -0.30
    msg.object_list[2].pose.position.z = 1.13
    msg.object_list[2].pose.orientation.x = 0.5
    msg.object_list[2].pose.orientation.y = -0.5
    msg.object_list[2].pose.orientation.z = 0.5
    msg.object_list[2].pose.orientation.w = -0.5
    msg.originalTimeStamp = rospy.Time.now()

    msg.object_list[3] = ObjectPose()
    msg.object_list[3].name = "juice"
    msg.object_list[3].pose = Pose()
    msg.object_list[3].pose.position.x = 0.30
    msg.object_list[3].pose.position.y = -0.30
    msg.object_list[3].pose.position.z = 1.13
    msg.object_list[3].pose.orientation.x = 0.5
    msg.object_list[3].pose.orientation.y = -0.5
    msg.object_list[3].pose.orientation.z = 0.5
    msg.object_list[3].pose.orientation.w = -0.5
    msg.originalTimeStamp = rospy.Time.now()

    msg.object_list[4] = ObjectPose()
    msg.object_list[4].name = "beer"
    msg.object_list[4].pose = Pose()
    msg.object_list[4].pose.position.x = 0.30
    msg.object_list[4].pose.position.y = -0.30
    msg.object_list[4].pose.position.z = 1.13
    msg.object_list[4].pose.orientation.x = 0.5
    msg.object_list[4].pose.orientation.y = -0.5
    msg.object_list[4].pose.orientation.z = 0.5
    msg.object_list[4].pose.orientation.w = -0.5
    msg.originalTimeStamp = rospy.Time.now()

    msg.object_list[5] = ObjectPose()
    msg.object_list[5].name = "water"
    msg.object_list[5].pose = Pose()
    msg.object_list[5].pose.position.x = 0.30
    msg.object_list[5].pose.position.y = -0.30
    msg.object_list[5].pose.position.z = 1.13
    msg.object_list[5].pose.orientation.x = 0.5
    msg.object_list[5].pose.orientation.y = -0.5
    msg.object_list[5].pose.orientation.z = 0.5
    msg.object_list[5].pose.orientation.w = -0.5
    msg.originalTimeStamp = rospy.Time.now()

    msg.object_list[6] = ObjectPose()
    msg.object_list[6].name = "wine"
    msg.object_list[6].pose = Pose()
    msg.object_list[6].pose.position.x = 0.30
    msg.object_list[6].pose.position.y = -0.30
    msg.object_list[6].pose.position.z = 1.13
    msg.object_list[6].pose.orientation.x = 0.5
    msg.object_list[6].pose.orientation.y = -0.5
    msg.object_list[6].pose.orientation.z = 0.5
    msg.object_list[6].pose.orientation.w = -0.5
    msg.originalTimeStamp = rospy.Time.now()

    while not rospy.is_shutdown():
            pub.publish(msg)
            print "Publishing close_object msg with ObjectName: " + msg.object_list[0].name
            rate.sleep()

currentStatus = False


def handle_mopedEnabler_call(data):
    print "Received " + str(data.enable)
    if not data.enable:
        currentStatus = False
    else:
        currentStatus = True
        # Simulate the recognition of something
        rospy.sleep(1)
    return enableResponse(True)  # response if correct


def mopedEnablerServer():
    s = rospy.Service('/iri_moped_handler/enable', enable, handle_mopedEnabler_call)
    print "mopedEnablerServer running..."
    currentStatus = False
    #rospy.spin()


if __name__ == "__main__":
    rospy.init_node('object_recognition')
    mopedEnablerServer()
    ObjectRecognitionPublisher()

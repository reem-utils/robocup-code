#! /usr/bin/env python

import roslib; roslib.load_manifest('rosbag_image_cropper')
import rospy
from sensor_msgs.msg import Image
import numpy as np
import cv2
import cv2.cv as cv
from cv_bridge import CvBridge, CvBridgeError
import copy
import os
import sys


class ImageCropperNode():

    def __init__(self, object_name, path_to_store):
        self.pub = rospy.Subscriber('/camera/rgb/image_color', Image, self.imgCb_color)
        self.sub = rospy.Subscriber('/camera/mask', Image, self.imgCb_mask)
        self.bridge = CvBridge()

      # Too lazy to manage the synchronism... they are slowly published and at aproximatelly the same time
        self.current_color_image = None
        self.new_color_image = False
        self.current_mask_image = None
        self.new_mask_image = False
        self.img_num = 0
        self.object_name = object_name
        self.store_path = path_to_store

    def imgCb_color(self, data):
        rospy.loginfo("Received color image " + str(self.img_num))
        cvImage = np.asarray(self.bridge.imgmsg_to_cv(data, "bgr8"))
        self.current_color_image = cvImage
        self.new_color_image = True
        # whoever goes last receiving will do the real call
        self.saveCroppedImage()

    def imgCb_mask(self, data):
        rospy.loginfo("Received mask image " + str(self.img_num))
        cvImage = np.asarray(self.bridge.imgmsg_to_cv(data, "bgr8"))
        self.current_mask_image = cvImage
        self.new_mask_image = True
        # whoever goes last receiving will do the real call
        self.saveCroppedImage()

    def saveCroppedImage(self):
        im_color = None
        im_mask = None
        if self.new_color_image and self.new_mask_image:
            rospy.loginfo("Cropping image " + str(self.img_num))
            im_color = copy.deepcopy(self.current_color_image)
            im_mask = copy.deepcopy(self.current_mask_image)
            self.new_color_image = False
            self.new_mask_image = False

            # Gray scale please, findContours needs it like that
            mask_gray = cv2.cvtColor(im_mask, cv.CV_BGR2GRAY)
            cv2.medianBlur(mask_gray, 7)
            # Get the contours
            contours, hierarchy = cv2.findContours(mask_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # Get the biggest one (noise is little ones)
            biggestcont = contours[0]
            for cont in contours:
                if len(biggestcont) < len(cont):
                    biggestcont = cont
            cnt = biggestcont
            # Get the rect
            x, y, w, h = cv2.boundingRect(cnt)
            # Crop stuff
            crop = im_color[y:y+h, x:x+w]
            # Save image
            if self.img_num > 0:  # First image is not usefull, it's too dark
                rospy.loginfo("Saving image " + str(self.img_num) + " to " + self.store_path + '/' + self.object_name + '/' + self.object_name + "_image_" + str(self.img_num).zfill(3) + '.png')
                cv2.imwrite(self.store_path + '/' + self.object_name + '/' + self.object_name + "_image_" + str(self.img_num).zfill(3) + '.png', crop)
            else:  # at least create the directory to store the images
                rospy.loginfo("Skipping first image as it's too dark. Creating directory to store images.")
                os.mkdir(self.store_path + '/' + self.object_name)
            self.img_num += 1

        # else:  # there are 2 calls, one won't do anything. Don't hit me
        #     rospy.loginfo("Fake call...")
        return




if __name__ == '__main__':
    rospy.init_node('rosbag_image_cropper_node')
    if len(sys.argv) < 2:
        print "Error, we need a parameter of the object name and where to store images (you should be launching this with a launcher!)"
        rospy.loginfo("No object name and/or path given, shutting down")
        exit()

    node = ImageCropperNode(sys.argv[1], sys.argv[2])
    rospy.loginfo('Cropping with object name: ' + sys.argv[1] + ' saving to the path: ' +  sys.argv[2])

    if sys.argv[1] == 'object':
        rospy.loginfo('(Are you sure you want to name it \"object\"?)')
    rospy.spin()

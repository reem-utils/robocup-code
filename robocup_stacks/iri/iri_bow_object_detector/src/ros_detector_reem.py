#!/usr/bin/env python
import roslib; roslib.load_manifest('iri_bow_object_detector')

import rospy

from cv_bridge import CvBridge, CvBridgeError

import numpy as np
from os.path import exists
from os import system

from iri_bow_object_detector.srv import *
from iri_bow_object_detector.msg import *
from iri_perception_msgs.msg import ImagePoint
from geometry_msgs.msg import Point

from iri_bow_object_detector import config_feats
from iri_bow_object_detector.pcl2numpy import get_auto
from iri_bow_object_detector.refine_grasp_point_finddd import select_grasp_point_finddd
from iri_bow_object_detector.refine_grasp_point_middle import select_grasp_point_middle
from iri_bow_object_detector.refine_grasp_point_manual import select_grasp_point_manual

#from iri_bow_object_detector.run_detector import gen_windows
from iri_bow_object_detector.run_detector import detect_boxes
#import ipdb
import cv
import pylab


def read_vws(geo_vw_sets):
	vws=[]
	for geo_vw_set in geo_vw_sets:
		vws.append([[geo_vw.x, geo_vw.y, geo_vw.word] for geo_vw in geo_vw_set.geo_vws])
	return vws


def handle_detector_cb(req):
	vws = read_vws(req.geo_vw_sets)

	bridge = CvBridge()
	try:
		cv_image = bridge.imgmsg_to_cv(req.image, "bgr8")
		cv_mask  = bridge.imgmsg_to_cv(req.mask, "bgr8")
	except CvBridgeError, e:
		print e

	cv_mask_gray = cv.CreateMat(cv_mask.rows, cv_mask.cols, cv.CV_8U)

	cv.CvtColor(cv_mask, cv_mask_gray, cv.CV_BGR2GRAY)
	#aux = np.ones((480, 640))
	#mask = cv.fromarray(aux)
	#cv_mask_gray = mask

	conf = config_feats.conf
	w  = np.load(rospy.get_param("~linear_svm_file"))

	if not exists(conf.det_results_dir):
		system('mkdir '+conf.det_results_dir)

	print "Processing the algorithm."
	(win, prob) = detect_boxes(w, rospy.get_param("~non_linear_svm_file"), cv_image, cv_mask_gray, conf, vws)

	print "Finished"
	rospy.loginfo("Detection box: " + str(win) + " probs: " + str(prob));

	res = GeoVwDetectionResponse()

	for idx, sol in enumerate(win):
		point1 = ImagePoint()
		point1.x = sol[0]
		point1.y = sol[1]

		point2 = ImagePoint()
		point2.x = sol[2]
		point2.y = sol[3]

		res.posible_solutions.append(ObjectBox(point1, point2, prob[idx]))

	return res


def get_auto(data, wants):
	resolution = (data.height, data.width)
	img = np.fromstring(data.data, np.float32)
	step=img.shape[0]/(data.height*data.width)
	ret = []
	for w, p in wants:
		if w=="pos":
			x = img[p::step].reshape(resolution)
			y = img[p+1::step].reshape(resolution)
			z = img[p+2::step].reshape(resolution)
			x    = np.flipud(x)
			y    = np.flipud(y)
			z    = np.flipud(z)
			ret.extend([x, y, z])
		elif w=="rgb":
			rgb = img[p::step]
			r = np.zeros(data.height*data.width)
			g = np.zeros(data.height*data.width)
			b = np.zeros(data.height*data.width)
			for i in range(rgb.shape[0]):
				int_rgb = struct.unpack('i', struct.pack('f', rgb[i]))[0]
				r[i] = (int_rgb & 0xff0000) >> 16
				g[i] = (int_rgb & 0xff00) >> 8
				b[i] = (int_rgb & 0xff)
			r = np.flipud(r.reshape(resolution))
			g = np.flipud(g.reshape(resolution))
			b = np.flipud(b.reshape(resolution))
			gray = (0.30*r+0.59*g+0.11*b).astype('uint8')
			ret.extend([r,g,b,gray])
		elif w=="norm":
			n_x = np.flipud(img[p::step].reshape(resolution))
			n_y = np.flipud(img[p+1::step].reshape(resolution))
			n_z = np.flipud(img[p+2::step].reshape(resolution))
			ret.extend([n_x, n_y, n_z])
		elif w=="curv":
			curv = np.flipud(img[p::step].reshape(resolution))
			ret.extend([curv])
	return ret



def select_grasp_point_cb(req):
	#return select_grasp_point_wrinkled_map(req)
	#return select_grasp_point_finddd(req, rospy.get_param("~finddd_svm_file"))
	return select_grasp_point_middle(req)
	#return select_grasp_point_manual(req)



def add_detector_server():
	rospy.init_node('detector')
	s1 = rospy.Service('geo_vw_detector', GeoVwDetection, handle_detector_cb)
	s2 = rospy.Service('refine_grasp_point', RefineGraspPoint, select_grasp_point_cb)

	# check params
	if (not rospy.has_param("~linear_svm_file")):
		rospy.logerr("Node has no param linear_svm_file. Please set it up on launch file")
		exit
	if (not rospy.has_param("~non_linear_svm_file")):
		rospy.logerr("Node has no param non_linear_svm_file. Please set it up on launch file")
		exit
	if (not rospy.has_param("~finddd_svm_file")):
		rospy.logerr("Node has no param non_linear_svm_file. Please set it up on launch file")
		exit
	print "Detecting regions."
	rospy.spin()

if __name__ == "__main__":
	add_detector_server()


# DEPRECATED Now using finddd
#def select_grasp_point_wrinkled_map(req):
	#(XX, YY, ZZ, W) = get_auto(req.wrinkled_map, [("pos", 0), ("curv", 4)])
	#P=[(box.point1.x, box.point1.y, box.point2.x, box.point2.y, box.value ) for box in req.posible_solutions]

	#P.sort(key=lambda x:x[4], reverse=True)
	#print P

	#if len(P) < 1:
		#return Point(0,0,0)

	#xc=(P[0][0]+P[0][2])/2
	#yc=(P[0][1]+P[0][3])/2

	#offset=30
	#print xc,yc, W.shape
	#WW=W[yc-30:yc+30,xc-30:xc+30]
	#print W[yc-30:yc+30,xc-30:xc+30].max()
	#y,x=np.unravel_index(np.argmax(WW),WW.shape)
	#print np.argmax(WW), WW[y,x]
	#x=xc-30+x
	#y=yc-30+y

	#print "Solution is " + str(y) + "," + str(x)

	## show result
	#bridge = CvBridge()
	#try:
		#image = bridge.imgmsg_to_cv(req.image, "bgr8")
	#except CvBridgeError, e:
		#print e
	#cv.Rectangle(image,(x-1,y-1), (x+1, y+1), (255,255,255))
	#cv.NamedWindow("Grasp point")
	#cv.ShowImage("Grasp point", image)
	#cv.WaitKey(10)

	#return Point(XX[y,x], YY[y,x], ZZ[y,x])

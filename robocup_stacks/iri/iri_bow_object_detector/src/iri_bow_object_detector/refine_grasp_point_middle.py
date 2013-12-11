import os
import numpy as np

from iri_bow_object_detector.pcl2numpy import get_auto
from geometry_msgs.msg import Point
from iri_perception_msgs.msg import ImagePoint
from iri_bow_object_detector.srv import RefineGraspPoint

import cv
from cv_bridge import CvBridge, CvBridgeError

#import ipdb


def select_grasp_point_middle(req):
	P=[(box.point1.x, box.point1.y, box.point2.x, box.point2.y, box.value ) for box in req.posible_solutions]
	P.sort(key=lambda x:x[4], reverse=True)
	if len(P) < 1:
		return Point(0,0,0)

	maxp2du = P[0][0] + (P[0][2] - P[0][0])/2
	maxp2dv = P[0][1] + (P[0][3] - P[0][1])/2
	maxp2d = (maxp2du, maxp2dv)

	#(XX, YY, ZZ, W) = get_auto(req.pointcloud, [("pos", 0), ("curv", 4)])
	#res = Point(XX[maxp2dv, maxp2du], YY[maxp2dv, maxp2du], ZZ[maxp2dv, maxp2du])

	# Draw boxes
	## show result
	bridge = CvBridge()
	try:
		image = bridge.imgmsg_to_cv(req.image, "bgr8")
	except CvBridgeError, e:
		print e

	probs = [wi[4] for wi in P]
	maxprob = max(probs)
	minprob = min(probs)
	for ii,wi in enumerate(P):
		if minprob==maxprob:
			wi_color = 255
		else:
			wi_color = int(np.round(255*((wi[4]-minprob)/(maxprob-minprob))))
		cv.Rectangle(image,(wi[0],wi[1]), (wi[2],wi[3]), (0, 0, wi_color), 3)


	cv.Rectangle(image,(maxp2d[0]-5,maxp2d[1]-1), (maxp2d[0]+5, maxp2d[1]+1), (255,255,255), 2)
	cv.Rectangle(image,(maxp2d[0]-1,maxp2d[1]-5), (maxp2d[0]+1, maxp2d[1]+5), (255,255,255), 2)
	cv.Rectangle(image,(maxp2d[0]-1,maxp2d[1]-1), (maxp2d[0]+1, maxp2d[1]+1), (0,0,0), 1)
	cv.NamedWindow("Grasp point")
	cv.ShowImage("Grasp point", image)
	cv.WaitKey(1000)

	basestr="/home/dmartinez/experimentos/ijrr13/exp-SIFT_"
	ps=os.popen('ls '+basestr+'*.png | cut -d "_" -f2 | cut -d "." -f1 2>/dev/null')
	nums=ps.readlines()
	if len(nums):
		num=max([int(x) for x in nums])
	else:
		num=-1
	cv.SaveImage(basestr+"%04d.png"%(num+1), image)

	# prints
	#print res
	print 'Res 2D: (' + str(maxp2du) + ',' + str(maxp2dv) + ')'
	res = ImagePoint(maxp2du, maxp2dv)

	return res









import numpy as np
import cPickle
import os
import cv
import cv2
import pylab
from cv_bridge import CvBridge, CvBridgeError
from shogun.Features import RealFeatures, Labels

from geometry_msgs.msg import Point
from iri_bow_object_detector.srv import RefineGraspPoint
from iri_perception_msgs.msg import ImagePoint

#import ipdb


def norm_descs(descs, l=1):
    print descs.shape
    norms = np.apply_along_axis(np.linalg.norm, 0, descs, l) #leave bias alone
    print sum(norms==0)
    descs/=norms
    descs[np.isnan(descs)]=0
    descs=np.sqrt(descs)
    return descs


def select_grasp_point_finddd(req, svm_file):
	orig_descs = req.descriptor_set
	P=[(box.point1.x, box.point1.y, box.point2.x, box.point2.y, box.value ) for box in req.posible_solutions]
	P.sort(key=lambda x:x[4], reverse=True)
	if len(P) < 1:
		return Point(0,0,0)
	# we will only use the first (best score) bounding box
	P0 = P[0]

	pf=open(svm_file, 'rb')
	svm = cPickle.load(pf)
	pf.close()

	descs = orig_descs.descriptors
	descs_n = [desc.descriptor for desc in descs if (desc.u > P0[0]) and (desc.u < P0[2]) and (desc.v > P0[1]) and (desc.v < P0[3])]
	xys = [(desc.u, desc.v) for desc in descs if (desc.u > P0[0]) and (desc.u < P0[2]) and (desc.v > P0[1]) and (desc.v < P0[3])]
	descs_n = np.asarray(descs_n)
	# descriptors are already normalized
	#descs_n = norm_descs(descs_np)

	print descs_n.shape

	descs_svm=RealFeatures(descs_n.T)
	out=svm.apply(descs_svm)
	print out.get_labels()
	sco=out.get_labels()
	maxp3d=None
	maxp2d=None
	maxpsco=None
	shape=(480,640)

	## show result
	bridge = CvBridge()
	try:
		image = bridge.imgmsg_to_cv(req.image, "bgr8")
	except CvBridgeError, e:
		print e

	image_cv2 = np.asarray(image)
	imabw=np.zeros((shape[0],shape[1])).astype('uint8')
	imabw=cv2.cvtColor(image_cv2,cv2.COLOR_RGB2GRAY)
	imabw2=np.zeros((shape[0]/3,shape[1]/3)).astype('uint8')
	imabw=(255*imabw).astype('uint8')
	imabw2=cv2.resize(src=imabw,dsize=(shape[1]/3,shape[0]/3),interpolation=cv2.INTER_LINEAR)
	edges=cv2.Canny(imabw2,50,60)

	# set scores and find biggest score in target box
	print sco
	scores = min(sco)*np.ones((shape[0]/3,shape[1]/3))

	for s,(u,v) in zip(sco,xys):
		if (u > P0[0]) and (u < P0[2]) and (v > P0[1]) and (v < P0[3]):
			if maxpsco==None or maxpsco<s:
				maxp2d=(u,v)
				maxpsco=s
		u = u/3
		v = v/3
		scores[v,u]=s
		#if edges[v,u]!=0:

	for d in descs:
		u = d.u/3
		v = d.v/3

		if (edges[v,u]!=0):
			scores[v,u]=np.nan



	# draw boxes
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

	basestr="/home/dmartinez/experimentos/iros13/exp-SIFT_"
	ps=os.popen('ls '+basestr+'*.png | cut -d "_" -f2 | cut -d "." -f1 2>/dev/null')
	nums=ps.readlines()
	if len(nums):
		num=max([int(x) for x in nums])
	else:
		num=-1
	cv.SaveImage(basestr+"%04d.png"%(num+1), image)

	cmap=pylab.cm.jet #spectral
	cmap.set_bad('black',1.)
	masked_array = np.ma.masked_where(np.isnan(scores), scores)

	pylab.ion()
	pylab.clf()
	pylab.imshow(masked_array, cmap=cmap)
	pylab.colorbar()
	pylab.draw()
	#pylab.show()
	#pylab.draw()

	pylab.savefig(basestr+"%04d_scores.png"%(num+1))

	#return Point(maxp3d.x, maxp3d.y, maxp3d.z)
	res = ImagePoint(maxp2d[0], maxp2d[1])
	return res

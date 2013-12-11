#!/usr/bin/env python
import roslib; roslib.load_manifest('entropy_descriptor_node')
 
import rospy
#from sensor_msgs.msg import Image
from entropy_descriptor_node.msg import heat_map
import numpy as np
import pylab

def show_map(data):
    #print data
    hmap=np.array(data.data)
    hmap.shape = (data.height, data.width)
    print hmap, hmap.max()
    pylab.imshow(hmap.astype('float'))
    pylab.colorbar()
    pylab.draw()


if __name__ == '__main__':
    print "check map"
    pylab.ion()
    rospy.init_node('check_map')
    rospy.Subscriber("/entropy_descriptor_driver_node/wrinkled_map", heat_map, show_map)
    rospy.spin()
    
    
    
    
    
    
    

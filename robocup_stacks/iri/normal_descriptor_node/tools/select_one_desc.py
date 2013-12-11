import roslib; roslib.load_manifest('normal_descriptor_node')
import sys
import rospy
from sensor_msgs.msg import PointCloud2, Image
from normal_descriptor_node.msg import ndesc, ndesc_pc
import numpy,pylab

class node_select_one_desc:
    
    def __init__(self):
        print "init node_select_one_desc"

    def listener(self):
        rospy.init_node("select_one_desc")
        self.sub = rospy.Subscriber("select_one_desc/ndescs_pc", ndesc_pc, self.callback_desc)
        self.pub = rospy.Publisher("select_one_desc/one_desc", ndesc)
        rospy.spin()
        
    def callback_desc(self, data):
        # get descriptor
        print data.num
        self.pub.publish(data.descriptors[1000])

#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

if __name__ == '__main__':
    A = node_select_one_desc()
    A.listener()
    

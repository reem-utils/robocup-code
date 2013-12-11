import roslib; roslib.load_manifest('normal_descriptor_node')
import sys
import rospy
from sensor_msgs.msg import PointCloud2
from normal_descriptor_node.msg import ndesc, ndesc_pc

import numpy as np
from scipy.misc import toimage
import pylab
import struct

def get_pos_rgb_gray(data):
    resolution = (data.height, data.width)
    # 3D position for each pixel
    img = np.fromstring(data.data, np.float32)

    x = img[0::8].reshape(resolution)
    y = img[1::8].reshape(resolution)
    z = img[2::8].reshape(resolution) 
    rgb = img[4::8]
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
    x    = np.flipud(x)
    y    = np.flipud(y)
    z    = np.flipud(z)
    gray = (0.30*r+0.59*g+0.11*b).astype('uint8')
    return (x, y, z, r, g, b, toimage(np.array([r,g,b]).astype('uint8')))#gray)



class node_visualize_descs:
    
    def __init__(self):
        print "init node_visualize_descs"
        self.pcl = None
        #self.stamp_pcl = None
        self.desc_centroid = None
        #self.stamp_desc_centroid = None
        self.desc_selected = None
        #self.stamp_desc_selected = None
        #assuming static descriptor parameters!!
        self.nori=4
        self.nspa=4
        self.pixw=20


    def listener(self):
        pylab.ion()
        rospy.init_node('node_visualize_descs', anonymous=True)
        # GET SUBSCRIBERS!
        rospy.Subscriber("visualize_descs/rgb_pcl", PointCloud2, self.callback_get_pcl)
        rospy.Subscriber("visualize_descs/ndesc_center", ndesc, self.callback_center)
        rospy.Subscriber("visualize_descs/ndesc_desc", ndesc, self.callback_desc)
        rospy.spin()
        
    def callback_get_pcl(self, data):
        (x, y, z, r, g, b, gray) = get_pos_rgb_gray(data)
        self.pcl = (x, y, z, r, g, b, gray)
        #self.stamp_pcl = data.header.stamp
        #if not ( (self.stamp_pcl == self.stamp_desc_selected) and (self.stamp_pcl == self.stamp_desc_centroid) ):
        if self.desc_centroid==None or self.desc_selected==None:
            #print self.stamp_pcl, self.stamp_desc_selected, self.stamp_desc_centroid
            return
        self.callback()

    def callback_center(self, data):
        #get descriptor
        self.desc_centroid = data
        #self.stamp_desc_centroid = data.header.stamp
        #if not ( (self.stamp_pcl == self.stamp_desc_selected) and (self.stamp_pcl == self.stamp_desc_centroid) ):
        if self.pcl==None or self.desc_selected==None:
            return
        self.callback()


    def callback_desc(self, data):
        # get descriptor
        self.desc_selected=data
        #self.stamp_desc_selected = data.header.stamp        
        #if not ( (self.stamp_pcl == self.stamp_desc_selected) and (self.stamp_pcl == self.stamp_desc_centroid) ):
        if self.pcl==None or self.desc_centroid==None:
            #print self.stamp_pcl, self.stamp_desc_selected, self.stamp_desc_centroid
            return
        self.callback()


    def callback(self):
        print "visualizing"
        pylab.figure(1)
        pylab.cla()
        pylab.imshow(self.pcl[6])
        pylab.hold('on')
        self.visualize_box_in_image(self.desc_selected.u, self.desc_selected.v)
        pylab.draw()
        pylab.draw()

        pylab.figure(2)
        self.visualize_one_desc(np.array(self.desc_selected.descriptor))
        pylab.suptitle("Desc selected")
        pylab.draw()
        pylab.draw()

        pylab.figure(3)
        self.visualize_one_desc(np.array(self.desc_centroid.descriptor))
        pylab.suptitle("Desc centroid")
        pylab.draw()
        pylab.draw()
        self.desc_centroid=None
        self.desc_selected=None
        self.pcl=None
    #-----------------------------------

    def visualize_one_desc(self, npdescs):
        nori = self.nori
        nspa = self.nspa
        pylab.cla()
        offset=0
        vmin=np.min(npdescs)
        vmax=np.max(npdescs)
        for ix in range(1,nspa*nspa+1):
            pylab.subplot(nspa,nspa,ix)
            pylab.imshow(npdescs[offset:offset+nori*nori].reshape(nori,nori), interpolation='nearest',vmin=vmin, vmax=vmax)
            pylab.yticks(np.arange(-0.5,4.5,1),[str(np.round(a,2)) for a in np.arange(-np.pi,np.pi+np.pi/2.,2*np.pi/4.)])
            pylab.xticks(np.arange(-0.5,4.5,1),[str(np.round(a,2)) for a in np.arange(np.pi/2.,np.pi+np.pi/4.,np.pi/8.)])    
        #pylab.bar(np.arange(0,nori*nori),npdescs[i][offset:offset+nori*nori],width=0.2)
            print zip(np.arange(0,nori*nori),npdescs[offset:offset+nori*nori])
            offset+=nori*nori
    #-----------------------------

    def visualize_box_in_image(self, u, v):
        nspa = self.nspa
        pixw = self.pixw
        pylab.plot(np.array([[u-pixw,u-pixw,u-pixw,u+pixw],[u+pixw,u-pixw,u+pixw,u+pixw] ]), np.array([[v-pixw,v-pixw,v+pixw,v-pixw],[v-pixw,v+pixw,v+pixw,v+pixw]]),'b')
        for ix in range(1,nspa):
            pylab.plot(np.array([u-pixw, u+pixw]).T,np.array([(v-pixw) + ix*(2*pixw+1)/float(nspa),(v-pixw) + ix*(2*pixw+1)/float(nspa)]).T,'g')
            pylab.plot(np.array([(u-pixw) + ix*(2*pixw+1)/float(nspa),(u-pixw) + ix*(2*pixw+1)/float(nspa)]).T,np.array([v-pixw, v+pixw]).T,'g')
        pylab.plot(u,v,'*r')
    #-----------------------------


#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

if __name__ == '__main__':

    pylab.ion()
    A = node_visualize_descs()
    A.listener()


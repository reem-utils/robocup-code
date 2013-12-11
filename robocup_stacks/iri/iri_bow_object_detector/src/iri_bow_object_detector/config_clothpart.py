from config import Config
from glob import glob
import numpy as np

# Helper functions

def gen_bbox_from_poly(polys):
    if type(polys)==list:
        bboxes = []
        for poly in polys:
            top    = int(round(min(poly[:,1])))
            left   = int(round(min(poly[:,0])))
            bottom = int(round(max(poly[:,1])))
            right  = int(round(max(poly[:,0])))
            bboxes.append((left, top, right, bottom))
    else:
        top    = int(round(min(polys[:,1])))
        left   = int(round(min(polys[:,0])))
        bottom = int(round(max(polys[:,1])))
        right  = int(round(max(polys[:,0])))
        bboxes = (left, top, right, bottom)
    return bboxes
#-----

def set_default_vlfeat_sift(config, cluster_extra_str=''):
    config.det_prog='vlfeat'
    config.desc_format='siftgeo'
    config.clusterfile=config.basedir+'cluster/'+cluster_extra_str+'vlfeat_dense_k'+str(config.nb_centroids)+'.fvecs'

#####################################################################
# Global Config (all images)
#####################################################################    

class ClothPartConfig(Config):

    def __init__(self, basedir='/home/aramisa/datasets/ClothPartDataset/'):
        Config.__init__(self)
        self.basedir=basedir
        self.nimg=len(glob(self.basedir+'png/*.png'))
        print "Num imgs", self.nimg

    def img_filename(self,n):
        return "%s/png/n%05d.png"%(self.basedir,n)

    def mask_filename(self,n):
        return "%s/masks/n%05d.png"%(self.basedir,n)

    def pcd_filename(self,n):
        return "%s/pcd/n%05d.pcd"%(self.basedir,n)
    
    def desc_filename(self,n):
        return None


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#OTHERS

class ICRA13Config(ClothPartConfig):
    def __init__(self):
        ClothPartConfig.__init__(self,'/home/dmartinez/icra13/')
        self.basepath2='/home/dmartinez/icra13/'

    def desc_filename(self,n): 
        return self.basepath2+"/feats/sp4_o8_rad31_sample6/n%05d.ndesc"%n

    def mask2_filename(self,n):
        return self.basepath2+"/masks2/n%05d.png"%n

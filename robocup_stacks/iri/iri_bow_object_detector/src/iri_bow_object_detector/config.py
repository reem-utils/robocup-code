
import sys,os
import math

class Config:
    """
    Base config class. Largely inspired in bigimbaz.
    Must be able to return:
    - img filename
    - descriptor filename
    - detector/descriptor params
    - ...
    """
    
    def __init__(self):
        self.dbname=self.__class__.__name__[:-6]

        # detector/descriptor type and params:
        # [] 'lava'
        # [] 'opencv'
        # [] 'obsidian'
        # [] 'miko'
        # [] 'koen'
        self.det_prog='opencv'
        self.det_args=''


        # smalldesc type
        # [] BOF
        self.smalldesc_type='bof'

        # Pre-filter image
        # Used to restrict size and improve quality
        self.det_pre_filter=''
        self.det_pre_scale=None

        # Disk storage format for local descs
        # [] 'siftgeo'
        # [] 'geofvec'
        self.localdesc_format='siftgeo'
        

        # Disk storage format for smalldescs (it implies wether det params are also
        # saved):
        # [] 'fvecs'
        # [] 'opencv' (yaml.gz)
        # [] 'koen' ?
        # [] 'siftgeo'
        self.smalldesc_format='fvecs'
        
        # Cluster
        self.clusterfile=''
        self.nb_centroids=None #"Visual words" of the cluster
        self.descsize=None #Number of dimensions of the final descriptor (for SPM when available)
        self.ma_k=1 #for if I use multiple assignment in the furture, as of now, useless...

        # Use PCA compression (specifies filenameor None)
        self.pca = None
        
        ## The visual words part is not (also) implemented here (as opposed to the bigimbaz case)
    
        # blocked bofs
        self.block_size=1000
    
    # for pcl descriptors
        self.use_pcd = False

    # Find image and desc files
    def smalldesc_filename(self,n):
        pass
    def desc_filename(self,n):
        pass
    def img_filename(self,n):
        pass
    def vw_filename(self,n):
        pass
    def pcd_filename(self,n): #for pcl computers
        pass
    def gt_bbox(self, n, iclass):
        pass
    def thumb_filename(self,n):
        #no thumbnail by default
        return None
        

    #working with smalldescs in blocks
    def smalldesc_block_filename(self,n):
        pass
    def block_to_imno(self,b):
        n=b*self.block_size
        if n>self.nimg:
            return self.nimg
        else:
            return n
    def imno_to_block(self,n):
        if n>self.nimg:
            n=self.nimg
        b=math.floor(n/self.block_size)
        
    ## may be useful
    def display_name(self,n):
        return self.img_filename(n).split('/')[-1]
        
    def set_default_compute_descriptors(self):
        self.det_prog='miko'
        self.det_args="-hesaff -thres 500 -sift"
        #tbi
        #self.det_pre_filter=(
        #    'djpeg "%s" | ppmtopgm | '+
        #    'pnmnorm -bpercent=0.01 -wpercent=0.01 -maxexpand=400 |'+
        #    'pamscale -pixels $[1024*768] > "%s"')
        #self.det_pre_scale=('maxpix',1024*768)    
            
### select_config (taken from bigimbaz)            
def select_config(dbname):
  """
  returns a config object from a configuration name. The name can be
  either:
  - XXXX gives classname XXXXConfig which must be defined in
  this file
  - YYYY:XXXX loads XXXXConfig from imported module YYYY. To
  subclass the Config clas in module YYYY, import config
  - YYYY.py:XXXX is expanded as XXXXConfig class defined in file
  YYYY.py. Nothing special is needed to access the Config class: it is
  passed with the module name
  """
  if not dbname:
    sys.stderr.write("weird dbname %s\n"%dbname)
    sys.exit(1)

  if "(" in dbname and dbname[-1]==")":
    ba=dbname.index("(")
    dbsuff=dbname[ba:]
    dbargs=[eval(a) for a in dbname[ba+1:-1].split(',')]
    dbname=dbname[:ba]
  else:
    dbargs=()
    dbsuff=""

  if not dbname.endswith('Config'):
    dbname+="Config"

  if ':' not in dbname:
    try:
      # build config class and convert to object (=constructor)                                                                                              
      configclass=globals()[dbname]
    except KeyError:
      raise RuntimeError("unknown config %s\n"%dbname)
  else:
    colon=dbname.index(':')
    filename=dbname[:colon]
    classname=dbname[colon+1:]
    if '.' not in filename:
      if not filename.startswith('config_'): filename='config_'+filename
      # load from this directory                                                                                                                             
      locs={}
      mod=__import__(filename,globals(),locs)
      configclass=getattr(mod,classname)
    else:
      # load from arbitrary file                                                                                                                             
      globs=globals()
      execfile(filename,globs,globs)
      configclass=globs[classname]

  c=configclass(*dbargs)
  c.dbname=c.__class__.__name__[:-6]+dbsuff

  return c
    

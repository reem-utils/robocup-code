import numpy as np

import time
import pylab
from scipy import ndimage
import cv

import config_feats
import cPickle
from shogun.Classifier import LibSVM
from shogun.Features import RealFeatures

import ehbsw

#import ipdb


def local_maxima(array, min_distance = 1, periodic=False,
                 edges_allowed=True):
    """Find all local maxima of the array, separated by at least
    min_distance.
    adapted from = http://old.nabble.com/Finding-local-minima-of-greater-than-a-given-depth-td18988309.html"""
    array = np.asarray(array)
    cval = 0
    if periodic:
        mode = 'wrap'
    elif edges_allowed:
        mode = 'nearest'
    else:
        mode = 'constant'
        cval = array.max()+1
    nbhood=ndimage.morphology.generate_binary_structure(len(array.shape),2)
    maxima = array == ndimage.maximum_filter(array, footprint=nbhood, mode=mode, cval=cval)
    background = (array==0)
    eroded_background = ndimage.morphology.binary_erosion(
        background, structure=nbhood, border_value=1)
    maxima = maxima - eroded_background
    maxpy, maxpx = np.where(maxima)
    max_points = [(maxpy[i],maxpx[i]) for i in range(len(maxpy))]
    if not type(max_points)==list:
        max_points=[max_points]
    return max_points


def fit_window(heat_map, margin=10, min_dist_maxima=5):

    #remove NaN
    heat_map[np.isnan(heat_map)]=0
    #gauss filter to remove aliasing
    heat_map=ndimage.gaussian_filter(heat_map, 5)

    #suppress margin
    if margin>0:
        heat_map[:,:margin]=0
        heat_map[:,-margin:]=0
        heat_map[:margin,:]=0
        heat_map[-margin:,:]=0

    ind = local_maxima(heat_map, min_distance=min_dist_maxima)

    if len(ind)>0:
        ind = np.array(ind).astype('int64')
        #estimate cov :(
        #for now average window (145x140):
        hw=145/2
        hh=140/2
        win = [(x-hw, y-hh, x+hw, y+hh) for y,x in ind]

    else:
        win = []
    return ind, heat_map[ind[:,0],ind[:,1]], win

#---------


def prepare_feats(desc, l=2, as_shogun=False):
    if l==2: desc = np.sqrt(desc) #bias not afected by sqrt

    norms = np.apply_along_axis(np.linalg.norm, 0, desc[:-1,:], l) #leave bias alone

    np.seterr(divide='ignore', invalid='ignore')

    desc[:-1,:]=desc[:-1,:]/norms #leave bias alone
    np.seterr(divide='warn', invalid='warn')

    if l==1: desc=desc[:-1,:] #removing bias dim if L1 -> nonlinear TODO find better way...

    desc[np.isnan(desc)]=0 #handle NaNs
    if as_shogun:
        desc=RealFeatures(desc.astype('float'))
    return desc


def gen_windows_SWIG_wrapper(xstep=10, ystep=10, widthmin=100,
                             widthmax=170, widthstep=10, whratios=[0.5, 1, 1.5],
                             xmax=640, ymax=480):
    #upper bound
    maxboxes = len(whratios) * ((widthmax-widthmin)/widthstep) * (xmax/xstep) * (ymax/ystep)
    bboxes, used = ehbsw.gen_windows(maxboxes*4, xstep, ystep, widthmin, widthmax, widthstep, whratios, xmax, ymax)
    bboxes = bboxes[:used,:]
    return bboxes
    
def gen_windows(xstep=10, ystep=10, widthmin=100,
                widthmax=170, widthstep=10, whratios=[0.5, 1, 1.5],
                xmax=640, ymax=480):
    bboxes=[]
    for whr in whratios:
        for w in range(widthmin, widthmax, widthstep):
            h = w*whr
            for x in range(int(0+w/2), int(xmax-w/2), xstep):
                for y in range(int(0+h/2), int(ymax-h/2), ystep):
                    bboxes.append( (int(round(x-w/2)), int(round(y-h/2)),
                                    int(round(x+w/2)), int(round(y+h/2))) )
    return bboxes

def splash_as_box(hmap, x1, y1, x2, y2, score, normit):
    hmap[y1:y2][:,x1:x2] += score * np.ones((y2-y1, x2-x1))
    normit[y1:y2][:,x1:x2] += np.ones((y2-y1, x2-x1))

def create_robust_histograms(vws, bboxes, NUM_VWORDS):
    hs=create_histograms_SWIG_wrapper(vws, bboxes, NUM_VWORDS)
    valid=hs.sum(0)!=0
    hs=hs[:,valid]
    valid=list(valid.nonzero()[0])
    bboxes=[bboxes[i] for i in valid]
    return hs,bboxes

def create_histograms_SWIG_wrapper(vws, bboxes, NUM_VWORDS):
    nh = len(bboxes)
    mh = NUM_VWORDS[0]
    
    bboxes = np.array(bboxes)
    vws = np.array(vws[0])
    
    h = ehbsw.create_histograms(nh*mh, nh, mh, vws.astype(np.int32), bboxes.astype(np.float32))
    h.shape = (nh, mh)
    h=np.hstack((h,np.ones(h.shape[0])))
    return h.T

def create_histograms(vws, bboxes, NUM_VWORDS):
#deprecated!
    hh=None
    for i_feat in range(len(NUM_VWORDS)):
        h = np.zeros((NUM_VWORDS[i_feat], len(bboxes)))
        for i, bb in enumerate(bboxes):
            (x1, y1, x2, y2) = bb
            for geovw in vws[i_feat]:
                x, y, vw = geovw
                if x>=x1 and x<=x2 and y>=y1 and y<=y2:
                    h[vw,i] += 1
        if hh==None:
            hh=h
        else:
            hh=np.vstack((hh,h))
    hh=np.vstack((hh,np.ones(hh.shape[1])))
    return hh

#---------------- Non-linear classifier ----------------
def recode_win(w,xs,ys,xo,yo):
    x1,y1,x2,y2=w
    cx = xo + (x2+x1)/2
    cy = yo + (y2+y1)/2
    w = xs * (x2-x1)/2
    h = ys * (y2-y1)/2
    nx1 = int(round(cx-w/2))
    ny1 = int(round(cy-h/2))
    nx2 = int(round(cx+w/2))
    ny2 = int(round(cy+h/2))
    return (nx1,ny1,nx2,ny2)

def local_search_wins(win):
    #shape factors (x_scale, y_scale)
    shape_factors=[(1,1.25), (1,1), (1.25,1),
                   (1.25, 1.25), (1.4,1), (1, 1.4), (1.4, 1.4)]
    #position factors (offset_x, offset_y)
    position_factors=[(0,0),
        (-32,0),   (-24,0),  (-16,0),  (32,0),
        (24,0),    (16,0),   (0,-32),  (0,-24),
        (0,-16),   (0,32),   (0,24),   (0,16),
        (-8,-8),   (-8,8),   (8,-8),   (8,8),
        (-16,-16), (-16,16), (16,-16), (16,16),
        (-24,-24), (-24,24), (24,-24), (24,24)]
    wins2=[]

    for w in win:
        wins2.append([])
        for xs,ys in shape_factors:
            for xo,yo in position_factors:
                wins2[-1].append(recode_win(w,xs,ys,xo,yo))
    return wins2




#def detect_parallel(pack):
def detect_boxes(w, non_linear_svm_file, ima, mask, conf, vws):
    gt_bboxes = None
    bias = None

    iclass = 'polo_collar'
    NUM_VWORDS = conf.num_vwords

    if 0: # Without EHBSW
        start=time.time()
        bboxes = gen_windows(xstep=20, ystep=20, widthstep=20, xmax=mask.width, ymax=mask.height)
        hs,bboxes = create_robust_histograms(vws, bboxes, NUM_VWORDS)
        hs=prepare_feats(hs,2)
        scores = 1/(1+np.exp(-np.dot(w,hs)))

        for i,b in enumerate(bboxes):
            if conf.use_mask:
                if mask[int(round((b[3]+b[1])/2)), int(round((b[2]+b[0])/2))]<=0:
                    scores[i]=0

        heat_map = np.zeros((mask.height,mask.width))
        normit = np.zeros((mask.height,mask.width))
        for p, s in zip(bboxes, scores):
            (x1, y1, x2, y2) = p
            splash_as_box(heat_map, x1, y1, x2, y2, s, normit)

        np.seterr(divide='ignore', invalid='ignore')
        heat_map=np.divide(heat_map,normit)
        np.seterr(divide='warn', invalid='warn')

        if conf.verb >= 1: print "TIMESTAMP: done gen_windows ", time.time()-start

    if 1: #EHBSW
        start=time.time()
        width=mask.width
        height=mask.height
        vw_image = np.zeros((height, width)).astype('int32')

        for geovw in vws[0]: #[i_feat]
            x, y, vw = geovw
            vw_image[y,x]=vw+1

        scores=ehbsw.ehbsw_pownorm(width*height, vw_image, 55, w.astype('float32'))
        scores.shape=(height,width)

        if conf.verb >= 1: print "TIMESTAMP: done EHBSW gen_windows ", time.time()-start

        pylab.ion()
        pylab.figure(1)
        pylab.clf()
        scores=scores*mask/255.0
        pylab.imshow(scores)
        pylab.colorbar()
        #pylab.figure(2)
        #pylab.imshow(heat_map)
        #pylab.draw()
        #pylab.figure(3)
        #pylab.imshow(ima)
        pylab.draw()
        pylab.show()
        #wwwww=raw_input('asdf>')

        heat_map = scores






    if conf.merge_windows==True:
        ind, prob, win = fit_window(heat_map)
    else: # scores is directly probabilities at this point
        prob=scores
        win=bboxes

    if conf.refine_nonlinear and conf.merge_windows:
        #multiply_windows

        start=time.time()
        win2=local_search_wins(win)

        hsbbox2=[create_robust_histograms(vws, w2, NUM_VWORDS) for w2 in win2]
        if conf.verb >= 2: print time.time()-start, "TIMESTAMP: create_robust_histograms non linear."

        start=time.time()
        #load nonlinear class
        #pf=open(dconfig.nonlinear_classifier_filename(iclass), 'rb')
        pf=open(non_linear_svm_file, 'rb')
        svm = cPickle.load(pf)
        chi2_width = cPickle.load(pf)
        AA = cPickle.load(pf)
        BB = cPickle.load(pf)
        pf.close()

        #eval new windows
        win=[]
        prob=[]
        for hs2, bboxes2 in hsbbox2:
            scores2 = svm.apply(prepare_feats(hs2,1,as_shogun=True)).get_labels()
            scores2 = scores2*AA+BB
            sel_neg = (scores2<0).nonzero()
            sel_pos = (scores2>=0).nonzero()
            scores2[sel_neg] = 1.0/(1.0+np.exp(scores2[sel_neg]))
            scores2[sel_pos] = np.exp(-scores2[sel_pos])/(1.0+np.exp(-scores2[sel_pos]))
            #pick one/few best
            orderscores2 = [(ii,s) for ii,s in enumerate(scores2)]
            orderscores2.sort(key=lambda x: x[1], reverse=True)
            win.append(bboxes2[orderscores2[0][0]])
            prob.append(orderscores2[0][1])
        if conf.single_pred==True:
            i=np.argmax(prob)
            win=[win[i]]
            prob=[prob[i]]
        if conf.verb >= 2: print time.time()-start, "TIMESTAMP: non linear svm."


    ## Save bboxes
    #apply mask
    # TODO add more filtering (maybe based on score?)
    win2=[]
    prob2=[]
    for w,p in zip(win,prob):
        if ((w[3]<mask.height and w[1]>=0 and w[2]<mask.width and w[0]>=0)
            and mask[int(round((w[3]+w[1])/2)), int(round((w[2]+w[0])/2))]>0):
            win2.append(w)
            prob2.append(p)

    win=win2
    prob=prob2


    if len(prob)>0:
        maxprob=max(prob)
        minprob=min(prob)
    for ii,wi in enumerate(win):
        if minprob==maxprob: wi_color = 255
        else:                wi_color = int(np.round(255*((prob[ii]-minprob)/(maxprob-minprob))))
        cv.Rectangle(ima,(wi[0],wi[1]), (wi[2],wi[3]), (wi_color,0,0), 3)

    #cv.ShowImage("Bow detector", ima)
    #cv.WaitKey(1000)


    return (win, prob)


    # TODO
    # borrar ventanas con baja prob



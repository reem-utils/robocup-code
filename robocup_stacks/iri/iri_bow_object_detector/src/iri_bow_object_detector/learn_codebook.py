import sys
import os

import pylab
import numpy as np
from load_ndesc import load_ndesc_pc
from scipy import cluster
import random
from config import select_config
import cPickle
from yael import yael
from shogun.Classifier import LibLinear, LibSVM
from shogun.Features import RealFeatures, Labels
from shogun.Kernel import Chi2Kernel
import cv2

def load_descs(config, i, norm=1, old_desc=False, invert_mask=False, use_masks2=0):
    fname = config.desc_filename(i)
    mask_name = config.mask_filename(i)
    mask      = pylab.imread(mask_name)
    descs     = load_ndesc_pc(fname, norm=norm, old_desc=old_desc)
    if use_masks2==0:
        descs     = [l for l in descs if bool(mask[l.v,l.u])!=bool(invert_mask)]
    elif use_masks2==1:
        mask2 = pylab.imread(config.mask2_filename(i))
        descs = [l for l in descs if bool(mask2[l.v,l.u])]
    elif use_masks2==2:
        mask2 = pylab.imread(config.mask2_filename(i))
        descs = [l for l in descs if not(mask2[l.v,l.u].astype('bool')) and mask[l.v,l.u].astype('bool')]
    return descs
    
def sel_descs(config, imnos, ratio_keep, norm=1, old_desc=False, invert_mask=False, use_masks2=0):
    sel_desc  = [] 

    for i in imnos:
        descs = load_descs(config, i, norm=norm, old_desc=old_desc, invert_mask=invert_mask, use_masks2=use_masks2)
        sel_desc.extend([l for l in descs if np.random.rand()<=ratio_keep])
        if not i%10: print i, len(sel_desc)
    print "selected", len(sel_desc), "descriptors"
    return np.array([l.desc for l in sel_desc]), sel_desc

def norm_descs(descs, l=1):
    print descs.shape
    norms = np.apply_along_axis(np.linalg.norm, 0, descs, l) #leave bias alone
    print sum(norms==0)
    descs/=norms
    descs[np.isnan(descs)]=0
    descs=np.sqrt(descs)
    return descs

def visualize_classes(svm, config, imnos):
    
    for n in imnos:
        # TODO BEGIN
        descs, origdescs = sel_descs(config, [n], 1)
        descs = norm_descs(descs)
        #print descs
        print descs.shape
        descs=RealFeatures(descs.T)
        out=svm.apply(descs)
        print out.get_labels()
        # TODO END
        origdescs_F=[o for o,x in zip(origdescs,out.get_labels()) if x>0]
        ima=pylab.imread(config.img_filename(n))
        #visualize_descs(ima, origdescs_F)
        convert_to_heatmap(ima, origdescs, out.get_labels())

def convert_to_heatmap(ima, descs, sco):
    imabw=np.zeros((ima.shape[0],ima.shape[1])).astype('uint8')
    imabw=cv2.cvtColor(ima,cv2.COLOR_RGB2GRAY)
    imabw2=np.zeros((ima.shape[0]/6,ima.shape[1]/6)).astype('uint8')
    imabw=(255*imabw).astype('uint8')
    imabw2=cv2.resize(src=imabw,dsize=(ima.shape[1]/6,ima.shape[0]/6),interpolation=cv2.INTER_LINEAR)
    edges=cv2.Canny(imabw2,50,60)        

    maxp=None
    maxpsco=None
    shape = ima.shape
    scores = min(sco)*np.ones((shape[0]/6,shape[1]/6))
    for s,desc in zip(sco,descs):
        u = desc.u/6
        v = desc.v/6
        if maxp==None or maxpsco<s:
            maxp=(desc.u,desc.v)
            maxpsco=s
        if edges[v,u]!=0:
            scores[v,u]=np.nan
        else:
            scores[v,u]=s
    cmap=pylab.cm.jet #spectral
    cmap.set_bad('black',1.)
    masked_array = np.ma.masked_where(np.isnan(scores), scores)
    
    pylab.imshow(masked_array, cmap=cmap)
    pylab.colorbar()
    pylab.figure()
    pylab.imshow(ima)
    print maxp[0], maxp[1], "WTRGAR"
    pylab.hold(True)
    pylab.plot(maxp[0], maxp[1], 'y*', markersize=15)
    pylab.show()

# TODO delete?
def visualize_descs(ima, descs):
    pylab.imshow(ima)
    pylab.hold(1)
    for desc in descs:
        u = desc.u 
        v = desc.v
        pylab.plot(u,v,'r*')
    pylab.show()
    #raw_input('sss')


# TODO delete?
def visualize_box_in_image(desc, nspa, pixw):
    u = desc.u 
    v = desc.v
    pylab.plot(np.array([[u-pixw,u-pixw,u-pixw,u+pixw],[u+pixw,u-pixw,u+pixw,u+pixw] ]), np.array([[v-pixw,v-pixw,v+pixw,v-pixw],[v-pixw,v+pixw,v+pixw,v+pixw]]),'r')
    for ix in range(1,nspa):
        pylab.plot(np.array([u-pixw, u+pixw]).T,np.array([(v-pixw) + ix*(2*pixw+1)/float(nspa),(v-pixw) + ix*(2*pixw+1)/float(nspa)]).T,'g')
        pylab.plot(np.array([(u-pixw) + ix*(2*pixw+1)/float(nspa),(u-pixw) + ix*(2*pixw+1)/float(nspa)]).T,np.array([v-pixw, v+pixw]).T,'g')
    pylab.plot(u,v,'*r')


# TODO delete?
def visualize_desc(descs, npdescs, ima, nori, nspa,pixw=15):
    pylab.ion()
    seldescs = range(len(descs))
    random.shuffle(seldescs)
    once=False
    cbar=None
    for i in seldescs: 
        print descs[i].u, descs[i].v, i
        pylab.figure(1)
        pylab.cla()
        pylab.imshow(ima)
        pylab.hold('on')
        visualize_box_in_image(descs[i], nspa, pixw)

        pylab.figure(2)
        visualize_one_desc(npdescs[i], nori, nspa)
        #pylab.cla()
        # offset=0
        # for ix in range(1,nspa*nspa+1):
        #     pylab.subplot(nspa,nspa,ix)
        #     pylab.imshow(npdescs[i][offset:offset+nori*nori].reshape(nori,nori), interpolation='nearest',vmin=vmin, vmax=vmax)
        #     pylab.yticks(np.arange(-0.5,4.5,1),[str(np.round(a,2)) for a in np.arange(-np.pi,np.pi+np.pi/2.,2*np.pi/4.)])
        #     pylab.xticks(np.arange(-0.5,4.5,1),[str(np.round(a,2)) for a in np.arange(np.pi/2.,np.pi+np.pi/4.,np.pi/8.)])
        
            
        #     #pylab.bar(np.arange(0,nori*nori),npdescs[i][offset:offset+nori*nori],width=0.2)
        #     print zip(np.arange(0,nori*nori),npdescs[i][offset:offset+nori*nori])
        #     offset+=nori*nori
        # if once==False:
        #     cbar=pylab.colorbar()
        #     once=True
        # else:
        #     pass #cbar.update_normal()
        pylab.show()

        c=raw_input(">")
        if c=='q':
            break

#def visualize_desc2(desc, nori, nspa):

def run_on_images(config,centroids,sel_i,imnos,select_mode=None, nspa=4,nori=4,pixw=15):
    colors=['*r','*g','*b','*k','*c','or','og','ob','ok','oc']
    for i in imnos:
        pylab.figure(1)
        pylab.cla()
        ima_name = config.img_filename(i)
        ima = pylab.imread(ima_name)
        
        descs = load_descs(config, i, old_desc=True)
        descs_feats = np.array([x.desc for x in descs])
        #visualize_desc(descs, descs_feats, pylab.imread(config.img_filename(i)), nori=4,nspa=4,pixw=20)
        assign=cluster.vq.vq(robust_whiten(descs_feats),centroids[0])
        pylab.cla()
        pylab.imshow(ima)
        pylab.hold('on')
        if select_mode==None:
            for i in range(len(descs)):
            #if assign[1][i]>centroids[1]*0.8:
                if assign[0][i]!=sel_i:
                    continue
                pylab.plot(descs[i].u,descs[i].v,colors[0]) #colors[assign[0][i]])
        elif select_mode=='closest':
            sel = (assign[0]==sel_i).nonzero()
            if not len(sel[0])==0:
                print "se",sel, assign[1][sel[0]]
                best=np.argmin(assign[1][sel[0]])
                print best
                visualize_box_in_image(descs[sel[0][best]], nspa, pixw)
                #pylab.plot(descs[sel[0][best]].u,descs[sel[0][best]].v,colors[0],markersize=15)
            else:
                print "NONE FOUND"
        elif select_mode=='highest':
            pass
        pylab.show()
        c=raw_input('t')
        if c=='q':
            break


if __name__=="__main__":
    args=sys.argv[1:]
    
    todo=[]
    dbname="none"
    im_begin=0
    im_end=-1
    n_thread=1
    imnos=None
    verb=False
    max_desc=200*1000
    k=25
    ratio_keep=0.2
    outfile="tmp.txt"
    infile=None
    hand_pick=False
    save_center=False
    use_masks2=1
    while args:
        a=args.pop(0)
        if a in ['-h','--help']:      usage()
        elif a=='-v':                 verb=True
        elif a=='-db':                dbname=args.pop(0)
        elif a=='-begin':             im_begin=int(args.pop(0))
        elif a=='-end':               im_end=int(args.pop(0))
        elif a=='-imnos':             imnos=[int(x) for x in args.pop(0).split(',')]
        elif a=='-nt':                n_thread=parse_nt(args.pop(0))
        elif a=='-max_desc':          max_desc=int(args.pop(0))
        elif a=='-k':                 k=int(args.pop(0))
        elif a=='-keep':              ratio_keep=float(args.pop(0))
        elif a=='-outfile':           outfile=args.pop(0)
        elif a=='-infile':            infile=args.pop(0)
        elif a=='-hand_pick':         hand_pick=True
        elif a=='-save':              save_center=True
        #elif a=='-mask2':             use_masks2=1
        else:
            sys.stderr.write("unknown arg %s\n"%a)
            usage()
            sys.exit(-1)
        
    config=select_config(dbname)
    keepvecs=[]

    ## LEARN CENTROIDS
    if im_end==-1: im_end=config.nimg
    if im_end>config.nimg:
        sys.stderr.write("warn: forcing -end to %i"%config.nimg)
        im_end=config.nimg
    if imnos == None:
        imnos=range(im_begin, im_end)
    descs, origdescs = sel_descs(config, imnos, ratio_keep, use_masks2=use_masks2)
    #if use_masks2>0:
    #descs_neg, origdescs_neg = sel_descs(config, [3], ratio_keep, use_masks2=2)
    #visualize_descs(pylab.imread(config.img_filename(3)), origdescs_neg)
    descs_neg, origdescs_neg = sel_descs(config, imnos, ratio_keep, use_masks2=2)
    #SVM
    npos = descs.shape[0]
    sel = range(descs_neg.shape[0])
    random.shuffle(sel)
    sel = sel[:npos]

    feats = np.vstack((descs.astype('float64'), descs_neg[sel].astype('float64')))
    feats = norm_descs(feats)
    feats = RealFeatures(feats.T)
    labels = Labels(np.hstack((np.ones((1,descs.shape[0])), -1*np.ones((1,len(sel)))))[0])

    svm = LibLinear(1, feats, labels)
    #k = Chi2Kernel(feats,feats, 1.0, 100)
    #svm = LibSVM(1, k, labels)
    svm.train()
    visualize_classes(svm, config, range(max(imnos),config.nimg))
    
    print "Writting SVM"
    pf=open('last_classifier.pkl','w')
    cPickle.dump(svm, pf)
    pf.close()
    
    
    #VISUALIZE CLASSES
    #pylab.ion()
    #for i in range(len(centroids[0])):
        #pylab.figure(2)
        #visualize_one_desc(centroids[0][i],nori=4,nspa=4)
        #pylab.draw()
        #pylab.draw()
    ##     pylab.cla()
    ##     pylab.bar(range(0,centroids[0][i].shape[0]),centroids[0][i])
    ##     pylab.show()
        #c=raw_input('w')
        #while c=='t':
            #pylab.figure(1)
            #pylab.cla()
            #run_on_images(config,centroids,i,imnos,select_mode='closest',nspa=4,nori=4,pixw=20)
            #c=raw_input('w')
            #if c=='k':
                #keepvecs.append(i)
    #if save_center:
        #np.savetxt(outfile+'.selected',np.array(keepvecs))


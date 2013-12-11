import sys


# class config:
#     basepath='/home/aramisa/datasets/PoloDataset/'
#     num_vwords=[1024]
#     test_list='lists/test50_blau.txt'
#     det_prob=0.4
#     min_overlap=0.5
#     gt_file='gt/necks_iripolo.txt'
#     merge_windows=False
#     verb=True
#     refine_nonlinear=False

class config:
    width=640
    height=480
    basepath='/home/dmartinez/experimentos/polo_live/' #'/home/aramisa/datasets/PoloDataset12/'
    num_vwords=[1024]
    det_prob=0.4
    min_overlap=0.5
    train_list='gt/necks_iripolo.txt'
    gt_file='gt/necks_iripolo.txt'
    merge_windows=False
    verb=2
    refine_nonlinear=False
    #neg_windows='full'
    neg_windows='random'
    single_pred=False
    use_mask=False

class polo_live(config):
    def __init__(self):
        k_gih='64'
        k_sift='128'
        self.vectors_suffix='_gih_features_k'+k_gih+'_lava_dense_sift_'+k_sift
        self.words_path=['tmp/gih/', 'tmp/sift/']
        self.classifier_suffix='_gih_features_'+k_gih+'_lava_dense_sift_'+k_sift
        self.det_results_dir='detect_v3_results_gih_features_k'+k_gih+'_lava_dense_sift_k'+k_sift+'/'
        self.num_vwords=[int(k_gih),int(k_sift)]
        self.merge_windows=True
        #self.min_overlap=0.4
        self.refine_nonlinear=True

class polo_live_sift(config):
    def __init__(self):
        k_sift='128'
        self.vectors_suffix='_sift_k'+k_sift
        self.words_path=['tmp/sift/']
        self.classifier_suffix='_dense_sift_'+k_sift
        self.det_results_dir='detect_v3_results_lava_dense_sift_k'+k_sift+'/'
        self.num_vwords=[int(k_sift)]
        self.merge_windows=True
        #self.min_overlap=0.4
        self.refine_nonlinear=True
        self.use_mask=True

if len(sys.argv)>1:
    if '(' in sys.argv[1]:
        func=sys.argv[1].split('(')[0]
        args=sys.argv[1].split('(')[1].split(')')[0]
        if ',' in args:
            args=args.split(',')
        else:
            args=[args]
        print args

        object = globals()[func]
        conf=object(*args)
    else:
        object = globals()[sys.argv[1]]
        conf=object()
else:
#conf=config_fpfh()
#conf=config_sift()
#conf=config_fpfh_sift()
#conf=config_fpfh_sift_v3_test_others()
#conf=config_sift_v3()
#conf=config_fpfh_v3()
#conf=config_fpfh_v3_test_others()
#conf=config_hks_sparse()
#conf=config_hks_sparse_v3()
#conf=config_sift_hks_sparse()
#conf=config_sift_hks_sparse_v3()
    conf=config_hks_basic_time()
#conf=config_hks_basic_time_v3()

%module ehbsw
%{
  #define SWIG_FILE_WITH_INIT
  void ehbsw_pownorm(float* scores, int dim_out, int* vw_ima, int height_in, int width_in, int half_win_size, int d, float* classifier);
  void create_histograms(float* h, int nmh, int nh, int mh, int* vws, int nvw, int mvw, float* bboxes, int nbboxes, int mbboxes);
  void gen_windows(float *bboxes_gw, int nmbboxes_gw, int* used, int xstep, int ystep, int widthmin, int widthmax, int widthstep, float *whratios, int nwhratios, int xmax, int ymax);
%}

%include "numpy.i"
%include "typemaps.i"
%init %{
  import_array();
  %}

%apply (int* IN_ARRAY2, int DIM1, int DIM2) {(int* vw_ima, int height_in, int width_in)}
%apply (int DIM1, float* IN_ARRAY1) {(int d, float* classifier)}
%apply (float* ARGOUT_ARRAY1, int DIM1) {(float* scores, int dim_out)}

/* %rename (ehbsw_pownorm) my_ehbsw_pownorm; */
/* %exception my_ehbsw_pownorm { */
/*   $action */
/*     if (PyErr_Occurred()) SWIG_fail; */
/*  } */

/* %inline %{ */
/*   void my_ehbsw_pownorm(float* scores, int width_out, int height_out, int* vw_ima, int width_in, int height_in, int half_win_size, int d, float *classifier) { */
/*     if ((width_in!=width_out) || (height_in!=height_out)) { */
/*       PyErr_Format(PyExc_ValueError,"Arrays of lengths (%d,%d), (%d,%d) given",width_in, height_in, width_out, height_out); */
/*     } */
/*     return ehbsw_pownorm(scores, vw_ima, width_in, height_in, half_win_size, d, classifier); */
/*   } */
/* %} */

void ehbsw_pownorm(float *scores, int dim_out, int* vw_ima, int height_in, int width_in, int half_win_size, int d, float* classifier);
%clear (int* vw_ima, int height_in, int width_in);
%clear (int d, float* classifier);
%clear (float* scores, int dim_out);


%apply (int* IN_ARRAY2, int DIM1, int DIM2) {(int* vws, int nvw, int mvw)}
%apply (float* IN_ARRAY2, int DIM1, int DIM2) {(float* bboxes, int nbboxes, int mbboxes)}
%apply (float* ARGOUT_ARRAY1, int DIM1) {(float* h, int nmh)}
void create_histograms(float* h, int nmh, int nh, int mh, int* vws, int nvw, int mvw, float* bboxes, int nbboxes, int mbboxes);
%clear (int* vws, int nvw, int mvw);
%clear (float* bboxes, int nbboxes, int mbboxes);
%clear (float* h, int nmh);


%apply (float* ARGOUT_ARRAY1, int DIM1) {(float* bboxes_gw, int nmbboxes_gw)}
%apply int *OUTPUT {int *used}
%apply (float* IN_ARRAY1, int DIM1) {(float* whratios, int nwhratios)}
void gen_windows(float *bboxes_gw, int nmbboxes_gw, int *used,  int xstep, int ystep, int widthmin, int widthmax, int widthstep, float *whratios, int nwhratios, int xmax, int ymax);
%clear (float* bboxes_gw, int nmbboxes_gw);
%clear (float* whratios, int nwhratios);
%clear int *OUTPUT;

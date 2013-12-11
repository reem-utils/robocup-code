/** @file dsift.h
 ** @brief Dense SIFT (@ref dsift)
 ** @author Andrea Vedaldi
 ** @author Brian Fulkerson
 **/

/*
Copyright (C) 2007-12 Andrea Vedaldi and Brian Fulkerson.
All rights reserved.

This file is part of the VLFeat library and is made available under
the terms of the BSD license (see the COPYING file).
*/

#ifndef VL_DSIFT_H
#define VL_DSIFT_H

//#include "generic.h"
#include <emmintrin.h>
#include <assert.h>

// various defines
#define VL_INLINE static __inline__
#define VL_EXPORT extern "C"
#define VL_EPSILON_F 1.19209290E-07F

typedef int vl_bool ;    /**< @brief Boolean. */

#define VL_TRUE 1   /**< @brief @c true (1) constant */
#define VL_FALSE 0  /**< @brief @c false (0) constant */
#define VL_TRANSPOSE         (0x1 << 2) /**< @brief Transpose result. */
#define VL_PAD_BY_CONTINUITY (0x1 << 0) /**< @brief Pad by continuity. */
#define VL_PAD_BY_ZERO       (0x0 << 0) /**< @brief Pad with zeroes. */
#define VL_PAD_MASK          (0x3)      /**< @brief Padding field selector. */
#define VSIZE  4
#define VSFX   s
#define VTYPE  __m128
#define VALIGNED(x) (! (((vl_uintptr)(x)) & 0xF))

#define VL_PI 3.141592653589793
#define VL_MAX(x,y) (((x)>(y))?(x):(y))
#define VL_MIN(x,y) (((x)<(y))?(x):(y))

#define VSTZ  _mm_setzero_ps
#define VADD  _mm_add_ps
#define VLD1 _mm_load1_ps
#define VMUL  _mm_mul_ps

// jic
/* #define VMAX  VL_XCAT(_mm_max_p,     VSFX) */
/* #define VDIV  VL_XCAT(_mm_div_p,     VSFX) */
/* #define VSUB  VL_XCAT(_mm_sub_p,     VSFX) */
/* #define VLDU  VL_XCAT(_mm_loadu_p,   VSFX) */
/* #define VST1  VL_XCAT(_mm_store_s,   VSFX) */
/* #define VSET1 VL_XCAT(_mm_set_s,     VSFX) */
/* #define VSHU  VL_XCAT(_mm_shuffle_p, VSFX) */
/* #define VNEQ  VL_XCAT(_mm_cmpneq_p,  VSFX) */
/* #define VAND  VL_XCAT(_mm_and_p,     VSFX) */
/* #define VANDN VL_XCAT(_mm_andnot_p,  VSFX) */

typedef long long           vl_int64 ;   /**< @brief Signed 64-bit integer. */
typedef long long unsigned  vl_uint64 ;  /**< @brief Unsigned 64-bit integer. */
typedef vl_uint64           vl_uintptr ; /**< @brief Unsigned integer holding a pointer. */
typedef vl_uint64           vl_size ;    /**< @brief Unsigned integer holding the size of a memory block. */
typedef int                 vl_int32 ;   /**< @brief Signed 32-bit integer. */
typedef vl_int64            vl_index ;   /**< @brief Signed version of ::vl_size and ::vl_uindex */


// Imported functions from other modules
/** @name Image convolution 
** @{ */
void vl_imconvcol_vf (float* dst, int dst_stride,
                      float const* src,
                      int src_width, int src_height, int src_stride,
                      float const* filt, int filt_begin, int filt_end,
                      int step, unsigned int flags) ;

void vl_imconvcoltri_f(float * dest, vl_size destStride,
		       float const * image,
		       vl_size imageWidth, vl_size imageHeight, vl_size imageStride,
		       vl_size filterSize,
		       vl_size step, unsigned int flags) ;


VL_INLINE float
vl_abs_f (float x)
{
// deactivated for precaution...
//#ifdef VL_COMPILER_GNUC
  return __builtin_fabsf (x) ;
//#else
//  return fabsf(x) ;
//#endif
}

VL_INLINE float
vl_mod_2pi_f (float x)
{
  while (x > (float)(2 * VL_PI)) x -= (float) (2 * VL_PI) ;
  while (x < 0.0F) x += (float) (2 * VL_PI);
  return x ;
}

VL_INLINE long int
vl_floor_f (float x)
{
  long int xi = (long int) x ;
  if (x >= 0 || (float) xi == x) return xi ;
  else return xi - 1 ;
}

VL_INLINE float
vl_fast_resqrt_f (float x)
{
  /* 32-bit version */
  union {
    float x ;
    vl_int32  i ;
  } u ;

  float xhalf = (float) 0.5 * x ;

  /* convert floating point value in RAW integer */
  u.x = x ;

  /* gives initial guess y0 */
  u.i = 0x5f3759df - (u.i >> 1);
  /*u.i = 0xdf59375f - (u.i>>1);*/

  /* two Newton steps */
  u.x = u.x * ( (float) 1.5  - xhalf*u.x*u.x) ;
  u.x = u.x * ( (float) 1.5  - xhalf*u.x*u.x) ;
  return u.x ;
}

VL_INLINE float
vl_fast_sqrt_f (float x)
{
  return (x < 1e-8) ? 0 : x * vl_fast_resqrt_f (x) ;
}

VL_INLINE float
vl_fast_atan2_f (float y, float x)
{
  float angle, r ;
  float const c3 = 0.1821F ;
  float const c1 = 0.9675F ;
  float abs_y    = vl_abs_f (y) + VL_EPSILON_F ;

  if (x >= 0) {
    r = (x - abs_y) / (x + abs_y) ;
    angle = (float) (VL_PI / 4) ;
  } else {
    r = (x + abs_y) / (abs_y - x) ;
    angle = (float) (3 * VL_PI / 4) ;
  }
  angle += (c3*r*r - c1) * r ;
  return (y < 0) ? - angle : angle ;
}





/// DSIFT H


/** @brief Dense SIFT keypoint */
typedef struct VlDsiftKeypoint_
{
  double x ; /**< x coordinate */
  double y ; /**< y coordinate */
  double s ; /**< scale */
  double norm ; /**< SIFT descriptor norm */
} VlDsiftKeypoint ;

/** @brief Dense SIFT descriptor geometry */
typedef struct VlDsiftDescriptorGeometry_
{
  int numBinT ;  /**< number of orientation bins */
  int numBinX ;  /**< number of bins along X */
  int numBinY ;  /**< number of bins along Y */
  int binSizeX ; /**< size of bins along X */
  int binSizeY ; /**< size of bins along Y */
} VlDsiftDescriptorGeometry ;

/** @brief Dense SIFT filter */
typedef struct VlDsiftFilter_
{
  int imWidth ;            /**< @internal @brief image width */
  int imHeight ;           /**< @internal @brief image height */

  int stepX ;              /**< frame sampling step X */
  int stepY ;              /**< frame sampling step Y */

  int boundMinX ;          /**< frame bounding box min X */
  int boundMinY ;          /**< frame bounding box min Y */
  int boundMaxX ;          /**< frame bounding box max X */
  int boundMaxY ;          /**< frame bounding box max Y */

  /** descriptor parameters */
  VlDsiftDescriptorGeometry geom ;

  int useFlatWindow ;      /**< flag: whether to approximate the Gaussian window with a flat one */
  double windowSize ;      /**< size of the Gaussian window */

  int numFrames ;          /**< number of sampled frames */
  int descrSize ;          /**< size of a descriptor */
  VlDsiftKeypoint *frames ; /**< frame buffer */
  float *descrs ;          /**< descriptor buffer */

  int numBinAlloc ;        /**< buffer allocated: descriptor size */
  int numFrameAlloc ;      /**< buffer allocated: number of frames  */
  int numGradAlloc ;       /**< buffer allocated: number of orientations */

  float **grads ;          /**< gradient buffer */
  float *convTmp1 ;        /**< temporary buffer */
  float *convTmp2 ;        /**< temporary buffer */
}  VlDsiftFilter ;

VlDsiftFilter *vl_dsift_new (int width, int height) ;
VlDsiftFilter *vl_dsift_new_basic (int width, int height, int step, int binSize) ;
void vl_dsift_delete (VlDsiftFilter *self) ;
void vl_dsift_process (VlDsiftFilter *self, float const* im) ;
VL_INLINE void vl_dsift_transpose_descriptor (float* dst,
                                             float const* src,
                                             int numBinT,
                                             int numBinX,
                                             int numBinY) ;

/** @name Setting parameters
 ** @{
 **/
VL_INLINE void vl_dsift_set_steps (VlDsiftFilter *self,
                                  int stepX,
                                  int stepY) ;
VL_INLINE void vl_dsift_set_bounds (VlDsiftFilter *self,
                                   int minX,
                                   int minY,
                                   int maxX,
                                   int maxY) ;
VL_INLINE void vl_dsift_set_geometry (VlDsiftFilter *self,
                                      VlDsiftDescriptorGeometry const* geom) ;
VL_INLINE void vl_dsift_set_flat_window (VlDsiftFilter *self, vl_bool useFlatWindow) ;
VL_INLINE void vl_dsift_set_window_size (VlDsiftFilter *self, double windowSize) ;
/** @} */

/** @name Retrieving data and parameters
 ** @{
 **/
VL_INLINE float const    *vl_dsift_get_descriptors     (VlDsiftFilter const *self) ;
VL_INLINE int             vl_dsift_get_descriptor_size (VlDsiftFilter const *self) ;
VL_INLINE int             vl_dsift_get_keypoint_num    (VlDsiftFilter const *self) ;
VL_INLINE VlDsiftKeypoint const *vl_dsift_get_keypoints (VlDsiftFilter const *self) ;
VL_INLINE void            vl_dsift_get_bounds          (VlDsiftFilter const *self,
                                                       int* minX,
                                                       int* minY,
                                                       int* maxX,
                                                       int* maxY) ;
VL_INLINE void            vl_dsift_get_steps           (VlDsiftFilter const* self,
                                                       int* stepX,
                                                       int* stepY) ;
VL_INLINE VlDsiftDescriptorGeometry const* vl_dsift_get_geometry (VlDsiftFilter const *self) ;
VL_INLINE vl_bool         vl_dsift_get_flat_window     (VlDsiftFilter const *self) ;
VL_INLINE double          vl_dsift_get_window_size     (VlDsiftFilter const *self) ;
/** @} */


void _vl_dsift_update_buffers (VlDsiftFilter *self) ;

/** ------------------------------------------------------------------
 ** @brief Get descriptor size.
 ** @param self DSIFT filter object.
 ** @return size of a descriptor.
 **/

int
vl_dsift_get_descriptor_size (VlDsiftFilter const *self)
{
  return self->descrSize ;
}

/** ------------------------------------------------------------------
 ** @brief Get descriptors.
 ** @param self DSIFT filter object.
 ** @return descriptors.
 **/

float const *
vl_dsift_get_descriptors (VlDsiftFilter const *self)
{
  return self->descrs ;
}

/** ------------------------------------------------------------------
 ** @brief Get keypoints
 ** @param self DSIFT filter object.
 **/

VlDsiftKeypoint const *
vl_dsift_get_keypoints (VlDsiftFilter const *self)
{
  return self->frames ;
}

/** ------------------------------------------------------------------
 ** @brief Get number of keypoints
 ** @param self DSIFT filter object.
 **/

int
vl_dsift_get_keypoint_num (VlDsiftFilter const *self)
{
  return self->numFrames ;
}

/** ------------------------------------------------------------------
 ** @brief Get SIFT descriptor geometry
 ** @param self DSIFT filter object.
 ** @return DSIFT descriptor geometry.
 **/

VlDsiftDescriptorGeometry const* vl_dsift_get_geometry (VlDsiftFilter const *self)
{
  return &self->geom ;
}

/** ------------------------------------------------------------------
 ** @brief Get bounds
 ** @param self DSIFT filter object.
 ** @param minX bounding box minimum X coordinate.
 ** @param minY bounding box minimum Y coordinate.
 ** @param maxX bounding box maximum X coordinate.
 ** @param maxY bounding box maximum Y coordinate.
 **/

void
vl_dsift_get_bounds (VlDsiftFilter const* self,
                    int *minX, int *minY, int *maxX, int *maxY)
{
  *minX = self->boundMinX ;
  *minY = self->boundMinY ;
  *maxX = self->boundMaxX ;
  *maxY = self->boundMaxY ;
}

/** ------------------------------------------------------------------
 ** @brief Get flat window flag
 ** @param self DSIFT filter object.
 ** @return @c TRUE if the DSIFT filter uses a flat window.
 **/

int
vl_dsift_get_flat_window (VlDsiftFilter const* self)
{
  return self->useFlatWindow ;
}

/** ------------------------------------------------------------------
 ** @brief Get steps
 ** @param self DSIFT filter object.
 ** @param stepX sampling step along X.
 ** @param stepY sampling step along Y.
 **/

void
vl_dsift_get_steps (VlDsiftFilter const* self,
                   int* stepX,
                   int* stepY)
{
  *stepX = self->stepX ;
  *stepY = self->stepY ;
}

/** ------------------------------------------------------------------
 ** @brief Set steps
 ** @param self DSIFT filter object.
 ** @param stepX sampling step along X.
 ** @param stepY sampling step along Y.
 **/

void
vl_dsift_set_steps (VlDsiftFilter* self,
                   int stepX,
                   int stepY)
{
  self->stepX = stepX ;
  self->stepY = stepY ;
  _vl_dsift_update_buffers(self) ;
}

/** ------------------------------------------------------------------
 ** @brief Set bounds
 ** @param self DSIFT filter object.
 ** @param minX bounding box minimum X coordinate.
 ** @param minY bounding box minimum Y coordinate.
 ** @param maxX bounding box maximum X coordinate.
 ** @param maxY bounding box maximum Y coordinate.
 **/

void
vl_dsift_set_bounds (VlDsiftFilter* self,
                    int minX, int minY, int maxX, int maxY)
{
  self->boundMinX = minX ;
  self->boundMinY = minY ;
  self->boundMaxX = maxX ;
  self->boundMaxY = maxY ;
  _vl_dsift_update_buffers(self) ;
}

/** ------------------------------------------------------------------
 ** @brief Set SIFT descriptor geometry
 ** @param self DSIFT filter object.
 ** @param geom descriptor geometry parameters.
 **/

void
vl_dsift_set_geometry (VlDsiftFilter *self,
                       VlDsiftDescriptorGeometry const *geom)
{
  self->geom = *geom ;
  _vl_dsift_update_buffers(self) ;
}

/** ------------------------------------------------------------------
 ** @brief Set flat window flag
 ** @param self DSIFT filter object.
 ** @param useFlatWindow @c true if the DSIFT filter should use a flat window.
 **/

void
vl_dsift_set_flat_window (VlDsiftFilter* self,
                         vl_bool useFlatWindow)
{
  self->useFlatWindow = useFlatWindow ;
}

/** ------------------------------------------------------------------
 ** @brief Transpose descriptor
 **
 ** @param dst destination buffer.
 ** @param src source buffer.
 ** @param numBinT
 ** @param numBinX
 ** @param numBinY
 **
 ** The function writes to @a dst the transpose of the SIFT descriptor
 ** @a src. Let <code>I</code> be an image. The transpose operator
 ** satisfies the equation <code>transpose(dsift(I,x,y)) =
 ** dsift(transpose(I),y,x)</code>
 **/

VL_INLINE void
vl_dsift_transpose_descriptor (float* dst,
                              float const* src,
                              int numBinT,
                              int numBinX,
                              int numBinY)
{
  int t, x, y ;

  for (y = 0 ; y < numBinY ; ++y) {
    for (x = 0 ; x < numBinX ; ++x) {
      int offset  = numBinT * (x + y * numBinX) ;
      int offsetT = numBinT * (y + x * numBinY) ;

      for (t = 0 ; t < numBinT ; ++t) {
        int tT = numBinT / 4 - t ;
        dst [offsetT + (tT + numBinT) % numBinT] = src [offset + t] ;
      }
    }
  }
}

/** ------------------------------------------------------------------
 ** @brief Set SIFT descriptor Gaussian window size
 ** @param self DSIFT filter object.
 ** @param windowSize window size.
 **/

void
vl_dsift_set_window_size(VlDsiftFilter * self, double windowSize)
{
  assert(windowSize >= 0.0) ;
  self->windowSize = windowSize ;
}

/** ------------------------------------------------------------------
 ** @brief Get SIFT descriptor Gaussian window size
 ** @param self DSIFT filter object.
 ** @return window size.
 **/

VL_INLINE double
vl_dsift_get_window_size(VlDsiftFilter const * self)
{
  return self->windowSize ;
}

/*  VL_DSIFT_H */
#endif

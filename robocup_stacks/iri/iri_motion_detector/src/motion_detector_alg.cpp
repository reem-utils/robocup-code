#include "motion_detector_alg.h"

MotionDetectorAlgorithm::MotionDetectorAlgorithm(void)
{
}

MotionDetectorAlgorithm::~MotionDetectorAlgorithm(void)
{
}

void MotionDetectorAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// MotionDetectorAlgorithm Public API
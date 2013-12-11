#include "bow_object_detector_alg.h"

BowObjectDetectorAlgorithm::BowObjectDetectorAlgorithm(void)
{
}

BowObjectDetectorAlgorithm::~BowObjectDetectorAlgorithm(void)
{
}

void BowObjectDetectorAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// BowObjectDetectorAlgorithm Public API
#include "floodfill_segmentation_alg.h"

FloodfillSegmentationAlgorithm::FloodfillSegmentationAlgorithm(void)
{
}

FloodfillSegmentationAlgorithm::~FloodfillSegmentationAlgorithm(void)
{
}

void FloodfillSegmentationAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// FloodfillSegmentationAlgorithm Public API
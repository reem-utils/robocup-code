#include "median_blur_alg.h"

MedianBlurAlgorithm::MedianBlurAlgorithm(void)
{
}

MedianBlurAlgorithm::~MedianBlurAlgorithm(void)
{
}

void MedianBlurAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// MedianBlurAlgorithm Public API
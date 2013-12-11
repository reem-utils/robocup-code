#include "remove_background_alg.h"

RemoveBackgroundAlgorithm::RemoveBackgroundAlgorithm(void)
{
}

RemoveBackgroundAlgorithm::~RemoveBackgroundAlgorithm(void)
{
}

void RemoveBackgroundAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// RemoveBackgroundAlgorithm Public API
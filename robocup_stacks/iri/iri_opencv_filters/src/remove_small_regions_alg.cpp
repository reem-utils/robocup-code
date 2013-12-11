#include "remove_small_regions_alg.h"

RemoveSmallRegionsAlgorithm::RemoveSmallRegionsAlgorithm(void)
{
	
}

RemoveSmallRegionsAlgorithm::~RemoveSmallRegionsAlgorithm(void)
{
}

void RemoveSmallRegionsAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// RemoveSmallRegionsAlgorithm Public API
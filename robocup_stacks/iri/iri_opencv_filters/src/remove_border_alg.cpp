#include "remove_border_alg.h"

RemoveBorderAlgorithm::RemoveBorderAlgorithm(void)
{
	
}

RemoveBorderAlgorithm::~RemoveBorderAlgorithm(void)
{
}

void RemoveBorderAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// RemoveBorderAlgorithm Public API
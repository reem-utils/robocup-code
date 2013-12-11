#include "as_hri_alg.h"

AsHriAlgorithm::AsHriAlgorithm(void)
{
}

AsHriAlgorithm::~AsHriAlgorithm(void)
{
}

void AsHriAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// AsHriAlgorithm Public API
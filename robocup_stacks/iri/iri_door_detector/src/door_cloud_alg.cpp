#include "door_cloud_alg.h"

DoorCloudAlgorithm::DoorCloudAlgorithm(void)
{
}

DoorCloudAlgorithm::~DoorCloudAlgorithm(void)
{
}

void DoorCloudAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// DoorCloudAlgorithm Public API
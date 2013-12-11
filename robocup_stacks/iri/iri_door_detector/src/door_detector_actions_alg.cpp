#include "door_detector_actions_alg.h"

DoorDetectorActionsAlgorithm::DoorDetectorActionsAlgorithm(void)
{
}

DoorDetectorActionsAlgorithm::~DoorDetectorActionsAlgorithm(void)
{
}

void DoorDetectorActionsAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// DoorDetectorActionsAlgorithm Public API

#include "closed_door_detector_alg.h"

ClosedDoorDetectorAlgorithm::ClosedDoorDetectorAlgorithm(void)
{
}

ClosedDoorDetectorAlgorithm::~ClosedDoorDetectorAlgorithm(void)
{
}

void ClosedDoorDetectorAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// ClosedDoorDetectorAlgorithm Public API
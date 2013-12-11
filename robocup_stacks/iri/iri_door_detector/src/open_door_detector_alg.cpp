#include "open_door_detector_alg.h"

OpenDoorDetectorAlgorithm::OpenDoorDetectorAlgorithm(void)
{
}

OpenDoorDetectorAlgorithm::~OpenDoorDetectorAlgorithm(void)
{
}

void OpenDoorDetectorAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// OpenDoorDetectorAlgorithm Public API
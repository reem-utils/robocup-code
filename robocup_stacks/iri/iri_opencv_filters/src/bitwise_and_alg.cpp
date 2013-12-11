#include "bitwise_and_alg.h"

BitwiseAndAlgorithm::BitwiseAndAlgorithm(void)
{
}

BitwiseAndAlgorithm::~BitwiseAndAlgorithm(void)
{
}

void BitwiseAndAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// BitwiseAndAlgorithm Public API
#include "as_move_base_alg.h"

AsMoveBaseAlgorithm::AsMoveBaseAlgorithm(void)
{
}

AsMoveBaseAlgorithm::~AsMoveBaseAlgorithm(void)
{
}

void AsMoveBaseAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// AsMoveBaseAlgorithm Public API
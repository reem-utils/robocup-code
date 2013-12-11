#include "moped_actionserver_alg.h"

MopedActionserverAlgorithm::MopedActionserverAlgorithm(void)
{
}

MopedActionserverAlgorithm::~MopedActionserverAlgorithm(void)
{
}

void MopedActionserverAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// MopedActionserverAlgorithm Public API
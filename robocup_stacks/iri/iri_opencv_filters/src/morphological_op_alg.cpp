#include "morphological_op_alg.h"

MorphologicalOpAlgorithm::MorphologicalOpAlgorithm(void)
{
}

MorphologicalOpAlgorithm::~MorphologicalOpAlgorithm(void)
{
}

void MorphologicalOpAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// MorphologicalOpAlgorithm Public API
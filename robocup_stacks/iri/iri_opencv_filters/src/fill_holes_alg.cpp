#include "fill_holes_alg.h"

FillHolesAlgorithm::FillHolesAlgorithm(void)
{
}

FillHolesAlgorithm::~FillHolesAlgorithm(void)
{
}

void FillHolesAlgorithm::config_update(Config& new_cfg, uint32_t level)
{
  this->lock();

  // save the current configuration
  this->config_=new_cfg;
  
  this->unlock();
}

// FillHolesAlgorithm Public API
#include "as_hri_alg_node.h"

AsHriAlgNode::AsHriAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<AsHriAlgorithm>(),
  hri_aserver_(public_node_handle_, "hri"),
  counter_(0)
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  
  // [init subscribers]
  
  // [init services]
  
  // [init clients]
  
  // [init action servers]
  hri_aserver_.registerStartCallback(boost::bind(&AsHriAlgNode::hriStartCallback, this, _1)); 
  hri_aserver_.registerStopCallback(boost::bind(&AsHriAlgNode::hriStopCallback, this)); 
  hri_aserver_.registerIsFinishedCallback(boost::bind(&AsHriAlgNode::hriIsFinishedCallback, this)); 
  hri_aserver_.registerHasSucceedCallback(boost::bind(&AsHriAlgNode::hriHasSucceedCallback, this)); 
  hri_aserver_.registerGetResultCallback(boost::bind(&AsHriAlgNode::hriGetResultCallback, this, _1)); 
  hri_aserver_.registerGetFeedbackCallback(boost::bind(&AsHriAlgNode::hriGetFeedbackCallback, this, _1)); 
  hri_aserver_.start();
  
  // [init action clients]
}

AsHriAlgNode::~AsHriAlgNode(void)
{
  // [free dynamic memory]
}

void AsHriAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
}

/*  [subscriber callbacks] */

/*  [service callbacks] */

/*  [action callbacks] */
void AsHriAlgNode::hriStartCallback(const tibi_dabo_msgs::sequenceGoalConstPtr& goal)
{ 
  alg_.lock(); 
    ROS_INFO("AsHriAlgNode::START! speech=%s", goal->sequence_file[0].c_str());
    counter_ = 0;
  alg_.unlock(); 
} 

void AsHriAlgNode::hriStopCallback(void) 
{ 
  alg_.lock(); 
    //stop action 
  alg_.unlock(); 
} 

bool AsHriAlgNode::hriIsFinishedCallback(void) 
{ 
  bool ret = false; 

  alg_.lock(); 
    if( counter_ < 5 )
    {
      counter_++;
      sleep(1);
    }
    else
    {
      ROS_INFO("AsHriAlgNode::DONE!");
      ret = true;
    }
  alg_.unlock(); 

  return ret; 
} 

bool AsHriAlgNode::hriHasSucceedCallback(void) 
{ 
  bool ret = true; 

  alg_.lock(); 
    //if goal was accomplished 
    //ret = true 
  alg_.unlock(); 

  return ret; 
} 

void AsHriAlgNode::hriGetResultCallback(tibi_dabo_msgs::sequenceResultPtr& result) 
{ 
  alg_.lock(); 
    //update result data to be sent to client 
    //result->data = data; 
  alg_.unlock(); 
} 

void AsHriAlgNode::hriGetFeedbackCallback(tibi_dabo_msgs::sequenceFeedbackPtr& feedback) 
{ 
  alg_.lock(); 
    //keep track of feedback 
    //ROS_INFO("feedback: %s", feedback->data.c_str()); 
  alg_.unlock(); 
}

/*  [action requests] */

void AsHriAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();

  this->alg_.unlock();
}

void AsHriAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<AsHriAlgNode>(argc, argv, "as_hri_alg_node");
}

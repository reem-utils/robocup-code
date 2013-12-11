#include "as_move_base_alg_node.h"

AsMoveBaseAlgNode::AsMoveBaseAlgNode(void) :
  algorithm_base::IriBaseAlgorithm<AsMoveBaseAlgorithm>(),
  move_base_aserver_(public_node_handle_, "move_base"),
  counter_(0)
{
  //init class attributes if necessary
  //this->loop_rate_ = 2;//in [Hz]

  // [init publishers]
  
  // [init subscribers]
  
  // [init services]
  
  // [init clients]
  
  // [init action servers]
  move_base_aserver_.registerStartCallback(boost::bind(&AsMoveBaseAlgNode::move_baseStartCallback, this, _1)); 
  move_base_aserver_.registerStopCallback(boost::bind(&AsMoveBaseAlgNode::move_baseStopCallback, this)); 
  move_base_aserver_.registerIsFinishedCallback(boost::bind(&AsMoveBaseAlgNode::move_baseIsFinishedCallback, this)); 
  move_base_aserver_.registerHasSucceedCallback(boost::bind(&AsMoveBaseAlgNode::move_baseHasSucceedCallback, this)); 
  move_base_aserver_.registerGetResultCallback(boost::bind(&AsMoveBaseAlgNode::move_baseGetResultCallback, this, _1)); 
  move_base_aserver_.registerGetFeedbackCallback(boost::bind(&AsMoveBaseAlgNode::move_baseGetFeedbackCallback, this, _1)); 
  move_base_aserver_.start();
  
  // [init action clients]
}

AsMoveBaseAlgNode::~AsMoveBaseAlgNode(void)
{
  // [free dynamic memory]
}

void AsMoveBaseAlgNode::mainNodeThread(void)
{
  // [fill msg structures]
  
  // [fill srv structure and make request to the server]
  
  // [fill action structure and make request to the action server]

  // [publish messages]
}

/*  [subscriber callbacks] */

/*  [service callbacks] */

/*  [action callbacks] */
void AsMoveBaseAlgNode::move_baseStartCallback(const move_base_msgs::MoveBaseGoalConstPtr& goal)
{ 
  alg_.lock();
    ROS_INFO("AsMoveBaseAlgNode::START! frame_id=%s goal=(%f,%f)", 
             goal->target_pose.header.frame_id.c_str(), 
             goal->target_pose.pose.position.x, goal->target_pose.pose.position.y);
    counter_ = 0;
  alg_.unlock(); 
} 

void AsMoveBaseAlgNode::move_baseStopCallback(void) 
{ 
  alg_.lock(); 
    //stop action 
  alg_.unlock(); 
} 

bool AsMoveBaseAlgNode::move_baseIsFinishedCallback(void) 
{ 
  bool ret = false; 

  alg_.lock(); 
    if( counter_ < 3 )
    {
      counter_++;
      sleep(1);
    }
    else
    {
      ROS_INFO("AsMoveBaseAlgNode::DONE!");
      ret = true;
    }
    //if action has finish for any reason 
    //ret = true; 
  alg_.unlock(); 

  return ret; 
} 

bool AsMoveBaseAlgNode::move_baseHasSucceedCallback(void) 
{ 
  bool ret = true; 

  alg_.lock(); 
    //if goal was accomplished 
    //ret = true 
  alg_.unlock(); 

  return ret; 
} 

void AsMoveBaseAlgNode::move_baseGetResultCallback(move_base_msgs::MoveBaseResultPtr& result) 
{ 
  alg_.lock(); 
    //update result data to be sent to client 
    //result->data = data; 
  alg_.unlock(); 
} 

void AsMoveBaseAlgNode::move_baseGetFeedbackCallback(move_base_msgs::MoveBaseFeedbackPtr& feedback) 
{ 
  alg_.lock(); 
    //keep track of feedback 
    //ROS_INFO("feedback: %s", feedback->data.c_str()); 
  alg_.unlock(); 
}

/*  [action requests] */

void AsMoveBaseAlgNode::node_config_update(Config &config, uint32_t level)
{
  this->alg_.lock();

  this->alg_.unlock();
}

void AsMoveBaseAlgNode::addNodeDiagnostics(void)
{
}

/* main function */
int main(int argc,char *argv[])
{
  return algorithm_base::main<AsMoveBaseAlgNode>(argc, argv, "as_move_base_alg_node");
}

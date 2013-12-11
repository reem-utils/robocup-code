//#line 2 "/opt/ros/electric/stacks/driver_common/dynamic_reconfigure/templates/ConfigType.h"
// *********************************************************
// 
// File autogenerated for the iri_closed_door_detector package 
// by the dynamic_reconfigure package.
// Please do not edit.
// 
// ********************************************************/

/***********************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2008, Willow Garage, Inc.
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of the Willow Garage nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 ***********************************************************/

// Author: Blaise Gassend


#ifndef __iri_closed_door_detector__CLOSEDDOORDETECTORCONFIG_H__
#define __iri_closed_door_detector__CLOSEDDOORDETECTORCONFIG_H__

#include <dynamic_reconfigure/config_tools.h>
#include <limits>
#include <ros/node_handle.h>
#include <dynamic_reconfigure/ConfigDescription.h>
#include <dynamic_reconfigure/ParamDescription.h>
#include <dynamic_reconfigure/config_init_mutex.h>

namespace iri_closed_door_detector
{
  class ClosedDoorDetectorConfigStatics;
  
  class ClosedDoorDetectorConfig
  {
  public:
    class AbstractParamDescription : public dynamic_reconfigure::ParamDescription
    {
    public:
      AbstractParamDescription(std::string n, std::string t, uint32_t l, 
          std::string d, std::string e)
      {
        name = n;
        type = t;
        level = l;
        description = d;
        edit_method = e;
      }
      
      virtual void clamp(ClosedDoorDetectorConfig &config, const ClosedDoorDetectorConfig &max, const ClosedDoorDetectorConfig &min) const = 0;
      virtual void calcLevel(uint32_t &level, const ClosedDoorDetectorConfig &config1, const ClosedDoorDetectorConfig &config2) const = 0;
      virtual void fromServer(const ros::NodeHandle &nh, ClosedDoorDetectorConfig &config) const = 0;
      virtual void toServer(const ros::NodeHandle &nh, const ClosedDoorDetectorConfig &config) const = 0;
      virtual bool fromMessage(const dynamic_reconfigure::Config &msg, ClosedDoorDetectorConfig &config) const = 0;
      virtual void toMessage(dynamic_reconfigure::Config &msg, const ClosedDoorDetectorConfig &config) const = 0;
    };

    typedef boost::shared_ptr<AbstractParamDescription> AbstractParamDescriptionPtr;
    typedef boost::shared_ptr<const AbstractParamDescription> AbstractParamDescriptionConstPtr;
    
    template <class T>
    class ParamDescription : public AbstractParamDescription
    {
    public:
      ParamDescription(std::string name, std::string type, uint32_t level, 
          std::string description, std::string edit_method, T ClosedDoorDetectorConfig::* f) :
        AbstractParamDescription(name, type, level, description, edit_method),
        field(f)
      {}

      T (ClosedDoorDetectorConfig::* field);

      virtual void clamp(ClosedDoorDetectorConfig &config, const ClosedDoorDetectorConfig &max, const ClosedDoorDetectorConfig &min) const
      {
        if (config.*field > max.*field)
          config.*field = max.*field;
        
        if (config.*field < min.*field)
          config.*field = min.*field;
      }

      virtual void calcLevel(uint32_t &comb_level, const ClosedDoorDetectorConfig &config1, const ClosedDoorDetectorConfig &config2) const
      {
        if (config1.*field != config2.*field)
          comb_level |= level;
      }

      virtual void fromServer(const ros::NodeHandle &nh, ClosedDoorDetectorConfig &config) const
      {
        nh.getParam(name, config.*field);
      }

      virtual void toServer(const ros::NodeHandle &nh, const ClosedDoorDetectorConfig &config) const
      {
        nh.setParam(name, config.*field);
      }

      virtual bool fromMessage(const dynamic_reconfigure::Config &msg, ClosedDoorDetectorConfig &config) const
      {
        return dynamic_reconfigure::ConfigTools::getParameter(msg, name, config.*field);
      }

      virtual void toMessage(dynamic_reconfigure::Config &msg, const ClosedDoorDetectorConfig &config) const
      {
        dynamic_reconfigure::ConfigTools::appendParameter(msg, name, config.*field);
      }
    };

//#line 42 "../cfg/closed_door_detector_alg_config.cfg"
      int min_door_width;
//#line 43 "../cfg/closed_door_detector_alg_config.cfg"
      int max_door_width;
//#line 44 "../cfg/closed_door_detector_alg_config.cfg"
      int min_door_height;
//#line 45 "../cfg/closed_door_detector_alg_config.cfg"
      int max_door_height;
//#line 46 "../cfg/closed_door_detector_alg_config.cfg"
      int handle_width;
//#line 47 "../cfg/closed_door_detector_alg_config.cfg"
      int handle_height;
//#line 48 "../cfg/closed_door_detector_alg_config.cfg"
      int debugging_images;
//#line 49 "../cfg/closed_door_detector_alg_config.cfg"
      int allowed_blobs;
//#line 50 "../cfg/closed_door_detector_alg_config.cfg"
      bool DSC;
//#line 51 "../cfg/closed_door_detector_alg_config.cfg"
      bool SHM;
//#line 52 "../cfg/closed_door_detector_alg_config.cfg"
      bool SVP;
//#line 53 "../cfg/closed_door_detector_alg_config.cfg"
      bool SFT;
//#line 54 "../cfg/closed_door_detector_alg_config.cfg"
      bool Range_filter;
//#line 55 "../cfg/closed_door_detector_alg_config.cfg"
      bool Persp_filter;
//#line 56 "../cfg/closed_door_detector_alg_config.cfg"
      bool Geom_filter;
//#line 57 "../cfg/closed_door_detector_alg_config.cfg"
      bool Size_filter;
//#line 58 "../cfg/closed_door_detector_alg_config.cfg"
      bool Aspect_filter;
//#line 138 "/opt/ros/electric/stacks/driver_common/dynamic_reconfigure/templates/ConfigType.h"

    bool __fromMessage__(dynamic_reconfigure::Config &msg)
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      int count = 0;
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); i++)
        if ((*i)->fromMessage(msg, *this))
          count++;
      if (count != dynamic_reconfigure::ConfigTools::size(msg))
      {
        ROS_ERROR("ClosedDoorDetectorConfig::__fromMessage__ called with an unexpected parameter.");
        ROS_ERROR("Booleans:");
        for (unsigned int i = 0; i < msg.bools.size(); i++)
          ROS_ERROR("  %s", msg.bools[i].name.c_str());
        ROS_ERROR("Integers:");
        for (unsigned int i = 0; i < msg.ints.size(); i++)
          ROS_ERROR("  %s", msg.ints[i].name.c_str());
        ROS_ERROR("Doubles:");
        for (unsigned int i = 0; i < msg.doubles.size(); i++)
          ROS_ERROR("  %s", msg.doubles[i].name.c_str());
        ROS_ERROR("Strings:");
        for (unsigned int i = 0; i < msg.strs.size(); i++)
          ROS_ERROR("  %s", msg.strs[i].name.c_str());
        // @todo Check that there are no duplicates. Make this error more
        // explicit.
        return false;
      }
      return true;
    }

    // This version of __toMessage__ is used during initialization of
    // statics when __getParamDescriptions__ can't be called yet.
    void __toMessage__(dynamic_reconfigure::Config &msg, const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__) const
    {
      dynamic_reconfigure::ConfigTools::clear(msg);
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); i++)
        (*i)->toMessage(msg, *this);
    }
    
    void __toMessage__(dynamic_reconfigure::Config &msg) const
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      __toMessage__(msg, __param_descriptions__);
    }
    
    void __toServer__(const ros::NodeHandle &nh) const
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); i++)
        (*i)->toServer(nh, *this);
    }

    void __fromServer__(const ros::NodeHandle &nh)
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); i++)
        (*i)->fromServer(nh, *this);
    }

    void __clamp__()
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      const ClosedDoorDetectorConfig &__max__ = __getMax__();
      const ClosedDoorDetectorConfig &__min__ = __getMin__();
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); i++)
        (*i)->clamp(*this, __max__, __min__);
    }

    uint32_t __level__(const ClosedDoorDetectorConfig &config) const
    {
      const std::vector<AbstractParamDescriptionConstPtr> &__param_descriptions__ = __getParamDescriptions__();
      uint32_t level = 0;
      for (std::vector<AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); i++)
        (*i)->calcLevel(level, config, *this);
      return level;
    }
    
    static const dynamic_reconfigure::ConfigDescription &__getDescriptionMessage__();
    static const ClosedDoorDetectorConfig &__getDefault__();
    static const ClosedDoorDetectorConfig &__getMax__();
    static const ClosedDoorDetectorConfig &__getMin__();
    static const std::vector<AbstractParamDescriptionConstPtr> &__getParamDescriptions__();
    
  private:
    static const ClosedDoorDetectorConfigStatics *__get_statics__();
  };
  
  template <> // Max and min are ignored for strings.
  inline void ClosedDoorDetectorConfig::ParamDescription<std::string>::clamp(ClosedDoorDetectorConfig &config, const ClosedDoorDetectorConfig &max, const ClosedDoorDetectorConfig &min) const
  {
    return;
  }

  class ClosedDoorDetectorConfigStatics
  {
    friend class ClosedDoorDetectorConfig;
    
    ClosedDoorDetectorConfigStatics()
    {
//#line 42 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.min_door_width = 50;
//#line 42 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.min_door_width = 1500;
//#line 42 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.min_door_width = 250;
//#line 42 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("min_door_width", "int", 0, "Minimum door width", "", &ClosedDoorDetectorConfig::min_door_width)));
//#line 43 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.max_door_width = 50;
//#line 43 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.max_door_width = 1500;
//#line 43 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.max_door_width = 650;
//#line 43 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("max_door_width", "int", 0, "Maximum door width", "", &ClosedDoorDetectorConfig::max_door_width)));
//#line 44 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.min_door_height = 50;
//#line 44 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.min_door_height = 1500;
//#line 44 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.min_door_height = 850;
//#line 44 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("min_door_height", "int", 0, "Minimum door height", "", &ClosedDoorDetectorConfig::min_door_height)));
//#line 45 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.max_door_height = 50;
//#line 45 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.max_door_height = 1500;
//#line 45 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.max_door_height = 1200;
//#line 45 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("max_door_height", "int", 0, "Maximum door height", "", &ClosedDoorDetectorConfig::max_door_height)));
//#line 46 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.handle_width = 1;
//#line 46 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.handle_width = 20;
//#line 46 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.handle_width = 13;
//#line 46 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("handle_width", "int", 0, "Percentage of door width", "", &ClosedDoorDetectorConfig::handle_width)));
//#line 47 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.handle_height = 1;
//#line 47 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.handle_height = 20;
//#line 47 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.handle_height = 6;
//#line 47 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("handle_height", "int", 0, "Percentage of door height", "", &ClosedDoorDetectorConfig::handle_height)));
//#line 48 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.debugging_images = 0;
//#line 48 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.debugging_images = 3;
//#line 48 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.debugging_images = 0;
//#line 48 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("debugging_images", "int", 0, "Show Images for Debugging", "", &ClosedDoorDetectorConfig::debugging_images)));
//#line 49 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.allowed_blobs = 30;
//#line 49 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.allowed_blobs = 400;
//#line 49 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.allowed_blobs = 250;
//#line 49 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<int>("allowed_blobs", "int", 0, "Blob Threshold", "", &ClosedDoorDetectorConfig::allowed_blobs)));
//#line 50 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.DSC = 0;
//#line 50 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.DSC = 1;
//#line 50 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.DSC = 0;
//#line 50 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("DSC", "bool", 0, "Show Door Size Calibrator", "", &ClosedDoorDetectorConfig::DSC)));
//#line 51 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.SHM = 0;
//#line 51 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.SHM = 1;
//#line 51 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.SHM = 0;
//#line 51 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("SHM", "bool", 0, "Show Handle Mask", "", &ClosedDoorDetectorConfig::SHM)));
//#line 52 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.SVP = 0;
//#line 52 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.SVP = 1;
//#line 52 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.SVP = 0;
//#line 52 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("SVP", "bool", 0, "Show Virtual Points", "", &ClosedDoorDetectorConfig::SVP)));
//#line 53 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.SFT = 0;
//#line 53 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.SFT = 1;
//#line 53 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.SFT = 0;
//#line 53 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("SFT", "bool", 0, "Show Flatness Test", "", &ClosedDoorDetectorConfig::SFT)));
//#line 54 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.Range_filter = 0;
//#line 54 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.Range_filter = 1;
//#line 54 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.Range_filter = 1;
//#line 54 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("Range_filter", "bool", 0, "Apply Sensor range filter", "", &ClosedDoorDetectorConfig::Range_filter)));
//#line 55 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.Persp_filter = 0;
//#line 55 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.Persp_filter = 1;
//#line 55 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.Persp_filter = 1;
//#line 55 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("Persp_filter", "bool", 0, "Apply Perspective filter", "", &ClosedDoorDetectorConfig::Persp_filter)));
//#line 56 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.Geom_filter = 0;
//#line 56 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.Geom_filter = 1;
//#line 56 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.Geom_filter = 1;
//#line 56 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("Geom_filter", "bool", 0, "Apply Geometry filter", "", &ClosedDoorDetectorConfig::Geom_filter)));
//#line 57 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.Size_filter = 0;
//#line 57 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.Size_filter = 1;
//#line 57 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.Size_filter = 1;
//#line 57 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("Size_filter", "bool", 0, "Apply Size filter", "", &ClosedDoorDetectorConfig::Size_filter)));
//#line 58 "../cfg/closed_door_detector_alg_config.cfg"
      __min__.Aspect_filter = 0;
//#line 58 "../cfg/closed_door_detector_alg_config.cfg"
      __max__.Aspect_filter = 1;
//#line 58 "../cfg/closed_door_detector_alg_config.cfg"
      __default__.Aspect_filter = 1;
//#line 58 "../cfg/closed_door_detector_alg_config.cfg"
      __param_descriptions__.push_back(ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr(new ClosedDoorDetectorConfig::ParamDescription<bool>("Aspect_filter", "bool", 0, "Apply Aspect ratio filter", "", &ClosedDoorDetectorConfig::Aspect_filter)));
//#line 239 "/opt/ros/electric/stacks/driver_common/dynamic_reconfigure/templates/ConfigType.h"
    
      for (std::vector<ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr>::const_iterator i = __param_descriptions__.begin(); i != __param_descriptions__.end(); i++)
        __description_message__.parameters.push_back(**i);
      __max__.__toMessage__(__description_message__.max, __param_descriptions__); 
      __min__.__toMessage__(__description_message__.min, __param_descriptions__); 
      __default__.__toMessage__(__description_message__.dflt, __param_descriptions__); 
    }
    std::vector<ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr> __param_descriptions__;
    ClosedDoorDetectorConfig __max__;
    ClosedDoorDetectorConfig __min__;
    ClosedDoorDetectorConfig __default__;
    dynamic_reconfigure::ConfigDescription __description_message__;
    static const ClosedDoorDetectorConfigStatics *get_instance()
    {
      // Split this off in a separate function because I know that
      // instance will get initialized the first time get_instance is
      // called, and I am guaranteeing that get_instance gets called at
      // most once.
      static ClosedDoorDetectorConfigStatics instance;
      return &instance;
    }
  };

  inline const dynamic_reconfigure::ConfigDescription &ClosedDoorDetectorConfig::__getDescriptionMessage__() 
  {
    return __get_statics__()->__description_message__;
  }

  inline const ClosedDoorDetectorConfig &ClosedDoorDetectorConfig::__getDefault__()
  {
    return __get_statics__()->__default__;
  }
  
  inline const ClosedDoorDetectorConfig &ClosedDoorDetectorConfig::__getMax__()
  {
    return __get_statics__()->__max__;
  }
  
  inline const ClosedDoorDetectorConfig &ClosedDoorDetectorConfig::__getMin__()
  {
    return __get_statics__()->__min__;
  }
  
  inline const std::vector<ClosedDoorDetectorConfig::AbstractParamDescriptionConstPtr> &ClosedDoorDetectorConfig::__getParamDescriptions__()
  {
    return __get_statics__()->__param_descriptions__;
  }

  inline const ClosedDoorDetectorConfigStatics *ClosedDoorDetectorConfig::__get_statics__()
  {
    const static ClosedDoorDetectorConfigStatics *statics;
  
    if (statics) // Common case
      return statics;

    boost::mutex::scoped_lock lock(dynamic_reconfigure::__init_mutex__);

    if (statics) // In case we lost a race.
      return statics;

    statics = ClosedDoorDetectorConfigStatics::get_instance();
    
    return statics;
  }


}

#endif // __CLOSEDDOORDETECTORRECONFIGURATOR_H__

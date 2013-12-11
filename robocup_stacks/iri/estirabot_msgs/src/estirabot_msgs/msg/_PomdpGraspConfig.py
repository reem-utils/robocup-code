"""autogenerated by genpy from estirabot_msgs/PomdpGraspConfig.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import estirabot_msgs.msg
import std_msgs.msg

class PomdpGraspConfig(genpy.Message):
  _md5sum = "38bd3d3705953515e94def1a3e168b6c"
  _type = "estirabot_msgs/PomdpGraspConfig"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Message containing configuration for the pomdp grasping process

# Define grabbing_zones
int8 GRAB = 0
int8 DROP = 1

# Define grabbing_zones
int8 BOTH_ZONES = 0
int8 LEFT_ZONE = 1
int8 RIGHT_ZONE = 2

# Define best pose algorithms
int8 MAX_HEIGHT_ALG = 0
int8 MAX_WRINKLE_ALG = 1
int8 FUSION_ALG = 2

# Define posible approach identifiers
int8 APPROACH_TOP_DEEP = 0
int8 APPROACH_TOP_SURFACE = 1
int8 APPROACH_SIDE_DEEP = 2
int8 APPROACH_SIDE_SURFACE = 3

int8 best_pose_algorithm_id
int8 actiontype
int8 grabbing_zone
estirabot_msgs/GraspPointParameters approach_config
string[] fingers_grasp_configs
geometry_msgs/PoseStamped place_point

================================================================================
MSG: estirabot_msgs/GraspPointParameters
# Message for parameters to modify a grasp point
# These parameters apply on a cartesian coordinate
# (geometry_msgs/pose).

geometry_msgs/Transform pre_grasp_modifier
geometry_msgs/Transform[] grasp_modifiers
uint8 grasp_modifier_used

================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

"""
  # Pseudo-constants
  GRAB = 0
  DROP = 1
  BOTH_ZONES = 0
  LEFT_ZONE = 1
  RIGHT_ZONE = 2
  MAX_HEIGHT_ALG = 0
  MAX_WRINKLE_ALG = 1
  FUSION_ALG = 2
  APPROACH_TOP_DEEP = 0
  APPROACH_TOP_SURFACE = 1
  APPROACH_SIDE_DEEP = 2
  APPROACH_SIDE_SURFACE = 3

  __slots__ = ['best_pose_algorithm_id','actiontype','grabbing_zone','approach_config','fingers_grasp_configs','place_point']
  _slot_types = ['int8','int8','int8','estirabot_msgs/GraspPointParameters','string[]','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       best_pose_algorithm_id,actiontype,grabbing_zone,approach_config,fingers_grasp_configs,place_point

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PomdpGraspConfig, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.best_pose_algorithm_id is None:
        self.best_pose_algorithm_id = 0
      if self.actiontype is None:
        self.actiontype = 0
      if self.grabbing_zone is None:
        self.grabbing_zone = 0
      if self.approach_config is None:
        self.approach_config = estirabot_msgs.msg.GraspPointParameters()
      if self.fingers_grasp_configs is None:
        self.fingers_grasp_configs = []
      if self.place_point is None:
        self.place_point = geometry_msgs.msg.PoseStamped()
    else:
      self.best_pose_algorithm_id = 0
      self.actiontype = 0
      self.grabbing_zone = 0
      self.approach_config = estirabot_msgs.msg.GraspPointParameters()
      self.fingers_grasp_configs = []
      self.place_point = geometry_msgs.msg.PoseStamped()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3b7d.pack(_x.best_pose_algorithm_id, _x.actiontype, _x.grabbing_zone, _x.approach_config.pre_grasp_modifier.translation.x, _x.approach_config.pre_grasp_modifier.translation.y, _x.approach_config.pre_grasp_modifier.translation.z, _x.approach_config.pre_grasp_modifier.rotation.x, _x.approach_config.pre_grasp_modifier.rotation.y, _x.approach_config.pre_grasp_modifier.rotation.z, _x.approach_config.pre_grasp_modifier.rotation.w))
      length = len(self.approach_config.grasp_modifiers)
      buff.write(_struct_I.pack(length))
      for val1 in self.approach_config.grasp_modifiers:
        _v1 = val1.translation
        _x = _v1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v2 = val1.rotation
        _x = _v2
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      buff.write(_struct_B.pack(self.approach_config.grasp_modifier_used))
      length = len(self.fingers_grasp_configs)
      buff.write(_struct_I.pack(length))
      for val1 in self.fingers_grasp_configs:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      _x = self
      buff.write(_struct_3I.pack(_x.place_point.header.seq, _x.place_point.header.stamp.secs, _x.place_point.header.stamp.nsecs))
      _x = self.place_point.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.place_point.pose.position.x, _x.place_point.pose.position.y, _x.place_point.pose.position.z, _x.place_point.pose.orientation.x, _x.place_point.pose.orientation.y, _x.place_point.pose.orientation.z, _x.place_point.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.approach_config is None:
        self.approach_config = estirabot_msgs.msg.GraspPointParameters()
      if self.place_point is None:
        self.place_point = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 59
      (_x.best_pose_algorithm_id, _x.actiontype, _x.grabbing_zone, _x.approach_config.pre_grasp_modifier.translation.x, _x.approach_config.pre_grasp_modifier.translation.y, _x.approach_config.pre_grasp_modifier.translation.z, _x.approach_config.pre_grasp_modifier.rotation.x, _x.approach_config.pre_grasp_modifier.rotation.y, _x.approach_config.pre_grasp_modifier.rotation.z, _x.approach_config.pre_grasp_modifier.rotation.w,) = _struct_3b7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.approach_config.grasp_modifiers = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v3 = val1.translation
        _x = _v3
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v4 = val1.rotation
        _x = _v4
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.approach_config.grasp_modifiers.append(val1)
      start = end
      end += 1
      (self.approach_config.grasp_modifier_used,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.fingers_grasp_configs = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.fingers_grasp_configs.append(val1)
      _x = self
      start = end
      end += 12
      (_x.place_point.header.seq, _x.place_point.header.stamp.secs, _x.place_point.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.place_point.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.place_point.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.place_point.pose.position.x, _x.place_point.pose.position.y, _x.place_point.pose.position.z, _x.place_point.pose.orientation.x, _x.place_point.pose.orientation.y, _x.place_point.pose.orientation.z, _x.place_point.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3b7d.pack(_x.best_pose_algorithm_id, _x.actiontype, _x.grabbing_zone, _x.approach_config.pre_grasp_modifier.translation.x, _x.approach_config.pre_grasp_modifier.translation.y, _x.approach_config.pre_grasp_modifier.translation.z, _x.approach_config.pre_grasp_modifier.rotation.x, _x.approach_config.pre_grasp_modifier.rotation.y, _x.approach_config.pre_grasp_modifier.rotation.z, _x.approach_config.pre_grasp_modifier.rotation.w))
      length = len(self.approach_config.grasp_modifiers)
      buff.write(_struct_I.pack(length))
      for val1 in self.approach_config.grasp_modifiers:
        _v5 = val1.translation
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = val1.rotation
        _x = _v6
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      buff.write(_struct_B.pack(self.approach_config.grasp_modifier_used))
      length = len(self.fingers_grasp_configs)
      buff.write(_struct_I.pack(length))
      for val1 in self.fingers_grasp_configs:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        buff.write(struct.pack('<I%ss'%length, length, val1))
      _x = self
      buff.write(_struct_3I.pack(_x.place_point.header.seq, _x.place_point.header.stamp.secs, _x.place_point.header.stamp.nsecs))
      _x = self.place_point.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.place_point.pose.position.x, _x.place_point.pose.position.y, _x.place_point.pose.position.z, _x.place_point.pose.orientation.x, _x.place_point.pose.orientation.y, _x.place_point.pose.orientation.z, _x.place_point.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.approach_config is None:
        self.approach_config = estirabot_msgs.msg.GraspPointParameters()
      if self.place_point is None:
        self.place_point = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 59
      (_x.best_pose_algorithm_id, _x.actiontype, _x.grabbing_zone, _x.approach_config.pre_grasp_modifier.translation.x, _x.approach_config.pre_grasp_modifier.translation.y, _x.approach_config.pre_grasp_modifier.translation.z, _x.approach_config.pre_grasp_modifier.rotation.x, _x.approach_config.pre_grasp_modifier.rotation.y, _x.approach_config.pre_grasp_modifier.rotation.z, _x.approach_config.pre_grasp_modifier.rotation.w,) = _struct_3b7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.approach_config.grasp_modifiers = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Transform()
        _v7 = val1.translation
        _x = _v7
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v8 = val1.rotation
        _x = _v8
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        self.approach_config.grasp_modifiers.append(val1)
      start = end
      end += 1
      (self.approach_config.grasp_modifier_used,) = _struct_B.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.fingers_grasp_configs = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.fingers_grasp_configs.append(val1)
      _x = self
      start = end
      end += 12
      (_x.place_point.header.seq, _x.place_point.header.stamp.secs, _x.place_point.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.place_point.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.place_point.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.place_point.pose.position.x, _x.place_point.pose.position.y, _x.place_point.pose.position.z, _x.place_point.pose.orientation.x, _x.place_point.pose.orientation.y, _x.place_point.pose.orientation.z, _x.place_point.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_3I = struct.Struct("<3I")
_struct_3b7d = struct.Struct("<3b7d")
_struct_7d = struct.Struct("<7d")
_struct_4d = struct.Struct("<4d")
_struct_3d = struct.Struct("<3d")

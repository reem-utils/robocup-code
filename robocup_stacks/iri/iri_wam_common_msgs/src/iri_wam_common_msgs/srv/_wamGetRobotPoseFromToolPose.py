"""autogenerated by genpy from iri_wam_common_msgs/wamGetRobotPoseFromToolPoseRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class wamGetRobotPoseFromToolPoseRequest(genpy.Message):
  _md5sum = "1f49009e637ac367cacdab60da3707bd"
  _type = "iri_wam_common_msgs/wamGetRobotPoseFromToolPoseRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
geometry_msgs/PoseStamped tool_pose

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

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['tool_pose']
  _slot_types = ['geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tool_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(wamGetRobotPoseFromToolPoseRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.tool_pose is None:
        self.tool_pose = geometry_msgs.msg.PoseStamped()
    else:
      self.tool_pose = geometry_msgs.msg.PoseStamped()

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
      buff.write(_struct_3I.pack(_x.tool_pose.header.seq, _x.tool_pose.header.stamp.secs, _x.tool_pose.header.stamp.nsecs))
      _x = self.tool_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.tool_pose.pose.position.x, _x.tool_pose.pose.position.y, _x.tool_pose.pose.position.z, _x.tool_pose.pose.orientation.x, _x.tool_pose.pose.orientation.y, _x.tool_pose.pose.orientation.z, _x.tool_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.tool_pose is None:
        self.tool_pose = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.tool_pose.header.seq, _x.tool_pose.header.stamp.secs, _x.tool_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tool_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.tool_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.tool_pose.pose.position.x, _x.tool_pose.pose.position.y, _x.tool_pose.pose.position.z, _x.tool_pose.pose.orientation.x, _x.tool_pose.pose.orientation.y, _x.tool_pose.pose.orientation.z, _x.tool_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
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
      buff.write(_struct_3I.pack(_x.tool_pose.header.seq, _x.tool_pose.header.stamp.secs, _x.tool_pose.header.stamp.nsecs))
      _x = self.tool_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.tool_pose.pose.position.x, _x.tool_pose.pose.position.y, _x.tool_pose.pose.position.z, _x.tool_pose.pose.orientation.x, _x.tool_pose.pose.orientation.y, _x.tool_pose.pose.orientation.z, _x.tool_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.tool_pose is None:
        self.tool_pose = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.tool_pose.header.seq, _x.tool_pose.header.stamp.secs, _x.tool_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.tool_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.tool_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.tool_pose.pose.position.x, _x.tool_pose.pose.position.y, _x.tool_pose.pose.position.z, _x.tool_pose.pose.orientation.x, _x.tool_pose.pose.orientation.y, _x.tool_pose.pose.orientation.z, _x.tool_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_7d = struct.Struct("<7d")
"""autogenerated by genpy from iri_wam_common_msgs/wamGetRobotPoseFromToolPoseResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class wamGetRobotPoseFromToolPoseResponse(genpy.Message):
  _md5sum = "bb46cd500e029a262f0c2284fecd8ed7"
  _type = "iri_wam_common_msgs/wamGetRobotPoseFromToolPoseResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
geometry_msgs/PoseStamped robot_pose


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

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['robot_pose']
  _slot_types = ['geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       robot_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(wamGetRobotPoseFromToolPoseResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.robot_pose is None:
        self.robot_pose = geometry_msgs.msg.PoseStamped()
    else:
      self.robot_pose = geometry_msgs.msg.PoseStamped()

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
      buff.write(_struct_3I.pack(_x.robot_pose.header.seq, _x.robot_pose.header.stamp.secs, _x.robot_pose.header.stamp.nsecs))
      _x = self.robot_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.robot_pose.pose.position.x, _x.robot_pose.pose.position.y, _x.robot_pose.pose.position.z, _x.robot_pose.pose.orientation.x, _x.robot_pose.pose.orientation.y, _x.robot_pose.pose.orientation.z, _x.robot_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.robot_pose is None:
        self.robot_pose = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.robot_pose.header.seq, _x.robot_pose.header.stamp.secs, _x.robot_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.robot_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.robot_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.robot_pose.pose.position.x, _x.robot_pose.pose.position.y, _x.robot_pose.pose.position.z, _x.robot_pose.pose.orientation.x, _x.robot_pose.pose.orientation.y, _x.robot_pose.pose.orientation.z, _x.robot_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
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
      buff.write(_struct_3I.pack(_x.robot_pose.header.seq, _x.robot_pose.header.stamp.secs, _x.robot_pose.header.stamp.nsecs))
      _x = self.robot_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.robot_pose.pose.position.x, _x.robot_pose.pose.position.y, _x.robot_pose.pose.position.z, _x.robot_pose.pose.orientation.x, _x.robot_pose.pose.orientation.y, _x.robot_pose.pose.orientation.z, _x.robot_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.robot_pose is None:
        self.robot_pose = geometry_msgs.msg.PoseStamped()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.robot_pose.header.seq, _x.robot_pose.header.stamp.secs, _x.robot_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.robot_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.robot_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.robot_pose.pose.position.x, _x.robot_pose.pose.position.y, _x.robot_pose.pose.position.z, _x.robot_pose.pose.orientation.x, _x.robot_pose.pose.orientation.y, _x.robot_pose.pose.orientation.z, _x.robot_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_7d = struct.Struct("<7d")
class wamGetRobotPoseFromToolPose(object):
  _type          = 'iri_wam_common_msgs/wamGetRobotPoseFromToolPose'
  _md5sum = '9bc33b41fd06e0cc64ed1e05be1d2898'
  _request_class  = wamGetRobotPoseFromToolPoseRequest
  _response_class = wamGetRobotPoseFromToolPoseResponse

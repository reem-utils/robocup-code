"""autogenerated by genpy from estirabot_msgs/GraspPointParameters.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class GraspPointParameters(genpy.Message):
  _md5sum = "4a7fd3c439b5601709521f9ae1410df2"
  _type = "estirabot_msgs/GraspPointParameters"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Message for parameters to modify a grasp point
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

"""
  __slots__ = ['pre_grasp_modifier','grasp_modifiers','grasp_modifier_used']
  _slot_types = ['geometry_msgs/Transform','geometry_msgs/Transform[]','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pre_grasp_modifier,grasp_modifiers,grasp_modifier_used

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GraspPointParameters, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pre_grasp_modifier is None:
        self.pre_grasp_modifier = geometry_msgs.msg.Transform()
      if self.grasp_modifiers is None:
        self.grasp_modifiers = []
      if self.grasp_modifier_used is None:
        self.grasp_modifier_used = 0
    else:
      self.pre_grasp_modifier = geometry_msgs.msg.Transform()
      self.grasp_modifiers = []
      self.grasp_modifier_used = 0

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
      buff.write(_struct_7d.pack(_x.pre_grasp_modifier.translation.x, _x.pre_grasp_modifier.translation.y, _x.pre_grasp_modifier.translation.z, _x.pre_grasp_modifier.rotation.x, _x.pre_grasp_modifier.rotation.y, _x.pre_grasp_modifier.rotation.z, _x.pre_grasp_modifier.rotation.w))
      length = len(self.grasp_modifiers)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasp_modifiers:
        _v1 = val1.translation
        _x = _v1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v2 = val1.rotation
        _x = _v2
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      buff.write(_struct_B.pack(self.grasp_modifier_used))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.pre_grasp_modifier is None:
        self.pre_grasp_modifier = geometry_msgs.msg.Transform()
      if self.grasp_modifiers is None:
        self.grasp_modifiers = None
      end = 0
      _x = self
      start = end
      end += 56
      (_x.pre_grasp_modifier.translation.x, _x.pre_grasp_modifier.translation.y, _x.pre_grasp_modifier.translation.z, _x.pre_grasp_modifier.rotation.x, _x.pre_grasp_modifier.rotation.y, _x.pre_grasp_modifier.rotation.z, _x.pre_grasp_modifier.rotation.w,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasp_modifiers = []
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
        self.grasp_modifiers.append(val1)
      start = end
      end += 1
      (self.grasp_modifier_used,) = _struct_B.unpack(str[start:end])
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
      buff.write(_struct_7d.pack(_x.pre_grasp_modifier.translation.x, _x.pre_grasp_modifier.translation.y, _x.pre_grasp_modifier.translation.z, _x.pre_grasp_modifier.rotation.x, _x.pre_grasp_modifier.rotation.y, _x.pre_grasp_modifier.rotation.z, _x.pre_grasp_modifier.rotation.w))
      length = len(self.grasp_modifiers)
      buff.write(_struct_I.pack(length))
      for val1 in self.grasp_modifiers:
        _v5 = val1.translation
        _x = _v5
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v6 = val1.rotation
        _x = _v6
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      buff.write(_struct_B.pack(self.grasp_modifier_used))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.pre_grasp_modifier is None:
        self.pre_grasp_modifier = geometry_msgs.msg.Transform()
      if self.grasp_modifiers is None:
        self.grasp_modifiers = None
      end = 0
      _x = self
      start = end
      end += 56
      (_x.pre_grasp_modifier.translation.x, _x.pre_grasp_modifier.translation.y, _x.pre_grasp_modifier.translation.z, _x.pre_grasp_modifier.rotation.x, _x.pre_grasp_modifier.rotation.y, _x.pre_grasp_modifier.rotation.z, _x.pre_grasp_modifier.rotation.w,) = _struct_7d.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grasp_modifiers = []
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
        self.grasp_modifiers.append(val1)
      start = end
      end += 1
      (self.grasp_modifier_used,) = _struct_B.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d = struct.Struct("<4d")
_struct_7d = struct.Struct("<7d")
_struct_B = struct.Struct("<B")
_struct_3d = struct.Struct("<3d")

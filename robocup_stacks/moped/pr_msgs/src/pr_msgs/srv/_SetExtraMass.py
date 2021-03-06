"""autogenerated by genpy from pr_msgs/SetExtraMassRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import pr_msgs.msg

class SetExtraMassRequest(genpy.Message):
  _md5sum = "711c76cfdcaf7366f06dc155d98f60d1"
  _type = "pr_msgs/SetExtraMassRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """pr_msgs/MassProperties m

================================================================================
MSG: pr_msgs/MassProperties
uint8 link
float64 mass
float64 cog_x
float64 cog_y
float64 cog_z
float64 inertia_xx
float64 inertia_xy
float64 inertia_xz
float64 inertia_yy
float64 inertia_yz
float64 inertia_zz

"""
  __slots__ = ['m']
  _slot_types = ['pr_msgs/MassProperties']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       m

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetExtraMassRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.m is None:
        self.m = pr_msgs.msg.MassProperties()
    else:
      self.m = pr_msgs.msg.MassProperties()

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
      buff.write(_struct_B10d.pack(_x.m.link, _x.m.mass, _x.m.cog_x, _x.m.cog_y, _x.m.cog_z, _x.m.inertia_xx, _x.m.inertia_xy, _x.m.inertia_xz, _x.m.inertia_yy, _x.m.inertia_yz, _x.m.inertia_zz))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.m is None:
        self.m = pr_msgs.msg.MassProperties()
      end = 0
      _x = self
      start = end
      end += 81
      (_x.m.link, _x.m.mass, _x.m.cog_x, _x.m.cog_y, _x.m.cog_z, _x.m.inertia_xx, _x.m.inertia_xy, _x.m.inertia_xz, _x.m.inertia_yy, _x.m.inertia_yz, _x.m.inertia_zz,) = _struct_B10d.unpack(str[start:end])
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
      buff.write(_struct_B10d.pack(_x.m.link, _x.m.mass, _x.m.cog_x, _x.m.cog_y, _x.m.cog_z, _x.m.inertia_xx, _x.m.inertia_xy, _x.m.inertia_xz, _x.m.inertia_yy, _x.m.inertia_yz, _x.m.inertia_zz))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.m is None:
        self.m = pr_msgs.msg.MassProperties()
      end = 0
      _x = self
      start = end
      end += 81
      (_x.m.link, _x.m.mass, _x.m.cog_x, _x.m.cog_y, _x.m.cog_z, _x.m.inertia_xx, _x.m.inertia_xy, _x.m.inertia_xz, _x.m.inertia_yy, _x.m.inertia_yz, _x.m.inertia_zz,) = _struct_B10d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B10d = struct.Struct("<B10d")
"""autogenerated by genpy from pr_msgs/SetExtraMassResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetExtraMassResponse(genpy.Message):
  _md5sum = "4679398f882e7cbdea165980d3ec2888"
  _type = "pr_msgs/SetExtraMassResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool ok
string reason


"""
  __slots__ = ['ok','reason']
  _slot_types = ['bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ok,reason

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetExtraMassResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.ok is None:
        self.ok = False
      if self.reason is None:
        self.reason = ''
    else:
      self.ok = False
      self.reason = ''

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
      buff.write(_struct_B.pack(self.ok))
      _x = self.reason
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _struct_B.unpack(str[start:end])
      self.ok = bool(self.ok)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.reason = str[start:end].decode('utf-8')
      else:
        self.reason = str[start:end]
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
      buff.write(_struct_B.pack(self.ok))
      _x = self.reason
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.ok,) = _struct_B.unpack(str[start:end])
      self.ok = bool(self.ok)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.reason = str[start:end].decode('utf-8')
      else:
        self.reason = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class SetExtraMass(object):
  _type          = 'pr_msgs/SetExtraMass'
  _md5sum = '6e56e849d39ef37144de532715dc61f9'
  _request_class  = SetExtraMassRequest
  _response_class = SetExtraMassResponse

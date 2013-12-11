"""autogenerated by genpy from coord_translator/ObjectTranslatorRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ObjectTranslatorRequest(genpy.Message):
  _md5sum = "c6eb39263756bf59242c791f46749c0f"
  _type = "coord_translator/ObjectTranslatorRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
string objname


"""
  __slots__ = ['objname']
  _slot_types = ['string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       objname

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectTranslatorRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.objname is None:
        self.objname = ''
    else:
      self.objname = ''

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
      _x = self.objname
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.objname = str[start:end].decode('utf-8')
      else:
        self.objname = str[start:end]
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
      _x = self.objname
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
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.objname = str[start:end].decode('utf-8')
      else:
        self.objname = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
"""autogenerated by genpy from coord_translator/ObjectTranslatorResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class ObjectTranslatorResponse(genpy.Message):
  _md5sum = "6d8104347d7e8516cb29e102a5348b7b"
  _type = "coord_translator/ObjectTranslatorResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
bool exists
string category
geometry_msgs/Point32 base_coordinates
geometry_msgs/Pose    arm_coordinates
int32 databaseID

================================================================================
MSG: geometry_msgs/Point32
# This contains the position of a point in free space(with 32 bits of precision).
# It is recommeded to use Point wherever possible instead of Point32.  
# 
# This recommendation is to promote interoperability.  
#
# This message is designed to take up less space when sending
# lots of points at once, as in the case of a PointCloud.  

float32 x
float32 y
float32 z
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
  __slots__ = ['exists','category','base_coordinates','arm_coordinates','databaseID']
  _slot_types = ['bool','string','geometry_msgs/Point32','geometry_msgs/Pose','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       exists,category,base_coordinates,arm_coordinates,databaseID

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObjectTranslatorResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.exists is None:
        self.exists = False
      if self.category is None:
        self.category = ''
      if self.base_coordinates is None:
        self.base_coordinates = geometry_msgs.msg.Point32()
      if self.arm_coordinates is None:
        self.arm_coordinates = geometry_msgs.msg.Pose()
      if self.databaseID is None:
        self.databaseID = 0
    else:
      self.exists = False
      self.category = ''
      self.base_coordinates = geometry_msgs.msg.Point32()
      self.arm_coordinates = geometry_msgs.msg.Pose()
      self.databaseID = 0

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
      buff.write(_struct_B.pack(self.exists))
      _x = self.category
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3f7di.pack(_x.base_coordinates.x, _x.base_coordinates.y, _x.base_coordinates.z, _x.arm_coordinates.position.x, _x.arm_coordinates.position.y, _x.arm_coordinates.position.z, _x.arm_coordinates.orientation.x, _x.arm_coordinates.orientation.y, _x.arm_coordinates.orientation.z, _x.arm_coordinates.orientation.w, _x.databaseID))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.base_coordinates is None:
        self.base_coordinates = geometry_msgs.msg.Point32()
      if self.arm_coordinates is None:
        self.arm_coordinates = geometry_msgs.msg.Pose()
      end = 0
      start = end
      end += 1
      (self.exists,) = _struct_B.unpack(str[start:end])
      self.exists = bool(self.exists)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.category = str[start:end].decode('utf-8')
      else:
        self.category = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.base_coordinates.x, _x.base_coordinates.y, _x.base_coordinates.z, _x.arm_coordinates.position.x, _x.arm_coordinates.position.y, _x.arm_coordinates.position.z, _x.arm_coordinates.orientation.x, _x.arm_coordinates.orientation.y, _x.arm_coordinates.orientation.z, _x.arm_coordinates.orientation.w, _x.databaseID,) = _struct_3f7di.unpack(str[start:end])
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
      buff.write(_struct_B.pack(self.exists))
      _x = self.category
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3f7di.pack(_x.base_coordinates.x, _x.base_coordinates.y, _x.base_coordinates.z, _x.arm_coordinates.position.x, _x.arm_coordinates.position.y, _x.arm_coordinates.position.z, _x.arm_coordinates.orientation.x, _x.arm_coordinates.orientation.y, _x.arm_coordinates.orientation.z, _x.arm_coordinates.orientation.w, _x.databaseID))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.base_coordinates is None:
        self.base_coordinates = geometry_msgs.msg.Point32()
      if self.arm_coordinates is None:
        self.arm_coordinates = geometry_msgs.msg.Pose()
      end = 0
      start = end
      end += 1
      (self.exists,) = _struct_B.unpack(str[start:end])
      self.exists = bool(self.exists)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.category = str[start:end].decode('utf-8')
      else:
        self.category = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.base_coordinates.x, _x.base_coordinates.y, _x.base_coordinates.z, _x.arm_coordinates.position.x, _x.arm_coordinates.position.y, _x.arm_coordinates.position.z, _x.arm_coordinates.orientation.x, _x.arm_coordinates.orientation.y, _x.arm_coordinates.orientation.z, _x.arm_coordinates.orientation.w, _x.databaseID,) = _struct_3f7di.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3f7di = struct.Struct("<3f7di")
_struct_B = struct.Struct("<B")
class ObjectTranslator(object):
  _type          = 'coord_translator/ObjectTranslator'
  _md5sum = '748eae5c7c477554adef5020bb3c1c94'
  _request_class  = ObjectTranslatorRequest
  _response_class = ObjectTranslatorResponse
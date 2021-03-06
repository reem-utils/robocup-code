"""autogenerated by genpy from estirabot_msgs/DirtyArea.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import estirabot_msgs.msg
import iri_perception_msgs.msg

class DirtyArea(genpy.Message):
  _md5sum = "2b156136a0460cfb7965b803a38c7cc1"
  _type = "estirabot_msgs/DirtyArea"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 id
estirabot_msgs/Ellipse ellipse
bool sparse
uint8 area
uint8 shape

================================================================================
MSG: estirabot_msgs/Ellipse
iri_perception_msgs/ImagePoint center
iri_perception_msgs/ImageSize size
float64 angle

================================================================================
MSG: iri_perception_msgs/ImagePoint
uint32 x
uint32 y
================================================================================
MSG: iri_perception_msgs/ImageSize
uint32 width
uint32 height
"""
  __slots__ = ['id','ellipse','sparse','area','shape']
  _slot_types = ['int32','estirabot_msgs/Ellipse','bool','uint8','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,ellipse,sparse,area,shape

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DirtyArea, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.ellipse is None:
        self.ellipse = estirabot_msgs.msg.Ellipse()
      if self.sparse is None:
        self.sparse = False
      if self.area is None:
        self.area = 0
      if self.shape is None:
        self.shape = 0
    else:
      self.id = 0
      self.ellipse = estirabot_msgs.msg.Ellipse()
      self.sparse = False
      self.area = 0
      self.shape = 0

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
      buff.write(_struct_i4Id3B.pack(_x.id, _x.ellipse.center.x, _x.ellipse.center.y, _x.ellipse.size.width, _x.ellipse.size.height, _x.ellipse.angle, _x.sparse, _x.area, _x.shape))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.ellipse is None:
        self.ellipse = estirabot_msgs.msg.Ellipse()
      end = 0
      _x = self
      start = end
      end += 31
      (_x.id, _x.ellipse.center.x, _x.ellipse.center.y, _x.ellipse.size.width, _x.ellipse.size.height, _x.ellipse.angle, _x.sparse, _x.area, _x.shape,) = _struct_i4Id3B.unpack(str[start:end])
      self.sparse = bool(self.sparse)
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
      buff.write(_struct_i4Id3B.pack(_x.id, _x.ellipse.center.x, _x.ellipse.center.y, _x.ellipse.size.width, _x.ellipse.size.height, _x.ellipse.angle, _x.sparse, _x.area, _x.shape))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.ellipse is None:
        self.ellipse = estirabot_msgs.msg.Ellipse()
      end = 0
      _x = self
      start = end
      end += 31
      (_x.id, _x.ellipse.center.x, _x.ellipse.center.y, _x.ellipse.size.width, _x.ellipse.size.height, _x.ellipse.angle, _x.sparse, _x.area, _x.shape,) = _struct_i4Id3B.unpack(str[start:end])
      self.sparse = bool(self.sparse)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i4Id3B = struct.Struct("<i4Id3B")

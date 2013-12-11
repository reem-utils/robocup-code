"""autogenerated by genpy from iri_perception_msgs/single_img_detection.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class single_img_detection(genpy.Message):
  _md5sum = "391d7f7d52529da7a7a00d7423444dda"
  _type = "iri_perception_msgs/single_img_detection"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# detection identifier
uint32 id

# OpenCV cv::Rect structure
# upper-left corner and width+height from the detection
float32 x
float32 y
float32 width
float32 height

# detection score
float32 score
"""
  __slots__ = ['id','x','y','width','height','score']
  _slot_types = ['uint32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,x,y,width,height,score

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(single_img_detection, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.width is None:
        self.width = 0.
      if self.height is None:
        self.height = 0.
      if self.score is None:
        self.score = 0.
    else:
      self.id = 0
      self.x = 0.
      self.y = 0.
      self.width = 0.
      self.height = 0.
      self.score = 0.

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
      buff.write(_struct_I5f.pack(_x.id, _x.x, _x.y, _x.width, _x.height, _x.score))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 24
      (_x.id, _x.x, _x.y, _x.width, _x.height, _x.score,) = _struct_I5f.unpack(str[start:end])
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
      buff.write(_struct_I5f.pack(_x.id, _x.x, _x.y, _x.width, _x.height, _x.score))
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
      _x = self
      start = end
      end += 24
      (_x.id, _x.x, _x.y, _x.width, _x.height, _x.score,) = _struct_I5f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_I5f = struct.Struct("<I5f")

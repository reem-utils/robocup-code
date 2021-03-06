"""autogenerated by genpy from person_detector_mock/peopleTracking.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class peopleTracking(genpy.Message):
  _md5sum = "70343516d9aaa5364e362443390175f5"
  _type = "person_detector_mock/peopleTracking"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 targetId
float64 x
float64 y
float64 vx
float64 vy
float64[16] covariances

"""
  __slots__ = ['targetId','x','y','vx','vy','covariances']
  _slot_types = ['int32','float64','float64','float64','float64','float64[16]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       targetId,x,y,vx,vy,covariances

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(peopleTracking, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.targetId is None:
        self.targetId = 0
      if self.x is None:
        self.x = 0.
      if self.y is None:
        self.y = 0.
      if self.vx is None:
        self.vx = 0.
      if self.vy is None:
        self.vy = 0.
      if self.covariances is None:
        self.covariances = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
    else:
      self.targetId = 0
      self.x = 0.
      self.y = 0.
      self.vx = 0.
      self.vy = 0.
      self.covariances = [0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

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
      buff.write(_struct_i4d.pack(_x.targetId, _x.x, _x.y, _x.vx, _x.vy))
      buff.write(_struct_16d.pack(*self.covariances))
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
      end += 36
      (_x.targetId, _x.x, _x.y, _x.vx, _x.vy,) = _struct_i4d.unpack(str[start:end])
      start = end
      end += 128
      self.covariances = _struct_16d.unpack(str[start:end])
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
      buff.write(_struct_i4d.pack(_x.targetId, _x.x, _x.y, _x.vx, _x.vy))
      buff.write(self.covariances.tostring())
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
      end += 36
      (_x.targetId, _x.x, _x.y, _x.vx, _x.vy,) = _struct_i4d.unpack(str[start:end])
      start = end
      end += 128
      self.covariances = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=16)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_16d = struct.Struct("<16d")
_struct_i4d = struct.Struct("<i4d")

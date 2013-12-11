"""autogenerated by genpy from estirabot_msgs/AddActionRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import estirabot_msgs.msg
import iri_perception_msgs.msg

class AddActionRequest(genpy.Message):
  _md5sum = "8b2f9ffeecdc99c7f6cf766613ded2cf"
  _type = "estirabot_msgs/AddActionRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string action
estirabot_msgs/DirtyArea[] dirty_areas
estirabot_msgs/ArrayIndexes target_dirty_areas
estirabot_msgs/PointsDistanceMsg[] distances
string state_string
bool action_movements_successful

================================================================================
MSG: estirabot_msgs/DirtyArea
int32 id
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
================================================================================
MSG: estirabot_msgs/ArrayIndexes
uint32[] indexes
================================================================================
MSG: estirabot_msgs/PointsDistanceMsg
uint32 origIdx
uint32 dstIdx
float64 distance

"""
  __slots__ = ['action','dirty_areas','target_dirty_areas','distances','state_string','action_movements_successful']
  _slot_types = ['string','estirabot_msgs/DirtyArea[]','estirabot_msgs/ArrayIndexes','estirabot_msgs/PointsDistanceMsg[]','string','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       action,dirty_areas,target_dirty_areas,distances,state_string,action_movements_successful

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AddActionRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.action is None:
        self.action = ''
      if self.dirty_areas is None:
        self.dirty_areas = []
      if self.target_dirty_areas is None:
        self.target_dirty_areas = estirabot_msgs.msg.ArrayIndexes()
      if self.distances is None:
        self.distances = []
      if self.state_string is None:
        self.state_string = ''
      if self.action_movements_successful is None:
        self.action_movements_successful = False
    else:
      self.action = ''
      self.dirty_areas = []
      self.target_dirty_areas = estirabot_msgs.msg.ArrayIndexes()
      self.distances = []
      self.state_string = ''
      self.action_movements_successful = False

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
      _x = self.action
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.dirty_areas)
      buff.write(_struct_I.pack(length))
      for val1 in self.dirty_areas:
        buff.write(_struct_i.pack(val1.id))
        _v1 = val1.ellipse
        _v2 = _v1.center
        _x = _v2
        buff.write(_struct_2I.pack(_x.x, _x.y))
        _v3 = _v1.size
        _x = _v3
        buff.write(_struct_2I.pack(_x.width, _x.height))
        buff.write(_struct_d.pack(_v1.angle))
        _x = val1
        buff.write(_struct_3B.pack(_x.sparse, _x.area, _x.shape))
      length = len(self.target_dirty_areas.indexes)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(struct.pack(pattern, *self.target_dirty_areas.indexes))
      length = len(self.distances)
      buff.write(_struct_I.pack(length))
      for val1 in self.distances:
        _x = val1
        buff.write(_struct_2Id.pack(_x.origIdx, _x.dstIdx, _x.distance))
      _x = self.state_string
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.action_movements_successful))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.dirty_areas is None:
        self.dirty_areas = None
      if self.target_dirty_areas is None:
        self.target_dirty_areas = estirabot_msgs.msg.ArrayIndexes()
      if self.distances is None:
        self.distances = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action = str[start:end].decode('utf-8')
      else:
        self.action = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.dirty_areas = []
      for i in range(0, length):
        val1 = estirabot_msgs.msg.DirtyArea()
        start = end
        end += 4
        (val1.id,) = _struct_i.unpack(str[start:end])
        _v4 = val1.ellipse
        _v5 = _v4.center
        _x = _v5
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2I.unpack(str[start:end])
        _v6 = _v4.size
        _x = _v6
        start = end
        end += 8
        (_x.width, _x.height,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 8
        (_v4.angle,) = _struct_d.unpack(str[start:end])
        _x = val1
        start = end
        end += 3
        (_x.sparse, _x.area, _x.shape,) = _struct_3B.unpack(str[start:end])
        val1.sparse = bool(val1.sparse)
        self.dirty_areas.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.target_dirty_areas.indexes = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.distances = []
      for i in range(0, length):
        val1 = estirabot_msgs.msg.PointsDistanceMsg()
        _x = val1
        start = end
        end += 16
        (_x.origIdx, _x.dstIdx, _x.distance,) = _struct_2Id.unpack(str[start:end])
        self.distances.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_string = str[start:end].decode('utf-8')
      else:
        self.state_string = str[start:end]
      start = end
      end += 1
      (self.action_movements_successful,) = _struct_B.unpack(str[start:end])
      self.action_movements_successful = bool(self.action_movements_successful)
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
      _x = self.action
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.dirty_areas)
      buff.write(_struct_I.pack(length))
      for val1 in self.dirty_areas:
        buff.write(_struct_i.pack(val1.id))
        _v7 = val1.ellipse
        _v8 = _v7.center
        _x = _v8
        buff.write(_struct_2I.pack(_x.x, _x.y))
        _v9 = _v7.size
        _x = _v9
        buff.write(_struct_2I.pack(_x.width, _x.height))
        buff.write(_struct_d.pack(_v7.angle))
        _x = val1
        buff.write(_struct_3B.pack(_x.sparse, _x.area, _x.shape))
      length = len(self.target_dirty_areas.indexes)
      buff.write(_struct_I.pack(length))
      pattern = '<%sI'%length
      buff.write(self.target_dirty_areas.indexes.tostring())
      length = len(self.distances)
      buff.write(_struct_I.pack(length))
      for val1 in self.distances:
        _x = val1
        buff.write(_struct_2Id.pack(_x.origIdx, _x.dstIdx, _x.distance))
      _x = self.state_string
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.action_movements_successful))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.dirty_areas is None:
        self.dirty_areas = None
      if self.target_dirty_areas is None:
        self.target_dirty_areas = estirabot_msgs.msg.ArrayIndexes()
      if self.distances is None:
        self.distances = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action = str[start:end].decode('utf-8')
      else:
        self.action = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.dirty_areas = []
      for i in range(0, length):
        val1 = estirabot_msgs.msg.DirtyArea()
        start = end
        end += 4
        (val1.id,) = _struct_i.unpack(str[start:end])
        _v10 = val1.ellipse
        _v11 = _v10.center
        _x = _v11
        start = end
        end += 8
        (_x.x, _x.y,) = _struct_2I.unpack(str[start:end])
        _v12 = _v10.size
        _x = _v12
        start = end
        end += 8
        (_x.width, _x.height,) = _struct_2I.unpack(str[start:end])
        start = end
        end += 8
        (_v10.angle,) = _struct_d.unpack(str[start:end])
        _x = val1
        start = end
        end += 3
        (_x.sparse, _x.area, _x.shape,) = _struct_3B.unpack(str[start:end])
        val1.sparse = bool(val1.sparse)
        self.dirty_areas.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sI'%length
      start = end
      end += struct.calcsize(pattern)
      self.target_dirty_areas.indexes = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.distances = []
      for i in range(0, length):
        val1 = estirabot_msgs.msg.PointsDistanceMsg()
        _x = val1
        start = end
        end += 16
        (_x.origIdx, _x.dstIdx, _x.distance,) = _struct_2Id.unpack(str[start:end])
        self.distances.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.state_string = str[start:end].decode('utf-8')
      else:
        self.state_string = str[start:end]
      start = end
      end += 1
      (self.action_movements_successful,) = _struct_B.unpack(str[start:end])
      self.action_movements_successful = bool(self.action_movements_successful)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
_struct_d = struct.Struct("<d")
_struct_i = struct.Struct("<i")
_struct_3B = struct.Struct("<3B")
_struct_2Id = struct.Struct("<2Id")
_struct_2I = struct.Struct("<2I")
"""autogenerated by genpy from estirabot_msgs/AddActionResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class AddActionResponse(genpy.Message):
  _md5sum = "f4377acd93bf078f61b24c8bc67a2b51"
  _type = "estirabot_msgs/AddActionResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool needs_learning


"""
  __slots__ = ['needs_learning']
  _slot_types = ['bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       needs_learning

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(AddActionResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.needs_learning is None:
        self.needs_learning = False
    else:
      self.needs_learning = False

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
      buff.write(_struct_B.pack(self.needs_learning))
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
      (self.needs_learning,) = _struct_B.unpack(str[start:end])
      self.needs_learning = bool(self.needs_learning)
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
      buff.write(_struct_B.pack(self.needs_learning))
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
      (self.needs_learning,) = _struct_B.unpack(str[start:end])
      self.needs_learning = bool(self.needs_learning)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B = struct.Struct("<B")
class AddAction(object):
  _type          = 'estirabot_msgs/AddAction'
  _md5sum = '3ef83f1df6473e149ff74e23eea70811'
  _request_class  = AddActionRequest
  _response_class = AddActionResponse
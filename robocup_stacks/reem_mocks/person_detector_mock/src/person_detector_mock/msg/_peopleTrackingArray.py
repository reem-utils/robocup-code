"""autogenerated by genpy from person_detector_mock/peopleTrackingArray.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import person_detector_mock.msg
import std_msgs.msg

class peopleTrackingArray(genpy.Message):
  _md5sum = "b1a0bb603fc2724e6108a7fa1155e266"
  _type = "person_detector_mock/peopleTrackingArray"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# timestamp, frame id
Header header

#set of targets being tracked
peopleTracking[] peopleSet

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
MSG: person_detector_mock/peopleTracking
int32 targetId
float64 x
float64 y
float64 vx
float64 vy
float64[16] covariances

"""
  __slots__ = ['header','peopleSet']
  _slot_types = ['std_msgs/Header','person_detector_mock/peopleTracking[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,peopleSet

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(peopleTrackingArray, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.peopleSet is None:
        self.peopleSet = []
    else:
      self.header = std_msgs.msg.Header()
      self.peopleSet = []

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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.peopleSet)
      buff.write(_struct_I.pack(length))
      for val1 in self.peopleSet:
        _x = val1
        buff.write(_struct_i4d.pack(_x.targetId, _x.x, _x.y, _x.vx, _x.vy))
        buff.write(_struct_16d.pack(*val1.covariances))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.peopleSet is None:
        self.peopleSet = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.peopleSet = []
      for i in range(0, length):
        val1 = person_detector_mock.msg.peopleTracking()
        _x = val1
        start = end
        end += 36
        (_x.targetId, _x.x, _x.y, _x.vx, _x.vy,) = _struct_i4d.unpack(str[start:end])
        start = end
        end += 128
        val1.covariances = _struct_16d.unpack(str[start:end])
        self.peopleSet.append(val1)
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
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.peopleSet)
      buff.write(_struct_I.pack(length))
      for val1 in self.peopleSet:
        _x = val1
        buff.write(_struct_i4d.pack(_x.targetId, _x.x, _x.y, _x.vx, _x.vy))
        buff.write(val1.covariances.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.peopleSet is None:
        self.peopleSet = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.peopleSet = []
      for i in range(0, length):
        val1 = person_detector_mock.msg.peopleTracking()
        _x = val1
        start = end
        end += 36
        (_x.targetId, _x.x, _x.y, _x.vx, _x.vy,) = _struct_i4d.unpack(str[start:end])
        start = end
        end += 128
        val1.covariances = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=16)
        self.peopleSet.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_16d = struct.Struct("<16d")
_struct_3I = struct.Struct("<3I")
_struct_i4d = struct.Struct("<i4d")

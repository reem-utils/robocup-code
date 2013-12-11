"""autogenerated by genpy from iri_perception_msgs/PclToDescriptorSetRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg
import sensor_msgs.msg

class PclToDescriptorSetRequest(genpy.Message):
  _md5sum = "56680b720436a8fbd002ea7abe6966e1"
  _type = "iri_perception_msgs/PclToDescriptorSetRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
sensor_msgs/PointCloud2 pointcloud

================================================================================
MSG: sensor_msgs/PointCloud2
# This message holds a collection of N-dimensional points, which may
# contain additional information such as normals, intensity, etc. The
# point data is stored as a binary blob, its layout described by the
# contents of the "fields" array.

# The point cloud data may be organized 2d (image-like) or 1d
# (unordered). Point clouds organized as 2d images may be produced by
# camera depth sensors such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d
# points).
Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points

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
MSG: sensor_msgs/PointField
# This message holds the description of one point entry in the
# PointCloud2 message format.
uint8 INT8    = 1
uint8 UINT8   = 2
uint8 INT16   = 3
uint8 UINT16  = 4
uint8 INT32   = 5
uint8 UINT32  = 6
uint8 FLOAT32 = 7
uint8 FLOAT64 = 8

string name      # Name of field
uint32 offset    # Offset from start of point struct
uint8  datatype  # Datatype enumeration, see above
uint32 count     # How many elements in the field

"""
  __slots__ = ['pointcloud']
  _slot_types = ['sensor_msgs/PointCloud2']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       pointcloud

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PclToDescriptorSetRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.pointcloud is None:
        self.pointcloud = sensor_msgs.msg.PointCloud2()
    else:
      self.pointcloud = sensor_msgs.msg.PointCloud2()

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
      buff.write(_struct_3I.pack(_x.pointcloud.header.seq, _x.pointcloud.header.stamp.secs, _x.pointcloud.header.stamp.nsecs))
      _x = self.pointcloud.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.pointcloud.height, _x.pointcloud.width))
      length = len(self.pointcloud.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.pointcloud.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_IBI.pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_struct_B2I.pack(_x.pointcloud.is_bigendian, _x.pointcloud.point_step, _x.pointcloud.row_step))
      _x = self.pointcloud.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.pointcloud.is_dense))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.pointcloud is None:
        self.pointcloud = sensor_msgs.msg.PointCloud2()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.pointcloud.header.seq, _x.pointcloud.header.stamp.secs, _x.pointcloud.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pointcloud.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pointcloud.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.pointcloud.height, _x.pointcloud.width,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pointcloud.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _struct_IBI.unpack(str[start:end])
        self.pointcloud.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.pointcloud.is_bigendian, _x.pointcloud.point_step, _x.pointcloud.row_step,) = _struct_B2I.unpack(str[start:end])
      self.pointcloud.is_bigendian = bool(self.pointcloud.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pointcloud.data = str[start:end].decode('utf-8')
      else:
        self.pointcloud.data = str[start:end]
      start = end
      end += 1
      (self.pointcloud.is_dense,) = _struct_B.unpack(str[start:end])
      self.pointcloud.is_dense = bool(self.pointcloud.is_dense)
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
      buff.write(_struct_3I.pack(_x.pointcloud.header.seq, _x.pointcloud.header.stamp.secs, _x.pointcloud.header.stamp.nsecs))
      _x = self.pointcloud.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.pointcloud.height, _x.pointcloud.width))
      length = len(self.pointcloud.fields)
      buff.write(_struct_I.pack(length))
      for val1 in self.pointcloud.fields:
        _x = val1.name
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.pack('<I%ss'%length, length, _x))
        _x = val1
        buff.write(_struct_IBI.pack(_x.offset, _x.datatype, _x.count))
      _x = self
      buff.write(_struct_B2I.pack(_x.pointcloud.is_bigendian, _x.pointcloud.point_step, _x.pointcloud.row_step))
      _x = self.pointcloud.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.pointcloud.is_dense))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.pointcloud is None:
        self.pointcloud = sensor_msgs.msg.PointCloud2()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.pointcloud.header.seq, _x.pointcloud.header.stamp.secs, _x.pointcloud.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pointcloud.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.pointcloud.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.pointcloud.height, _x.pointcloud.width,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.pointcloud.fields = []
      for i in range(0, length):
        val1 = sensor_msgs.msg.PointField()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.name = str[start:end].decode('utf-8')
        else:
          val1.name = str[start:end]
        _x = val1
        start = end
        end += 9
        (_x.offset, _x.datatype, _x.count,) = _struct_IBI.unpack(str[start:end])
        self.pointcloud.fields.append(val1)
      _x = self
      start = end
      end += 9
      (_x.pointcloud.is_bigendian, _x.pointcloud.point_step, _x.pointcloud.row_step,) = _struct_B2I.unpack(str[start:end])
      self.pointcloud.is_bigendian = bool(self.pointcloud.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.pointcloud.data = str[start:end].decode('utf-8')
      else:
        self.pointcloud.data = str[start:end]
      start = end
      end += 1
      (self.pointcloud.is_dense,) = _struct_B.unpack(str[start:end])
      self.pointcloud.is_dense = bool(self.pointcloud.is_dense)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_IBI = struct.Struct("<IBI")
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_2I = struct.Struct("<2I")
_struct_B2I = struct.Struct("<B2I")
"""autogenerated by genpy from iri_perception_msgs/PclToDescriptorSetResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import iri_perception_msgs.msg
import std_msgs.msg

class PclToDescriptorSetResponse(genpy.Message):
  _md5sum = "db5e12e66d3b02ca867728f150b58d69"
  _type = "iri_perception_msgs/PclToDescriptorSetResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
iri_perception_msgs/DescriptorSet descriptor_set


================================================================================
MSG: iri_perception_msgs/DescriptorSet
Header header
int32 num_orient_bins
int32 num_spa_bins
int32 num
int32 len
int32 width
int32 height
iri_perception_msgs/Descriptor[] descriptors

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
MSG: iri_perception_msgs/Descriptor
float32[] descriptor
geometry_msgs/Vector3 point3d
int32 u
int32 v
float32 orientation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
"""
  __slots__ = ['descriptor_set']
  _slot_types = ['iri_perception_msgs/DescriptorSet']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       descriptor_set

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PclToDescriptorSetResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.descriptor_set is None:
        self.descriptor_set = iri_perception_msgs.msg.DescriptorSet()
    else:
      self.descriptor_set = iri_perception_msgs.msg.DescriptorSet()

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
      buff.write(_struct_3I.pack(_x.descriptor_set.header.seq, _x.descriptor_set.header.stamp.secs, _x.descriptor_set.header.stamp.nsecs))
      _x = self.descriptor_set.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6i.pack(_x.descriptor_set.num_orient_bins, _x.descriptor_set.num_spa_bins, _x.descriptor_set.num, _x.descriptor_set.len, _x.descriptor_set.width, _x.descriptor_set.height))
      length = len(self.descriptor_set.descriptors)
      buff.write(_struct_I.pack(length))
      for val1 in self.descriptor_set.descriptors:
        length = len(val1.descriptor)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.descriptor))
        _v1 = val1.point3d
        _x = _v1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_2if.pack(_x.u, _x.v, _x.orientation))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.descriptor_set is None:
        self.descriptor_set = iri_perception_msgs.msg.DescriptorSet()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.descriptor_set.header.seq, _x.descriptor_set.header.stamp.secs, _x.descriptor_set.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.descriptor_set.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.descriptor_set.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.descriptor_set.num_orient_bins, _x.descriptor_set.num_spa_bins, _x.descriptor_set.num, _x.descriptor_set.len, _x.descriptor_set.width, _x.descriptor_set.height,) = _struct_6i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.descriptor_set.descriptors = []
      for i in range(0, length):
        val1 = iri_perception_msgs.msg.Descriptor()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.descriptor = struct.unpack(pattern, str[start:end])
        _v2 = val1.point3d
        _x = _v2
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 12
        (_x.u, _x.v, _x.orientation,) = _struct_2if.unpack(str[start:end])
        self.descriptor_set.descriptors.append(val1)
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
      buff.write(_struct_3I.pack(_x.descriptor_set.header.seq, _x.descriptor_set.header.stamp.secs, _x.descriptor_set.header.stamp.nsecs))
      _x = self.descriptor_set.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6i.pack(_x.descriptor_set.num_orient_bins, _x.descriptor_set.num_spa_bins, _x.descriptor_set.num, _x.descriptor_set.len, _x.descriptor_set.width, _x.descriptor_set.height))
      length = len(self.descriptor_set.descriptors)
      buff.write(_struct_I.pack(length))
      for val1 in self.descriptor_set.descriptors:
        length = len(val1.descriptor)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.descriptor.tostring())
        _v3 = val1.point3d
        _x = _v3
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _x = val1
        buff.write(_struct_2if.pack(_x.u, _x.v, _x.orientation))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.descriptor_set is None:
        self.descriptor_set = iri_perception_msgs.msg.DescriptorSet()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.descriptor_set.header.seq, _x.descriptor_set.header.stamp.secs, _x.descriptor_set.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.descriptor_set.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.descriptor_set.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 24
      (_x.descriptor_set.num_orient_bins, _x.descriptor_set.num_spa_bins, _x.descriptor_set.num, _x.descriptor_set.len, _x.descriptor_set.width, _x.descriptor_set.height,) = _struct_6i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.descriptor_set.descriptors = []
      for i in range(0, length):
        val1 = iri_perception_msgs.msg.Descriptor()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.descriptor = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        _v4 = val1.point3d
        _x = _v4
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _x = val1
        start = end
        end += 12
        (_x.u, _x.v, _x.orientation,) = _struct_2if.unpack(str[start:end])
        self.descriptor_set.descriptors.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2if = struct.Struct("<2if")
_struct_6i = struct.Struct("<6i")
_struct_3I = struct.Struct("<3I")
_struct_3d = struct.Struct("<3d")
class PclToDescriptorSet(object):
  _type          = 'iri_perception_msgs/PclToDescriptorSet'
  _md5sum = 'f55bbc2d3d079e04fdc51edb942f1d11'
  _request_class  = PclToDescriptorSetRequest
  _response_class = PclToDescriptorSetResponse
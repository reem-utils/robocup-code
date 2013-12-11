"""autogenerated by genpy from pr_msgs/ReplaceTrajectoryRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import pr_msgs.msg

class ReplaceTrajectoryRequest(genpy.Message):
  _md5sum = "f88b0684f828fc14e642b3386053416d"
  _type = "pr_msgs/ReplaceTrajectoryRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """pr_msgs/JointTraj traj
uint32 id

================================================================================
MSG: pr_msgs/JointTraj
pr_msgs/Joints[] positions
float32[] blend_radius
uint32 options

# options should be powers of 2, so that they can be OR'd together
uint32 opt_WaitForStart=1
uint32 opt_CancelOnStall=2
uint32 opt_CancelOnForceInput=4
uint32 opt_CancelOnTactileInput=8
#uint32 opt_          =16  # placeholder for next value

================================================================================
MSG: pr_msgs/Joints
float64[] j

"""
  __slots__ = ['traj','id']
  _slot_types = ['pr_msgs/JointTraj','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       traj,id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReplaceTrajectoryRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.traj is None:
        self.traj = pr_msgs.msg.JointTraj()
      if self.id is None:
        self.id = 0
    else:
      self.traj = pr_msgs.msg.JointTraj()
      self.id = 0

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
      length = len(self.traj.positions)
      buff.write(_struct_I.pack(length))
      for val1 in self.traj.positions:
        length = len(val1.j)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *val1.j))
      length = len(self.traj.blend_radius)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.traj.blend_radius))
      _x = self
      buff.write(_struct_2I.pack(_x.traj.options, _x.id))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.traj is None:
        self.traj = pr_msgs.msg.JointTraj()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.traj.positions = []
      for i in range(0, length):
        val1 = pr_msgs.msg.Joints()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.j = struct.unpack(pattern, str[start:end])
        self.traj.positions.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.traj.blend_radius = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 8
      (_x.traj.options, _x.id,) = _struct_2I.unpack(str[start:end])
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
      length = len(self.traj.positions)
      buff.write(_struct_I.pack(length))
      for val1 in self.traj.positions:
        length = len(val1.j)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(val1.j.tostring())
      length = len(self.traj.blend_radius)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.traj.blend_radius.tostring())
      _x = self
      buff.write(_struct_2I.pack(_x.traj.options, _x.id))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.traj is None:
        self.traj = pr_msgs.msg.JointTraj()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.traj.positions = []
      for i in range(0, length):
        val1 = pr_msgs.msg.Joints()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        val1.j = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        self.traj.positions.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.traj.blend_radius = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 8
      (_x.traj.options, _x.id,) = _struct_2I.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_2I = struct.Struct("<2I")
"""autogenerated by genpy from pr_msgs/ReplaceTrajectoryResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ReplaceTrajectoryResponse(genpy.Message):
  _md5sum = "309d4b30834b338cced19e5622a97a03"
  _type = "pr_msgs/ReplaceTrajectoryResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """uint32 id


"""
  __slots__ = ['id']
  _slot_types = ['uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ReplaceTrajectoryResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
    else:
      self.id = 0

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
      buff.write(_struct_I.pack(self.id))
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
      (self.id,) = _struct_I.unpack(str[start:end])
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
      buff.write(_struct_I.pack(self.id))
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
      (self.id,) = _struct_I.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
class ReplaceTrajectory(object):
  _type          = 'pr_msgs/ReplaceTrajectory'
  _md5sum = '97dd1d908c94df542702cce333822c2a'
  _request_class  = ReplaceTrajectoryRequest
  _response_class = ReplaceTrajectoryResponse
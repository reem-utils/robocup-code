"""autogenerated by genpy from pr_msgs/WAMPrecomputedBlendedTrajectory.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import pr_msgs.msg

class WAMPrecomputedBlendedTrajectory(genpy.Message):
  _md5sum = "71bcabe3695718cad854012f233bf235"
  _type = "pr_msgs/WAMPrecomputedBlendedTrajectory"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int16 id
bool HoldOnStall
bool WaitForStart
pr_msgs/Joints start_position
pr_msgs/Joints end_position
pr_msgs/Joints max_joint_vel
pr_msgs/Joints max_joint_accel
pr_msgs/WAMPrecomputedBlendElement[] macpieces
float64 traj_duration

================================================================================
MSG: pr_msgs/Joints
float64[] j

================================================================================
MSG: pr_msgs/WAMPrecomputedBlendElement
pr_msgs/Joints start_pos
pr_msgs/Joints end_pos
float64 start_time
float64 duration
float64 max_path_velocity
float64 max_path_acceleration

"""
  __slots__ = ['id','HoldOnStall','WaitForStart','start_position','end_position','max_joint_vel','max_joint_accel','macpieces','traj_duration']
  _slot_types = ['int16','bool','bool','pr_msgs/Joints','pr_msgs/Joints','pr_msgs/Joints','pr_msgs/Joints','pr_msgs/WAMPrecomputedBlendElement[]','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,HoldOnStall,WaitForStart,start_position,end_position,max_joint_vel,max_joint_accel,macpieces,traj_duration

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WAMPrecomputedBlendedTrajectory, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.HoldOnStall is None:
        self.HoldOnStall = False
      if self.WaitForStart is None:
        self.WaitForStart = False
      if self.start_position is None:
        self.start_position = pr_msgs.msg.Joints()
      if self.end_position is None:
        self.end_position = pr_msgs.msg.Joints()
      if self.max_joint_vel is None:
        self.max_joint_vel = pr_msgs.msg.Joints()
      if self.max_joint_accel is None:
        self.max_joint_accel = pr_msgs.msg.Joints()
      if self.macpieces is None:
        self.macpieces = []
      if self.traj_duration is None:
        self.traj_duration = 0.
    else:
      self.id = 0
      self.HoldOnStall = False
      self.WaitForStart = False
      self.start_position = pr_msgs.msg.Joints()
      self.end_position = pr_msgs.msg.Joints()
      self.max_joint_vel = pr_msgs.msg.Joints()
      self.max_joint_accel = pr_msgs.msg.Joints()
      self.macpieces = []
      self.traj_duration = 0.

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
      buff.write(_struct_h2B.pack(_x.id, _x.HoldOnStall, _x.WaitForStart))
      length = len(self.start_position.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.start_position.j))
      length = len(self.end_position.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.end_position.j))
      length = len(self.max_joint_vel.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.max_joint_vel.j))
      length = len(self.max_joint_accel.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.max_joint_accel.j))
      length = len(self.macpieces)
      buff.write(_struct_I.pack(length))
      for val1 in self.macpieces:
        _v1 = val1.start_pos
        length = len(_v1.j)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *_v1.j))
        _v2 = val1.end_pos
        length = len(_v2.j)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(struct.pack(pattern, *_v2.j))
        _x = val1
        buff.write(_struct_4d.pack(_x.start_time, _x.duration, _x.max_path_velocity, _x.max_path_acceleration))
      buff.write(_struct_d.pack(self.traj_duration))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.start_position is None:
        self.start_position = pr_msgs.msg.Joints()
      if self.end_position is None:
        self.end_position = pr_msgs.msg.Joints()
      if self.max_joint_vel is None:
        self.max_joint_vel = pr_msgs.msg.Joints()
      if self.max_joint_accel is None:
        self.max_joint_accel = pr_msgs.msg.Joints()
      if self.macpieces is None:
        self.macpieces = None
      end = 0
      _x = self
      start = end
      end += 4
      (_x.id, _x.HoldOnStall, _x.WaitForStart,) = _struct_h2B.unpack(str[start:end])
      self.HoldOnStall = bool(self.HoldOnStall)
      self.WaitForStart = bool(self.WaitForStart)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.start_position.j = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.end_position.j = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.max_joint_vel.j = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.max_joint_accel.j = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.macpieces = []
      for i in range(0, length):
        val1 = pr_msgs.msg.WAMPrecomputedBlendElement()
        _v3 = val1.start_pos
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        _v3.j = struct.unpack(pattern, str[start:end])
        _v4 = val1.end_pos
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        _v4.j = struct.unpack(pattern, str[start:end])
        _x = val1
        start = end
        end += 32
        (_x.start_time, _x.duration, _x.max_path_velocity, _x.max_path_acceleration,) = _struct_4d.unpack(str[start:end])
        self.macpieces.append(val1)
      start = end
      end += 8
      (self.traj_duration,) = _struct_d.unpack(str[start:end])
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
      buff.write(_struct_h2B.pack(_x.id, _x.HoldOnStall, _x.WaitForStart))
      length = len(self.start_position.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.start_position.j.tostring())
      length = len(self.end_position.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.end_position.j.tostring())
      length = len(self.max_joint_vel.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.max_joint_vel.j.tostring())
      length = len(self.max_joint_accel.j)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.max_joint_accel.j.tostring())
      length = len(self.macpieces)
      buff.write(_struct_I.pack(length))
      for val1 in self.macpieces:
        _v5 = val1.start_pos
        length = len(_v5.j)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(_v5.j.tostring())
        _v6 = val1.end_pos
        length = len(_v6.j)
        buff.write(_struct_I.pack(length))
        pattern = '<%sd'%length
        buff.write(_v6.j.tostring())
        _x = val1
        buff.write(_struct_4d.pack(_x.start_time, _x.duration, _x.max_path_velocity, _x.max_path_acceleration))
      buff.write(_struct_d.pack(self.traj_duration))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.start_position is None:
        self.start_position = pr_msgs.msg.Joints()
      if self.end_position is None:
        self.end_position = pr_msgs.msg.Joints()
      if self.max_joint_vel is None:
        self.max_joint_vel = pr_msgs.msg.Joints()
      if self.max_joint_accel is None:
        self.max_joint_accel = pr_msgs.msg.Joints()
      if self.macpieces is None:
        self.macpieces = None
      end = 0
      _x = self
      start = end
      end += 4
      (_x.id, _x.HoldOnStall, _x.WaitForStart,) = _struct_h2B.unpack(str[start:end])
      self.HoldOnStall = bool(self.HoldOnStall)
      self.WaitForStart = bool(self.WaitForStart)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.start_position.j = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.end_position.j = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.max_joint_vel.j = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.max_joint_accel.j = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.macpieces = []
      for i in range(0, length):
        val1 = pr_msgs.msg.WAMPrecomputedBlendElement()
        _v7 = val1.start_pos
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        _v7.j = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _v8 = val1.end_pos
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sd'%length
        start = end
        end += struct.calcsize(pattern)
        _v8.j = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
        _x = val1
        start = end
        end += 32
        (_x.start_time, _x.duration, _x.max_path_velocity, _x.max_path_acceleration,) = _struct_4d.unpack(str[start:end])
        self.macpieces.append(val1)
      start = end
      end += 8
      (self.traj_duration,) = _struct_d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4d = struct.Struct("<4d")
_struct_d = struct.Struct("<d")
_struct_h2B = struct.Struct("<h2B")
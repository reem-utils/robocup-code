; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude RotatedLaserScan.msg.html

(cl:defclass <RotatedLaserScan> (roslisp-msg-protocol:ros-message)
  ((angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0)
   (velocity
    :reader velocity
    :initarg :velocity
    :type cl:float
    :initform 0.0)
   (laser_scan
    :reader laser_scan
    :initarg :laser_scan
    :type sensor_msgs-msg:LaserScan
    :initform (cl:make-instance 'sensor_msgs-msg:LaserScan)))
)

(cl:defclass RotatedLaserScan (<RotatedLaserScan>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RotatedLaserScan>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RotatedLaserScan)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<RotatedLaserScan> is deprecated: use pr_msgs-msg:RotatedLaserScan instead.")))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <RotatedLaserScan>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:angle-val is deprecated.  Use pr_msgs-msg:angle instead.")
  (angle m))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <RotatedLaserScan>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:velocity-val is deprecated.  Use pr_msgs-msg:velocity instead.")
  (velocity m))

(cl:ensure-generic-function 'laser_scan-val :lambda-list '(m))
(cl:defmethod laser_scan-val ((m <RotatedLaserScan>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:laser_scan-val is deprecated.  Use pr_msgs-msg:laser_scan instead.")
  (laser_scan m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RotatedLaserScan>) ostream)
  "Serializes a message object of type '<RotatedLaserScan>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'laser_scan) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RotatedLaserScan>) istream)
  "Deserializes a message object of type '<RotatedLaserScan>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'laser_scan) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RotatedLaserScan>)))
  "Returns string type for a message object of type '<RotatedLaserScan>"
  "pr_msgs/RotatedLaserScan")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RotatedLaserScan)))
  "Returns string type for a message object of type 'RotatedLaserScan"
  "pr_msgs/RotatedLaserScan")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RotatedLaserScan>)))
  "Returns md5sum for a message object of type '<RotatedLaserScan>"
  "3c54b452087e2e0b6fb2114d826dfdb4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RotatedLaserScan)))
  "Returns md5sum for a message object of type 'RotatedLaserScan"
  "3c54b452087e2e0b6fb2114d826dfdb4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RotatedLaserScan>)))
  "Returns full string definition for message of type '<RotatedLaserScan>"
  (cl:format cl:nil "float64 angle~%float64 velocity~%sensor_msgs/LaserScan laser_scan~%~%================================================================================~%MSG: sensor_msgs/LaserScan~%# Single scan from a planar laser range-finder~%#~%# If you have another ranging device with different behavior (e.g. a sonar~%# array), please find or create a different message, since applications~%# will make fairly laser-specific assumptions about this data~%~%Header header            # timestamp in the header is the acquisition time of ~%                         # the first ray in the scan.~%                         #~%                         # in frame frame_id, angles are measured around ~%                         # the positive Z axis (counterclockwise, if Z is up)~%                         # with zero angle being forward along the x axis~%                         ~%float32 angle_min        # start angle of the scan [rad]~%float32 angle_max        # end angle of the scan [rad]~%float32 angle_increment  # angular distance between measurements [rad]~%~%float32 time_increment   # time between measurements [seconds] - if your scanner~%                         # is moving, this will be used in interpolating position~%                         # of 3d points~%float32 scan_time        # time between scans [seconds]~%~%float32 range_min        # minimum range value [m]~%float32 range_max        # maximum range value [m]~%~%float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)~%float32[] intensities    # intensity data [device-specific units].  If your~%                         # device does not provide intensities, please leave~%                         # the array empty.~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RotatedLaserScan)))
  "Returns full string definition for message of type 'RotatedLaserScan"
  (cl:format cl:nil "float64 angle~%float64 velocity~%sensor_msgs/LaserScan laser_scan~%~%================================================================================~%MSG: sensor_msgs/LaserScan~%# Single scan from a planar laser range-finder~%#~%# If you have another ranging device with different behavior (e.g. a sonar~%# array), please find or create a different message, since applications~%# will make fairly laser-specific assumptions about this data~%~%Header header            # timestamp in the header is the acquisition time of ~%                         # the first ray in the scan.~%                         #~%                         # in frame frame_id, angles are measured around ~%                         # the positive Z axis (counterclockwise, if Z is up)~%                         # with zero angle being forward along the x axis~%                         ~%float32 angle_min        # start angle of the scan [rad]~%float32 angle_max        # end angle of the scan [rad]~%float32 angle_increment  # angular distance between measurements [rad]~%~%float32 time_increment   # time between measurements [seconds] - if your scanner~%                         # is moving, this will be used in interpolating position~%                         # of 3d points~%float32 scan_time        # time between scans [seconds]~%~%float32 range_min        # minimum range value [m]~%float32 range_max        # maximum range value [m]~%~%float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)~%float32[] intensities    # intensity data [device-specific units].  If your~%                         # device does not provide intensities, please leave~%                         # the array empty.~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RotatedLaserScan>))
  (cl:+ 0
     8
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'laser_scan))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RotatedLaserScan>))
  "Converts a ROS message object to a list"
  (cl:list 'RotatedLaserScan
    (cl:cons ':angle (angle msg))
    (cl:cons ':velocity (velocity msg))
    (cl:cons ':laser_scan (laser_scan msg))
))

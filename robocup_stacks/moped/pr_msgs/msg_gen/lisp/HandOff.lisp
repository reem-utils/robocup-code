; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude HandOff.msg.html

(cl:defclass <HandOff> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (point
    :reader point
    :initarg :point
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (point_world
    :reader point_world
    :initarg :point_world
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (offset
    :reader offset
    :initarg :offset
    :type geometry_msgs-msg:Point
    :initform (cl:make-instance 'geometry_msgs-msg:Point))
   (status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0)
   (mode
    :reader mode
    :initarg :mode
    :type cl:fixnum
    :initform 0)
   (object
    :reader object
    :initarg :object
    :type cl:fixnum
    :initform 0))
)

(cl:defclass HandOff (<HandOff>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <HandOff>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'HandOff)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<HandOff> is deprecated: use pr_msgs-msg:HandOff instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <HandOff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:header-val is deprecated.  Use pr_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'point-val :lambda-list '(m))
(cl:defmethod point-val ((m <HandOff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:point-val is deprecated.  Use pr_msgs-msg:point instead.")
  (point m))

(cl:ensure-generic-function 'point_world-val :lambda-list '(m))
(cl:defmethod point_world-val ((m <HandOff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:point_world-val is deprecated.  Use pr_msgs-msg:point_world instead.")
  (point_world m))

(cl:ensure-generic-function 'offset-val :lambda-list '(m))
(cl:defmethod offset-val ((m <HandOff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:offset-val is deprecated.  Use pr_msgs-msg:offset instead.")
  (offset m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <HandOff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:status-val is deprecated.  Use pr_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <HandOff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:mode-val is deprecated.  Use pr_msgs-msg:mode instead.")
  (mode m))

(cl:ensure-generic-function 'object-val :lambda-list '(m))
(cl:defmethod object-val ((m <HandOff>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:object-val is deprecated.  Use pr_msgs-msg:object instead.")
  (object m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<HandOff>)))
    "Constants for message type '<HandOff>"
  '((:STATUS_NONE . 0)
    (:STATUS_HANDOFF . 1)
    (:MODE_RETRACT . 0)
    (:MODE_FOLLOW . 1)
    (:MODE_ADVANCE . 2)
    (:OBJECT_NONE . 0)
    (:OBJECT_POPTARTS . 1)
    (:OBJECT_FUZE . 2)
    (:OBJECT_CONTAINER . 3)
    (:OBJECT_UNKNOWN . 4))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'HandOff)))
    "Constants for message type 'HandOff"
  '((:STATUS_NONE . 0)
    (:STATUS_HANDOFF . 1)
    (:MODE_RETRACT . 0)
    (:MODE_FOLLOW . 1)
    (:MODE_ADVANCE . 2)
    (:OBJECT_NONE . 0)
    (:OBJECT_POPTARTS . 1)
    (:OBJECT_FUZE . 2)
    (:OBJECT_CONTAINER . 3)
    (:OBJECT_UNKNOWN . 4))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <HandOff>) ostream)
  "Serializes a message object of type '<HandOff>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point_world) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'offset) ostream)
  (cl:let* ((signed (cl:slot-value msg 'status)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'mode)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'object)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <HandOff>) istream)
  "Deserializes a message object of type '<HandOff>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point_world) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'offset) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'status) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'mode) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'object) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<HandOff>)))
  "Returns string type for a message object of type '<HandOff>"
  "pr_msgs/HandOff")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'HandOff)))
  "Returns string type for a message object of type 'HandOff"
  "pr_msgs/HandOff")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<HandOff>)))
  "Returns md5sum for a message object of type '<HandOff>"
  "8d06d08893b771d81e1543bd706af0bf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'HandOff)))
  "Returns md5sum for a message object of type 'HandOff"
  "8d06d08893b771d81e1543bd706af0bf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<HandOff>)))
  "Returns full string definition for message of type '<HandOff>"
  (cl:format cl:nil "Header header~%geometry_msgs/Point point~%geometry_msgs/Point point_world~%geometry_msgs/Point offset~%int16 status~%int16 mode~%int16 object~%~%int16 status_none=0~%int16 status_handoff=1~%~%int16 mode_retract=0~%int16 mode_follow=1~%int16 mode_advance=2~%~%int16 object_none=0~%int16 object_poptarts=1~%int16 object_fuze=2~%int16 object_container=3~%int16 object_unknown=4~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'HandOff)))
  "Returns full string definition for message of type 'HandOff"
  (cl:format cl:nil "Header header~%geometry_msgs/Point point~%geometry_msgs/Point point_world~%geometry_msgs/Point offset~%int16 status~%int16 mode~%int16 object~%~%int16 status_none=0~%int16 status_handoff=1~%~%int16 mode_retract=0~%int16 mode_follow=1~%int16 mode_advance=2~%~%int16 object_none=0~%int16 object_poptarts=1~%int16 object_fuze=2~%int16 object_container=3~%int16 object_unknown=4~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <HandOff>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point_world))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'offset))
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <HandOff>))
  "Converts a ROS message object to a list"
  (cl:list 'HandOff
    (cl:cons ':header (header msg))
    (cl:cons ':point (point msg))
    (cl:cons ':point_world (point_world msg))
    (cl:cons ':offset (offset msg))
    (cl:cons ':status (status msg))
    (cl:cons ':mode (mode msg))
    (cl:cons ':object (object msg))
))

; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude DefineLocation.msg.html

(cl:defclass <DefineLocation> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (xx
    :reader xx
    :initarg :xx
    :type cl:float
    :initform 0.0)
   (yy
    :reader yy
    :initarg :yy
    :type cl:float
    :initform 0.0)
   (th
    :reader th
    :initarg :th
    :type cl:float
    :initform 0.0)
   (dist_thresh
    :reader dist_thresh
    :initarg :dist_thresh
    :type cl:float
    :initform 0.0)
   (angle_thresh
    :reader angle_thresh
    :initarg :angle_thresh
    :type cl:float
    :initform 0.0)
   (type
    :reader type
    :initarg :type
    :type cl:fixnum
    :initform 0))
)

(cl:defclass DefineLocation (<DefineLocation>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DefineLocation>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DefineLocation)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<DefineLocation> is deprecated: use pr_msgs-msg:DefineLocation instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:header-val is deprecated.  Use pr_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:name-val is deprecated.  Use pr_msgs-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'xx-val :lambda-list '(m))
(cl:defmethod xx-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:xx-val is deprecated.  Use pr_msgs-msg:xx instead.")
  (xx m))

(cl:ensure-generic-function 'yy-val :lambda-list '(m))
(cl:defmethod yy-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:yy-val is deprecated.  Use pr_msgs-msg:yy instead.")
  (yy m))

(cl:ensure-generic-function 'th-val :lambda-list '(m))
(cl:defmethod th-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:th-val is deprecated.  Use pr_msgs-msg:th instead.")
  (th m))

(cl:ensure-generic-function 'dist_thresh-val :lambda-list '(m))
(cl:defmethod dist_thresh-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:dist_thresh-val is deprecated.  Use pr_msgs-msg:dist_thresh instead.")
  (dist_thresh m))

(cl:ensure-generic-function 'angle_thresh-val :lambda-list '(m))
(cl:defmethod angle_thresh-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:angle_thresh-val is deprecated.  Use pr_msgs-msg:angle_thresh instead.")
  (angle_thresh m))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <DefineLocation>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:type-val is deprecated.  Use pr_msgs-msg:type instead.")
  (type m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<DefineLocation>)))
    "Constants for message type '<DefineLocation>"
  '((:TYPE_PLACE . 1)
    (:TYPE_THING . 2))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'DefineLocation)))
    "Constants for message type 'DefineLocation"
  '((:TYPE_PLACE . 1)
    (:TYPE_THING . 2))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DefineLocation>) ostream)
  "Serializes a message object of type '<DefineLocation>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'xx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'yy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'th))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dist_thresh))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'angle_thresh))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'type)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DefineLocation>) istream)
  "Deserializes a message object of type '<DefineLocation>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'xx) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'yy) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'th) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dist_thresh) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle_thresh) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'type)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DefineLocation>)))
  "Returns string type for a message object of type '<DefineLocation>"
  "pr_msgs/DefineLocation")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DefineLocation)))
  "Returns string type for a message object of type 'DefineLocation"
  "pr_msgs/DefineLocation")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DefineLocation>)))
  "Returns md5sum for a message object of type '<DefineLocation>"
  "0be26fc27c554ba0d2e3b0713e9ab224")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DefineLocation)))
  "Returns md5sum for a message object of type 'DefineLocation"
  "0be26fc27c554ba0d2e3b0713e9ab224")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DefineLocation>)))
  "Returns full string definition for message of type '<DefineLocation>"
  (cl:format cl:nil "# This message defines a named location.  Coordinates reference the~%# global map.  The robot can be asked to go to locations by their~%# name.  How the robot goes to a location depends on its type--a~%# place or a thing.  In the latter case, something can be expected~%# to occupy the defined coordinates.  However, the robot should get~%# as close as possible.~%~%Header header~%~%# How the location is known~%string name~%~%# Pose of the location~%float32 xx~%float32 yy~%float32 th~%~%# Desired precision with which the pose must be attained.~%float32 dist_thresh~%float32 angle_thresh~%~%# One of the below types, which identifies how to go to this place.~%uint8 type~%~%uint8 type_place=1	# The pose can be attained by the robot~%uint8 type_thing=2	# Something is at this pose; just get close.~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DefineLocation)))
  "Returns full string definition for message of type 'DefineLocation"
  (cl:format cl:nil "# This message defines a named location.  Coordinates reference the~%# global map.  The robot can be asked to go to locations by their~%# name.  How the robot goes to a location depends on its type--a~%# place or a thing.  In the latter case, something can be expected~%# to occupy the defined coordinates.  However, the robot should get~%# as close as possible.~%~%Header header~%~%# How the location is known~%string name~%~%# Pose of the location~%float32 xx~%float32 yy~%float32 th~%~%# Desired precision with which the pose must be attained.~%float32 dist_thresh~%float32 angle_thresh~%~%# One of the below types, which identifies how to go to this place.~%uint8 type~%~%uint8 type_place=1	# The pose can be attained by the robot~%uint8 type_thing=2	# Something is at this pose; just get close.~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DefineLocation>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'name))
     4
     4
     4
     4
     4
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DefineLocation>))
  "Converts a ROS message object to a list"
  (cl:list 'DefineLocation
    (cl:cons ':header (header msg))
    (cl:cons ':name (name msg))
    (cl:cons ':xx (xx msg))
    (cl:cons ':yy (yy msg))
    (cl:cons ':th (th msg))
    (cl:cons ':dist_thresh (dist_thresh msg))
    (cl:cons ':angle_thresh (angle_thresh msg))
    (cl:cons ':type (type msg))
))

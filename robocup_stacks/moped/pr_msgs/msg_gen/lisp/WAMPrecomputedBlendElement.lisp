; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude WAMPrecomputedBlendElement.msg.html

(cl:defclass <WAMPrecomputedBlendElement> (roslisp-msg-protocol:ros-message)
  ((start_pos
    :reader start_pos
    :initarg :start_pos
    :type pr_msgs-msg:Joints
    :initform (cl:make-instance 'pr_msgs-msg:Joints))
   (end_pos
    :reader end_pos
    :initarg :end_pos
    :type pr_msgs-msg:Joints
    :initform (cl:make-instance 'pr_msgs-msg:Joints))
   (start_time
    :reader start_time
    :initarg :start_time
    :type cl:float
    :initform 0.0)
   (duration
    :reader duration
    :initarg :duration
    :type cl:float
    :initform 0.0)
   (max_path_velocity
    :reader max_path_velocity
    :initarg :max_path_velocity
    :type cl:float
    :initform 0.0)
   (max_path_acceleration
    :reader max_path_acceleration
    :initarg :max_path_acceleration
    :type cl:float
    :initform 0.0))
)

(cl:defclass WAMPrecomputedBlendElement (<WAMPrecomputedBlendElement>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WAMPrecomputedBlendElement>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WAMPrecomputedBlendElement)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<WAMPrecomputedBlendElement> is deprecated: use pr_msgs-msg:WAMPrecomputedBlendElement instead.")))

(cl:ensure-generic-function 'start_pos-val :lambda-list '(m))
(cl:defmethod start_pos-val ((m <WAMPrecomputedBlendElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:start_pos-val is deprecated.  Use pr_msgs-msg:start_pos instead.")
  (start_pos m))

(cl:ensure-generic-function 'end_pos-val :lambda-list '(m))
(cl:defmethod end_pos-val ((m <WAMPrecomputedBlendElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:end_pos-val is deprecated.  Use pr_msgs-msg:end_pos instead.")
  (end_pos m))

(cl:ensure-generic-function 'start_time-val :lambda-list '(m))
(cl:defmethod start_time-val ((m <WAMPrecomputedBlendElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:start_time-val is deprecated.  Use pr_msgs-msg:start_time instead.")
  (start_time m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <WAMPrecomputedBlendElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:duration-val is deprecated.  Use pr_msgs-msg:duration instead.")
  (duration m))

(cl:ensure-generic-function 'max_path_velocity-val :lambda-list '(m))
(cl:defmethod max_path_velocity-val ((m <WAMPrecomputedBlendElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:max_path_velocity-val is deprecated.  Use pr_msgs-msg:max_path_velocity instead.")
  (max_path_velocity m))

(cl:ensure-generic-function 'max_path_acceleration-val :lambda-list '(m))
(cl:defmethod max_path_acceleration-val ((m <WAMPrecomputedBlendElement>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:max_path_acceleration-val is deprecated.  Use pr_msgs-msg:max_path_acceleration instead.")
  (max_path_acceleration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WAMPrecomputedBlendElement>) ostream)
  "Serializes a message object of type '<WAMPrecomputedBlendElement>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'start_pos) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'end_pos) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'start_time))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'max_path_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'max_path_acceleration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WAMPrecomputedBlendElement>) istream)
  "Deserializes a message object of type '<WAMPrecomputedBlendElement>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'start_pos) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'end_pos) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'start_time) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'duration) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_path_velocity) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'max_path_acceleration) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WAMPrecomputedBlendElement>)))
  "Returns string type for a message object of type '<WAMPrecomputedBlendElement>"
  "pr_msgs/WAMPrecomputedBlendElement")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WAMPrecomputedBlendElement)))
  "Returns string type for a message object of type 'WAMPrecomputedBlendElement"
  "pr_msgs/WAMPrecomputedBlendElement")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WAMPrecomputedBlendElement>)))
  "Returns md5sum for a message object of type '<WAMPrecomputedBlendElement>"
  "431cf004c67a8db19f0c5e2f55655018")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WAMPrecomputedBlendElement)))
  "Returns md5sum for a message object of type 'WAMPrecomputedBlendElement"
  "431cf004c67a8db19f0c5e2f55655018")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WAMPrecomputedBlendElement>)))
  "Returns full string definition for message of type '<WAMPrecomputedBlendElement>"
  (cl:format cl:nil "pr_msgs/Joints start_pos~%pr_msgs/Joints end_pos~%float64 start_time~%float64 duration~%float64 max_path_velocity~%float64 max_path_acceleration~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WAMPrecomputedBlendElement)))
  "Returns full string definition for message of type 'WAMPrecomputedBlendElement"
  (cl:format cl:nil "pr_msgs/Joints start_pos~%pr_msgs/Joints end_pos~%float64 start_time~%float64 duration~%float64 max_path_velocity~%float64 max_path_acceleration~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WAMPrecomputedBlendElement>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'start_pos))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'end_pos))
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WAMPrecomputedBlendElement>))
  "Converts a ROS message object to a list"
  (cl:list 'WAMPrecomputedBlendElement
    (cl:cons ':start_pos (start_pos msg))
    (cl:cons ':end_pos (end_pos msg))
    (cl:cons ':start_time (start_time msg))
    (cl:cons ':duration (duration msg))
    (cl:cons ':max_path_velocity (max_path_velocity msg))
    (cl:cons ':max_path_acceleration (max_path_acceleration msg))
))

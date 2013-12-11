; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude MaglevFeedback.msg.html

(cl:defclass <MaglevFeedback> (roslisp-msg-protocol:ros-message)
  ((mode
    :reader mode
    :initarg :mode
    :type cl:fixnum
    :initform 0)
   (value
    :reader value
    :initarg :value
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass MaglevFeedback (<MaglevFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MaglevFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MaglevFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<MaglevFeedback> is deprecated: use pr_msgs-msg:MaglevFeedback instead.")))

(cl:ensure-generic-function 'mode-val :lambda-list '(m))
(cl:defmethod mode-val ((m <MaglevFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:mode-val is deprecated.  Use pr_msgs-msg:mode instead.")
  (mode m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <MaglevFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:value-val is deprecated.  Use pr_msgs-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<MaglevFeedback>)))
    "Constants for message type '<MaglevFeedback>"
  '((:POSITION . 0)
    (:FORCE . 1))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'MaglevFeedback)))
    "Constants for message type 'MaglevFeedback"
  '((:POSITION . 0)
    (:FORCE . 1))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MaglevFeedback>) ostream)
  "Serializes a message object of type '<MaglevFeedback>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mode)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'value))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MaglevFeedback>) istream)
  "Deserializes a message object of type '<MaglevFeedback>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'mode)) (cl:read-byte istream))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'value) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'value)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MaglevFeedback>)))
  "Returns string type for a message object of type '<MaglevFeedback>"
  "pr_msgs/MaglevFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MaglevFeedback)))
  "Returns string type for a message object of type 'MaglevFeedback"
  "pr_msgs/MaglevFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MaglevFeedback>)))
  "Returns md5sum for a message object of type '<MaglevFeedback>"
  "def18e2e7b5c4406e703d277c2474767")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MaglevFeedback)))
  "Returns md5sum for a message object of type 'MaglevFeedback"
  "def18e2e7b5c4406e703d277c2474767")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MaglevFeedback>)))
  "Returns full string definition for message of type '<MaglevFeedback>"
  (cl:format cl:nil "uint8 mode~%float32[] value~%uint8 POSITION=0~%uint8 FORCE=1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MaglevFeedback)))
  "Returns full string definition for message of type 'MaglevFeedback"
  (cl:format cl:nil "uint8 mode~%float32[] value~%uint8 POSITION=0~%uint8 FORCE=1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MaglevFeedback>))
  (cl:+ 0
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'value) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MaglevFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'MaglevFeedback
    (cl:cons ':mode (mode msg))
    (cl:cons ':value (value msg))
))

; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude MaglevSense.msg.html

(cl:defclass <MaglevSense> (roslisp-msg-protocol:ros-message)
  ((position
    :reader position
    :initarg :position
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (force
    :reader force
    :initarg :force
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass MaglevSense (<MaglevSense>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MaglevSense>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MaglevSense)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<MaglevSense> is deprecated: use pr_msgs-msg:MaglevSense instead.")))

(cl:ensure-generic-function 'position-val :lambda-list '(m))
(cl:defmethod position-val ((m <MaglevSense>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:position-val is deprecated.  Use pr_msgs-msg:position instead.")
  (position m))

(cl:ensure-generic-function 'force-val :lambda-list '(m))
(cl:defmethod force-val ((m <MaglevSense>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:force-val is deprecated.  Use pr_msgs-msg:force instead.")
  (force m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MaglevSense>) ostream)
  "Serializes a message object of type '<MaglevSense>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'position))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'position))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'force))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'force))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MaglevSense>) istream)
  "Deserializes a message object of type '<MaglevSense>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'position) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'position)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'force) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'force)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MaglevSense>)))
  "Returns string type for a message object of type '<MaglevSense>"
  "pr_msgs/MaglevSense")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MaglevSense)))
  "Returns string type for a message object of type 'MaglevSense"
  "pr_msgs/MaglevSense")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MaglevSense>)))
  "Returns md5sum for a message object of type '<MaglevSense>"
  "82871840a2fd06a041e9e9618073ff7c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MaglevSense)))
  "Returns md5sum for a message object of type 'MaglevSense"
  "82871840a2fd06a041e9e9618073ff7c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MaglevSense>)))
  "Returns full string definition for message of type '<MaglevSense>"
  (cl:format cl:nil "float32[] position~%float32[] force~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MaglevSense)))
  "Returns full string definition for message of type 'MaglevSense"
  (cl:format cl:nil "float32[] position~%float32[] force~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MaglevSense>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'position) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'force) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MaglevSense>))
  "Converts a ROS message object to a list"
  (cl:list 'MaglevSense
    (cl:cons ':position (position msg))
    (cl:cons ':force (force msg))
))

; Auto-generated. Do not edit!


(cl:in-package normal_descriptor_node-msg)


;//! \htmlinclude ndesc.msg.html

(cl:defclass <ndesc> (roslisp-msg-protocol:ros-message)
  ((descriptor
    :reader descriptor
    :initarg :descriptor
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (point3d
    :reader point3d
    :initarg :point3d
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (u
    :reader u
    :initarg :u
    :type cl:integer
    :initform 0)
   (v
    :reader v
    :initarg :v
    :type cl:integer
    :initform 0)
   (ori
    :reader ori
    :initarg :ori
    :type cl:float
    :initform 0.0))
)

(cl:defclass ndesc (<ndesc>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ndesc>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ndesc)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name normal_descriptor_node-msg:<ndesc> is deprecated: use normal_descriptor_node-msg:ndesc instead.")))

(cl:ensure-generic-function 'descriptor-val :lambda-list '(m))
(cl:defmethod descriptor-val ((m <ndesc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:descriptor-val is deprecated.  Use normal_descriptor_node-msg:descriptor instead.")
  (descriptor m))

(cl:ensure-generic-function 'point3d-val :lambda-list '(m))
(cl:defmethod point3d-val ((m <ndesc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:point3d-val is deprecated.  Use normal_descriptor_node-msg:point3d instead.")
  (point3d m))

(cl:ensure-generic-function 'u-val :lambda-list '(m))
(cl:defmethod u-val ((m <ndesc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:u-val is deprecated.  Use normal_descriptor_node-msg:u instead.")
  (u m))

(cl:ensure-generic-function 'v-val :lambda-list '(m))
(cl:defmethod v-val ((m <ndesc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:v-val is deprecated.  Use normal_descriptor_node-msg:v instead.")
  (v m))

(cl:ensure-generic-function 'ori-val :lambda-list '(m))
(cl:defmethod ori-val ((m <ndesc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:ori-val is deprecated.  Use normal_descriptor_node-msg:ori instead.")
  (ori m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ndesc>) ostream)
  "Serializes a message object of type '<ndesc>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'descriptor))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'descriptor))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point3d) ostream)
  (cl:let* ((signed (cl:slot-value msg 'u)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'v)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'ori))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ndesc>) istream)
  "Deserializes a message object of type '<ndesc>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'descriptor) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'descriptor)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point3d) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'u) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'v) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'ori) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ndesc>)))
  "Returns string type for a message object of type '<ndesc>"
  "normal_descriptor_node/ndesc")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ndesc)))
  "Returns string type for a message object of type 'ndesc"
  "normal_descriptor_node/ndesc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ndesc>)))
  "Returns md5sum for a message object of type '<ndesc>"
  "6efcdd88f5aa9024bcc7df7fd26a0f88")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ndesc)))
  "Returns md5sum for a message object of type 'ndesc"
  "6efcdd88f5aa9024bcc7df7fd26a0f88")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ndesc>)))
  "Returns full string definition for message of type '<ndesc>"
  (cl:format cl:nil "float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 ori~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ndesc)))
  "Returns full string definition for message of type 'ndesc"
  (cl:format cl:nil "float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 ori~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ndesc>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'descriptor) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point3d))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ndesc>))
  "Converts a ROS message object to a list"
  (cl:list 'ndesc
    (cl:cons ':descriptor (descriptor msg))
    (cl:cons ':point3d (point3d msg))
    (cl:cons ':u (u msg))
    (cl:cons ':v (v msg))
    (cl:cons ':ori (ori msg))
))

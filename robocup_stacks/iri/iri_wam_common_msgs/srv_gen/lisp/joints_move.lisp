; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude joints_move-request.msg.html

(cl:defclass <joints_move-request> (roslisp-msg-protocol:ros-message)
  ((joints
    :reader joints
    :initarg :joints
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (velocities
    :reader velocities
    :initarg :velocities
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (accelerations
    :reader accelerations
    :initarg :accelerations
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass joints_move-request (<joints_move-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joints_move-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joints_move-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<joints_move-request> is deprecated: use iri_wam_common_msgs-srv:joints_move-request instead.")))

(cl:ensure-generic-function 'joints-val :lambda-list '(m))
(cl:defmethod joints-val ((m <joints_move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:joints-val is deprecated.  Use iri_wam_common_msgs-srv:joints instead.")
  (joints m))

(cl:ensure-generic-function 'velocities-val :lambda-list '(m))
(cl:defmethod velocities-val ((m <joints_move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:velocities-val is deprecated.  Use iri_wam_common_msgs-srv:velocities instead.")
  (velocities m))

(cl:ensure-generic-function 'accelerations-val :lambda-list '(m))
(cl:defmethod accelerations-val ((m <joints_move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:accelerations-val is deprecated.  Use iri_wam_common_msgs-srv:accelerations instead.")
  (accelerations m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joints_move-request>) ostream)
  "Serializes a message object of type '<joints_move-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'joints))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'joints))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'velocities))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'velocities))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'accelerations))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'accelerations))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joints_move-request>) istream)
  "Deserializes a message object of type '<joints_move-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'joints) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'joints)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'velocities) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'velocities)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'accelerations) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'accelerations)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joints_move-request>)))
  "Returns string type for a service object of type '<joints_move-request>"
  "iri_wam_common_msgs/joints_moveRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joints_move-request)))
  "Returns string type for a service object of type 'joints_move-request"
  "iri_wam_common_msgs/joints_moveRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joints_move-request>)))
  "Returns md5sum for a message object of type '<joints_move-request>"
  "6771f2ed5e81879f848f17f32a0fd19d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joints_move-request)))
  "Returns md5sum for a message object of type 'joints_move-request"
  "6771f2ed5e81879f848f17f32a0fd19d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joints_move-request>)))
  "Returns full string definition for message of type '<joints_move-request>"
  (cl:format cl:nil "~%float64[] joints~%~%~%~%~%~%float64[] velocities~%float64[] accelerations~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joints_move-request)))
  "Returns full string definition for message of type 'joints_move-request"
  (cl:format cl:nil "~%float64[] joints~%~%~%~%~%~%float64[] velocities~%float64[] accelerations~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joints_move-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'joints) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'velocities) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'accelerations) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joints_move-request>))
  "Converts a ROS message object to a list"
  (cl:list 'joints_move-request
    (cl:cons ':joints (joints msg))
    (cl:cons ':velocities (velocities msg))
    (cl:cons ':accelerations (accelerations msg))
))
;//! \htmlinclude joints_move-response.msg.html

(cl:defclass <joints_move-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:fixnum
    :initform 0))
)

(cl:defclass joints_move-response (<joints_move-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <joints_move-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'joints_move-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<joints_move-response> is deprecated: use iri_wam_common_msgs-srv:joints_move-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <joints_move-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:success-val is deprecated.  Use iri_wam_common_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <joints_move-response>) ostream)
  "Serializes a message object of type '<joints_move-response>"
  (cl:let* ((signed (cl:slot-value msg 'success)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <joints_move-response>) istream)
  "Deserializes a message object of type '<joints_move-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'success) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<joints_move-response>)))
  "Returns string type for a service object of type '<joints_move-response>"
  "iri_wam_common_msgs/joints_moveResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joints_move-response)))
  "Returns string type for a service object of type 'joints_move-response"
  "iri_wam_common_msgs/joints_moveResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<joints_move-response>)))
  "Returns md5sum for a message object of type '<joints_move-response>"
  "6771f2ed5e81879f848f17f32a0fd19d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'joints_move-response)))
  "Returns md5sum for a message object of type 'joints_move-response"
  "6771f2ed5e81879f848f17f32a0fd19d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<joints_move-response>)))
  "Returns full string definition for message of type '<joints_move-response>"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'joints_move-response)))
  "Returns full string definition for message of type 'joints_move-response"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <joints_move-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <joints_move-response>))
  "Converts a ROS message object to a list"
  (cl:list 'joints_move-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'joints_move)))
  'joints_move-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'joints_move)))
  'joints_move-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'joints_move)))
  "Returns string type for a service object of type '<joints_move>"
  "iri_wam_common_msgs/joints_move")
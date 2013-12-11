; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude wamaction-request.msg.html

(cl:defclass <wamaction-request> (roslisp-msg-protocol:ros-message)
  ((action
    :reader action
    :initarg :action
    :type cl:integer
    :initform 0)
   (hand
    :reader hand
    :initarg :hand
    :type cl:integer
    :initform 0)
   (zone
    :reader zone
    :initarg :zone
    :type cl:integer
    :initform 0))
)

(cl:defclass wamaction-request (<wamaction-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamaction-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamaction-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamaction-request> is deprecated: use iri_wam_common_msgs-srv:wamaction-request instead.")))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <wamaction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:action-val is deprecated.  Use iri_wam_common_msgs-srv:action instead.")
  (action m))

(cl:ensure-generic-function 'hand-val :lambda-list '(m))
(cl:defmethod hand-val ((m <wamaction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:hand-val is deprecated.  Use iri_wam_common_msgs-srv:hand instead.")
  (hand m))

(cl:ensure-generic-function 'zone-val :lambda-list '(m))
(cl:defmethod zone-val ((m <wamaction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:zone-val is deprecated.  Use iri_wam_common_msgs-srv:zone instead.")
  (zone m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamaction-request>) ostream)
  "Serializes a message object of type '<wamaction-request>"
  (cl:let* ((signed (cl:slot-value msg 'action)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'hand)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'zone)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamaction-request>) istream)
  "Deserializes a message object of type '<wamaction-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'hand) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'zone) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamaction-request>)))
  "Returns string type for a service object of type '<wamaction-request>"
  "iri_wam_common_msgs/wamactionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamaction-request)))
  "Returns string type for a service object of type 'wamaction-request"
  "iri_wam_common_msgs/wamactionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamaction-request>)))
  "Returns md5sum for a message object of type '<wamaction-request>"
  "8691f58a29d2fae97626e408082c84d8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamaction-request)))
  "Returns md5sum for a message object of type 'wamaction-request"
  "8691f58a29d2fae97626e408082c84d8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamaction-request>)))
  "Returns full string definition for message of type '<wamaction-request>"
  (cl:format cl:nil "int32 action~%int32 hand~%int32 zone~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamaction-request)))
  "Returns full string definition for message of type 'wamaction-request"
  (cl:format cl:nil "int32 action~%int32 hand~%int32 zone~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamaction-request>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamaction-request>))
  "Converts a ROS message object to a list"
  (cl:list 'wamaction-request
    (cl:cons ':action (action msg))
    (cl:cons ':hand (hand msg))
    (cl:cons ':zone (zone msg))
))
;//! \htmlinclude wamaction-response.msg.html

(cl:defclass <wamaction-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:fixnum
    :initform 0))
)

(cl:defclass wamaction-response (<wamaction-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamaction-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamaction-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamaction-response> is deprecated: use iri_wam_common_msgs-srv:wamaction-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <wamaction-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:success-val is deprecated.  Use iri_wam_common_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamaction-response>) ostream)
  "Serializes a message object of type '<wamaction-response>"
  (cl:let* ((signed (cl:slot-value msg 'success)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamaction-response>) istream)
  "Deserializes a message object of type '<wamaction-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'success) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamaction-response>)))
  "Returns string type for a service object of type '<wamaction-response>"
  "iri_wam_common_msgs/wamactionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamaction-response)))
  "Returns string type for a service object of type 'wamaction-response"
  "iri_wam_common_msgs/wamactionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamaction-response>)))
  "Returns md5sum for a message object of type '<wamaction-response>"
  "8691f58a29d2fae97626e408082c84d8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamaction-response)))
  "Returns md5sum for a message object of type 'wamaction-response"
  "8691f58a29d2fae97626e408082c84d8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamaction-response>)))
  "Returns full string definition for message of type '<wamaction-response>"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamaction-response)))
  "Returns full string definition for message of type 'wamaction-response"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamaction-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamaction-response>))
  "Converts a ROS message object to a list"
  (cl:list 'wamaction-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'wamaction)))
  'wamaction-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'wamaction)))
  'wamaction-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamaction)))
  "Returns string type for a service object of type '<wamaction>"
  "iri_wam_common_msgs/wamaction")
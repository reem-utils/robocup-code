; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude wamdriver-request.msg.html

(cl:defclass <wamdriver-request> (roslisp-msg-protocol:ros-message)
  ((call
    :reader call
    :initarg :call
    :type cl:integer
    :initform 0))
)

(cl:defclass wamdriver-request (<wamdriver-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamdriver-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamdriver-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamdriver-request> is deprecated: use iri_wam_common_msgs-srv:wamdriver-request instead.")))

(cl:ensure-generic-function 'call-val :lambda-list '(m))
(cl:defmethod call-val ((m <wamdriver-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:call-val is deprecated.  Use iri_wam_common_msgs-srv:call instead.")
  (call m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamdriver-request>) ostream)
  "Serializes a message object of type '<wamdriver-request>"
  (cl:let* ((signed (cl:slot-value msg 'call)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamdriver-request>) istream)
  "Deserializes a message object of type '<wamdriver-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'call) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamdriver-request>)))
  "Returns string type for a service object of type '<wamdriver-request>"
  "iri_wam_common_msgs/wamdriverRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamdriver-request)))
  "Returns string type for a service object of type 'wamdriver-request"
  "iri_wam_common_msgs/wamdriverRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamdriver-request>)))
  "Returns md5sum for a message object of type '<wamdriver-request>"
  "7845bcca17e28428f0ba550cb354008a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamdriver-request)))
  "Returns md5sum for a message object of type 'wamdriver-request"
  "7845bcca17e28428f0ba550cb354008a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamdriver-request>)))
  "Returns full string definition for message of type '<wamdriver-request>"
  (cl:format cl:nil "int32 call~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamdriver-request)))
  "Returns full string definition for message of type 'wamdriver-request"
  (cl:format cl:nil "int32 call~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamdriver-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamdriver-request>))
  "Converts a ROS message object to a list"
  (cl:list 'wamdriver-request
    (cl:cons ':call (call msg))
))
;//! \htmlinclude wamdriver-response.msg.html

(cl:defclass <wamdriver-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:fixnum
    :initform 0))
)

(cl:defclass wamdriver-response (<wamdriver-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamdriver-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamdriver-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamdriver-response> is deprecated: use iri_wam_common_msgs-srv:wamdriver-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <wamdriver-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:success-val is deprecated.  Use iri_wam_common_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamdriver-response>) ostream)
  "Serializes a message object of type '<wamdriver-response>"
  (cl:let* ((signed (cl:slot-value msg 'success)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamdriver-response>) istream)
  "Deserializes a message object of type '<wamdriver-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'success) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamdriver-response>)))
  "Returns string type for a service object of type '<wamdriver-response>"
  "iri_wam_common_msgs/wamdriverResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamdriver-response)))
  "Returns string type for a service object of type 'wamdriver-response"
  "iri_wam_common_msgs/wamdriverResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamdriver-response>)))
  "Returns md5sum for a message object of type '<wamdriver-response>"
  "7845bcca17e28428f0ba550cb354008a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamdriver-response)))
  "Returns md5sum for a message object of type 'wamdriver-response"
  "7845bcca17e28428f0ba550cb354008a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamdriver-response>)))
  "Returns full string definition for message of type '<wamdriver-response>"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamdriver-response)))
  "Returns full string definition for message of type 'wamdriver-response"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamdriver-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamdriver-response>))
  "Converts a ROS message object to a list"
  (cl:list 'wamdriver-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'wamdriver)))
  'wamdriver-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'wamdriver)))
  'wamdriver-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamdriver)))
  "Returns string type for a service object of type '<wamdriver>"
  "iri_wam_common_msgs/wamdriver")
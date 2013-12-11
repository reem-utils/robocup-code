; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude bhand_cmd-request.msg.html

(cl:defclass <bhand_cmd-request> (roslisp-msg-protocol:ros-message)
  ((bhandcmd
    :reader bhandcmd
    :initarg :bhandcmd
    :type cl:string
    :initform ""))
)

(cl:defclass bhand_cmd-request (<bhand_cmd-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <bhand_cmd-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'bhand_cmd-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<bhand_cmd-request> is deprecated: use iri_wam_common_msgs-srv:bhand_cmd-request instead.")))

(cl:ensure-generic-function 'bhandcmd-val :lambda-list '(m))
(cl:defmethod bhandcmd-val ((m <bhand_cmd-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:bhandcmd-val is deprecated.  Use iri_wam_common_msgs-srv:bhandcmd instead.")
  (bhandcmd m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <bhand_cmd-request>) ostream)
  "Serializes a message object of type '<bhand_cmd-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'bhandcmd))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'bhandcmd))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <bhand_cmd-request>) istream)
  "Deserializes a message object of type '<bhand_cmd-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'bhandcmd) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'bhandcmd) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<bhand_cmd-request>)))
  "Returns string type for a service object of type '<bhand_cmd-request>"
  "iri_wam_common_msgs/bhand_cmdRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bhand_cmd-request)))
  "Returns string type for a service object of type 'bhand_cmd-request"
  "iri_wam_common_msgs/bhand_cmdRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<bhand_cmd-request>)))
  "Returns md5sum for a message object of type '<bhand_cmd-request>"
  "d0e06140c76220845bac05af0d04d346")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'bhand_cmd-request)))
  "Returns md5sum for a message object of type 'bhand_cmd-request"
  "d0e06140c76220845bac05af0d04d346")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<bhand_cmd-request>)))
  "Returns full string definition for message of type '<bhand_cmd-request>"
  (cl:format cl:nil "string bhandcmd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'bhand_cmd-request)))
  "Returns full string definition for message of type 'bhand_cmd-request"
  (cl:format cl:nil "string bhandcmd~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <bhand_cmd-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'bhandcmd))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <bhand_cmd-request>))
  "Converts a ROS message object to a list"
  (cl:list 'bhand_cmd-request
    (cl:cons ':bhandcmd (bhandcmd msg))
))
;//! \htmlinclude bhand_cmd-response.msg.html

(cl:defclass <bhand_cmd-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:fixnum
    :initform 0))
)

(cl:defclass bhand_cmd-response (<bhand_cmd-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <bhand_cmd-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'bhand_cmd-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<bhand_cmd-response> is deprecated: use iri_wam_common_msgs-srv:bhand_cmd-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <bhand_cmd-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:success-val is deprecated.  Use iri_wam_common_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <bhand_cmd-response>) ostream)
  "Serializes a message object of type '<bhand_cmd-response>"
  (cl:let* ((signed (cl:slot-value msg 'success)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <bhand_cmd-response>) istream)
  "Deserializes a message object of type '<bhand_cmd-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'success) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<bhand_cmd-response>)))
  "Returns string type for a service object of type '<bhand_cmd-response>"
  "iri_wam_common_msgs/bhand_cmdResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bhand_cmd-response)))
  "Returns string type for a service object of type 'bhand_cmd-response"
  "iri_wam_common_msgs/bhand_cmdResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<bhand_cmd-response>)))
  "Returns md5sum for a message object of type '<bhand_cmd-response>"
  "d0e06140c76220845bac05af0d04d346")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'bhand_cmd-response)))
  "Returns md5sum for a message object of type 'bhand_cmd-response"
  "d0e06140c76220845bac05af0d04d346")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<bhand_cmd-response>)))
  "Returns full string definition for message of type '<bhand_cmd-response>"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'bhand_cmd-response)))
  "Returns full string definition for message of type 'bhand_cmd-response"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <bhand_cmd-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <bhand_cmd-response>))
  "Converts a ROS message object to a list"
  (cl:list 'bhand_cmd-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'bhand_cmd)))
  'bhand_cmd-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'bhand_cmd)))
  'bhand_cmd-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'bhand_cmd)))
  "Returns string type for a service object of type '<bhand_cmd>"
  "iri_wam_common_msgs/bhand_cmd")
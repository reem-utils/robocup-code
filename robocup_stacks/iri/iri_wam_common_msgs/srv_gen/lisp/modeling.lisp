; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude modeling-request.msg.html

(cl:defclass <modeling-request> (roslisp-msg-protocol:ros-message)
  ((stateFamily
    :reader stateFamily
    :initarg :stateFamily
    :type cl:integer
    :initform 0))
)

(cl:defclass modeling-request (<modeling-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <modeling-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'modeling-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<modeling-request> is deprecated: use iri_wam_common_msgs-srv:modeling-request instead.")))

(cl:ensure-generic-function 'stateFamily-val :lambda-list '(m))
(cl:defmethod stateFamily-val ((m <modeling-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:stateFamily-val is deprecated.  Use iri_wam_common_msgs-srv:stateFamily instead.")
  (stateFamily m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <modeling-request>) ostream)
  "Serializes a message object of type '<modeling-request>"
  (cl:let* ((signed (cl:slot-value msg 'stateFamily)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <modeling-request>) istream)
  "Deserializes a message object of type '<modeling-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'stateFamily) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<modeling-request>)))
  "Returns string type for a service object of type '<modeling-request>"
  "iri_wam_common_msgs/modelingRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'modeling-request)))
  "Returns string type for a service object of type 'modeling-request"
  "iri_wam_common_msgs/modelingRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<modeling-request>)))
  "Returns md5sum for a message object of type '<modeling-request>"
  "d5871fb07f6885288ee9a7b1038ab364")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'modeling-request)))
  "Returns md5sum for a message object of type 'modeling-request"
  "d5871fb07f6885288ee9a7b1038ab364")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<modeling-request>)))
  "Returns full string definition for message of type '<modeling-request>"
  (cl:format cl:nil "int32 stateFamily~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'modeling-request)))
  "Returns full string definition for message of type 'modeling-request"
  (cl:format cl:nil "int32 stateFamily~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <modeling-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <modeling-request>))
  "Converts a ROS message object to a list"
  (cl:list 'modeling-request
    (cl:cons ':stateFamily (stateFamily msg))
))
;//! \htmlinclude modeling-response.msg.html

(cl:defclass <modeling-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass modeling-response (<modeling-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <modeling-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'modeling-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<modeling-response> is deprecated: use iri_wam_common_msgs-srv:modeling-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <modeling-response>) ostream)
  "Serializes a message object of type '<modeling-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <modeling-response>) istream)
  "Deserializes a message object of type '<modeling-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<modeling-response>)))
  "Returns string type for a service object of type '<modeling-response>"
  "iri_wam_common_msgs/modelingResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'modeling-response)))
  "Returns string type for a service object of type 'modeling-response"
  "iri_wam_common_msgs/modelingResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<modeling-response>)))
  "Returns md5sum for a message object of type '<modeling-response>"
  "d5871fb07f6885288ee9a7b1038ab364")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'modeling-response)))
  "Returns md5sum for a message object of type 'modeling-response"
  "d5871fb07f6885288ee9a7b1038ab364")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<modeling-response>)))
  "Returns full string definition for message of type '<modeling-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'modeling-response)))
  "Returns full string definition for message of type 'modeling-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <modeling-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <modeling-response>))
  "Converts a ROS message object to a list"
  (cl:list 'modeling-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'modeling)))
  'modeling-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'modeling)))
  'modeling-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'modeling)))
  "Returns string type for a service object of type '<modeling>"
  "iri_wam_common_msgs/modeling")
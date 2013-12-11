; Auto-generated. Do not edit!


(cl:in-package iri_moped_handler-srv)


;//! \htmlinclude enable-request.msg.html

(cl:defclass <enable-request> (roslisp-msg-protocol:ros-message)
  ((enable
    :reader enable
    :initarg :enable
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass enable-request (<enable-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <enable-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'enable-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_moped_handler-srv:<enable-request> is deprecated: use iri_moped_handler-srv:enable-request instead.")))

(cl:ensure-generic-function 'enable-val :lambda-list '(m))
(cl:defmethod enable-val ((m <enable-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_moped_handler-srv:enable-val is deprecated.  Use iri_moped_handler-srv:enable instead.")
  (enable m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <enable-request>) ostream)
  "Serializes a message object of type '<enable-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enable) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <enable-request>) istream)
  "Deserializes a message object of type '<enable-request>"
    (cl:setf (cl:slot-value msg 'enable) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<enable-request>)))
  "Returns string type for a service object of type '<enable-request>"
  "iri_moped_handler/enableRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'enable-request)))
  "Returns string type for a service object of type 'enable-request"
  "iri_moped_handler/enableRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<enable-request>)))
  "Returns md5sum for a message object of type '<enable-request>"
  "99eaaa12ab016a770e9c949413327e2b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'enable-request)))
  "Returns md5sum for a message object of type 'enable-request"
  "99eaaa12ab016a770e9c949413327e2b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<enable-request>)))
  "Returns full string definition for message of type '<enable-request>"
  (cl:format cl:nil "~%bool enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'enable-request)))
  "Returns full string definition for message of type 'enable-request"
  (cl:format cl:nil "~%bool enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <enable-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <enable-request>))
  "Converts a ROS message object to a list"
  (cl:list 'enable-request
    (cl:cons ':enable (enable msg))
))
;//! \htmlinclude enable-response.msg.html

(cl:defclass <enable-response> (roslisp-msg-protocol:ros-message)
  ((correct
    :reader correct
    :initarg :correct
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass enable-response (<enable-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <enable-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'enable-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_moped_handler-srv:<enable-response> is deprecated: use iri_moped_handler-srv:enable-response instead.")))

(cl:ensure-generic-function 'correct-val :lambda-list '(m))
(cl:defmethod correct-val ((m <enable-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_moped_handler-srv:correct-val is deprecated.  Use iri_moped_handler-srv:correct instead.")
  (correct m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <enable-response>) ostream)
  "Serializes a message object of type '<enable-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'correct) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <enable-response>) istream)
  "Deserializes a message object of type '<enable-response>"
    (cl:setf (cl:slot-value msg 'correct) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<enable-response>)))
  "Returns string type for a service object of type '<enable-response>"
  "iri_moped_handler/enableResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'enable-response)))
  "Returns string type for a service object of type 'enable-response"
  "iri_moped_handler/enableResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<enable-response>)))
  "Returns md5sum for a message object of type '<enable-response>"
  "99eaaa12ab016a770e9c949413327e2b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'enable-response)))
  "Returns md5sum for a message object of type 'enable-response"
  "99eaaa12ab016a770e9c949413327e2b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<enable-response>)))
  "Returns full string definition for message of type '<enable-response>"
  (cl:format cl:nil "~%bool correct~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'enable-response)))
  "Returns full string definition for message of type 'enable-response"
  (cl:format cl:nil "~%bool correct~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <enable-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <enable-response>))
  "Converts a ROS message object to a list"
  (cl:list 'enable-response
    (cl:cons ':correct (correct msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'enable)))
  'enable-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'enable)))
  'enable-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'enable)))
  "Returns string type for a service object of type '<enable>"
  "iri_moped_handler/enable")
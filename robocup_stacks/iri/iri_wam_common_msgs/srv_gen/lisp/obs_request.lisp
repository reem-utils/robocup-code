; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude obs_request-request.msg.html

(cl:defclass <obs_request-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass obs_request-request (<obs_request-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <obs_request-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'obs_request-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<obs_request-request> is deprecated: use iri_wam_common_msgs-srv:obs_request-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <obs_request-request>) ostream)
  "Serializes a message object of type '<obs_request-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <obs_request-request>) istream)
  "Deserializes a message object of type '<obs_request-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<obs_request-request>)))
  "Returns string type for a service object of type '<obs_request-request>"
  "iri_wam_common_msgs/obs_requestRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'obs_request-request)))
  "Returns string type for a service object of type 'obs_request-request"
  "iri_wam_common_msgs/obs_requestRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<obs_request-request>)))
  "Returns md5sum for a message object of type '<obs_request-request>"
  "0e32b8b15917ccf8bc1a37974adf32eb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'obs_request-request)))
  "Returns md5sum for a message object of type 'obs_request-request"
  "0e32b8b15917ccf8bc1a37974adf32eb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<obs_request-request>)))
  "Returns full string definition for message of type '<obs_request-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'obs_request-request)))
  "Returns full string definition for message of type 'obs_request-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <obs_request-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <obs_request-request>))
  "Converts a ROS message object to a list"
  (cl:list 'obs_request-request
))
;//! \htmlinclude obs_request-response.msg.html

(cl:defclass <obs_request-response> (roslisp-msg-protocol:ros-message)
  ((num_objects
    :reader num_objects
    :initarg :num_objects
    :type cl:integer
    :initform 0)
   (num_objectsA
    :reader num_objectsA
    :initarg :num_objectsA
    :type cl:integer
    :initform 0)
   (num_objectsB
    :reader num_objectsB
    :initarg :num_objectsB
    :type cl:integer
    :initform 0))
)

(cl:defclass obs_request-response (<obs_request-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <obs_request-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'obs_request-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<obs_request-response> is deprecated: use iri_wam_common_msgs-srv:obs_request-response instead.")))

(cl:ensure-generic-function 'num_objects-val :lambda-list '(m))
(cl:defmethod num_objects-val ((m <obs_request-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:num_objects-val is deprecated.  Use iri_wam_common_msgs-srv:num_objects instead.")
  (num_objects m))

(cl:ensure-generic-function 'num_objectsA-val :lambda-list '(m))
(cl:defmethod num_objectsA-val ((m <obs_request-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:num_objectsA-val is deprecated.  Use iri_wam_common_msgs-srv:num_objectsA instead.")
  (num_objectsA m))

(cl:ensure-generic-function 'num_objectsB-val :lambda-list '(m))
(cl:defmethod num_objectsB-val ((m <obs_request-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:num_objectsB-val is deprecated.  Use iri_wam_common_msgs-srv:num_objectsB instead.")
  (num_objectsB m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <obs_request-response>) ostream)
  "Serializes a message object of type '<obs_request-response>"
  (cl:let* ((signed (cl:slot-value msg 'num_objects)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'num_objectsA)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'num_objectsB)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <obs_request-response>) istream)
  "Deserializes a message object of type '<obs_request-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_objects) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_objectsA) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_objectsB) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<obs_request-response>)))
  "Returns string type for a service object of type '<obs_request-response>"
  "iri_wam_common_msgs/obs_requestResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'obs_request-response)))
  "Returns string type for a service object of type 'obs_request-response"
  "iri_wam_common_msgs/obs_requestResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<obs_request-response>)))
  "Returns md5sum for a message object of type '<obs_request-response>"
  "0e32b8b15917ccf8bc1a37974adf32eb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'obs_request-response)))
  "Returns md5sum for a message object of type 'obs_request-response"
  "0e32b8b15917ccf8bc1a37974adf32eb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<obs_request-response>)))
  "Returns full string definition for message of type '<obs_request-response>"
  (cl:format cl:nil "int32 num_objects~%int32 num_objectsA~%int32 num_objectsB~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'obs_request-response)))
  "Returns full string definition for message of type 'obs_request-response"
  (cl:format cl:nil "int32 num_objects~%int32 num_objectsA~%int32 num_objectsB~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <obs_request-response>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <obs_request-response>))
  "Converts a ROS message object to a list"
  (cl:list 'obs_request-response
    (cl:cons ':num_objects (num_objects msg))
    (cl:cons ':num_objectsA (num_objectsA msg))
    (cl:cons ':num_objectsB (num_objectsB msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'obs_request)))
  'obs_request-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'obs_request)))
  'obs_request-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'obs_request)))
  "Returns string type for a service object of type '<obs_request>"
  "iri_wam_common_msgs/obs_request")
; Auto-generated. Do not edit!


(cl:in-package coord_translator-srv)


;//! \htmlinclude LocationTranslator-request.msg.html

(cl:defclass <LocationTranslator-request> (roslisp-msg-protocol:ros-message)
  ((location
    :reader location
    :initarg :location
    :type cl:string
    :initform ""))
)

(cl:defclass LocationTranslator-request (<LocationTranslator-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LocationTranslator-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LocationTranslator-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coord_translator-srv:<LocationTranslator-request> is deprecated: use coord_translator-srv:LocationTranslator-request instead.")))

(cl:ensure-generic-function 'location-val :lambda-list '(m))
(cl:defmethod location-val ((m <LocationTranslator-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:location-val is deprecated.  Use coord_translator-srv:location instead.")
  (location m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LocationTranslator-request>) ostream)
  "Serializes a message object of type '<LocationTranslator-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'location))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'location))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LocationTranslator-request>) istream)
  "Deserializes a message object of type '<LocationTranslator-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'location) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'location) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LocationTranslator-request>)))
  "Returns string type for a service object of type '<LocationTranslator-request>"
  "coord_translator/LocationTranslatorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LocationTranslator-request)))
  "Returns string type for a service object of type 'LocationTranslator-request"
  "coord_translator/LocationTranslatorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LocationTranslator-request>)))
  "Returns md5sum for a message object of type '<LocationTranslator-request>"
  "24b2d7b03ddf0d6054a3fe0bd4687b2d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LocationTranslator-request)))
  "Returns md5sum for a message object of type 'LocationTranslator-request"
  "24b2d7b03ddf0d6054a3fe0bd4687b2d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LocationTranslator-request>)))
  "Returns full string definition for message of type '<LocationTranslator-request>"
  (cl:format cl:nil "~%string location~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LocationTranslator-request)))
  "Returns full string definition for message of type 'LocationTranslator-request"
  (cl:format cl:nil "~%string location~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LocationTranslator-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'location))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LocationTranslator-request>))
  "Converts a ROS message object to a list"
  (cl:list 'LocationTranslator-request
    (cl:cons ':location (location msg))
))
;//! \htmlinclude LocationTranslator-response.msg.html

(cl:defclass <LocationTranslator-response> (roslisp-msg-protocol:ros-message)
  ((exists
    :reader exists
    :initarg :exists
    :type cl:boolean
    :initform cl:nil)
   (submap
    :reader submap
    :initarg :submap
    :type cl:string
    :initform "")
   (coordinates
    :reader coordinates
    :initarg :coordinates
    :type geometry_msgs-msg:Point32
    :initform (cl:make-instance 'geometry_msgs-msg:Point32)))
)

(cl:defclass LocationTranslator-response (<LocationTranslator-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LocationTranslator-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LocationTranslator-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coord_translator-srv:<LocationTranslator-response> is deprecated: use coord_translator-srv:LocationTranslator-response instead.")))

(cl:ensure-generic-function 'exists-val :lambda-list '(m))
(cl:defmethod exists-val ((m <LocationTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:exists-val is deprecated.  Use coord_translator-srv:exists instead.")
  (exists m))

(cl:ensure-generic-function 'submap-val :lambda-list '(m))
(cl:defmethod submap-val ((m <LocationTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:submap-val is deprecated.  Use coord_translator-srv:submap instead.")
  (submap m))

(cl:ensure-generic-function 'coordinates-val :lambda-list '(m))
(cl:defmethod coordinates-val ((m <LocationTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:coordinates-val is deprecated.  Use coord_translator-srv:coordinates instead.")
  (coordinates m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LocationTranslator-response>) ostream)
  "Serializes a message object of type '<LocationTranslator-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'exists) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'submap))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'submap))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'coordinates) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LocationTranslator-response>) istream)
  "Deserializes a message object of type '<LocationTranslator-response>"
    (cl:setf (cl:slot-value msg 'exists) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'submap) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'submap) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'coordinates) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LocationTranslator-response>)))
  "Returns string type for a service object of type '<LocationTranslator-response>"
  "coord_translator/LocationTranslatorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LocationTranslator-response)))
  "Returns string type for a service object of type 'LocationTranslator-response"
  "coord_translator/LocationTranslatorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LocationTranslator-response>)))
  "Returns md5sum for a message object of type '<LocationTranslator-response>"
  "24b2d7b03ddf0d6054a3fe0bd4687b2d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LocationTranslator-response)))
  "Returns md5sum for a message object of type 'LocationTranslator-response"
  "24b2d7b03ddf0d6054a3fe0bd4687b2d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LocationTranslator-response>)))
  "Returns full string definition for message of type '<LocationTranslator-response>"
  (cl:format cl:nil "~%bool exists~%string submap~%geometry_msgs/Point32 coordinates~%~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LocationTranslator-response)))
  "Returns full string definition for message of type 'LocationTranslator-response"
  (cl:format cl:nil "~%bool exists~%string submap~%geometry_msgs/Point32 coordinates~%~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LocationTranslator-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'submap))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'coordinates))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LocationTranslator-response>))
  "Converts a ROS message object to a list"
  (cl:list 'LocationTranslator-response
    (cl:cons ':exists (exists msg))
    (cl:cons ':submap (submap msg))
    (cl:cons ':coordinates (coordinates msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'LocationTranslator)))
  'LocationTranslator-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'LocationTranslator)))
  'LocationTranslator-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LocationTranslator)))
  "Returns string type for a service object of type '<LocationTranslator>"
  "coord_translator/LocationTranslator")
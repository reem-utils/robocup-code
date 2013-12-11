; Auto-generated. Do not edit!


(cl:in-package coord_translator-srv)


;//! \htmlinclude ObjectTranslator-request.msg.html

(cl:defclass <ObjectTranslator-request> (roslisp-msg-protocol:ros-message)
  ((objname
    :reader objname
    :initarg :objname
    :type cl:string
    :initform ""))
)

(cl:defclass ObjectTranslator-request (<ObjectTranslator-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectTranslator-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectTranslator-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coord_translator-srv:<ObjectTranslator-request> is deprecated: use coord_translator-srv:ObjectTranslator-request instead.")))

(cl:ensure-generic-function 'objname-val :lambda-list '(m))
(cl:defmethod objname-val ((m <ObjectTranslator-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:objname-val is deprecated.  Use coord_translator-srv:objname instead.")
  (objname m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectTranslator-request>) ostream)
  "Serializes a message object of type '<ObjectTranslator-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'objname))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'objname))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectTranslator-request>) istream)
  "Deserializes a message object of type '<ObjectTranslator-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'objname) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'objname) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectTranslator-request>)))
  "Returns string type for a service object of type '<ObjectTranslator-request>"
  "coord_translator/ObjectTranslatorRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectTranslator-request)))
  "Returns string type for a service object of type 'ObjectTranslator-request"
  "coord_translator/ObjectTranslatorRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectTranslator-request>)))
  "Returns md5sum for a message object of type '<ObjectTranslator-request>"
  "748eae5c7c477554adef5020bb3c1c94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectTranslator-request)))
  "Returns md5sum for a message object of type 'ObjectTranslator-request"
  "748eae5c7c477554adef5020bb3c1c94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectTranslator-request>)))
  "Returns full string definition for message of type '<ObjectTranslator-request>"
  (cl:format cl:nil "~%string objname~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectTranslator-request)))
  "Returns full string definition for message of type 'ObjectTranslator-request"
  (cl:format cl:nil "~%string objname~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectTranslator-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'objname))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectTranslator-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectTranslator-request
    (cl:cons ':objname (objname msg))
))
;//! \htmlinclude ObjectTranslator-response.msg.html

(cl:defclass <ObjectTranslator-response> (roslisp-msg-protocol:ros-message)
  ((exists
    :reader exists
    :initarg :exists
    :type cl:boolean
    :initform cl:nil)
   (category
    :reader category
    :initarg :category
    :type cl:string
    :initform "")
   (base_coordinates
    :reader base_coordinates
    :initarg :base_coordinates
    :type geometry_msgs-msg:Point32
    :initform (cl:make-instance 'geometry_msgs-msg:Point32))
   (arm_coordinates
    :reader arm_coordinates
    :initarg :arm_coordinates
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (databaseID
    :reader databaseID
    :initarg :databaseID
    :type cl:integer
    :initform 0))
)

(cl:defclass ObjectTranslator-response (<ObjectTranslator-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectTranslator-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectTranslator-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coord_translator-srv:<ObjectTranslator-response> is deprecated: use coord_translator-srv:ObjectTranslator-response instead.")))

(cl:ensure-generic-function 'exists-val :lambda-list '(m))
(cl:defmethod exists-val ((m <ObjectTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:exists-val is deprecated.  Use coord_translator-srv:exists instead.")
  (exists m))

(cl:ensure-generic-function 'category-val :lambda-list '(m))
(cl:defmethod category-val ((m <ObjectTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:category-val is deprecated.  Use coord_translator-srv:category instead.")
  (category m))

(cl:ensure-generic-function 'base_coordinates-val :lambda-list '(m))
(cl:defmethod base_coordinates-val ((m <ObjectTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:base_coordinates-val is deprecated.  Use coord_translator-srv:base_coordinates instead.")
  (base_coordinates m))

(cl:ensure-generic-function 'arm_coordinates-val :lambda-list '(m))
(cl:defmethod arm_coordinates-val ((m <ObjectTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:arm_coordinates-val is deprecated.  Use coord_translator-srv:arm_coordinates instead.")
  (arm_coordinates m))

(cl:ensure-generic-function 'databaseID-val :lambda-list '(m))
(cl:defmethod databaseID-val ((m <ObjectTranslator-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:databaseID-val is deprecated.  Use coord_translator-srv:databaseID instead.")
  (databaseID m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectTranslator-response>) ostream)
  "Serializes a message object of type '<ObjectTranslator-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'exists) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'category))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'category))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'base_coordinates) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'arm_coordinates) ostream)
  (cl:let* ((signed (cl:slot-value msg 'databaseID)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectTranslator-response>) istream)
  "Deserializes a message object of type '<ObjectTranslator-response>"
    (cl:setf (cl:slot-value msg 'exists) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'category) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'category) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'base_coordinates) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'arm_coordinates) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'databaseID) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectTranslator-response>)))
  "Returns string type for a service object of type '<ObjectTranslator-response>"
  "coord_translator/ObjectTranslatorResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectTranslator-response)))
  "Returns string type for a service object of type 'ObjectTranslator-response"
  "coord_translator/ObjectTranslatorResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectTranslator-response>)))
  "Returns md5sum for a message object of type '<ObjectTranslator-response>"
  "748eae5c7c477554adef5020bb3c1c94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectTranslator-response)))
  "Returns md5sum for a message object of type 'ObjectTranslator-response"
  "748eae5c7c477554adef5020bb3c1c94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectTranslator-response>)))
  "Returns full string definition for message of type '<ObjectTranslator-response>"
  (cl:format cl:nil "~%bool exists~%string category~%geometry_msgs/Point32 base_coordinates~%geometry_msgs/Pose    arm_coordinates~%int32 databaseID~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectTranslator-response)))
  "Returns full string definition for message of type 'ObjectTranslator-response"
  (cl:format cl:nil "~%bool exists~%string category~%geometry_msgs/Point32 base_coordinates~%geometry_msgs/Pose    arm_coordinates~%int32 databaseID~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectTranslator-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'category))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'base_coordinates))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'arm_coordinates))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectTranslator-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectTranslator-response
    (cl:cons ':exists (exists msg))
    (cl:cons ':category (category msg))
    (cl:cons ':base_coordinates (base_coordinates msg))
    (cl:cons ':arm_coordinates (arm_coordinates msg))
    (cl:cons ':databaseID (databaseID msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ObjectTranslator)))
  'ObjectTranslator-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ObjectTranslator)))
  'ObjectTranslator-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectTranslator)))
  "Returns string type for a service object of type '<ObjectTranslator>"
  "coord_translator/ObjectTranslator")
; Auto-generated. Do not edit!


(cl:in-package coord_translator-srv)


;//! \htmlinclude ObjectTranslatorDataBase-request.msg.html

(cl:defclass <ObjectTranslatorDataBase-request> (roslisp-msg-protocol:ros-message)
  ((databaseID
    :reader databaseID
    :initarg :databaseID
    :type cl:integer
    :initform 0))
)

(cl:defclass ObjectTranslatorDataBase-request (<ObjectTranslatorDataBase-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectTranslatorDataBase-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectTranslatorDataBase-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coord_translator-srv:<ObjectTranslatorDataBase-request> is deprecated: use coord_translator-srv:ObjectTranslatorDataBase-request instead.")))

(cl:ensure-generic-function 'databaseID-val :lambda-list '(m))
(cl:defmethod databaseID-val ((m <ObjectTranslatorDataBase-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:databaseID-val is deprecated.  Use coord_translator-srv:databaseID instead.")
  (databaseID m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectTranslatorDataBase-request>) ostream)
  "Serializes a message object of type '<ObjectTranslatorDataBase-request>"
  (cl:let* ((signed (cl:slot-value msg 'databaseID)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectTranslatorDataBase-request>) istream)
  "Deserializes a message object of type '<ObjectTranslatorDataBase-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'databaseID) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectTranslatorDataBase-request>)))
  "Returns string type for a service object of type '<ObjectTranslatorDataBase-request>"
  "coord_translator/ObjectTranslatorDataBaseRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectTranslatorDataBase-request)))
  "Returns string type for a service object of type 'ObjectTranslatorDataBase-request"
  "coord_translator/ObjectTranslatorDataBaseRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectTranslatorDataBase-request>)))
  "Returns md5sum for a message object of type '<ObjectTranslatorDataBase-request>"
  "02b3a84d67a1e7ca6847416a119312c7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectTranslatorDataBase-request)))
  "Returns md5sum for a message object of type 'ObjectTranslatorDataBase-request"
  "02b3a84d67a1e7ca6847416a119312c7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectTranslatorDataBase-request>)))
  "Returns full string definition for message of type '<ObjectTranslatorDataBase-request>"
  (cl:format cl:nil "~%int32 databaseID~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectTranslatorDataBase-request)))
  "Returns full string definition for message of type 'ObjectTranslatorDataBase-request"
  (cl:format cl:nil "~%int32 databaseID~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectTranslatorDataBase-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectTranslatorDataBase-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectTranslatorDataBase-request
    (cl:cons ':databaseID (databaseID msg))
))
;//! \htmlinclude ObjectTranslatorDataBase-response.msg.html

(cl:defclass <ObjectTranslatorDataBase-response> (roslisp-msg-protocol:ros-message)
  ((exists
    :reader exists
    :initarg :exists
    :type cl:boolean
    :initform cl:nil)
   (objname
    :reader objname
    :initarg :objname
    :type cl:string
    :initform "")
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
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass ObjectTranslatorDataBase-response (<ObjectTranslatorDataBase-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectTranslatorDataBase-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectTranslatorDataBase-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name coord_translator-srv:<ObjectTranslatorDataBase-response> is deprecated: use coord_translator-srv:ObjectTranslatorDataBase-response instead.")))

(cl:ensure-generic-function 'exists-val :lambda-list '(m))
(cl:defmethod exists-val ((m <ObjectTranslatorDataBase-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:exists-val is deprecated.  Use coord_translator-srv:exists instead.")
  (exists m))

(cl:ensure-generic-function 'objname-val :lambda-list '(m))
(cl:defmethod objname-val ((m <ObjectTranslatorDataBase-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:objname-val is deprecated.  Use coord_translator-srv:objname instead.")
  (objname m))

(cl:ensure-generic-function 'category-val :lambda-list '(m))
(cl:defmethod category-val ((m <ObjectTranslatorDataBase-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:category-val is deprecated.  Use coord_translator-srv:category instead.")
  (category m))

(cl:ensure-generic-function 'base_coordinates-val :lambda-list '(m))
(cl:defmethod base_coordinates-val ((m <ObjectTranslatorDataBase-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:base_coordinates-val is deprecated.  Use coord_translator-srv:base_coordinates instead.")
  (base_coordinates m))

(cl:ensure-generic-function 'arm_coordinates-val :lambda-list '(m))
(cl:defmethod arm_coordinates-val ((m <ObjectTranslatorDataBase-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader coord_translator-srv:arm_coordinates-val is deprecated.  Use coord_translator-srv:arm_coordinates instead.")
  (arm_coordinates m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectTranslatorDataBase-response>) ostream)
  "Serializes a message object of type '<ObjectTranslatorDataBase-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'exists) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'objname))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'objname))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'category))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'category))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'base_coordinates) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'arm_coordinates) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectTranslatorDataBase-response>) istream)
  "Deserializes a message object of type '<ObjectTranslatorDataBase-response>"
    (cl:setf (cl:slot-value msg 'exists) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'objname) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'objname) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectTranslatorDataBase-response>)))
  "Returns string type for a service object of type '<ObjectTranslatorDataBase-response>"
  "coord_translator/ObjectTranslatorDataBaseResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectTranslatorDataBase-response)))
  "Returns string type for a service object of type 'ObjectTranslatorDataBase-response"
  "coord_translator/ObjectTranslatorDataBaseResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectTranslatorDataBase-response>)))
  "Returns md5sum for a message object of type '<ObjectTranslatorDataBase-response>"
  "02b3a84d67a1e7ca6847416a119312c7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectTranslatorDataBase-response)))
  "Returns md5sum for a message object of type 'ObjectTranslatorDataBase-response"
  "02b3a84d67a1e7ca6847416a119312c7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectTranslatorDataBase-response>)))
  "Returns full string definition for message of type '<ObjectTranslatorDataBase-response>"
  (cl:format cl:nil "~%bool exists~%string objname~%string category~%geometry_msgs/Point32 base_coordinates~%geometry_msgs/Pose    arm_coordinates~%~%~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectTranslatorDataBase-response)))
  "Returns full string definition for message of type 'ObjectTranslatorDataBase-response"
  (cl:format cl:nil "~%bool exists~%string objname~%string category~%geometry_msgs/Point32 base_coordinates~%geometry_msgs/Pose    arm_coordinates~%~%~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectTranslatorDataBase-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'objname))
     4 (cl:length (cl:slot-value msg 'category))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'base_coordinates))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'arm_coordinates))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectTranslatorDataBase-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectTranslatorDataBase-response
    (cl:cons ':exists (exists msg))
    (cl:cons ':objname (objname msg))
    (cl:cons ':category (category msg))
    (cl:cons ':base_coordinates (base_coordinates msg))
    (cl:cons ':arm_coordinates (arm_coordinates msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ObjectTranslatorDataBase)))
  'ObjectTranslatorDataBase-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ObjectTranslatorDataBase)))
  'ObjectTranslatorDataBase-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectTranslatorDataBase)))
  "Returns string type for a service object of type '<ObjectTranslatorDataBase>"
  "coord_translator/ObjectTranslatorDataBase")
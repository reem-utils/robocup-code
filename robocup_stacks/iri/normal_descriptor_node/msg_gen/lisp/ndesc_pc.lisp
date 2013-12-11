; Auto-generated. Do not edit!


(cl:in-package normal_descriptor_node-msg)


;//! \htmlinclude ndesc_pc.msg.html

(cl:defclass <ndesc_pc> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (num_orient_bins
    :reader num_orient_bins
    :initarg :num_orient_bins
    :type cl:integer
    :initform 0)
   (num_spa_bins
    :reader num_spa_bins
    :initarg :num_spa_bins
    :type cl:integer
    :initform 0)
   (num
    :reader num
    :initarg :num
    :type cl:integer
    :initform 0)
   (len
    :reader len
    :initarg :len
    :type cl:integer
    :initform 0)
   (width
    :reader width
    :initarg :width
    :type cl:integer
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0)
   (descriptors
    :reader descriptors
    :initarg :descriptors
    :type (cl:vector normal_descriptor_node-msg:ndesc)
   :initform (cl:make-array 0 :element-type 'normal_descriptor_node-msg:ndesc :initial-element (cl:make-instance 'normal_descriptor_node-msg:ndesc))))
)

(cl:defclass ndesc_pc (<ndesc_pc>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ndesc_pc>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ndesc_pc)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name normal_descriptor_node-msg:<ndesc_pc> is deprecated: use normal_descriptor_node-msg:ndesc_pc instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:header-val is deprecated.  Use normal_descriptor_node-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'num_orient_bins-val :lambda-list '(m))
(cl:defmethod num_orient_bins-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:num_orient_bins-val is deprecated.  Use normal_descriptor_node-msg:num_orient_bins instead.")
  (num_orient_bins m))

(cl:ensure-generic-function 'num_spa_bins-val :lambda-list '(m))
(cl:defmethod num_spa_bins-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:num_spa_bins-val is deprecated.  Use normal_descriptor_node-msg:num_spa_bins instead.")
  (num_spa_bins m))

(cl:ensure-generic-function 'num-val :lambda-list '(m))
(cl:defmethod num-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:num-val is deprecated.  Use normal_descriptor_node-msg:num instead.")
  (num m))

(cl:ensure-generic-function 'len-val :lambda-list '(m))
(cl:defmethod len-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:len-val is deprecated.  Use normal_descriptor_node-msg:len instead.")
  (len m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:width-val is deprecated.  Use normal_descriptor_node-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:height-val is deprecated.  Use normal_descriptor_node-msg:height instead.")
  (height m))

(cl:ensure-generic-function 'descriptors-val :lambda-list '(m))
(cl:defmethod descriptors-val ((m <ndesc_pc>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-msg:descriptors-val is deprecated.  Use normal_descriptor_node-msg:descriptors instead.")
  (descriptors m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ndesc_pc>) ostream)
  "Serializes a message object of type '<ndesc_pc>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let* ((signed (cl:slot-value msg 'num_orient_bins)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'num_spa_bins)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'len)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'width)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'height)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'descriptors))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'descriptors))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ndesc_pc>) istream)
  "Deserializes a message object of type '<ndesc_pc>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_orient_bins) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num_spa_bins) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'len) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'width) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'height) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'descriptors) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'descriptors)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'normal_descriptor_node-msg:ndesc))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ndesc_pc>)))
  "Returns string type for a message object of type '<ndesc_pc>"
  "normal_descriptor_node/ndesc_pc")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ndesc_pc)))
  "Returns string type for a message object of type 'ndesc_pc"
  "normal_descriptor_node/ndesc_pc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ndesc_pc>)))
  "Returns md5sum for a message object of type '<ndesc_pc>"
  "c679de87ba14c801c3867289ca709eb0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ndesc_pc)))
  "Returns md5sum for a message object of type 'ndesc_pc"
  "c679de87ba14c801c3867289ca709eb0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ndesc_pc>)))
  "Returns full string definition for message of type '<ndesc_pc>"
  (cl:format cl:nil "Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%normal_descriptor_node/ndesc[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: normal_descriptor_node/ndesc~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 ori~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ndesc_pc)))
  "Returns full string definition for message of type 'ndesc_pc"
  (cl:format cl:nil "Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%normal_descriptor_node/ndesc[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: normal_descriptor_node/ndesc~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 ori~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ndesc_pc>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'descriptors) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ndesc_pc>))
  "Converts a ROS message object to a list"
  (cl:list 'ndesc_pc
    (cl:cons ':header (header msg))
    (cl:cons ':num_orient_bins (num_orient_bins msg))
    (cl:cons ':num_spa_bins (num_spa_bins msg))
    (cl:cons ':num (num msg))
    (cl:cons ':len (len msg))
    (cl:cons ':width (width msg))
    (cl:cons ':height (height msg))
    (cl:cons ':descriptors (descriptors msg))
))

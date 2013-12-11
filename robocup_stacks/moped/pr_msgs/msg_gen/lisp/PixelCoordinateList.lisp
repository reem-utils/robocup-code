; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude PixelCoordinateList.msg.html

(cl:defclass <PixelCoordinateList> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (coordinates
    :reader coordinates
    :initarg :coordinates
    :type (cl:vector pr_msgs-msg:PixelCoordinate)
   :initform (cl:make-array 0 :element-type 'pr_msgs-msg:PixelCoordinate :initial-element (cl:make-instance 'pr_msgs-msg:PixelCoordinate)))
   (originalTimeStamp
    :reader originalTimeStamp
    :initarg :originalTimeStamp
    :type cl:real
    :initform 0))
)

(cl:defclass PixelCoordinateList (<PixelCoordinateList>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PixelCoordinateList>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PixelCoordinateList)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<PixelCoordinateList> is deprecated: use pr_msgs-msg:PixelCoordinateList instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <PixelCoordinateList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:header-val is deprecated.  Use pr_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'coordinates-val :lambda-list '(m))
(cl:defmethod coordinates-val ((m <PixelCoordinateList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:coordinates-val is deprecated.  Use pr_msgs-msg:coordinates instead.")
  (coordinates m))

(cl:ensure-generic-function 'originalTimeStamp-val :lambda-list '(m))
(cl:defmethod originalTimeStamp-val ((m <PixelCoordinateList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:originalTimeStamp-val is deprecated.  Use pr_msgs-msg:originalTimeStamp instead.")
  (originalTimeStamp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PixelCoordinateList>) ostream)
  "Serializes a message object of type '<PixelCoordinateList>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'coordinates))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'coordinates))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'originalTimeStamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'originalTimeStamp) (cl:floor (cl:slot-value msg 'originalTimeStamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PixelCoordinateList>) istream)
  "Deserializes a message object of type '<PixelCoordinateList>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'coordinates) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'coordinates)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pr_msgs-msg:PixelCoordinate))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'originalTimeStamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PixelCoordinateList>)))
  "Returns string type for a message object of type '<PixelCoordinateList>"
  "pr_msgs/PixelCoordinateList")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PixelCoordinateList)))
  "Returns string type for a message object of type 'PixelCoordinateList"
  "pr_msgs/PixelCoordinateList")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PixelCoordinateList>)))
  "Returns md5sum for a message object of type '<PixelCoordinateList>"
  "3c9bc0eadac36ef3a77fd4cd41e78c02")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PixelCoordinateList)))
  "Returns md5sum for a message object of type 'PixelCoordinateList"
  "3c9bc0eadac36ef3a77fd4cd41e78c02")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PixelCoordinateList>)))
  "Returns full string definition for message of type '<PixelCoordinateList>"
  (cl:format cl:nil "Header header~%~%PixelCoordinate[] coordinates~%~%time originalTimeStamp~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: pr_msgs/PixelCoordinate~%int16 x~%int16 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PixelCoordinateList)))
  "Returns full string definition for message of type 'PixelCoordinateList"
  (cl:format cl:nil "Header header~%~%PixelCoordinate[] coordinates~%~%time originalTimeStamp~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: pr_msgs/PixelCoordinate~%int16 x~%int16 y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PixelCoordinateList>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'coordinates) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PixelCoordinateList>))
  "Converts a ROS message object to a list"
  (cl:list 'PixelCoordinateList
    (cl:cons ':header (header msg))
    (cl:cons ':coordinates (coordinates msg))
    (cl:cons ':originalTimeStamp (originalTimeStamp msg))
))

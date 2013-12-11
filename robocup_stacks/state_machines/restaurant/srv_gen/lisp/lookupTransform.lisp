; Auto-generated. Do not edit!


(cl:in-package restaurant-srv)


;//! \htmlinclude lookupTransform-request.msg.html

(cl:defclass <lookupTransform-request> (roslisp-msg-protocol:ros-message)
  ((target_frame
    :reader target_frame
    :initarg :target_frame
    :type cl:string
    :initform "")
   (source_frame
    :reader source_frame
    :initarg :source_frame
    :type cl:string
    :initform "")
   (transform_time
    :reader transform_time
    :initarg :transform_time
    :type cl:real
    :initform 0))
)

(cl:defclass lookupTransform-request (<lookupTransform-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <lookupTransform-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'lookupTransform-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name restaurant-srv:<lookupTransform-request> is deprecated: use restaurant-srv:lookupTransform-request instead.")))

(cl:ensure-generic-function 'target_frame-val :lambda-list '(m))
(cl:defmethod target_frame-val ((m <lookupTransform-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader restaurant-srv:target_frame-val is deprecated.  Use restaurant-srv:target_frame instead.")
  (target_frame m))

(cl:ensure-generic-function 'source_frame-val :lambda-list '(m))
(cl:defmethod source_frame-val ((m <lookupTransform-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader restaurant-srv:source_frame-val is deprecated.  Use restaurant-srv:source_frame instead.")
  (source_frame m))

(cl:ensure-generic-function 'transform_time-val :lambda-list '(m))
(cl:defmethod transform_time-val ((m <lookupTransform-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader restaurant-srv:transform_time-val is deprecated.  Use restaurant-srv:transform_time instead.")
  (transform_time m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <lookupTransform-request>) ostream)
  "Serializes a message object of type '<lookupTransform-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'target_frame))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'target_frame))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'source_frame))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'source_frame))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'transform_time)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'transform_time) (cl:floor (cl:slot-value msg 'transform_time)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <lookupTransform-request>) istream)
  "Deserializes a message object of type '<lookupTransform-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'target_frame) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'target_frame) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'source_frame) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'source_frame) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'transform_time) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<lookupTransform-request>)))
  "Returns string type for a service object of type '<lookupTransform-request>"
  "restaurant/lookupTransformRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'lookupTransform-request)))
  "Returns string type for a service object of type 'lookupTransform-request"
  "restaurant/lookupTransformRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<lookupTransform-request>)))
  "Returns md5sum for a message object of type '<lookupTransform-request>"
  "02c6b9366a79d71ff07f2dc56c230415")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'lookupTransform-request)))
  "Returns md5sum for a message object of type 'lookupTransform-request"
  "02c6b9366a79d71ff07f2dc56c230415")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<lookupTransform-request>)))
  "Returns full string definition for message of type '<lookupTransform-request>"
  (cl:format cl:nil "string target_frame~%string source_frame~%time transform_time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'lookupTransform-request)))
  "Returns full string definition for message of type 'lookupTransform-request"
  (cl:format cl:nil "string target_frame~%string source_frame~%time transform_time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <lookupTransform-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'target_frame))
     4 (cl:length (cl:slot-value msg 'source_frame))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <lookupTransform-request>))
  "Converts a ROS message object to a list"
  (cl:list 'lookupTransform-request
    (cl:cons ':target_frame (target_frame msg))
    (cl:cons ':source_frame (source_frame msg))
    (cl:cons ':transform_time (transform_time msg))
))
;//! \htmlinclude lookupTransform-response.msg.html

(cl:defclass <lookupTransform-response> (roslisp-msg-protocol:ros-message)
  ((transform
    :reader transform
    :initarg :transform
    :type geometry_msgs-msg:TransformStamped
    :initform (cl:make-instance 'geometry_msgs-msg:TransformStamped)))
)

(cl:defclass lookupTransform-response (<lookupTransform-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <lookupTransform-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'lookupTransform-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name restaurant-srv:<lookupTransform-response> is deprecated: use restaurant-srv:lookupTransform-response instead.")))

(cl:ensure-generic-function 'transform-val :lambda-list '(m))
(cl:defmethod transform-val ((m <lookupTransform-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader restaurant-srv:transform-val is deprecated.  Use restaurant-srv:transform instead.")
  (transform m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <lookupTransform-response>) ostream)
  "Serializes a message object of type '<lookupTransform-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'transform) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <lookupTransform-response>) istream)
  "Deserializes a message object of type '<lookupTransform-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'transform) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<lookupTransform-response>)))
  "Returns string type for a service object of type '<lookupTransform-response>"
  "restaurant/lookupTransformResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'lookupTransform-response)))
  "Returns string type for a service object of type 'lookupTransform-response"
  "restaurant/lookupTransformResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<lookupTransform-response>)))
  "Returns md5sum for a message object of type '<lookupTransform-response>"
  "02c6b9366a79d71ff07f2dc56c230415")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'lookupTransform-response)))
  "Returns md5sum for a message object of type 'lookupTransform-response"
  "02c6b9366a79d71ff07f2dc56c230415")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<lookupTransform-response>)))
  "Returns full string definition for message of type '<lookupTransform-response>"
  (cl:format cl:nil "geometry_msgs/TransformStamped transform~%~%~%================================================================================~%MSG: geometry_msgs/TransformStamped~%# This expresses a transform from coordinate frame header.frame_id~%# to the coordinate frame child_frame_id~%#~%# This message is mostly used by the ~%# <a href=\"http://www.ros.org/wiki/tf\">tf</a> package. ~%# See it's documentation for more information.~%~%Header header~%string child_frame_id # the frame id of the child frame~%Transform transform~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'lookupTransform-response)))
  "Returns full string definition for message of type 'lookupTransform-response"
  (cl:format cl:nil "geometry_msgs/TransformStamped transform~%~%~%================================================================================~%MSG: geometry_msgs/TransformStamped~%# This expresses a transform from coordinate frame header.frame_id~%# to the coordinate frame child_frame_id~%#~%# This message is mostly used by the ~%# <a href=\"http://www.ros.org/wiki/tf\">tf</a> package. ~%# See it's documentation for more information.~%~%Header header~%string child_frame_id # the frame id of the child frame~%Transform transform~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <lookupTransform-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'transform))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <lookupTransform-response>))
  "Converts a ROS message object to a list"
  (cl:list 'lookupTransform-response
    (cl:cons ':transform (transform msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'lookupTransform)))
  'lookupTransform-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'lookupTransform)))
  'lookupTransform-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'lookupTransform)))
  "Returns string type for a service object of type '<lookupTransform>"
  "restaurant/lookupTransform")
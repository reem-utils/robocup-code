; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-srv)


;//! \htmlinclude ArmMovementsPosesSrv-request.msg.html

(cl:defclass <ArmMovementsPosesSrv-request> (roslisp-msg-protocol:ros-message)
  ((poses
    :reader poses
    :initarg :poses
    :type (cl:vector geometry_msgs-msg:PoseStamped)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:PoseStamped :initial-element (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
   (secondary_arm
    :reader secondary_arm
    :initarg :secondary_arm
    :type (cl:vector cl:boolean)
   :initform (cl:make-array 0 :element-type 'cl:boolean :initial-element cl:nil))
   (plane_coefficients
    :reader plane_coefficients
    :initarg :plane_coefficients
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (movement_type
    :reader movement_type
    :initarg :movement_type
    :type cl:fixnum
    :initform 0))
)

(cl:defclass ArmMovementsPosesSrv-request (<ArmMovementsPosesSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArmMovementsPosesSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArmMovementsPosesSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<ArmMovementsPosesSrv-request> is deprecated: use estirabot_msgs-srv:ArmMovementsPosesSrv-request instead.")))

(cl:ensure-generic-function 'poses-val :lambda-list '(m))
(cl:defmethod poses-val ((m <ArmMovementsPosesSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:poses-val is deprecated.  Use estirabot_msgs-srv:poses instead.")
  (poses m))

(cl:ensure-generic-function 'secondary_arm-val :lambda-list '(m))
(cl:defmethod secondary_arm-val ((m <ArmMovementsPosesSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:secondary_arm-val is deprecated.  Use estirabot_msgs-srv:secondary_arm instead.")
  (secondary_arm m))

(cl:ensure-generic-function 'plane_coefficients-val :lambda-list '(m))
(cl:defmethod plane_coefficients-val ((m <ArmMovementsPosesSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:plane_coefficients-val is deprecated.  Use estirabot_msgs-srv:plane_coefficients instead.")
  (plane_coefficients m))

(cl:ensure-generic-function 'movement_type-val :lambda-list '(m))
(cl:defmethod movement_type-val ((m <ArmMovementsPosesSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:movement_type-val is deprecated.  Use estirabot_msgs-srv:movement_type instead.")
  (movement_type m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArmMovementsPosesSrv-request>) ostream)
  "Serializes a message object of type '<ArmMovementsPosesSrv-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'poses))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'poses))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'secondary_arm))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if ele 1 0)) ostream))
   (cl:slot-value msg 'secondary_arm))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'plane_coefficients))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'plane_coefficients))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'movement_type)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArmMovementsPosesSrv-request>) istream)
  "Deserializes a message object of type '<ArmMovementsPosesSrv-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'poses) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'poses)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:PoseStamped))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'secondary_arm) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'secondary_arm)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:not (cl:zerop (cl:read-byte istream)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'plane_coefficients) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'plane_coefficients)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'movement_type)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArmMovementsPosesSrv-request>)))
  "Returns string type for a service object of type '<ArmMovementsPosesSrv-request>"
  "estirabot_msgs/ArmMovementsPosesSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmMovementsPosesSrv-request)))
  "Returns string type for a service object of type 'ArmMovementsPosesSrv-request"
  "estirabot_msgs/ArmMovementsPosesSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArmMovementsPosesSrv-request>)))
  "Returns md5sum for a message object of type '<ArmMovementsPosesSrv-request>"
  "c44995b3495201366633238004174553")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArmMovementsPosesSrv-request)))
  "Returns md5sum for a message object of type 'ArmMovementsPosesSrv-request"
  "c44995b3495201366633238004174553")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArmMovementsPosesSrv-request>)))
  "Returns full string definition for message of type '<ArmMovementsPosesSrv-request>"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped[] poses~%~%bool[] secondary_arm~%~%float32[] plane_coefficients~%~%~%uint8 movement_type~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArmMovementsPosesSrv-request)))
  "Returns full string definition for message of type 'ArmMovementsPosesSrv-request"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped[] poses~%~%bool[] secondary_arm~%~%float32[] plane_coefficients~%~%~%uint8 movement_type~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArmMovementsPosesSrv-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'poses) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'secondary_arm) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'plane_coefficients) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArmMovementsPosesSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ArmMovementsPosesSrv-request
    (cl:cons ':poses (poses msg))
    (cl:cons ':secondary_arm (secondary_arm msg))
    (cl:cons ':plane_coefficients (plane_coefficients msg))
    (cl:cons ':movement_type (movement_type msg))
))
;//! \htmlinclude ArmMovementsPosesSrv-response.msg.html

(cl:defclass <ArmMovementsPosesSrv-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (too_far_points_indexes
    :reader too_far_points_indexes
    :initarg :too_far_points_indexes
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass ArmMovementsPosesSrv-response (<ArmMovementsPosesSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArmMovementsPosesSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArmMovementsPosesSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<ArmMovementsPosesSrv-response> is deprecated: use estirabot_msgs-srv:ArmMovementsPosesSrv-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <ArmMovementsPosesSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:success-val is deprecated.  Use estirabot_msgs-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'too_far_points_indexes-val :lambda-list '(m))
(cl:defmethod too_far_points_indexes-val ((m <ArmMovementsPosesSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:too_far_points_indexes-val is deprecated.  Use estirabot_msgs-srv:too_far_points_indexes instead.")
  (too_far_points_indexes m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArmMovementsPosesSrv-response>) ostream)
  "Serializes a message object of type '<ArmMovementsPosesSrv-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'too_far_points_indexes))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'too_far_points_indexes))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArmMovementsPosesSrv-response>) istream)
  "Deserializes a message object of type '<ArmMovementsPosesSrv-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'too_far_points_indexes) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'too_far_points_indexes)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArmMovementsPosesSrv-response>)))
  "Returns string type for a service object of type '<ArmMovementsPosesSrv-response>"
  "estirabot_msgs/ArmMovementsPosesSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmMovementsPosesSrv-response)))
  "Returns string type for a service object of type 'ArmMovementsPosesSrv-response"
  "estirabot_msgs/ArmMovementsPosesSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArmMovementsPosesSrv-response>)))
  "Returns md5sum for a message object of type '<ArmMovementsPosesSrv-response>"
  "c44995b3495201366633238004174553")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArmMovementsPosesSrv-response)))
  "Returns md5sum for a message object of type 'ArmMovementsPosesSrv-response"
  "c44995b3495201366633238004174553")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArmMovementsPosesSrv-response>)))
  "Returns full string definition for message of type '<ArmMovementsPosesSrv-response>"
  (cl:format cl:nil "~%bool success~%~%uint32[] too_far_points_indexes~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArmMovementsPosesSrv-response)))
  "Returns full string definition for message of type 'ArmMovementsPosesSrv-response"
  (cl:format cl:nil "~%bool success~%~%uint32[] too_far_points_indexes~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArmMovementsPosesSrv-response>))
  (cl:+ 0
     1
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'too_far_points_indexes) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArmMovementsPosesSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ArmMovementsPosesSrv-response
    (cl:cons ':success (success msg))
    (cl:cons ':too_far_points_indexes (too_far_points_indexes msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ArmMovementsPosesSrv)))
  'ArmMovementsPosesSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ArmMovementsPosesSrv)))
  'ArmMovementsPosesSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmMovementsPosesSrv)))
  "Returns string type for a service object of type '<ArmMovementsPosesSrv>"
  "estirabot_msgs/ArmMovementsPosesSrv")
; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude wamForwardKinematics-request.msg.html

(cl:defclass <wamForwardKinematics-request> (roslisp-msg-protocol:ros-message)
  ((joints
    :reader joints
    :initarg :joints
    :type sensor_msgs-msg:JointState
    :initform (cl:make-instance 'sensor_msgs-msg:JointState)))
)

(cl:defclass wamForwardKinematics-request (<wamForwardKinematics-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamForwardKinematics-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamForwardKinematics-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamForwardKinematics-request> is deprecated: use iri_wam_common_msgs-srv:wamForwardKinematics-request instead.")))

(cl:ensure-generic-function 'joints-val :lambda-list '(m))
(cl:defmethod joints-val ((m <wamForwardKinematics-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:joints-val is deprecated.  Use iri_wam_common_msgs-srv:joints instead.")
  (joints m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamForwardKinematics-request>) ostream)
  "Serializes a message object of type '<wamForwardKinematics-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'joints) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamForwardKinematics-request>) istream)
  "Deserializes a message object of type '<wamForwardKinematics-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'joints) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamForwardKinematics-request>)))
  "Returns string type for a service object of type '<wamForwardKinematics-request>"
  "iri_wam_common_msgs/wamForwardKinematicsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamForwardKinematics-request)))
  "Returns string type for a service object of type 'wamForwardKinematics-request"
  "iri_wam_common_msgs/wamForwardKinematicsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamForwardKinematics-request>)))
  "Returns md5sum for a message object of type '<wamForwardKinematics-request>"
  "20d24d0bf00b897e2f0a8ed596d36c4d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamForwardKinematics-request)))
  "Returns md5sum for a message object of type 'wamForwardKinematics-request"
  "20d24d0bf00b897e2f0a8ed596d36c4d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamForwardKinematics-request>)))
  "Returns full string definition for message of type '<wamForwardKinematics-request>"
  (cl:format cl:nil "sensor_msgs/JointState joints~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamForwardKinematics-request)))
  "Returns full string definition for message of type 'wamForwardKinematics-request"
  (cl:format cl:nil "sensor_msgs/JointState joints~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamForwardKinematics-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'joints))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamForwardKinematics-request>))
  "Converts a ROS message object to a list"
  (cl:list 'wamForwardKinematics-request
    (cl:cons ':joints (joints msg))
))
;//! \htmlinclude wamForwardKinematics-response.msg.html

(cl:defclass <wamForwardKinematics-response> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass wamForwardKinematics-response (<wamForwardKinematics-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamForwardKinematics-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamForwardKinematics-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamForwardKinematics-response> is deprecated: use iri_wam_common_msgs-srv:wamForwardKinematics-response instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <wamForwardKinematics-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:pose-val is deprecated.  Use iri_wam_common_msgs-srv:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamForwardKinematics-response>) ostream)
  "Serializes a message object of type '<wamForwardKinematics-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamForwardKinematics-response>) istream)
  "Deserializes a message object of type '<wamForwardKinematics-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamForwardKinematics-response>)))
  "Returns string type for a service object of type '<wamForwardKinematics-response>"
  "iri_wam_common_msgs/wamForwardKinematicsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamForwardKinematics-response)))
  "Returns string type for a service object of type 'wamForwardKinematics-response"
  "iri_wam_common_msgs/wamForwardKinematicsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamForwardKinematics-response>)))
  "Returns md5sum for a message object of type '<wamForwardKinematics-response>"
  "20d24d0bf00b897e2f0a8ed596d36c4d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamForwardKinematics-response)))
  "Returns md5sum for a message object of type 'wamForwardKinematics-response"
  "20d24d0bf00b897e2f0a8ed596d36c4d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamForwardKinematics-response>)))
  "Returns full string definition for message of type '<wamForwardKinematics-response>"
  (cl:format cl:nil "geometry_msgs/Pose pose~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamForwardKinematics-response)))
  "Returns full string definition for message of type 'wamForwardKinematics-response"
  (cl:format cl:nil "geometry_msgs/Pose pose~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamForwardKinematics-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamForwardKinematics-response>))
  "Converts a ROS message object to a list"
  (cl:list 'wamForwardKinematics-response
    (cl:cons ':pose (pose msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'wamForwardKinematics)))
  'wamForwardKinematics-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'wamForwardKinematics)))
  'wamForwardKinematics-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamForwardKinematics)))
  "Returns string type for a service object of type '<wamForwardKinematics>"
  "iri_wam_common_msgs/wamForwardKinematics")
; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude wamInverseKinematics-request.msg.html

(cl:defclass <wamInverseKinematics-request> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass wamInverseKinematics-request (<wamInverseKinematics-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamInverseKinematics-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamInverseKinematics-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamInverseKinematics-request> is deprecated: use iri_wam_common_msgs-srv:wamInverseKinematics-request instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <wamInverseKinematics-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:pose-val is deprecated.  Use iri_wam_common_msgs-srv:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamInverseKinematics-request>) ostream)
  "Serializes a message object of type '<wamInverseKinematics-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamInverseKinematics-request>) istream)
  "Deserializes a message object of type '<wamInverseKinematics-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamInverseKinematics-request>)))
  "Returns string type for a service object of type '<wamInverseKinematics-request>"
  "iri_wam_common_msgs/wamInverseKinematicsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamInverseKinematics-request)))
  "Returns string type for a service object of type 'wamInverseKinematics-request"
  "iri_wam_common_msgs/wamInverseKinematicsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamInverseKinematics-request>)))
  "Returns md5sum for a message object of type '<wamInverseKinematics-request>"
  "8ac06277c177a69b8a112af3d82067a8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamInverseKinematics-request)))
  "Returns md5sum for a message object of type 'wamInverseKinematics-request"
  "8ac06277c177a69b8a112af3d82067a8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamInverseKinematics-request>)))
  "Returns full string definition for message of type '<wamInverseKinematics-request>"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamInverseKinematics-request)))
  "Returns full string definition for message of type 'wamInverseKinematics-request"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamInverseKinematics-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamInverseKinematics-request>))
  "Converts a ROS message object to a list"
  (cl:list 'wamInverseKinematics-request
    (cl:cons ':pose (pose msg))
))
;//! \htmlinclude wamInverseKinematics-response.msg.html

(cl:defclass <wamInverseKinematics-response> (roslisp-msg-protocol:ros-message)
  ((joints
    :reader joints
    :initarg :joints
    :type sensor_msgs-msg:JointState
    :initform (cl:make-instance 'sensor_msgs-msg:JointState)))
)

(cl:defclass wamInverseKinematics-response (<wamInverseKinematics-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamInverseKinematics-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamInverseKinematics-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamInverseKinematics-response> is deprecated: use iri_wam_common_msgs-srv:wamInverseKinematics-response instead.")))

(cl:ensure-generic-function 'joints-val :lambda-list '(m))
(cl:defmethod joints-val ((m <wamInverseKinematics-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:joints-val is deprecated.  Use iri_wam_common_msgs-srv:joints instead.")
  (joints m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamInverseKinematics-response>) ostream)
  "Serializes a message object of type '<wamInverseKinematics-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'joints) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamInverseKinematics-response>) istream)
  "Deserializes a message object of type '<wamInverseKinematics-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'joints) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamInverseKinematics-response>)))
  "Returns string type for a service object of type '<wamInverseKinematics-response>"
  "iri_wam_common_msgs/wamInverseKinematicsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamInverseKinematics-response)))
  "Returns string type for a service object of type 'wamInverseKinematics-response"
  "iri_wam_common_msgs/wamInverseKinematicsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamInverseKinematics-response>)))
  "Returns md5sum for a message object of type '<wamInverseKinematics-response>"
  "8ac06277c177a69b8a112af3d82067a8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamInverseKinematics-response)))
  "Returns md5sum for a message object of type 'wamInverseKinematics-response"
  "8ac06277c177a69b8a112af3d82067a8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamInverseKinematics-response>)))
  "Returns full string definition for message of type '<wamInverseKinematics-response>"
  (cl:format cl:nil "~%sensor_msgs/JointState joints~%~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamInverseKinematics-response)))
  "Returns full string definition for message of type 'wamInverseKinematics-response"
  (cl:format cl:nil "~%sensor_msgs/JointState joints~%~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamInverseKinematics-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'joints))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamInverseKinematics-response>))
  "Converts a ROS message object to a list"
  (cl:list 'wamInverseKinematics-response
    (cl:cons ':joints (joints msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'wamInverseKinematics)))
  'wamInverseKinematics-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'wamInverseKinematics)))
  'wamInverseKinematics-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamInverseKinematics)))
  "Returns string type for a service object of type '<wamInverseKinematics>"
  "iri_wam_common_msgs/wamInverseKinematics")
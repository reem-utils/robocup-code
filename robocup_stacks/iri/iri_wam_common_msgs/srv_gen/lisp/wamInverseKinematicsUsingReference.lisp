; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude wamInverseKinematicsUsingReference-request.msg.html

(cl:defclass <wamInverseKinematicsUsingReference-request> (roslisp-msg-protocol:ros-message)
  ((desired_pose
    :reader desired_pose
    :initarg :desired_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (reference_joints
    :reader reference_joints
    :initarg :reference_joints
    :type sensor_msgs-msg:JointState
    :initform (cl:make-instance 'sensor_msgs-msg:JointState)))
)

(cl:defclass wamInverseKinematicsUsingReference-request (<wamInverseKinematicsUsingReference-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamInverseKinematicsUsingReference-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamInverseKinematicsUsingReference-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamInverseKinematicsUsingReference-request> is deprecated: use iri_wam_common_msgs-srv:wamInverseKinematicsUsingReference-request instead.")))

(cl:ensure-generic-function 'desired_pose-val :lambda-list '(m))
(cl:defmethod desired_pose-val ((m <wamInverseKinematicsUsingReference-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:desired_pose-val is deprecated.  Use iri_wam_common_msgs-srv:desired_pose instead.")
  (desired_pose m))

(cl:ensure-generic-function 'reference_joints-val :lambda-list '(m))
(cl:defmethod reference_joints-val ((m <wamInverseKinematicsUsingReference-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:reference_joints-val is deprecated.  Use iri_wam_common_msgs-srv:reference_joints instead.")
  (reference_joints m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamInverseKinematicsUsingReference-request>) ostream)
  "Serializes a message object of type '<wamInverseKinematicsUsingReference-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'desired_pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'reference_joints) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamInverseKinematicsUsingReference-request>) istream)
  "Deserializes a message object of type '<wamInverseKinematicsUsingReference-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'desired_pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'reference_joints) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamInverseKinematicsUsingReference-request>)))
  "Returns string type for a service object of type '<wamInverseKinematicsUsingReference-request>"
  "iri_wam_common_msgs/wamInverseKinematicsUsingReferenceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamInverseKinematicsUsingReference-request)))
  "Returns string type for a service object of type 'wamInverseKinematicsUsingReference-request"
  "iri_wam_common_msgs/wamInverseKinematicsUsingReferenceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamInverseKinematicsUsingReference-request>)))
  "Returns md5sum for a message object of type '<wamInverseKinematicsUsingReference-request>"
  "a5595624ca0857056aba4ee6b248dbbd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamInverseKinematicsUsingReference-request)))
  "Returns md5sum for a message object of type 'wamInverseKinematicsUsingReference-request"
  "a5595624ca0857056aba4ee6b248dbbd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamInverseKinematicsUsingReference-request>)))
  "Returns full string definition for message of type '<wamInverseKinematicsUsingReference-request>"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped desired_pose~%sensor_msgs/JointState reference_joints~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamInverseKinematicsUsingReference-request)))
  "Returns full string definition for message of type 'wamInverseKinematicsUsingReference-request"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped desired_pose~%sensor_msgs/JointState reference_joints~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamInverseKinematicsUsingReference-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'desired_pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'reference_joints))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamInverseKinematicsUsingReference-request>))
  "Converts a ROS message object to a list"
  (cl:list 'wamInverseKinematicsUsingReference-request
    (cl:cons ':desired_pose (desired_pose msg))
    (cl:cons ':reference_joints (reference_joints msg))
))
;//! \htmlinclude wamInverseKinematicsUsingReference-response.msg.html

(cl:defclass <wamInverseKinematicsUsingReference-response> (roslisp-msg-protocol:ros-message)
  ((desired_joints
    :reader desired_joints
    :initarg :desired_joints
    :type sensor_msgs-msg:JointState
    :initform (cl:make-instance 'sensor_msgs-msg:JointState)))
)

(cl:defclass wamInverseKinematicsUsingReference-response (<wamInverseKinematicsUsingReference-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamInverseKinematicsUsingReference-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamInverseKinematicsUsingReference-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamInverseKinematicsUsingReference-response> is deprecated: use iri_wam_common_msgs-srv:wamInverseKinematicsUsingReference-response instead.")))

(cl:ensure-generic-function 'desired_joints-val :lambda-list '(m))
(cl:defmethod desired_joints-val ((m <wamInverseKinematicsUsingReference-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:desired_joints-val is deprecated.  Use iri_wam_common_msgs-srv:desired_joints instead.")
  (desired_joints m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamInverseKinematicsUsingReference-response>) ostream)
  "Serializes a message object of type '<wamInverseKinematicsUsingReference-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'desired_joints) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamInverseKinematicsUsingReference-response>) istream)
  "Deserializes a message object of type '<wamInverseKinematicsUsingReference-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'desired_joints) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamInverseKinematicsUsingReference-response>)))
  "Returns string type for a service object of type '<wamInverseKinematicsUsingReference-response>"
  "iri_wam_common_msgs/wamInverseKinematicsUsingReferenceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamInverseKinematicsUsingReference-response)))
  "Returns string type for a service object of type 'wamInverseKinematicsUsingReference-response"
  "iri_wam_common_msgs/wamInverseKinematicsUsingReferenceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamInverseKinematicsUsingReference-response>)))
  "Returns md5sum for a message object of type '<wamInverseKinematicsUsingReference-response>"
  "a5595624ca0857056aba4ee6b248dbbd")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamInverseKinematicsUsingReference-response)))
  "Returns md5sum for a message object of type 'wamInverseKinematicsUsingReference-response"
  "a5595624ca0857056aba4ee6b248dbbd")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamInverseKinematicsUsingReference-response>)))
  "Returns full string definition for message of type '<wamInverseKinematicsUsingReference-response>"
  (cl:format cl:nil "~%sensor_msgs/JointState desired_joints~%~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamInverseKinematicsUsingReference-response)))
  "Returns full string definition for message of type 'wamInverseKinematicsUsingReference-response"
  (cl:format cl:nil "~%sensor_msgs/JointState desired_joints~%~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamInverseKinematicsUsingReference-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'desired_joints))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamInverseKinematicsUsingReference-response>))
  "Converts a ROS message object to a list"
  (cl:list 'wamInverseKinematicsUsingReference-response
    (cl:cons ':desired_joints (desired_joints msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'wamInverseKinematicsUsingReference)))
  'wamInverseKinematicsUsingReference-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'wamInverseKinematicsUsingReference)))
  'wamInverseKinematicsUsingReference-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamInverseKinematicsUsingReference)))
  "Returns string type for a service object of type '<wamInverseKinematicsUsingReference>"
  "iri_wam_common_msgs/wamInverseKinematicsUsingReference")
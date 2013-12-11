; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude ArmConfigCheck-request.msg.html

(cl:defclass <ArmConfigCheck-request> (roslisp-msg-protocol:ros-message)
  ((joint_state
    :reader joint_state
    :initarg :joint_state
    :type sensor_msgs-msg:JointState
    :initform (cl:make-instance 'sensor_msgs-msg:JointState)))
)

(cl:defclass ArmConfigCheck-request (<ArmConfigCheck-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArmConfigCheck-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArmConfigCheck-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<ArmConfigCheck-request> is deprecated: use pr_msgs-srv:ArmConfigCheck-request instead.")))

(cl:ensure-generic-function 'joint_state-val :lambda-list '(m))
(cl:defmethod joint_state-val ((m <ArmConfigCheck-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:joint_state-val is deprecated.  Use pr_msgs-srv:joint_state instead.")
  (joint_state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArmConfigCheck-request>) ostream)
  "Serializes a message object of type '<ArmConfigCheck-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'joint_state) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArmConfigCheck-request>) istream)
  "Deserializes a message object of type '<ArmConfigCheck-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'joint_state) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArmConfigCheck-request>)))
  "Returns string type for a service object of type '<ArmConfigCheck-request>"
  "pr_msgs/ArmConfigCheckRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmConfigCheck-request)))
  "Returns string type for a service object of type 'ArmConfigCheck-request"
  "pr_msgs/ArmConfigCheckRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArmConfigCheck-request>)))
  "Returns md5sum for a message object of type '<ArmConfigCheck-request>"
  "a5df7a19c6f627a079d9c14658ecf093")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArmConfigCheck-request)))
  "Returns md5sum for a message object of type 'ArmConfigCheck-request"
  "a5df7a19c6f627a079d9c14658ecf093")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArmConfigCheck-request>)))
  "Returns full string definition for message of type '<ArmConfigCheck-request>"
  (cl:format cl:nil "sensor_msgs/JointState joint_state~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArmConfigCheck-request)))
  "Returns full string definition for message of type 'ArmConfigCheck-request"
  (cl:format cl:nil "sensor_msgs/JointState joint_state~%~%================================================================================~%MSG: sensor_msgs/JointState~%# This is a message that holds data to describe the state of a set of torque controlled joints. ~%#~%# The state of each joint (revolute or prismatic) is defined by:~%#  * the position of the joint (rad or m),~%#  * the velocity of the joint (rad/s or m/s) and ~%#  * the effort that is applied in the joint (Nm or N).~%#~%# Each joint is uniquely identified by its name~%# The header specifies the time at which the joint states were recorded. All the joint states~%# in one message have to be recorded at the same time.~%#~%# This message consists of a multiple arrays, one for each part of the joint state. ~%# The goal is to make each of the fields optional. When e.g. your joints have no~%# effort associated with them, you can leave the effort array empty. ~%#~%# All arrays in this message should have the same size, or be empty.~%# This is the only way to uniquely associate the joint name with the correct~%# states.~%~%~%Header header~%~%string[] name~%float64[] position~%float64[] velocity~%float64[] effort~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArmConfigCheck-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'joint_state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArmConfigCheck-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ArmConfigCheck-request
    (cl:cons ':joint_state (joint_state msg))
))
;//! \htmlinclude ArmConfigCheck-response.msg.html

(cl:defclass <ArmConfigCheck-response> (roslisp-msg-protocol:ros-message)
  ((current_self_collision
    :reader current_self_collision
    :initarg :current_self_collision
    :type cl:boolean
    :initform cl:nil)
   (current_env_collision
    :reader current_env_collision
    :initarg :current_env_collision
    :type cl:boolean
    :initform cl:nil)
   (future_self_collision
    :reader future_self_collision
    :initarg :future_self_collision
    :type cl:boolean
    :initform cl:nil)
   (future_env_collision
    :reader future_env_collision
    :initarg :future_env_collision
    :type cl:boolean
    :initform cl:nil)
   (current_joint_limits_exceeded
    :reader current_joint_limits_exceeded
    :initarg :current_joint_limits_exceeded
    :type cl:boolean
    :initform cl:nil)
   (future_joint_limits_exceeded
    :reader future_joint_limits_exceeded
    :initarg :future_joint_limits_exceeded
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ArmConfigCheck-response (<ArmConfigCheck-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArmConfigCheck-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArmConfigCheck-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<ArmConfigCheck-response> is deprecated: use pr_msgs-srv:ArmConfigCheck-response instead.")))

(cl:ensure-generic-function 'current_self_collision-val :lambda-list '(m))
(cl:defmethod current_self_collision-val ((m <ArmConfigCheck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:current_self_collision-val is deprecated.  Use pr_msgs-srv:current_self_collision instead.")
  (current_self_collision m))

(cl:ensure-generic-function 'current_env_collision-val :lambda-list '(m))
(cl:defmethod current_env_collision-val ((m <ArmConfigCheck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:current_env_collision-val is deprecated.  Use pr_msgs-srv:current_env_collision instead.")
  (current_env_collision m))

(cl:ensure-generic-function 'future_self_collision-val :lambda-list '(m))
(cl:defmethod future_self_collision-val ((m <ArmConfigCheck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:future_self_collision-val is deprecated.  Use pr_msgs-srv:future_self_collision instead.")
  (future_self_collision m))

(cl:ensure-generic-function 'future_env_collision-val :lambda-list '(m))
(cl:defmethod future_env_collision-val ((m <ArmConfigCheck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:future_env_collision-val is deprecated.  Use pr_msgs-srv:future_env_collision instead.")
  (future_env_collision m))

(cl:ensure-generic-function 'current_joint_limits_exceeded-val :lambda-list '(m))
(cl:defmethod current_joint_limits_exceeded-val ((m <ArmConfigCheck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:current_joint_limits_exceeded-val is deprecated.  Use pr_msgs-srv:current_joint_limits_exceeded instead.")
  (current_joint_limits_exceeded m))

(cl:ensure-generic-function 'future_joint_limits_exceeded-val :lambda-list '(m))
(cl:defmethod future_joint_limits_exceeded-val ((m <ArmConfigCheck-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:future_joint_limits_exceeded-val is deprecated.  Use pr_msgs-srv:future_joint_limits_exceeded instead.")
  (future_joint_limits_exceeded m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArmConfigCheck-response>) ostream)
  "Serializes a message object of type '<ArmConfigCheck-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'current_self_collision) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'current_env_collision) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'future_self_collision) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'future_env_collision) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'current_joint_limits_exceeded) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'future_joint_limits_exceeded) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArmConfigCheck-response>) istream)
  "Deserializes a message object of type '<ArmConfigCheck-response>"
    (cl:setf (cl:slot-value msg 'current_self_collision) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'current_env_collision) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'future_self_collision) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'future_env_collision) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'current_joint_limits_exceeded) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'future_joint_limits_exceeded) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArmConfigCheck-response>)))
  "Returns string type for a service object of type '<ArmConfigCheck-response>"
  "pr_msgs/ArmConfigCheckResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmConfigCheck-response)))
  "Returns string type for a service object of type 'ArmConfigCheck-response"
  "pr_msgs/ArmConfigCheckResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArmConfigCheck-response>)))
  "Returns md5sum for a message object of type '<ArmConfigCheck-response>"
  "a5df7a19c6f627a079d9c14658ecf093")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArmConfigCheck-response)))
  "Returns md5sum for a message object of type 'ArmConfigCheck-response"
  "a5df7a19c6f627a079d9c14658ecf093")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArmConfigCheck-response>)))
  "Returns full string definition for message of type '<ArmConfigCheck-response>"
  (cl:format cl:nil "bool current_self_collision~%bool current_env_collision~%bool future_self_collision~%bool future_env_collision~%~%bool current_joint_limits_exceeded~%bool future_joint_limits_exceeded~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArmConfigCheck-response)))
  "Returns full string definition for message of type 'ArmConfigCheck-response"
  (cl:format cl:nil "bool current_self_collision~%bool current_env_collision~%bool future_self_collision~%bool future_env_collision~%~%bool current_joint_limits_exceeded~%bool future_joint_limits_exceeded~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArmConfigCheck-response>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArmConfigCheck-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ArmConfigCheck-response
    (cl:cons ':current_self_collision (current_self_collision msg))
    (cl:cons ':current_env_collision (current_env_collision msg))
    (cl:cons ':future_self_collision (future_self_collision msg))
    (cl:cons ':future_env_collision (future_env_collision msg))
    (cl:cons ':current_joint_limits_exceeded (current_joint_limits_exceeded msg))
    (cl:cons ':future_joint_limits_exceeded (future_joint_limits_exceeded msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ArmConfigCheck)))
  'ArmConfigCheck-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ArmConfigCheck)))
  'ArmConfigCheck-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmConfigCheck)))
  "Returns string type for a service object of type '<ArmConfigCheck>"
  "pr_msgs/ArmConfigCheck")
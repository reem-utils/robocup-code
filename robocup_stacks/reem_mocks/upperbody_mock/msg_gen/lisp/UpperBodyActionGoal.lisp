; Auto-generated. Do not edit!


(cl:in-package upperbody_mock-msg)


;//! \htmlinclude UpperBodyActionGoal.msg.html

(cl:defclass <UpperBodyActionGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (goal_id
    :reader goal_id
    :initarg :goal_id
    :type actionlib_msgs-msg:GoalID
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalID))
   (goal
    :reader goal
    :initarg :goal
    :type upperbody_mock-msg:UpperBodyGoal
    :initform (cl:make-instance 'upperbody_mock-msg:UpperBodyGoal)))
)

(cl:defclass UpperBodyActionGoal (<UpperBodyActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UpperBodyActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UpperBodyActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name upperbody_mock-msg:<UpperBodyActionGoal> is deprecated: use upperbody_mock-msg:UpperBodyActionGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <UpperBodyActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader upperbody_mock-msg:header-val is deprecated.  Use upperbody_mock-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'goal_id-val :lambda-list '(m))
(cl:defmethod goal_id-val ((m <UpperBodyActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader upperbody_mock-msg:goal_id-val is deprecated.  Use upperbody_mock-msg:goal_id instead.")
  (goal_id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <UpperBodyActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader upperbody_mock-msg:goal-val is deprecated.  Use upperbody_mock-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UpperBodyActionGoal>) ostream)
  "Serializes a message object of type '<UpperBodyActionGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_id) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UpperBodyActionGoal>) istream)
  "Deserializes a message object of type '<UpperBodyActionGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_id) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UpperBodyActionGoal>)))
  "Returns string type for a message object of type '<UpperBodyActionGoal>"
  "upperbody_mock/UpperBodyActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UpperBodyActionGoal)))
  "Returns string type for a message object of type 'UpperBodyActionGoal"
  "upperbody_mock/UpperBodyActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UpperBodyActionGoal>)))
  "Returns md5sum for a message object of type '<UpperBodyActionGoal>"
  "7f3c77c0a5325272e825ad8a4d712a89")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UpperBodyActionGoal)))
  "Returns md5sum for a message object of type 'UpperBodyActionGoal"
  "7f3c77c0a5325272e825ad8a4d712a89")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UpperBodyActionGoal>)))
  "Returns full string definition for message of type '<UpperBodyActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%UpperBodyGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%# name of XML file containing motions for the robot~%string motion_file~%~%# true if trajectory validation is to be performed~%bool validate_trajectory~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UpperBodyActionGoal)))
  "Returns full string definition for message of type 'UpperBodyActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%UpperBodyGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%# name of XML file containing motions for the robot~%string motion_file~%~%# true if trajectory validation is to be performed~%bool validate_trajectory~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UpperBodyActionGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UpperBodyActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'UpperBodyActionGoal
    (cl:cons ':header (header msg))
    (cl:cons ':goal_id (goal_id msg))
    (cl:cons ':goal (goal msg))
))

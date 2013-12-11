; Auto-generated. Do not edit!


(cl:in-package upperbody_mock-msg)


;//! \htmlinclude UpperBodyAction.msg.html

(cl:defclass <UpperBodyAction> (roslisp-msg-protocol:ros-message)
  ((action_goal
    :reader action_goal
    :initarg :action_goal
    :type upperbody_mock-msg:UpperBodyActionGoal
    :initform (cl:make-instance 'upperbody_mock-msg:UpperBodyActionGoal))
   (action_result
    :reader action_result
    :initarg :action_result
    :type upperbody_mock-msg:UpperBodyActionResult
    :initform (cl:make-instance 'upperbody_mock-msg:UpperBodyActionResult))
   (action_feedback
    :reader action_feedback
    :initarg :action_feedback
    :type upperbody_mock-msg:UpperBodyActionFeedback
    :initform (cl:make-instance 'upperbody_mock-msg:UpperBodyActionFeedback)))
)

(cl:defclass UpperBodyAction (<UpperBodyAction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UpperBodyAction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UpperBodyAction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name upperbody_mock-msg:<UpperBodyAction> is deprecated: use upperbody_mock-msg:UpperBodyAction instead.")))

(cl:ensure-generic-function 'action_goal-val :lambda-list '(m))
(cl:defmethod action_goal-val ((m <UpperBodyAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader upperbody_mock-msg:action_goal-val is deprecated.  Use upperbody_mock-msg:action_goal instead.")
  (action_goal m))

(cl:ensure-generic-function 'action_result-val :lambda-list '(m))
(cl:defmethod action_result-val ((m <UpperBodyAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader upperbody_mock-msg:action_result-val is deprecated.  Use upperbody_mock-msg:action_result instead.")
  (action_result m))

(cl:ensure-generic-function 'action_feedback-val :lambda-list '(m))
(cl:defmethod action_feedback-val ((m <UpperBodyAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader upperbody_mock-msg:action_feedback-val is deprecated.  Use upperbody_mock-msg:action_feedback instead.")
  (action_feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UpperBodyAction>) ostream)
  "Serializes a message object of type '<UpperBodyAction>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_goal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_result) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_feedback) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UpperBodyAction>) istream)
  "Deserializes a message object of type '<UpperBodyAction>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_goal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_result) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_feedback) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UpperBodyAction>)))
  "Returns string type for a message object of type '<UpperBodyAction>"
  "upperbody_mock/UpperBodyAction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UpperBodyAction)))
  "Returns string type for a message object of type 'UpperBodyAction"
  "upperbody_mock/UpperBodyAction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UpperBodyAction>)))
  "Returns md5sum for a message object of type '<UpperBodyAction>"
  "3d0c87e03a9955caee5d82b882ca257d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UpperBodyAction)))
  "Returns md5sum for a message object of type 'UpperBodyAction"
  "3d0c87e03a9955caee5d82b882ca257d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UpperBodyAction>)))
  "Returns full string definition for message of type '<UpperBodyAction>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%UpperBodyActionGoal action_goal~%UpperBodyActionResult action_result~%UpperBodyActionFeedback action_feedback~%~%================================================================================~%MSG: upperbody_mock/UpperBodyActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%UpperBodyGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%# name of XML file containing motions for the robot~%string motion_file~%~%# true if trajectory validation is to be performed~%bool validate_trajectory~%~%================================================================================~%MSG: upperbody_mock/UpperBodyActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%UpperBodyResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%UpperBodyFeedback feedback~%~%================================================================================~%MSG: upperbody_mock/UpperBodyFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# feedback message~%# no feedback for the moment. could be remaining time or current configuration~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UpperBodyAction)))
  "Returns full string definition for message of type 'UpperBodyAction"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%UpperBodyActionGoal action_goal~%UpperBodyActionResult action_result~%UpperBodyActionFeedback action_feedback~%~%================================================================================~%MSG: upperbody_mock/UpperBodyActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%UpperBodyGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%# name of XML file containing motions for the robot~%string motion_file~%~%# true if trajectory validation is to be performed~%bool validate_trajectory~%~%================================================================================~%MSG: upperbody_mock/UpperBodyActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%UpperBodyResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%================================================================================~%MSG: upperbody_mock/UpperBodyActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%UpperBodyFeedback feedback~%~%================================================================================~%MSG: upperbody_mock/UpperBodyFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# feedback message~%# no feedback for the moment. could be remaining time or current configuration~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UpperBodyAction>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_goal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_result))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_feedback))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UpperBodyAction>))
  "Converts a ROS message object to a list"
  (cl:list 'UpperBodyAction
    (cl:cons ':action_goal (action_goal msg))
    (cl:cons ':action_result (action_result msg))
    (cl:cons ':action_feedback (action_feedback msg))
))
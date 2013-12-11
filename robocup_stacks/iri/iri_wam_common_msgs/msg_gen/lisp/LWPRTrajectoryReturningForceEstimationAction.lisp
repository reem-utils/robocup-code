; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-msg)


;//! \htmlinclude LWPRTrajectoryReturningForceEstimationAction.msg.html

(cl:defclass <LWPRTrajectoryReturningForceEstimationAction> (roslisp-msg-protocol:ros-message)
  ((action_goal
    :reader action_goal
    :initarg :action_goal
    :type iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationActionGoal
    :initform (cl:make-instance 'iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationActionGoal))
   (action_result
    :reader action_result
    :initarg :action_result
    :type iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationActionResult
    :initform (cl:make-instance 'iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationActionResult))
   (action_feedback
    :reader action_feedback
    :initarg :action_feedback
    :type iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationActionFeedback
    :initform (cl:make-instance 'iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationActionFeedback)))
)

(cl:defclass LWPRTrajectoryReturningForceEstimationAction (<LWPRTrajectoryReturningForceEstimationAction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LWPRTrajectoryReturningForceEstimationAction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LWPRTrajectoryReturningForceEstimationAction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-msg:<LWPRTrajectoryReturningForceEstimationAction> is deprecated: use iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationAction instead.")))

(cl:ensure-generic-function 'action_goal-val :lambda-list '(m))
(cl:defmethod action_goal-val ((m <LWPRTrajectoryReturningForceEstimationAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:action_goal-val is deprecated.  Use iri_wam_common_msgs-msg:action_goal instead.")
  (action_goal m))

(cl:ensure-generic-function 'action_result-val :lambda-list '(m))
(cl:defmethod action_result-val ((m <LWPRTrajectoryReturningForceEstimationAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:action_result-val is deprecated.  Use iri_wam_common_msgs-msg:action_result instead.")
  (action_result m))

(cl:ensure-generic-function 'action_feedback-val :lambda-list '(m))
(cl:defmethod action_feedback-val ((m <LWPRTrajectoryReturningForceEstimationAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:action_feedback-val is deprecated.  Use iri_wam_common_msgs-msg:action_feedback instead.")
  (action_feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LWPRTrajectoryReturningForceEstimationAction>) ostream)
  "Serializes a message object of type '<LWPRTrajectoryReturningForceEstimationAction>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_goal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_result) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_feedback) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LWPRTrajectoryReturningForceEstimationAction>) istream)
  "Deserializes a message object of type '<LWPRTrajectoryReturningForceEstimationAction>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_goal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_result) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_feedback) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LWPRTrajectoryReturningForceEstimationAction>)))
  "Returns string type for a message object of type '<LWPRTrajectoryReturningForceEstimationAction>"
  "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationAction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LWPRTrajectoryReturningForceEstimationAction)))
  "Returns string type for a message object of type 'LWPRTrajectoryReturningForceEstimationAction"
  "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationAction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LWPRTrajectoryReturningForceEstimationAction>)))
  "Returns md5sum for a message object of type '<LWPRTrajectoryReturningForceEstimationAction>"
  "0592c1ed5f73ef46d87caf22ed58f5eb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LWPRTrajectoryReturningForceEstimationAction)))
  "Returns md5sum for a message object of type 'LWPRTrajectoryReturningForceEstimationAction"
  "0592c1ed5f73ef46d87caf22ed58f5eb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LWPRTrajectoryReturningForceEstimationAction>)))
  "Returns full string definition for message of type '<LWPRTrajectoryReturningForceEstimationAction>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%LWPRTrajectoryReturningForceEstimationActionGoal action_goal~%LWPRTrajectoryReturningForceEstimationActionResult action_result~%LWPRTrajectoryReturningForceEstimationActionFeedback action_feedback~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%LWPRTrajectoryReturningForceEstimationGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%string model_filename~%string points_filename~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%LWPRTrajectoryReturningForceEstimationResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# result~%float32 force~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%LWPRTrajectoryReturningForceEstimationFeedback feedback~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# feedback~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LWPRTrajectoryReturningForceEstimationAction)))
  "Returns full string definition for message of type 'LWPRTrajectoryReturningForceEstimationAction"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%LWPRTrajectoryReturningForceEstimationActionGoal action_goal~%LWPRTrajectoryReturningForceEstimationActionResult action_result~%LWPRTrajectoryReturningForceEstimationActionFeedback action_feedback~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%LWPRTrajectoryReturningForceEstimationGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%string model_filename~%string points_filename~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%LWPRTrajectoryReturningForceEstimationResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# result~%float32 force~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%LWPRTrajectoryReturningForceEstimationFeedback feedback~%~%================================================================================~%MSG: iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# feedback~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LWPRTrajectoryReturningForceEstimationAction>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_goal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_result))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_feedback))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LWPRTrajectoryReturningForceEstimationAction>))
  "Converts a ROS message object to a list"
  (cl:list 'LWPRTrajectoryReturningForceEstimationAction
    (cl:cons ':action_goal (action_goal msg))
    (cl:cons ':action_result (action_result msg))
    (cl:cons ':action_feedback (action_feedback msg))
))
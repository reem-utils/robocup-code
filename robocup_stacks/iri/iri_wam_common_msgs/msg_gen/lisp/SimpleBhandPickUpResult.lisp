; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-msg)


;//! \htmlinclude SimpleBhandPickUpResult.msg.html

(cl:defclass <SimpleBhandPickUpResult> (roslisp-msg-protocol:ros-message)
  ((grasp_result
    :reader grasp_result
    :initarg :grasp_result
    :type object_manipulation_msgs-msg:GraspResult
    :initform (cl:make-instance 'object_manipulation_msgs-msg:GraspResult)))
)

(cl:defclass SimpleBhandPickUpResult (<SimpleBhandPickUpResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SimpleBhandPickUpResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SimpleBhandPickUpResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-msg:<SimpleBhandPickUpResult> is deprecated: use iri_wam_common_msgs-msg:SimpleBhandPickUpResult instead.")))

(cl:ensure-generic-function 'grasp_result-val :lambda-list '(m))
(cl:defmethod grasp_result-val ((m <SimpleBhandPickUpResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:grasp_result-val is deprecated.  Use iri_wam_common_msgs-msg:grasp_result instead.")
  (grasp_result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SimpleBhandPickUpResult>) ostream)
  "Serializes a message object of type '<SimpleBhandPickUpResult>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'grasp_result) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SimpleBhandPickUpResult>) istream)
  "Deserializes a message object of type '<SimpleBhandPickUpResult>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'grasp_result) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SimpleBhandPickUpResult>)))
  "Returns string type for a message object of type '<SimpleBhandPickUpResult>"
  "iri_wam_common_msgs/SimpleBhandPickUpResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SimpleBhandPickUpResult)))
  "Returns string type for a message object of type 'SimpleBhandPickUpResult"
  "iri_wam_common_msgs/SimpleBhandPickUpResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SimpleBhandPickUpResult>)))
  "Returns md5sum for a message object of type '<SimpleBhandPickUpResult>"
  "57a29b864b3e031ed431325393849b26")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SimpleBhandPickUpResult)))
  "Returns md5sum for a message object of type 'SimpleBhandPickUpResult"
  "57a29b864b3e031ed431325393849b26")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SimpleBhandPickUpResult>)))
  "Returns full string definition for message of type '<SimpleBhandPickUpResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# result~%object_manipulation_msgs/GraspResult grasp_result~%~%~%================================================================================~%MSG: object_manipulation_msgs/GraspResult~%int32 SUCCESS = 1~%int32 GRASP_OUT_OF_REACH = 2~%int32 GRASP_IN_COLLISION = 3~%int32 GRASP_UNFEASIBLE = 4~%int32 PREGRASP_OUT_OF_REACH = 5~%int32 PREGRASP_IN_COLLISION = 6~%int32 PREGRASP_UNFEASIBLE = 7~%int32 LIFT_OUT_OF_REACH = 8~%int32 LIFT_IN_COLLISION = 9~%int32 LIFT_UNFEASIBLE = 10~%int32 MOVE_ARM_FAILED = 11~%int32 GRASP_FAILED = 12~%int32 LIFT_FAILED = 13~%int32 RETREAT_FAILED = 14~%int32 result_code~%~%# whether the state of the world was disturbed by this attempt. generally, this flag~%# shows if another task can be attempted, or a new sensed world model is recommeded~%# before proceeding~%bool continuation_possible~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SimpleBhandPickUpResult)))
  "Returns full string definition for message of type 'SimpleBhandPickUpResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# result~%object_manipulation_msgs/GraspResult grasp_result~%~%~%================================================================================~%MSG: object_manipulation_msgs/GraspResult~%int32 SUCCESS = 1~%int32 GRASP_OUT_OF_REACH = 2~%int32 GRASP_IN_COLLISION = 3~%int32 GRASP_UNFEASIBLE = 4~%int32 PREGRASP_OUT_OF_REACH = 5~%int32 PREGRASP_IN_COLLISION = 6~%int32 PREGRASP_UNFEASIBLE = 7~%int32 LIFT_OUT_OF_REACH = 8~%int32 LIFT_IN_COLLISION = 9~%int32 LIFT_UNFEASIBLE = 10~%int32 MOVE_ARM_FAILED = 11~%int32 GRASP_FAILED = 12~%int32 LIFT_FAILED = 13~%int32 RETREAT_FAILED = 14~%int32 result_code~%~%# whether the state of the world was disturbed by this attempt. generally, this flag~%# shows if another task can be attempted, or a new sensed world model is recommeded~%# before proceeding~%bool continuation_possible~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SimpleBhandPickUpResult>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'grasp_result))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SimpleBhandPickUpResult>))
  "Converts a ROS message object to a list"
  (cl:list 'SimpleBhandPickUpResult
    (cl:cons ':grasp_result (grasp_result msg))
))

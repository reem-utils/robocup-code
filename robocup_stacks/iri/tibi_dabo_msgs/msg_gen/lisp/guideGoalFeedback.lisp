; Auto-generated. Do not edit!


(cl:in-package tibi_dabo_msgs-msg)


;//! \htmlinclude guideGoalFeedback.msg.html

(cl:defclass <guideGoalFeedback> (roslisp-msg-protocol:ros-message)
  ((distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass guideGoalFeedback (<guideGoalFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <guideGoalFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'guideGoalFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tibi_dabo_msgs-msg:<guideGoalFeedback> is deprecated: use tibi_dabo_msgs-msg:guideGoalFeedback instead.")))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <guideGoalFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:distance-val is deprecated.  Use tibi_dabo_msgs-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <guideGoalFeedback>) ostream)
  "Serializes a message object of type '<guideGoalFeedback>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <guideGoalFeedback>) istream)
  "Deserializes a message object of type '<guideGoalFeedback>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<guideGoalFeedback>)))
  "Returns string type for a message object of type '<guideGoalFeedback>"
  "tibi_dabo_msgs/guideGoalFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'guideGoalFeedback)))
  "Returns string type for a message object of type 'guideGoalFeedback"
  "tibi_dabo_msgs/guideGoalFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<guideGoalFeedback>)))
  "Returns md5sum for a message object of type '<guideGoalFeedback>"
  "6e77fb10f0c8b4833ec273aa9ac74459")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'guideGoalFeedback)))
  "Returns md5sum for a message object of type 'guideGoalFeedback"
  "6e77fb10f0c8b4833ec273aa9ac74459")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<guideGoalFeedback>)))
  "Returns full string definition for message of type '<guideGoalFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%float32 distance~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'guideGoalFeedback)))
  "Returns full string definition for message of type 'guideGoalFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%float32 distance~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <guideGoalFeedback>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <guideGoalFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'guideGoalFeedback
    (cl:cons ':distance (distance msg))
))

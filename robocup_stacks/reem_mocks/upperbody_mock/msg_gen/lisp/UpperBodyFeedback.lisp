; Auto-generated. Do not edit!


(cl:in-package upperbody_mock-msg)


;//! \htmlinclude UpperBodyFeedback.msg.html

(cl:defclass <UpperBodyFeedback> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass UpperBodyFeedback (<UpperBodyFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UpperBodyFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UpperBodyFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name upperbody_mock-msg:<UpperBodyFeedback> is deprecated: use upperbody_mock-msg:UpperBodyFeedback instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UpperBodyFeedback>) ostream)
  "Serializes a message object of type '<UpperBodyFeedback>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UpperBodyFeedback>) istream)
  "Deserializes a message object of type '<UpperBodyFeedback>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UpperBodyFeedback>)))
  "Returns string type for a message object of type '<UpperBodyFeedback>"
  "upperbody_mock/UpperBodyFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UpperBodyFeedback)))
  "Returns string type for a message object of type 'UpperBodyFeedback"
  "upperbody_mock/UpperBodyFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UpperBodyFeedback>)))
  "Returns md5sum for a message object of type '<UpperBodyFeedback>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UpperBodyFeedback)))
  "Returns md5sum for a message object of type 'UpperBodyFeedback"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UpperBodyFeedback>)))
  "Returns full string definition for message of type '<UpperBodyFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# feedback message~%# no feedback for the moment. could be remaining time or current configuration~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UpperBodyFeedback)))
  "Returns full string definition for message of type 'UpperBodyFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# feedback message~%# no feedback for the moment. could be remaining time or current configuration~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UpperBodyFeedback>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UpperBodyFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'UpperBodyFeedback
))

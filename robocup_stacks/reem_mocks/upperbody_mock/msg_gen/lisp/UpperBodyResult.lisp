; Auto-generated. Do not edit!


(cl:in-package upperbody_mock-msg)


;//! \htmlinclude UpperBodyResult.msg.html

(cl:defclass <UpperBodyResult> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass UpperBodyResult (<UpperBodyResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <UpperBodyResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'UpperBodyResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name upperbody_mock-msg:<UpperBodyResult> is deprecated: use upperbody_mock-msg:UpperBodyResult instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <UpperBodyResult>) ostream)
  "Serializes a message object of type '<UpperBodyResult>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <UpperBodyResult>) istream)
  "Deserializes a message object of type '<UpperBodyResult>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<UpperBodyResult>)))
  "Returns string type for a message object of type '<UpperBodyResult>"
  "upperbody_mock/UpperBodyResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'UpperBodyResult)))
  "Returns string type for a message object of type 'UpperBodyResult"
  "upperbody_mock/UpperBodyResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<UpperBodyResult>)))
  "Returns md5sum for a message object of type '<UpperBodyResult>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'UpperBodyResult)))
  "Returns md5sum for a message object of type 'UpperBodyResult"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<UpperBodyResult>)))
  "Returns full string definition for message of type '<UpperBodyResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'UpperBodyResult)))
  "Returns full string definition for message of type 'UpperBodyResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <UpperBodyResult>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <UpperBodyResult>))
  "Converts a ROS message object to a list"
  (cl:list 'UpperBodyResult
))

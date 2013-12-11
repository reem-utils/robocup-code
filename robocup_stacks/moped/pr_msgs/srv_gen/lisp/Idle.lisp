; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude Idle-request.msg.html

(cl:defclass <Idle-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Idle-request (<Idle-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Idle-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Idle-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<Idle-request> is deprecated: use pr_msgs-srv:Idle-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Idle-request>) ostream)
  "Serializes a message object of type '<Idle-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Idle-request>) istream)
  "Deserializes a message object of type '<Idle-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Idle-request>)))
  "Returns string type for a service object of type '<Idle-request>"
  "pr_msgs/IdleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Idle-request)))
  "Returns string type for a service object of type 'Idle-request"
  "pr_msgs/IdleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Idle-request>)))
  "Returns md5sum for a message object of type '<Idle-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Idle-request)))
  "Returns md5sum for a message object of type 'Idle-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Idle-request>)))
  "Returns full string definition for message of type '<Idle-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Idle-request)))
  "Returns full string definition for message of type 'Idle-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Idle-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Idle-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Idle-request
))
;//! \htmlinclude Idle-response.msg.html

(cl:defclass <Idle-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Idle-response (<Idle-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Idle-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Idle-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<Idle-response> is deprecated: use pr_msgs-srv:Idle-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Idle-response>) ostream)
  "Serializes a message object of type '<Idle-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Idle-response>) istream)
  "Deserializes a message object of type '<Idle-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Idle-response>)))
  "Returns string type for a service object of type '<Idle-response>"
  "pr_msgs/IdleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Idle-response)))
  "Returns string type for a service object of type 'Idle-response"
  "pr_msgs/IdleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Idle-response>)))
  "Returns md5sum for a message object of type '<Idle-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Idle-response)))
  "Returns md5sum for a message object of type 'Idle-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Idle-response>)))
  "Returns full string definition for message of type '<Idle-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Idle-response)))
  "Returns full string definition for message of type 'Idle-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Idle-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Idle-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Idle-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Idle)))
  'Idle-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Idle)))
  'Idle-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Idle)))
  "Returns string type for a service object of type '<Idle>"
  "pr_msgs/Idle")
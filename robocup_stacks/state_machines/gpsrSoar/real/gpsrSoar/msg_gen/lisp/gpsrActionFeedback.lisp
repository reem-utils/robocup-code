; Auto-generated. Do not edit!


(cl:in-package gpsrSoar-msg)


;//! \htmlinclude gpsrActionFeedback.msg.html

(cl:defclass <gpsrActionFeedback> (roslisp-msg-protocol:ros-message)
  ((order_id
    :reader order_id
    :initarg :order_id
    :type cl:fixnum
    :initform 0))
)

(cl:defclass gpsrActionFeedback (<gpsrActionFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gpsrActionFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gpsrActionFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gpsrSoar-msg:<gpsrActionFeedback> is deprecated: use gpsrSoar-msg:gpsrActionFeedback instead.")))

(cl:ensure-generic-function 'order_id-val :lambda-list '(m))
(cl:defmethod order_id-val ((m <gpsrActionFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsrSoar-msg:order_id-val is deprecated.  Use gpsrSoar-msg:order_id instead.")
  (order_id m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gpsrActionFeedback>) ostream)
  "Serializes a message object of type '<gpsrActionFeedback>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'order_id)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gpsrActionFeedback>) istream)
  "Deserializes a message object of type '<gpsrActionFeedback>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'order_id)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gpsrActionFeedback>)))
  "Returns string type for a message object of type '<gpsrActionFeedback>"
  "gpsrSoar/gpsrActionFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gpsrActionFeedback)))
  "Returns string type for a message object of type 'gpsrActionFeedback"
  "gpsrSoar/gpsrActionFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gpsrActionFeedback>)))
  "Returns md5sum for a message object of type '<gpsrActionFeedback>"
  "380a887720e23b07d9d68a5be3c3ff4a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gpsrActionFeedback)))
  "Returns md5sum for a message object of type 'gpsrActionFeedback"
  "380a887720e23b07d9d68a5be3c3ff4a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gpsrActionFeedback>)))
  "Returns full string definition for message of type '<gpsrActionFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%uint8   order_id~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gpsrActionFeedback)))
  "Returns full string definition for message of type 'gpsrActionFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%uint8   order_id~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gpsrActionFeedback>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gpsrActionFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'gpsrActionFeedback
    (cl:cons ':order_id (order_id msg))
))
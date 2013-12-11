; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-srv)


;//! \htmlinclude AddState-request.msg.html

(cl:defclass <AddState-request> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type cl:string
    :initform ""))
)

(cl:defclass AddState-request (<AddState-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddState-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddState-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<AddState-request> is deprecated: use estirabot_msgs-srv:AddState-request instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <AddState-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:state-val is deprecated.  Use estirabot_msgs-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddState-request>) ostream)
  "Serializes a message object of type '<AddState-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddState-request>) istream)
  "Deserializes a message object of type '<AddState-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddState-request>)))
  "Returns string type for a service object of type '<AddState-request>"
  "estirabot_msgs/AddStateRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddState-request)))
  "Returns string type for a service object of type 'AddState-request"
  "estirabot_msgs/AddStateRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddState-request>)))
  "Returns md5sum for a message object of type '<AddState-request>"
  "cad71f86d65cfc59264a59a7bd0dbfe8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddState-request)))
  "Returns md5sum for a message object of type 'AddState-request"
  "cad71f86d65cfc59264a59a7bd0dbfe8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddState-request>)))
  "Returns full string definition for message of type '<AddState-request>"
  (cl:format cl:nil "~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddState-request)))
  "Returns full string definition for message of type 'AddState-request"
  (cl:format cl:nil "~%string state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddState-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddState-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AddState-request
    (cl:cons ':state (state msg))
))
;//! \htmlinclude AddState-response.msg.html

(cl:defclass <AddState-response> (roslisp-msg-protocol:ros-message)
  ((rules_updated
    :reader rules_updated
    :initarg :rules_updated
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass AddState-response (<AddState-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddState-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddState-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<AddState-response> is deprecated: use estirabot_msgs-srv:AddState-response instead.")))

(cl:ensure-generic-function 'rules_updated-val :lambda-list '(m))
(cl:defmethod rules_updated-val ((m <AddState-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:rules_updated-val is deprecated.  Use estirabot_msgs-srv:rules_updated instead.")
  (rules_updated m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddState-response>) ostream)
  "Serializes a message object of type '<AddState-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'rules_updated) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddState-response>) istream)
  "Deserializes a message object of type '<AddState-response>"
    (cl:setf (cl:slot-value msg 'rules_updated) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddState-response>)))
  "Returns string type for a service object of type '<AddState-response>"
  "estirabot_msgs/AddStateResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddState-response)))
  "Returns string type for a service object of type 'AddState-response"
  "estirabot_msgs/AddStateResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddState-response>)))
  "Returns md5sum for a message object of type '<AddState-response>"
  "cad71f86d65cfc59264a59a7bd0dbfe8")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddState-response)))
  "Returns md5sum for a message object of type 'AddState-response"
  "cad71f86d65cfc59264a59a7bd0dbfe8")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddState-response>)))
  "Returns full string definition for message of type '<AddState-response>"
  (cl:format cl:nil "bool rules_updated~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddState-response)))
  "Returns full string definition for message of type 'AddState-response"
  (cl:format cl:nil "bool rules_updated~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddState-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddState-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AddState-response
    (cl:cons ':rules_updated (rules_updated msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AddState)))
  'AddState-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AddState)))
  'AddState-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddState)))
  "Returns string type for a service object of type '<AddState>"
  "estirabot_msgs/AddState")
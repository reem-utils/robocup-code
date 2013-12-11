; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-srv)


;//! \htmlinclude obs2action-request.msg.html

(cl:defclass <obs2action-request> (roslisp-msg-protocol:ros-message)
  ((first
    :reader first
    :initarg :first
    :type cl:boolean
    :initform cl:nil)
   (observation
    :reader observation
    :initarg :observation
    :type cl:integer
    :initform 0))
)

(cl:defclass obs2action-request (<obs2action-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <obs2action-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'obs2action-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<obs2action-request> is deprecated: use estirabot_msgs-srv:obs2action-request instead.")))

(cl:ensure-generic-function 'first-val :lambda-list '(m))
(cl:defmethod first-val ((m <obs2action-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:first-val is deprecated.  Use estirabot_msgs-srv:first instead.")
  (first m))

(cl:ensure-generic-function 'observation-val :lambda-list '(m))
(cl:defmethod observation-val ((m <obs2action-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:observation-val is deprecated.  Use estirabot_msgs-srv:observation instead.")
  (observation m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <obs2action-request>) ostream)
  "Serializes a message object of type '<obs2action-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'first) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'observation)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'observation)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'observation)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'observation)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <obs2action-request>) istream)
  "Deserializes a message object of type '<obs2action-request>"
    (cl:setf (cl:slot-value msg 'first) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'observation)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'observation)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'observation)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'observation)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<obs2action-request>)))
  "Returns string type for a service object of type '<obs2action-request>"
  "estirabot_msgs/obs2actionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'obs2action-request)))
  "Returns string type for a service object of type 'obs2action-request"
  "estirabot_msgs/obs2actionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<obs2action-request>)))
  "Returns md5sum for a message object of type '<obs2action-request>"
  "370c545e7c55b03ea2f710e8d5f68de6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'obs2action-request)))
  "Returns md5sum for a message object of type 'obs2action-request"
  "370c545e7c55b03ea2f710e8d5f68de6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<obs2action-request>)))
  "Returns full string definition for message of type '<obs2action-request>"
  (cl:format cl:nil "bool first~%uint32 observation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'obs2action-request)))
  "Returns full string definition for message of type 'obs2action-request"
  (cl:format cl:nil "bool first~%uint32 observation~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <obs2action-request>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <obs2action-request>))
  "Converts a ROS message object to a list"
  (cl:list 'obs2action-request
    (cl:cons ':first (first msg))
    (cl:cons ':observation (observation msg))
))
;//! \htmlinclude obs2action-response.msg.html

(cl:defclass <obs2action-response> (roslisp-msg-protocol:ros-message)
  ((goal_reached
    :reader goal_reached
    :initarg :goal_reached
    :type cl:boolean
    :initform cl:nil)
   (action
    :reader action
    :initarg :action
    :type cl:integer
    :initform 0))
)

(cl:defclass obs2action-response (<obs2action-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <obs2action-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'obs2action-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<obs2action-response> is deprecated: use estirabot_msgs-srv:obs2action-response instead.")))

(cl:ensure-generic-function 'goal_reached-val :lambda-list '(m))
(cl:defmethod goal_reached-val ((m <obs2action-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:goal_reached-val is deprecated.  Use estirabot_msgs-srv:goal_reached instead.")
  (goal_reached m))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <obs2action-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:action-val is deprecated.  Use estirabot_msgs-srv:action instead.")
  (action m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <obs2action-response>) ostream)
  "Serializes a message object of type '<obs2action-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'goal_reached) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <obs2action-response>) istream)
  "Deserializes a message object of type '<obs2action-response>"
    (cl:setf (cl:slot-value msg 'goal_reached) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<obs2action-response>)))
  "Returns string type for a service object of type '<obs2action-response>"
  "estirabot_msgs/obs2actionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'obs2action-response)))
  "Returns string type for a service object of type 'obs2action-response"
  "estirabot_msgs/obs2actionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<obs2action-response>)))
  "Returns md5sum for a message object of type '<obs2action-response>"
  "370c545e7c55b03ea2f710e8d5f68de6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'obs2action-response)))
  "Returns md5sum for a message object of type 'obs2action-response"
  "370c545e7c55b03ea2f710e8d5f68de6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<obs2action-response>)))
  "Returns full string definition for message of type '<obs2action-response>"
  (cl:format cl:nil "bool goal_reached~%uint32 action~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'obs2action-response)))
  "Returns full string definition for message of type 'obs2action-response"
  (cl:format cl:nil "bool goal_reached~%uint32 action~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <obs2action-response>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <obs2action-response>))
  "Converts a ROS message object to a list"
  (cl:list 'obs2action-response
    (cl:cons ':goal_reached (goal_reached msg))
    (cl:cons ':action (action msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'obs2action)))
  'obs2action-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'obs2action)))
  'obs2action-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'obs2action)))
  "Returns string type for a service object of type '<obs2action>"
  "estirabot_msgs/obs2action")
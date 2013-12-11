; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude GuardedMove-request.msg.html

(cl:defclass <GuardedMove-request> (roslisp-msg-protocol:ros-message)
  ((positions
    :reader positions
    :initarg :positions
    :type pr_msgs-msg:Joints
    :initform (cl:make-instance 'pr_msgs-msg:Joints)))
)

(cl:defclass GuardedMove-request (<GuardedMove-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GuardedMove-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GuardedMove-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<GuardedMove-request> is deprecated: use pr_msgs-srv:GuardedMove-request instead.")))

(cl:ensure-generic-function 'positions-val :lambda-list '(m))
(cl:defmethod positions-val ((m <GuardedMove-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:positions-val is deprecated.  Use pr_msgs-srv:positions instead.")
  (positions m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GuardedMove-request>) ostream)
  "Serializes a message object of type '<GuardedMove-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'positions) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GuardedMove-request>) istream)
  "Deserializes a message object of type '<GuardedMove-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'positions) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GuardedMove-request>)))
  "Returns string type for a service object of type '<GuardedMove-request>"
  "pr_msgs/GuardedMoveRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GuardedMove-request)))
  "Returns string type for a service object of type 'GuardedMove-request"
  "pr_msgs/GuardedMoveRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GuardedMove-request>)))
  "Returns md5sum for a message object of type '<GuardedMove-request>"
  "4083b8b868daf15fc9fc8191fdaeff6e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GuardedMove-request)))
  "Returns md5sum for a message object of type 'GuardedMove-request"
  "4083b8b868daf15fc9fc8191fdaeff6e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GuardedMove-request>)))
  "Returns full string definition for message of type '<GuardedMove-request>"
  (cl:format cl:nil "pr_msgs/Joints positions~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GuardedMove-request)))
  "Returns full string definition for message of type 'GuardedMove-request"
  (cl:format cl:nil "pr_msgs/Joints positions~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GuardedMove-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'positions))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GuardedMove-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GuardedMove-request
    (cl:cons ':positions (positions msg))
))
;//! \htmlinclude GuardedMove-response.msg.html

(cl:defclass <GuardedMove-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass GuardedMove-response (<GuardedMove-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GuardedMove-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GuardedMove-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<GuardedMove-response> is deprecated: use pr_msgs-srv:GuardedMove-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <GuardedMove-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:ok-val is deprecated.  Use pr_msgs-srv:ok instead.")
  (ok m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GuardedMove-response>) ostream)
  "Serializes a message object of type '<GuardedMove-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GuardedMove-response>) istream)
  "Deserializes a message object of type '<GuardedMove-response>"
    (cl:setf (cl:slot-value msg 'ok) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GuardedMove-response>)))
  "Returns string type for a service object of type '<GuardedMove-response>"
  "pr_msgs/GuardedMoveResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GuardedMove-response)))
  "Returns string type for a service object of type 'GuardedMove-response"
  "pr_msgs/GuardedMoveResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GuardedMove-response>)))
  "Returns md5sum for a message object of type '<GuardedMove-response>"
  "4083b8b868daf15fc9fc8191fdaeff6e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GuardedMove-response)))
  "Returns md5sum for a message object of type 'GuardedMove-response"
  "4083b8b868daf15fc9fc8191fdaeff6e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GuardedMove-response>)))
  "Returns full string definition for message of type '<GuardedMove-response>"
  (cl:format cl:nil "bool ok~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GuardedMove-response)))
  "Returns full string definition for message of type 'GuardedMove-response"
  (cl:format cl:nil "bool ok~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GuardedMove-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GuardedMove-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GuardedMove-response
    (cl:cons ':ok (ok msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GuardedMove)))
  'GuardedMove-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GuardedMove)))
  'GuardedMove-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GuardedMove)))
  "Returns string type for a service object of type '<GuardedMove>"
  "pr_msgs/GuardedMove")
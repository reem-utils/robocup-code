; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude ResumeTrajectory-request.msg.html

(cl:defclass <ResumeTrajectory-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ResumeTrajectory-request (<ResumeTrajectory-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ResumeTrajectory-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ResumeTrajectory-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<ResumeTrajectory-request> is deprecated: use pr_msgs-srv:ResumeTrajectory-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ResumeTrajectory-request>) ostream)
  "Serializes a message object of type '<ResumeTrajectory-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ResumeTrajectory-request>) istream)
  "Deserializes a message object of type '<ResumeTrajectory-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ResumeTrajectory-request>)))
  "Returns string type for a service object of type '<ResumeTrajectory-request>"
  "pr_msgs/ResumeTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ResumeTrajectory-request)))
  "Returns string type for a service object of type 'ResumeTrajectory-request"
  "pr_msgs/ResumeTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ResumeTrajectory-request>)))
  "Returns md5sum for a message object of type '<ResumeTrajectory-request>"
  "4679398f882e7cbdea165980d3ec2888")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ResumeTrajectory-request)))
  "Returns md5sum for a message object of type 'ResumeTrajectory-request"
  "4679398f882e7cbdea165980d3ec2888")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ResumeTrajectory-request>)))
  "Returns full string definition for message of type '<ResumeTrajectory-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ResumeTrajectory-request)))
  "Returns full string definition for message of type 'ResumeTrajectory-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ResumeTrajectory-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ResumeTrajectory-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ResumeTrajectory-request
))
;//! \htmlinclude ResumeTrajectory-response.msg.html

(cl:defclass <ResumeTrajectory-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:boolean
    :initform cl:nil)
   (reason
    :reader reason
    :initarg :reason
    :type cl:string
    :initform ""))
)

(cl:defclass ResumeTrajectory-response (<ResumeTrajectory-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ResumeTrajectory-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ResumeTrajectory-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<ResumeTrajectory-response> is deprecated: use pr_msgs-srv:ResumeTrajectory-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <ResumeTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:ok-val is deprecated.  Use pr_msgs-srv:ok instead.")
  (ok m))

(cl:ensure-generic-function 'reason-val :lambda-list '(m))
(cl:defmethod reason-val ((m <ResumeTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:reason-val is deprecated.  Use pr_msgs-srv:reason instead.")
  (reason m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ResumeTrajectory-response>) ostream)
  "Serializes a message object of type '<ResumeTrajectory-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'reason))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'reason))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ResumeTrajectory-response>) istream)
  "Deserializes a message object of type '<ResumeTrajectory-response>"
    (cl:setf (cl:slot-value msg 'ok) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'reason) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'reason) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ResumeTrajectory-response>)))
  "Returns string type for a service object of type '<ResumeTrajectory-response>"
  "pr_msgs/ResumeTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ResumeTrajectory-response)))
  "Returns string type for a service object of type 'ResumeTrajectory-response"
  "pr_msgs/ResumeTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ResumeTrajectory-response>)))
  "Returns md5sum for a message object of type '<ResumeTrajectory-response>"
  "4679398f882e7cbdea165980d3ec2888")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ResumeTrajectory-response)))
  "Returns md5sum for a message object of type 'ResumeTrajectory-response"
  "4679398f882e7cbdea165980d3ec2888")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ResumeTrajectory-response>)))
  "Returns full string definition for message of type '<ResumeTrajectory-response>"
  (cl:format cl:nil "bool ok~%string reason~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ResumeTrajectory-response)))
  "Returns full string definition for message of type 'ResumeTrajectory-response"
  (cl:format cl:nil "bool ok~%string reason~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ResumeTrajectory-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'reason))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ResumeTrajectory-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ResumeTrajectory-response
    (cl:cons ':ok (ok msg))
    (cl:cons ':reason (reason msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ResumeTrajectory)))
  'ResumeTrajectory-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ResumeTrajectory)))
  'ResumeTrajectory-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ResumeTrajectory)))
  "Returns string type for a service object of type '<ResumeTrajectory>"
  "pr_msgs/ResumeTrajectory")
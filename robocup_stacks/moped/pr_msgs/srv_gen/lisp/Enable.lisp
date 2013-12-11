; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude Enable-request.msg.html

(cl:defclass <Enable-request> (roslisp-msg-protocol:ros-message)
  ((Enable
    :reader Enable
    :initarg :Enable
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Enable-request (<Enable-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Enable-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Enable-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<Enable-request> is deprecated: use pr_msgs-srv:Enable-request instead.")))

(cl:ensure-generic-function 'Enable-val :lambda-list '(m))
(cl:defmethod Enable-val ((m <Enable-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:Enable-val is deprecated.  Use pr_msgs-srv:Enable instead.")
  (Enable m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Enable-request>) ostream)
  "Serializes a message object of type '<Enable-request>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'Enable) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Enable-request>) istream)
  "Deserializes a message object of type '<Enable-request>"
    (cl:setf (cl:slot-value msg 'Enable) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Enable-request>)))
  "Returns string type for a service object of type '<Enable-request>"
  "pr_msgs/EnableRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Enable-request)))
  "Returns string type for a service object of type 'Enable-request"
  "pr_msgs/EnableRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Enable-request>)))
  "Returns md5sum for a message object of type '<Enable-request>"
  "46e2c93ae1cc7896720bf5acee0f2e89")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Enable-request)))
  "Returns md5sum for a message object of type 'Enable-request"
  "46e2c93ae1cc7896720bf5acee0f2e89")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Enable-request>)))
  "Returns full string definition for message of type '<Enable-request>"
  (cl:format cl:nil "bool Enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Enable-request)))
  "Returns full string definition for message of type 'Enable-request"
  (cl:format cl:nil "bool Enable~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Enable-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Enable-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Enable-request
    (cl:cons ':Enable (Enable msg))
))
;//! \htmlinclude Enable-response.msg.html

(cl:defclass <Enable-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass Enable-response (<Enable-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Enable-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Enable-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<Enable-response> is deprecated: use pr_msgs-srv:Enable-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <Enable-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:ok-val is deprecated.  Use pr_msgs-srv:ok instead.")
  (ok m))

(cl:ensure-generic-function 'reason-val :lambda-list '(m))
(cl:defmethod reason-val ((m <Enable-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:reason-val is deprecated.  Use pr_msgs-srv:reason instead.")
  (reason m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Enable-response>) ostream)
  "Serializes a message object of type '<Enable-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'reason))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'reason))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Enable-response>) istream)
  "Deserializes a message object of type '<Enable-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Enable-response>)))
  "Returns string type for a service object of type '<Enable-response>"
  "pr_msgs/EnableResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Enable-response)))
  "Returns string type for a service object of type 'Enable-response"
  "pr_msgs/EnableResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Enable-response>)))
  "Returns md5sum for a message object of type '<Enable-response>"
  "46e2c93ae1cc7896720bf5acee0f2e89")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Enable-response)))
  "Returns md5sum for a message object of type 'Enable-response"
  "46e2c93ae1cc7896720bf5acee0f2e89")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Enable-response>)))
  "Returns full string definition for message of type '<Enable-response>"
  (cl:format cl:nil "bool ok~%string reason~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Enable-response)))
  "Returns full string definition for message of type 'Enable-response"
  (cl:format cl:nil "bool ok~%string reason~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Enable-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'reason))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Enable-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Enable-response
    (cl:cons ':ok (ok msg))
    (cl:cons ':reason (reason msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Enable)))
  'Enable-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Enable)))
  'Enable-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Enable)))
  "Returns string type for a service object of type '<Enable>"
  "pr_msgs/Enable")
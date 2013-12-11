; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude AppletCommand-request.msg.html

(cl:defclass <AppletCommand-request> (roslisp-msg-protocol:ros-message)
  ((action_name
    :reader action_name
    :initarg :action_name
    :type cl:string
    :initform "")
   (target_name
    :reader target_name
    :initarg :target_name
    :type cl:string
    :initform "")
   (prep_timelimit
    :reader prep_timelimit
    :initarg :prep_timelimit
    :type cl:integer
    :initform 0)
   (execution_timelimit
    :reader execution_timelimit
    :initarg :execution_timelimit
    :type cl:integer
    :initform 0))
)

(cl:defclass AppletCommand-request (<AppletCommand-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AppletCommand-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AppletCommand-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<AppletCommand-request> is deprecated: use pr_msgs-srv:AppletCommand-request instead.")))

(cl:ensure-generic-function 'action_name-val :lambda-list '(m))
(cl:defmethod action_name-val ((m <AppletCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:action_name-val is deprecated.  Use pr_msgs-srv:action_name instead.")
  (action_name m))

(cl:ensure-generic-function 'target_name-val :lambda-list '(m))
(cl:defmethod target_name-val ((m <AppletCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:target_name-val is deprecated.  Use pr_msgs-srv:target_name instead.")
  (target_name m))

(cl:ensure-generic-function 'prep_timelimit-val :lambda-list '(m))
(cl:defmethod prep_timelimit-val ((m <AppletCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:prep_timelimit-val is deprecated.  Use pr_msgs-srv:prep_timelimit instead.")
  (prep_timelimit m))

(cl:ensure-generic-function 'execution_timelimit-val :lambda-list '(m))
(cl:defmethod execution_timelimit-val ((m <AppletCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:execution_timelimit-val is deprecated.  Use pr_msgs-srv:execution_timelimit instead.")
  (execution_timelimit m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AppletCommand-request>) ostream)
  "Serializes a message object of type '<AppletCommand-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action_name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'target_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'target_name))
  (cl:let* ((signed (cl:slot-value msg 'prep_timelimit)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'execution_timelimit)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AppletCommand-request>) istream)
  "Deserializes a message object of type '<AppletCommand-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'target_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'target_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'prep_timelimit) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'execution_timelimit) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AppletCommand-request>)))
  "Returns string type for a service object of type '<AppletCommand-request>"
  "pr_msgs/AppletCommandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AppletCommand-request)))
  "Returns string type for a service object of type 'AppletCommand-request"
  "pr_msgs/AppletCommandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AppletCommand-request>)))
  "Returns md5sum for a message object of type '<AppletCommand-request>"
  "6f67d009a5b105353f04c370165b4fd2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AppletCommand-request)))
  "Returns md5sum for a message object of type 'AppletCommand-request"
  "6f67d009a5b105353f04c370165b4fd2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AppletCommand-request>)))
  "Returns full string definition for message of type '<AppletCommand-request>"
  (cl:format cl:nil "string action_name~%~%string target_name~%~%int32 prep_timelimit~%~%int32 execution_timelimit~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AppletCommand-request)))
  "Returns full string definition for message of type 'AppletCommand-request"
  (cl:format cl:nil "string action_name~%~%string target_name~%~%int32 prep_timelimit~%~%int32 execution_timelimit~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AppletCommand-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'action_name))
     4 (cl:length (cl:slot-value msg 'target_name))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AppletCommand-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AppletCommand-request
    (cl:cons ':action_name (action_name msg))
    (cl:cons ':target_name (target_name msg))
    (cl:cons ':prep_timelimit (prep_timelimit msg))
    (cl:cons ':execution_timelimit (execution_timelimit msg))
))
;//! \htmlinclude AppletCommand-response.msg.html

(cl:defclass <AppletCommand-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:fixnum
    :initform 0)
   (info
    :reader info
    :initarg :info
    :type cl:string
    :initform ""))
)

(cl:defclass AppletCommand-response (<AppletCommand-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AppletCommand-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AppletCommand-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<AppletCommand-response> is deprecated: use pr_msgs-srv:AppletCommand-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <AppletCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:result-val is deprecated.  Use pr_msgs-srv:result instead.")
  (result m))

(cl:ensure-generic-function 'info-val :lambda-list '(m))
(cl:defmethod info-val ((m <AppletCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:info-val is deprecated.  Use pr_msgs-srv:info instead.")
  (info m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<AppletCommand-response>)))
    "Constants for message type '<AppletCommand-response>"
  '((:DONE . 0)
    (:UNKNOWN_COMMAND . 1)
    (:UNAVAILABLE . 2)
    (:TIMEOUT . 3)
    (:ERROR . 4))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'AppletCommand-response)))
    "Constants for message type 'AppletCommand-response"
  '((:DONE . 0)
    (:UNKNOWN_COMMAND . 1)
    (:UNAVAILABLE . 2)
    (:TIMEOUT . 3)
    (:ERROR . 4))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AppletCommand-response>) ostream)
  "Serializes a message object of type '<AppletCommand-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'result)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'info))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'info))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AppletCommand-response>) istream)
  "Deserializes a message object of type '<AppletCommand-response>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'result)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'info) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'info) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AppletCommand-response>)))
  "Returns string type for a service object of type '<AppletCommand-response>"
  "pr_msgs/AppletCommandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AppletCommand-response)))
  "Returns string type for a service object of type 'AppletCommand-response"
  "pr_msgs/AppletCommandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AppletCommand-response>)))
  "Returns md5sum for a message object of type '<AppletCommand-response>"
  "6f67d009a5b105353f04c370165b4fd2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AppletCommand-response)))
  "Returns md5sum for a message object of type 'AppletCommand-response"
  "6f67d009a5b105353f04c370165b4fd2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AppletCommand-response>)))
  "Returns full string definition for message of type '<AppletCommand-response>"
  (cl:format cl:nil "uint8 result~%string info~%~%uint8 DONE=0~%uint8 UNKNOWN_COMMAND=1~%uint8 UNAVAILABLE=2~%uint8 TIMEOUT=3~%uint8 ERROR=4~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AppletCommand-response)))
  "Returns full string definition for message of type 'AppletCommand-response"
  (cl:format cl:nil "uint8 result~%string info~%~%uint8 DONE=0~%uint8 UNKNOWN_COMMAND=1~%uint8 UNAVAILABLE=2~%uint8 TIMEOUT=3~%uint8 ERROR=4~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AppletCommand-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'info))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AppletCommand-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AppletCommand-response
    (cl:cons ':result (result msg))
    (cl:cons ':info (info msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AppletCommand)))
  'AppletCommand-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AppletCommand)))
  'AppletCommand-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AppletCommand)))
  "Returns string type for a service object of type '<AppletCommand>"
  "pr_msgs/AppletCommand")
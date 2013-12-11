; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude oldAppletCommand.msg.html

(cl:defclass <oldAppletCommand> (roslisp-msg-protocol:ros-message)
  ((node_name
    :reader node_name
    :initarg :node_name
    :type cl:string
    :initform "")
   (action_name
    :reader action_name
    :initarg :action_name
    :type cl:string
    :initform "")
   (target_name
    :reader target_name
    :initarg :target_name
    :type cl:string
    :initform "")
   (command_id
    :reader command_id
    :initarg :command_id
    :type cl:integer
    :initform 0)
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

(cl:defclass oldAppletCommand (<oldAppletCommand>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <oldAppletCommand>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'oldAppletCommand)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<oldAppletCommand> is deprecated: use pr_msgs-msg:oldAppletCommand instead.")))

(cl:ensure-generic-function 'node_name-val :lambda-list '(m))
(cl:defmethod node_name-val ((m <oldAppletCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:node_name-val is deprecated.  Use pr_msgs-msg:node_name instead.")
  (node_name m))

(cl:ensure-generic-function 'action_name-val :lambda-list '(m))
(cl:defmethod action_name-val ((m <oldAppletCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:action_name-val is deprecated.  Use pr_msgs-msg:action_name instead.")
  (action_name m))

(cl:ensure-generic-function 'target_name-val :lambda-list '(m))
(cl:defmethod target_name-val ((m <oldAppletCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:target_name-val is deprecated.  Use pr_msgs-msg:target_name instead.")
  (target_name m))

(cl:ensure-generic-function 'command_id-val :lambda-list '(m))
(cl:defmethod command_id-val ((m <oldAppletCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:command_id-val is deprecated.  Use pr_msgs-msg:command_id instead.")
  (command_id m))

(cl:ensure-generic-function 'prep_timelimit-val :lambda-list '(m))
(cl:defmethod prep_timelimit-val ((m <oldAppletCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:prep_timelimit-val is deprecated.  Use pr_msgs-msg:prep_timelimit instead.")
  (prep_timelimit m))

(cl:ensure-generic-function 'execution_timelimit-val :lambda-list '(m))
(cl:defmethod execution_timelimit-val ((m <oldAppletCommand>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:execution_timelimit-val is deprecated.  Use pr_msgs-msg:execution_timelimit instead.")
  (execution_timelimit m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <oldAppletCommand>) ostream)
  "Serializes a message object of type '<oldAppletCommand>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'node_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'node_name))
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
  (cl:let* ((signed (cl:slot-value msg 'command_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <oldAppletCommand>) istream)
  "Deserializes a message object of type '<oldAppletCommand>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'node_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'node_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
      (cl:setf (cl:slot-value msg 'command_id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<oldAppletCommand>)))
  "Returns string type for a message object of type '<oldAppletCommand>"
  "pr_msgs/oldAppletCommand")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'oldAppletCommand)))
  "Returns string type for a message object of type 'oldAppletCommand"
  "pr_msgs/oldAppletCommand")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<oldAppletCommand>)))
  "Returns md5sum for a message object of type '<oldAppletCommand>"
  "3d5ec065e60aaea41600679f9f3cdd68")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'oldAppletCommand)))
  "Returns md5sum for a message object of type 'oldAppletCommand"
  "3d5ec065e60aaea41600679f9f3cdd68")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<oldAppletCommand>)))
  "Returns full string definition for message of type '<oldAppletCommand>"
  (cl:format cl:nil "string node_name       # name of the node to perform the action~%~%string action_name     # name of the action~%~%string target_name     # name of the target to act upon~%~%int32 command_id         # unique identifier for this command~%~%int32 prep_timelimit     # max time to spend before moving the robot~%~%int32 execution_timelimit  # max time to spend while moving the robot~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'oldAppletCommand)))
  "Returns full string definition for message of type 'oldAppletCommand"
  (cl:format cl:nil "string node_name       # name of the node to perform the action~%~%string action_name     # name of the action~%~%string target_name     # name of the target to act upon~%~%int32 command_id         # unique identifier for this command~%~%int32 prep_timelimit     # max time to spend before moving the robot~%~%int32 execution_timelimit  # max time to spend while moving the robot~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <oldAppletCommand>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'node_name))
     4 (cl:length (cl:slot-value msg 'action_name))
     4 (cl:length (cl:slot-value msg 'target_name))
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <oldAppletCommand>))
  "Converts a ROS message object to a list"
  (cl:list 'oldAppletCommand
    (cl:cons ':node_name (node_name msg))
    (cl:cons ':action_name (action_name msg))
    (cl:cons ':target_name (target_name msg))
    (cl:cons ':command_id (command_id msg))
    (cl:cons ':prep_timelimit (prep_timelimit msg))
    (cl:cons ':execution_timelimit (execution_timelimit msg))
))

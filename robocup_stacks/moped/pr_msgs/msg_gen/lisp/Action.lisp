; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude Action.msg.html

(cl:defclass <Action> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (target_name
    :reader target_name
    :initarg :target_name
    :type cl:string
    :initform "")
   (prep_duration
    :reader prep_duration
    :initarg :prep_duration
    :type cl:integer
    :initform 0)
   (execution_duration
    :reader execution_duration
    :initarg :execution_duration
    :type cl:integer
    :initform 0))
)

(cl:defclass Action (<Action>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Action>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Action)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<Action> is deprecated: use pr_msgs-msg:Action instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <Action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:name-val is deprecated.  Use pr_msgs-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'target_name-val :lambda-list '(m))
(cl:defmethod target_name-val ((m <Action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:target_name-val is deprecated.  Use pr_msgs-msg:target_name instead.")
  (target_name m))

(cl:ensure-generic-function 'prep_duration-val :lambda-list '(m))
(cl:defmethod prep_duration-val ((m <Action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:prep_duration-val is deprecated.  Use pr_msgs-msg:prep_duration instead.")
  (prep_duration m))

(cl:ensure-generic-function 'execution_duration-val :lambda-list '(m))
(cl:defmethod execution_duration-val ((m <Action>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:execution_duration-val is deprecated.  Use pr_msgs-msg:execution_duration instead.")
  (execution_duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Action>) ostream)
  "Serializes a message object of type '<Action>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'target_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'target_name))
  (cl:let* ((signed (cl:slot-value msg 'prep_duration)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'execution_duration)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Action>) istream)
  "Deserializes a message object of type '<Action>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
      (cl:setf (cl:slot-value msg 'prep_duration) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'execution_duration) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Action>)))
  "Returns string type for a message object of type '<Action>"
  "pr_msgs/Action")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Action)))
  "Returns string type for a message object of type 'Action"
  "pr_msgs/Action")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Action>)))
  "Returns md5sum for a message object of type '<Action>"
  "6ddf77916fbb7875e9cbd82630d8ea35")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Action)))
  "Returns md5sum for a message object of type 'Action"
  "6ddf77916fbb7875e9cbd82630d8ea35")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Action>)))
  "Returns full string definition for message of type '<Action>"
  (cl:format cl:nil "string name         # name of this action (e.g. pickup_juice_box)~%~%string target_name  # distinguishes the target of this action from others~%                    #  (could be a global object id, world coordinates, etc)~%~%int32 prep_duration   # how long to expect before any movement commences~%~%int32 execution_duration  # how long to expect the movement to take~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Action)))
  "Returns full string definition for message of type 'Action"
  (cl:format cl:nil "string name         # name of this action (e.g. pickup_juice_box)~%~%string target_name  # distinguishes the target of this action from others~%                    #  (could be a global object id, world coordinates, etc)~%~%int32 prep_duration   # how long to expect before any movement commences~%~%int32 execution_duration  # how long to expect the movement to take~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Action>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'target_name))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Action>))
  "Converts a ROS message object to a list"
  (cl:list 'Action
    (cl:cons ':name (name msg))
    (cl:cons ':target_name (target_name msg))
    (cl:cons ':prep_duration (prep_duration msg))
    (cl:cons ':execution_duration (execution_duration msg))
))

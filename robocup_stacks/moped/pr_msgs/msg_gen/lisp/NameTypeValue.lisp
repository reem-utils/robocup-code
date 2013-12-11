; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude NameTypeValue.msg.html

(cl:defclass <NameTypeValue> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (type
    :reader type
    :initarg :type
    :type cl:string
    :initform "")
   (value
    :reader value
    :initarg :value
    :type cl:string
    :initform ""))
)

(cl:defclass NameTypeValue (<NameTypeValue>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NameTypeValue>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NameTypeValue)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<NameTypeValue> is deprecated: use pr_msgs-msg:NameTypeValue instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <NameTypeValue>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:name-val is deprecated.  Use pr_msgs-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'type-val :lambda-list '(m))
(cl:defmethod type-val ((m <NameTypeValue>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:type-val is deprecated.  Use pr_msgs-msg:type instead.")
  (type m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <NameTypeValue>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:value-val is deprecated.  Use pr_msgs-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NameTypeValue>) ostream)
  "Serializes a message object of type '<NameTypeValue>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'type))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'value))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NameTypeValue>) istream)
  "Deserializes a message object of type '<NameTypeValue>"
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
      (cl:setf (cl:slot-value msg 'type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'value) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'value) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NameTypeValue>)))
  "Returns string type for a message object of type '<NameTypeValue>"
  "pr_msgs/NameTypeValue")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NameTypeValue)))
  "Returns string type for a message object of type 'NameTypeValue"
  "pr_msgs/NameTypeValue")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NameTypeValue>)))
  "Returns md5sum for a message object of type '<NameTypeValue>"
  "2a06900160ca5ec95f57a5ec28eaaa33")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NameTypeValue)))
  "Returns md5sum for a message object of type 'NameTypeValue"
  "2a06900160ca5ec95f57a5ec28eaaa33")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NameTypeValue>)))
  "Returns full string definition for message of type '<NameTypeValue>"
  (cl:format cl:nil "string name~%string type~%string value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NameTypeValue)))
  "Returns full string definition for message of type 'NameTypeValue"
  (cl:format cl:nil "string name~%string type~%string value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NameTypeValue>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     4 (cl:length (cl:slot-value msg 'type))
     4 (cl:length (cl:slot-value msg 'value))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NameTypeValue>))
  "Converts a ROS message object to a list"
  (cl:list 'NameTypeValue
    (cl:cons ':name (name msg))
    (cl:cons ':type (type msg))
    (cl:cons ':value (value msg))
))

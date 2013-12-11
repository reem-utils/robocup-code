; Auto-generated. Do not edit!


(cl:in-package gpsr-msg)


;//! \htmlinclude order.msg.html

(cl:defclass <order> (roslisp-msg-protocol:ros-message)
  ((action
    :reader action
    :initarg :action
    :type cl:string
    :initform "")
   (person
    :reader person
    :initarg :person
    :type cl:string
    :initform "")
   (location
    :reader location
    :initarg :location
    :type cl:string
    :initform "")
   (item
    :reader item
    :initarg :item
    :type cl:string
    :initform "")
   (other
    :reader other
    :initarg :other
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass order (<order>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <order>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'order)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gpsr-msg:<order> is deprecated: use gpsr-msg:order instead.")))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <order>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsr-msg:action-val is deprecated.  Use gpsr-msg:action instead.")
  (action m))

(cl:ensure-generic-function 'person-val :lambda-list '(m))
(cl:defmethod person-val ((m <order>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsr-msg:person-val is deprecated.  Use gpsr-msg:person instead.")
  (person m))

(cl:ensure-generic-function 'location-val :lambda-list '(m))
(cl:defmethod location-val ((m <order>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsr-msg:location-val is deprecated.  Use gpsr-msg:location instead.")
  (location m))

(cl:ensure-generic-function 'item-val :lambda-list '(m))
(cl:defmethod item-val ((m <order>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsr-msg:item-val is deprecated.  Use gpsr-msg:item instead.")
  (item m))

(cl:ensure-generic-function 'other-val :lambda-list '(m))
(cl:defmethod other-val ((m <order>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsr-msg:other-val is deprecated.  Use gpsr-msg:other instead.")
  (other m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <order>) ostream)
  "Serializes a message object of type '<order>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'person))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'person))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'location))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'location))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'item))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'item))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'other))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'other))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <order>) istream)
  "Deserializes a message object of type '<order>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'person) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'person) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'location) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'location) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'item) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'item) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'other) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'other)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<order>)))
  "Returns string type for a message object of type '<order>"
  "gpsr/order")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'order)))
  "Returns string type for a message object of type 'order"
  "gpsr/order")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<order>)))
  "Returns md5sum for a message object of type '<order>"
  "b4ae35fceb89861812a87ec5fbec597a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'order)))
  "Returns md5sum for a message object of type 'order"
  "b4ae35fceb89861812a87ec5fbec597a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<order>)))
  "Returns full string definition for message of type '<order>"
  (cl:format cl:nil "string action~%string person~%string location~%string item~%string[] other~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'order)))
  "Returns full string definition for message of type 'order"
  (cl:format cl:nil "string action~%string person~%string location~%string item~%string[] other~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <order>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'action))
     4 (cl:length (cl:slot-value msg 'person))
     4 (cl:length (cl:slot-value msg 'location))
     4 (cl:length (cl:slot-value msg 'item))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'other) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <order>))
  "Converts a ROS message object to a list"
  (cl:list 'order
    (cl:cons ':action (action msg))
    (cl:cons ':person (person msg))
    (cl:cons ':location (location msg))
    (cl:cons ':item (item msg))
    (cl:cons ':other (other msg))
))

; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude ArrayIndexes.msg.html

(cl:defclass <ArrayIndexes> (roslisp-msg-protocol:ros-message)
  ((indexes
    :reader indexes
    :initarg :indexes
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass ArrayIndexes (<ArrayIndexes>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArrayIndexes>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArrayIndexes)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<ArrayIndexes> is deprecated: use estirabot_msgs-msg:ArrayIndexes instead.")))

(cl:ensure-generic-function 'indexes-val :lambda-list '(m))
(cl:defmethod indexes-val ((m <ArrayIndexes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:indexes-val is deprecated.  Use estirabot_msgs-msg:indexes instead.")
  (indexes m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArrayIndexes>) ostream)
  "Serializes a message object of type '<ArrayIndexes>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'indexes))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) ele) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) ele) ostream))
   (cl:slot-value msg 'indexes))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArrayIndexes>) istream)
  "Deserializes a message object of type '<ArrayIndexes>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'indexes) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'indexes)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:aref vals i)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArrayIndexes>)))
  "Returns string type for a message object of type '<ArrayIndexes>"
  "estirabot_msgs/ArrayIndexes")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArrayIndexes)))
  "Returns string type for a message object of type 'ArrayIndexes"
  "estirabot_msgs/ArrayIndexes")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArrayIndexes>)))
  "Returns md5sum for a message object of type '<ArrayIndexes>"
  "548f4b0df4a06b3a5adcd286cfc278aa")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArrayIndexes)))
  "Returns md5sum for a message object of type 'ArrayIndexes"
  "548f4b0df4a06b3a5adcd286cfc278aa")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArrayIndexes>)))
  "Returns full string definition for message of type '<ArrayIndexes>"
  (cl:format cl:nil "uint32[] indexes~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArrayIndexes)))
  "Returns full string definition for message of type 'ArrayIndexes"
  (cl:format cl:nil "uint32[] indexes~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArrayIndexes>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'indexes) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArrayIndexes>))
  "Converts a ROS message object to a list"
  (cl:list 'ArrayIndexes
    (cl:cons ':indexes (indexes msg))
))

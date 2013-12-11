; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude QR.msg.html

(cl:defclass <QR> (roslisp-msg-protocol:ros-message)
  ((qr_strings
    :reader qr_strings
    :initarg :qr_strings
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass QR (<QR>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <QR>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'QR)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<QR> is deprecated: use pr_msgs-msg:QR instead.")))

(cl:ensure-generic-function 'qr_strings-val :lambda-list '(m))
(cl:defmethod qr_strings-val ((m <QR>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:qr_strings-val is deprecated.  Use pr_msgs-msg:qr_strings instead.")
  (qr_strings m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <QR>) ostream)
  "Serializes a message object of type '<QR>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'qr_strings))))
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
   (cl:slot-value msg 'qr_strings))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <QR>) istream)
  "Deserializes a message object of type '<QR>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'qr_strings) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'qr_strings)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<QR>)))
  "Returns string type for a message object of type '<QR>"
  "pr_msgs/QR")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'QR)))
  "Returns string type for a message object of type 'QR"
  "pr_msgs/QR")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<QR>)))
  "Returns md5sum for a message object of type '<QR>"
  "88cf0519306dea0fed4b6d2dec050a5c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'QR)))
  "Returns md5sum for a message object of type 'QR"
  "88cf0519306dea0fed4b6d2dec050a5c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<QR>)))
  "Returns full string definition for message of type '<QR>"
  (cl:format cl:nil "string[] qr_strings~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'QR)))
  "Returns full string definition for message of type 'QR"
  (cl:format cl:nil "string[] qr_strings~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <QR>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'qr_strings) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <QR>))
  "Converts a ROS message object to a list"
  (cl:list 'QR
    (cl:cons ':qr_strings (qr_strings msg))
))

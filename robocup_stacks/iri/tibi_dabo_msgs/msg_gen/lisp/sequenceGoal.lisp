; Auto-generated. Do not edit!


(cl:in-package tibi_dabo_msgs-msg)


;//! \htmlinclude sequenceGoal.msg.html

(cl:defclass <sequenceGoal> (roslisp-msg-protocol:ros-message)
  ((sequence_file
    :reader sequence_file
    :initarg :sequence_file
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (num_repetitions
    :reader num_repetitions
    :initarg :num_repetitions
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass sequenceGoal (<sequenceGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sequenceGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sequenceGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tibi_dabo_msgs-msg:<sequenceGoal> is deprecated: use tibi_dabo_msgs-msg:sequenceGoal instead.")))

(cl:ensure-generic-function 'sequence_file-val :lambda-list '(m))
(cl:defmethod sequence_file-val ((m <sequenceGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:sequence_file-val is deprecated.  Use tibi_dabo_msgs-msg:sequence_file instead.")
  (sequence_file m))

(cl:ensure-generic-function 'num_repetitions-val :lambda-list '(m))
(cl:defmethod num_repetitions-val ((m <sequenceGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:num_repetitions-val is deprecated.  Use tibi_dabo_msgs-msg:num_repetitions instead.")
  (num_repetitions m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sequenceGoal>) ostream)
  "Serializes a message object of type '<sequenceGoal>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'sequence_file))))
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
   (cl:slot-value msg 'sequence_file))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'num_repetitions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'num_repetitions))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sequenceGoal>) istream)
  "Deserializes a message object of type '<sequenceGoal>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'sequence_file) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'sequence_file)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'num_repetitions) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'num_repetitions)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sequenceGoal>)))
  "Returns string type for a message object of type '<sequenceGoal>"
  "tibi_dabo_msgs/sequenceGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sequenceGoal)))
  "Returns string type for a message object of type 'sequenceGoal"
  "tibi_dabo_msgs/sequenceGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sequenceGoal>)))
  "Returns md5sum for a message object of type '<sequenceGoal>"
  "f43f9a28a5d82ac92983f1e553ed78b4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sequenceGoal)))
  "Returns md5sum for a message object of type 'sequenceGoal"
  "f43f9a28a5d82ac92983f1e553ed78b4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sequenceGoal>)))
  "Returns full string definition for message of type '<sequenceGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%string[]  sequence_file~%int32[]   num_repetitions~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sequenceGoal)))
  "Returns full string definition for message of type 'sequenceGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%string[]  sequence_file~%int32[]   num_repetitions~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sequenceGoal>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'sequence_file) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'num_repetitions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sequenceGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'sequenceGoal
    (cl:cons ':sequence_file (sequence_file msg))
    (cl:cons ':num_repetitions (num_repetitions msg))
))

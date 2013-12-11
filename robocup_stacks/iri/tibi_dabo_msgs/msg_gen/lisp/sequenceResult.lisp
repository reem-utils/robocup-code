; Auto-generated. Do not edit!


(cl:in-package tibi_dabo_msgs-msg)


;//! \htmlinclude sequenceResult.msg.html

(cl:defclass <sequenceResult> (roslisp-msg-protocol:ros-message)
  ((successful
    :reader successful
    :initarg :successful
    :type (cl:vector cl:boolean)
   :initform (cl:make-array 0 :element-type 'cl:boolean :initial-element cl:nil))
   (observations
    :reader observations
    :initarg :observations
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element "")))
)

(cl:defclass sequenceResult (<sequenceResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <sequenceResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'sequenceResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tibi_dabo_msgs-msg:<sequenceResult> is deprecated: use tibi_dabo_msgs-msg:sequenceResult instead.")))

(cl:ensure-generic-function 'successful-val :lambda-list '(m))
(cl:defmethod successful-val ((m <sequenceResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:successful-val is deprecated.  Use tibi_dabo_msgs-msg:successful instead.")
  (successful m))

(cl:ensure-generic-function 'observations-val :lambda-list '(m))
(cl:defmethod observations-val ((m <sequenceResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:observations-val is deprecated.  Use tibi_dabo_msgs-msg:observations instead.")
  (observations m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <sequenceResult>) ostream)
  "Serializes a message object of type '<sequenceResult>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'successful))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if ele 1 0)) ostream))
   (cl:slot-value msg 'successful))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'observations))))
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
   (cl:slot-value msg 'observations))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <sequenceResult>) istream)
  "Deserializes a message object of type '<sequenceResult>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'successful) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'successful)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:not (cl:zerop (cl:read-byte istream)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'observations) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'observations)))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<sequenceResult>)))
  "Returns string type for a message object of type '<sequenceResult>"
  "tibi_dabo_msgs/sequenceResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'sequenceResult)))
  "Returns string type for a message object of type 'sequenceResult"
  "tibi_dabo_msgs/sequenceResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<sequenceResult>)))
  "Returns md5sum for a message object of type '<sequenceResult>"
  "5166c3db2c743179afd29dd6caf59d72")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'sequenceResult)))
  "Returns md5sum for a message object of type 'sequenceResult"
  "5166c3db2c743179afd29dd6caf59d72")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<sequenceResult>)))
  "Returns full string definition for message of type '<sequenceResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%bool[]    successful~%string[]  observations~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'sequenceResult)))
  "Returns full string definition for message of type 'sequenceResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%bool[]    successful~%string[]  observations~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <sequenceResult>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'successful) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'observations) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <sequenceResult>))
  "Converts a ROS message object to a list"
  (cl:list 'sequenceResult
    (cl:cons ':successful (successful msg))
    (cl:cons ':observations (observations msg))
))

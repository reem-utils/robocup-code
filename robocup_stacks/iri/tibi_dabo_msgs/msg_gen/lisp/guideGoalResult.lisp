; Auto-generated. Do not edit!


(cl:in-package tibi_dabo_msgs-msg)


;//! \htmlinclude guideGoalResult.msg.html

(cl:defclass <guideGoalResult> (roslisp-msg-protocol:ros-message)
  ((result_code
    :reader result_code
    :initarg :result_code
    :type cl:integer
    :initform 0)
   (result_type
    :reader result_type
    :initarg :result_type
    :type cl:string
    :initform ""))
)

(cl:defclass guideGoalResult (<guideGoalResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <guideGoalResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'guideGoalResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tibi_dabo_msgs-msg:<guideGoalResult> is deprecated: use tibi_dabo_msgs-msg:guideGoalResult instead.")))

(cl:ensure-generic-function 'result_code-val :lambda-list '(m))
(cl:defmethod result_code-val ((m <guideGoalResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:result_code-val is deprecated.  Use tibi_dabo_msgs-msg:result_code instead.")
  (result_code m))

(cl:ensure-generic-function 'result_type-val :lambda-list '(m))
(cl:defmethod result_type-val ((m <guideGoalResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:result_type-val is deprecated.  Use tibi_dabo_msgs-msg:result_type instead.")
  (result_type m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <guideGoalResult>) ostream)
  "Serializes a message object of type '<guideGoalResult>"
  (cl:let* ((signed (cl:slot-value msg 'result_code)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'result_type))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'result_type))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <guideGoalResult>) istream)
  "Deserializes a message object of type '<guideGoalResult>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result_code) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'result_type) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'result_type) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<guideGoalResult>)))
  "Returns string type for a message object of type '<guideGoalResult>"
  "tibi_dabo_msgs/guideGoalResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'guideGoalResult)))
  "Returns string type for a message object of type 'guideGoalResult"
  "tibi_dabo_msgs/guideGoalResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<guideGoalResult>)))
  "Returns md5sum for a message object of type '<guideGoalResult>"
  "2454c0379328f65ed8da186dfdff41ca")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'guideGoalResult)))
  "Returns md5sum for a message object of type 'guideGoalResult"
  "2454c0379328f65ed8da186dfdff41ca")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<guideGoalResult>)))
  "Returns full string definition for message of type '<guideGoalResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%int32    result_code~%string   result_type~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'guideGoalResult)))
  "Returns full string definition for message of type 'guideGoalResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%int32    result_code~%string   result_type~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <guideGoalResult>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'result_type))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <guideGoalResult>))
  "Converts a ROS message object to a list"
  (cl:list 'guideGoalResult
    (cl:cons ':result_code (result_code msg))
    (cl:cons ':result_type (result_type msg))
))

; Auto-generated. Do not edit!


(cl:in-package gpsrSoar-msg)


;//! \htmlinclude gpsrActionResult.msg.html

(cl:defclass <gpsrActionResult> (roslisp-msg-protocol:ros-message)
  ((outcome
    :reader outcome
    :initarg :outcome
    :type cl:string
    :initform ""))
)

(cl:defclass gpsrActionResult (<gpsrActionResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <gpsrActionResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'gpsrActionResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gpsrSoar-msg:<gpsrActionResult> is deprecated: use gpsrSoar-msg:gpsrActionResult instead.")))

(cl:ensure-generic-function 'outcome-val :lambda-list '(m))
(cl:defmethod outcome-val ((m <gpsrActionResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsrSoar-msg:outcome-val is deprecated.  Use gpsrSoar-msg:outcome instead.")
  (outcome m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <gpsrActionResult>) ostream)
  "Serializes a message object of type '<gpsrActionResult>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'outcome))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'outcome))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <gpsrActionResult>) istream)
  "Deserializes a message object of type '<gpsrActionResult>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'outcome) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'outcome) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<gpsrActionResult>)))
  "Returns string type for a message object of type '<gpsrActionResult>"
  "gpsrSoar/gpsrActionResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'gpsrActionResult)))
  "Returns string type for a message object of type 'gpsrActionResult"
  "gpsrSoar/gpsrActionResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<gpsrActionResult>)))
  "Returns md5sum for a message object of type '<gpsrActionResult>"
  "2b95071cca675b3d5b80ad0bdaf20389")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'gpsrActionResult)))
  "Returns md5sum for a message object of type 'gpsrActionResult"
  "2b95071cca675b3d5b80ad0bdaf20389")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<gpsrActionResult>)))
  "Returns full string definition for message of type '<gpsrActionResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%string   outcome~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'gpsrActionResult)))
  "Returns full string definition for message of type 'gpsrActionResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%string   outcome~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <gpsrActionResult>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'outcome))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <gpsrActionResult>))
  "Converts a ROS message object to a list"
  (cl:list 'gpsrActionResult
    (cl:cons ':outcome (outcome msg))
))

; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-msg)


;//! \htmlinclude voiceRecognitionAnswer.msg.html

(cl:defclass <voiceRecognitionAnswer> (roslisp-msg-protocol:ros-message)
  ((code
    :reader code
    :initarg :code
    :type cl:integer
    :initform 0)
   (answer
    :reader answer
    :initarg :answer
    :type cl:string
    :initform ""))
)

(cl:defclass voiceRecognitionAnswer (<voiceRecognitionAnswer>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <voiceRecognitionAnswer>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'voiceRecognitionAnswer)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-msg:<voiceRecognitionAnswer> is deprecated: use iri_perception_msgs-msg:voiceRecognitionAnswer instead.")))

(cl:ensure-generic-function 'code-val :lambda-list '(m))
(cl:defmethod code-val ((m <voiceRecognitionAnswer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:code-val is deprecated.  Use iri_perception_msgs-msg:code instead.")
  (code m))

(cl:ensure-generic-function 'answer-val :lambda-list '(m))
(cl:defmethod answer-val ((m <voiceRecognitionAnswer>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:answer-val is deprecated.  Use iri_perception_msgs-msg:answer instead.")
  (answer m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <voiceRecognitionAnswer>) ostream)
  "Serializes a message object of type '<voiceRecognitionAnswer>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'code)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'code)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'code)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'code)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'answer))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'answer))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <voiceRecognitionAnswer>) istream)
  "Deserializes a message object of type '<voiceRecognitionAnswer>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'code)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'code)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'code)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'code)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'answer) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'answer) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<voiceRecognitionAnswer>)))
  "Returns string type for a message object of type '<voiceRecognitionAnswer>"
  "iri_perception_msgs/voiceRecognitionAnswer")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'voiceRecognitionAnswer)))
  "Returns string type for a message object of type 'voiceRecognitionAnswer"
  "iri_perception_msgs/voiceRecognitionAnswer")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<voiceRecognitionAnswer>)))
  "Returns md5sum for a message object of type '<voiceRecognitionAnswer>"
  "8af98cfda9adf4e1ce1333303c85eeb9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'voiceRecognitionAnswer)))
  "Returns md5sum for a message object of type 'voiceRecognitionAnswer"
  "8af98cfda9adf4e1ce1333303c85eeb9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<voiceRecognitionAnswer>)))
  "Returns full string definition for message of type '<voiceRecognitionAnswer>"
  (cl:format cl:nil "uint32 code~%string answer~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'voiceRecognitionAnswer)))
  "Returns full string definition for message of type 'voiceRecognitionAnswer"
  (cl:format cl:nil "uint32 code~%string answer~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <voiceRecognitionAnswer>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'answer))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <voiceRecognitionAnswer>))
  "Converts a ROS message object to a list"
  (cl:list 'voiceRecognitionAnswer
    (cl:cons ':code (code msg))
    (cl:cons ':answer (answer msg))
))

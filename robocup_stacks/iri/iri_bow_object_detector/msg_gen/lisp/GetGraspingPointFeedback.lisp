; Auto-generated. Do not edit!


(cl:in-package iri_bow_object_detector-msg)


;//! \htmlinclude GetGraspingPointFeedback.msg.html

(cl:defclass <GetGraspingPointFeedback> (roslisp-msg-protocol:ros-message)
  ((percent_complete
    :reader percent_complete
    :initarg :percent_complete
    :type cl:float
    :initform 0.0))
)

(cl:defclass GetGraspingPointFeedback (<GetGraspingPointFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GetGraspingPointFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GetGraspingPointFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_bow_object_detector-msg:<GetGraspingPointFeedback> is deprecated: use iri_bow_object_detector-msg:GetGraspingPointFeedback instead.")))

(cl:ensure-generic-function 'percent_complete-val :lambda-list '(m))
(cl:defmethod percent_complete-val ((m <GetGraspingPointFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-msg:percent_complete-val is deprecated.  Use iri_bow_object_detector-msg:percent_complete instead.")
  (percent_complete m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GetGraspingPointFeedback>) ostream)
  "Serializes a message object of type '<GetGraspingPointFeedback>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'percent_complete))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GetGraspingPointFeedback>) istream)
  "Deserializes a message object of type '<GetGraspingPointFeedback>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'percent_complete) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GetGraspingPointFeedback>)))
  "Returns string type for a message object of type '<GetGraspingPointFeedback>"
  "iri_bow_object_detector/GetGraspingPointFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GetGraspingPointFeedback)))
  "Returns string type for a message object of type 'GetGraspingPointFeedback"
  "iri_bow_object_detector/GetGraspingPointFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GetGraspingPointFeedback>)))
  "Returns md5sum for a message object of type '<GetGraspingPointFeedback>"
  "d342375c60a5a58d3bc32664070a1368")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GetGraspingPointFeedback)))
  "Returns md5sum for a message object of type 'GetGraspingPointFeedback"
  "d342375c60a5a58d3bc32664070a1368")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GetGraspingPointFeedback>)))
  "Returns full string definition for message of type '<GetGraspingPointFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define a feedback message~%float32 percent_complete~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GetGraspingPointFeedback)))
  "Returns full string definition for message of type 'GetGraspingPointFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define a feedback message~%float32 percent_complete~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GetGraspingPointFeedback>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GetGraspingPointFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'GetGraspingPointFeedback
    (cl:cons ':percent_complete (percent_complete msg))
))

; Auto-generated. Do not edit!


(cl:in-package iri_door_detector-msg)


;//! \htmlinclude FindADoorFeedback.msg.html

(cl:defclass <FindADoorFeedback> (roslisp-msg-protocol:ros-message)
  ((searching
    :reader searching
    :initarg :searching
    :type cl:fixnum
    :initform 0))
)

(cl:defclass FindADoorFeedback (<FindADoorFeedback>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <FindADoorFeedback>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'FindADoorFeedback)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_door_detector-msg:<FindADoorFeedback> is deprecated: use iri_door_detector-msg:FindADoorFeedback instead.")))

(cl:ensure-generic-function 'searching-val :lambda-list '(m))
(cl:defmethod searching-val ((m <FindADoorFeedback>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_door_detector-msg:searching-val is deprecated.  Use iri_door_detector-msg:searching instead.")
  (searching m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <FindADoorFeedback>) ostream)
  "Serializes a message object of type '<FindADoorFeedback>"
  (cl:let* ((signed (cl:slot-value msg 'searching)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <FindADoorFeedback>) istream)
  "Deserializes a message object of type '<FindADoorFeedback>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'searching) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<FindADoorFeedback>)))
  "Returns string type for a message object of type '<FindADoorFeedback>"
  "iri_door_detector/FindADoorFeedback")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'FindADoorFeedback)))
  "Returns string type for a message object of type 'FindADoorFeedback"
  "iri_door_detector/FindADoorFeedback")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<FindADoorFeedback>)))
  "Returns md5sum for a message object of type '<FindADoorFeedback>"
  "4274b685fb21d0a271aa2b0b6878fd96")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'FindADoorFeedback)))
  "Returns md5sum for a message object of type 'FindADoorFeedback"
  "4274b685fb21d0a271aa2b0b6878fd96")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<FindADoorFeedback>)))
  "Returns full string definition for message of type '<FindADoorFeedback>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define a feedback message~%int8 searching~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'FindADoorFeedback)))
  "Returns full string definition for message of type 'FindADoorFeedback"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Define a feedback message~%int8 searching~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <FindADoorFeedback>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <FindADoorFeedback>))
  "Converts a ROS message object to a list"
  (cl:list 'FindADoorFeedback
    (cl:cons ':searching (searching msg))
))

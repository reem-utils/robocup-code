; Auto-generated. Do not edit!


(cl:in-package iri_bow_object_detector-msg)


;//! \htmlinclude ObjectBox.msg.html

(cl:defclass <ObjectBox> (roslisp-msg-protocol:ros-message)
  ((point1
    :reader point1
    :initarg :point1
    :type iri_perception_msgs-msg:ImagePoint
    :initform (cl:make-instance 'iri_perception_msgs-msg:ImagePoint))
   (point2
    :reader point2
    :initarg :point2
    :type iri_perception_msgs-msg:ImagePoint
    :initform (cl:make-instance 'iri_perception_msgs-msg:ImagePoint))
   (value
    :reader value
    :initarg :value
    :type cl:float
    :initform 0.0))
)

(cl:defclass ObjectBox (<ObjectBox>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectBox>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectBox)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_bow_object_detector-msg:<ObjectBox> is deprecated: use iri_bow_object_detector-msg:ObjectBox instead.")))

(cl:ensure-generic-function 'point1-val :lambda-list '(m))
(cl:defmethod point1-val ((m <ObjectBox>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-msg:point1-val is deprecated.  Use iri_bow_object_detector-msg:point1 instead.")
  (point1 m))

(cl:ensure-generic-function 'point2-val :lambda-list '(m))
(cl:defmethod point2-val ((m <ObjectBox>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-msg:point2-val is deprecated.  Use iri_bow_object_detector-msg:point2 instead.")
  (point2 m))

(cl:ensure-generic-function 'value-val :lambda-list '(m))
(cl:defmethod value-val ((m <ObjectBox>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-msg:value-val is deprecated.  Use iri_bow_object_detector-msg:value instead.")
  (value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectBox>) ostream)
  "Serializes a message object of type '<ObjectBox>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point1) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point2) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'value))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectBox>) istream)
  "Deserializes a message object of type '<ObjectBox>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point1) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point2) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'value) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectBox>)))
  "Returns string type for a message object of type '<ObjectBox>"
  "iri_bow_object_detector/ObjectBox")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectBox)))
  "Returns string type for a message object of type 'ObjectBox"
  "iri_bow_object_detector/ObjectBox")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectBox>)))
  "Returns md5sum for a message object of type '<ObjectBox>"
  "3b124018a1260659fa76923e9a54718c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectBox)))
  "Returns md5sum for a message object of type 'ObjectBox"
  "3b124018a1260659fa76923e9a54718c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectBox>)))
  "Returns full string definition for message of type '<ObjectBox>"
  (cl:format cl:nil "iri_perception_msgs/ImagePoint point1~%iri_perception_msgs/ImagePoint point2~%float32 value~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectBox)))
  "Returns full string definition for message of type 'ObjectBox"
  (cl:format cl:nil "iri_perception_msgs/ImagePoint point1~%iri_perception_msgs/ImagePoint point2~%float32 value~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectBox>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point1))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point2))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectBox>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectBox
    (cl:cons ':point1 (point1 msg))
    (cl:cons ':point2 (point2 msg))
    (cl:cons ':value (value msg))
))

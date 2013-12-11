; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-msg)


;//! \htmlinclude GeoVwSet.msg.html

(cl:defclass <GeoVwSet> (roslisp-msg-protocol:ros-message)
  ((geo_vws
    :reader geo_vws
    :initarg :geo_vws
    :type (cl:vector iri_perception_msgs-msg:GeoVw)
   :initform (cl:make-array 0 :element-type 'iri_perception_msgs-msg:GeoVw :initial-element (cl:make-instance 'iri_perception_msgs-msg:GeoVw))))
)

(cl:defclass GeoVwSet (<GeoVwSet>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GeoVwSet>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GeoVwSet)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-msg:<GeoVwSet> is deprecated: use iri_perception_msgs-msg:GeoVwSet instead.")))

(cl:ensure-generic-function 'geo_vws-val :lambda-list '(m))
(cl:defmethod geo_vws-val ((m <GeoVwSet>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:geo_vws-val is deprecated.  Use iri_perception_msgs-msg:geo_vws instead.")
  (geo_vws m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GeoVwSet>) ostream)
  "Serializes a message object of type '<GeoVwSet>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'geo_vws))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'geo_vws))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GeoVwSet>) istream)
  "Deserializes a message object of type '<GeoVwSet>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'geo_vws) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'geo_vws)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'iri_perception_msgs-msg:GeoVw))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GeoVwSet>)))
  "Returns string type for a message object of type '<GeoVwSet>"
  "iri_perception_msgs/GeoVwSet")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVwSet)))
  "Returns string type for a message object of type 'GeoVwSet"
  "iri_perception_msgs/GeoVwSet")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GeoVwSet>)))
  "Returns md5sum for a message object of type '<GeoVwSet>"
  "b756dd2b9516b315bb183bf5d4030e0b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GeoVwSet)))
  "Returns md5sum for a message object of type 'GeoVwSet"
  "b756dd2b9516b315bb183bf5d4030e0b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GeoVwSet>)))
  "Returns full string definition for message of type '<GeoVwSet>"
  (cl:format cl:nil "iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GeoVwSet)))
  "Returns full string definition for message of type 'GeoVwSet"
  (cl:format cl:nil "iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GeoVwSet>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'geo_vws) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GeoVwSet>))
  "Converts a ROS message object to a list"
  (cl:list 'GeoVwSet
    (cl:cons ':geo_vws (geo_vws msg))
))

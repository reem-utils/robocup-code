; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-msg)


;//! \htmlinclude ImagePoint.msg.html

(cl:defclass <ImagePoint> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0))
)

(cl:defclass ImagePoint (<ImagePoint>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImagePoint>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImagePoint)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-msg:<ImagePoint> is deprecated: use iri_perception_msgs-msg:ImagePoint instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <ImagePoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:x-val is deprecated.  Use iri_perception_msgs-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <ImagePoint>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:y-val is deprecated.  Use iri_perception_msgs-msg:y instead.")
  (y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImagePoint>) ostream)
  "Serializes a message object of type '<ImagePoint>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'y)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImagePoint>) istream)
  "Deserializes a message object of type '<ImagePoint>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'y)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImagePoint>)))
  "Returns string type for a message object of type '<ImagePoint>"
  "iri_perception_msgs/ImagePoint")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImagePoint)))
  "Returns string type for a message object of type 'ImagePoint"
  "iri_perception_msgs/ImagePoint")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImagePoint>)))
  "Returns md5sum for a message object of type '<ImagePoint>"
  "64be90712af6ea79ae6f103da824ffcf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImagePoint)))
  "Returns md5sum for a message object of type 'ImagePoint"
  "64be90712af6ea79ae6f103da824ffcf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImagePoint>)))
  "Returns full string definition for message of type '<ImagePoint>"
  (cl:format cl:nil "uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImagePoint)))
  "Returns full string definition for message of type 'ImagePoint"
  (cl:format cl:nil "uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImagePoint>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImagePoint>))
  "Converts a ROS message object to a list"
  (cl:list 'ImagePoint
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
))

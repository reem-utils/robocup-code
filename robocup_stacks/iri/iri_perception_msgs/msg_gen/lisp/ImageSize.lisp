; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-msg)


;//! \htmlinclude ImageSize.msg.html

(cl:defclass <ImageSize> (roslisp-msg-protocol:ros-message)
  ((width
    :reader width
    :initarg :width
    :type cl:integer
    :initform 0)
   (height
    :reader height
    :initarg :height
    :type cl:integer
    :initform 0))
)

(cl:defclass ImageSize (<ImageSize>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImageSize>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImageSize)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-msg:<ImageSize> is deprecated: use iri_perception_msgs-msg:ImageSize instead.")))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <ImageSize>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:width-val is deprecated.  Use iri_perception_msgs-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'height-val :lambda-list '(m))
(cl:defmethod height-val ((m <ImageSize>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:height-val is deprecated.  Use iri_perception_msgs-msg:height instead.")
  (height m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImageSize>) ostream)
  "Serializes a message object of type '<ImageSize>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'width)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'height)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'height)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImageSize>) istream)
  "Deserializes a message object of type '<ImageSize>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'width)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'height)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'height)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImageSize>)))
  "Returns string type for a message object of type '<ImageSize>"
  "iri_perception_msgs/ImageSize")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImageSize)))
  "Returns string type for a message object of type 'ImageSize"
  "iri_perception_msgs/ImageSize")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImageSize>)))
  "Returns md5sum for a message object of type '<ImageSize>"
  "d00b1659f7d843bad3388af53e042f94")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImageSize)))
  "Returns md5sum for a message object of type 'ImageSize"
  "d00b1659f7d843bad3388af53e042f94")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImageSize>)))
  "Returns full string definition for message of type '<ImageSize>"
  (cl:format cl:nil "uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImageSize)))
  "Returns full string definition for message of type 'ImageSize"
  (cl:format cl:nil "uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImageSize>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImageSize>))
  "Converts a ROS message object to a list"
  (cl:list 'ImageSize
    (cl:cons ':width (width msg))
    (cl:cons ':height (height msg))
))

; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude Ellipse.msg.html

(cl:defclass <Ellipse> (roslisp-msg-protocol:ros-message)
  ((center
    :reader center
    :initarg :center
    :type iri_perception_msgs-msg:ImagePoint
    :initform (cl:make-instance 'iri_perception_msgs-msg:ImagePoint))
   (size
    :reader size
    :initarg :size
    :type iri_perception_msgs-msg:ImageSize
    :initform (cl:make-instance 'iri_perception_msgs-msg:ImageSize))
   (angle
    :reader angle
    :initarg :angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass Ellipse (<Ellipse>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Ellipse>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Ellipse)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<Ellipse> is deprecated: use estirabot_msgs-msg:Ellipse instead.")))

(cl:ensure-generic-function 'center-val :lambda-list '(m))
(cl:defmethod center-val ((m <Ellipse>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:center-val is deprecated.  Use estirabot_msgs-msg:center instead.")
  (center m))

(cl:ensure-generic-function 'size-val :lambda-list '(m))
(cl:defmethod size-val ((m <Ellipse>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:size-val is deprecated.  Use estirabot_msgs-msg:size instead.")
  (size m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <Ellipse>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:angle-val is deprecated.  Use estirabot_msgs-msg:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Ellipse>) ostream)
  "Serializes a message object of type '<Ellipse>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'center) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'size) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Ellipse>) istream)
  "Deserializes a message object of type '<Ellipse>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'center) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'size) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angle) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Ellipse>)))
  "Returns string type for a message object of type '<Ellipse>"
  "estirabot_msgs/Ellipse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Ellipse)))
  "Returns string type for a message object of type 'Ellipse"
  "estirabot_msgs/Ellipse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Ellipse>)))
  "Returns md5sum for a message object of type '<Ellipse>"
  "5ea4b3e7d2b823108215d29388898442")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Ellipse)))
  "Returns md5sum for a message object of type 'Ellipse"
  "5ea4b3e7d2b823108215d29388898442")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Ellipse>)))
  "Returns full string definition for message of type '<Ellipse>"
  (cl:format cl:nil "iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Ellipse)))
  "Returns full string definition for message of type 'Ellipse"
  (cl:format cl:nil "iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Ellipse>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'center))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'size))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Ellipse>))
  "Converts a ROS message object to a list"
  (cl:list 'Ellipse
    (cl:cons ':center (center msg))
    (cl:cons ':size (size msg))
    (cl:cons ':angle (angle msg))
))

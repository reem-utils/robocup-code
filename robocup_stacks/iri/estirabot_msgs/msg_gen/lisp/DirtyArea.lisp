; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude DirtyArea.msg.html

(cl:defclass <DirtyArea> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (ellipse
    :reader ellipse
    :initarg :ellipse
    :type estirabot_msgs-msg:Ellipse
    :initform (cl:make-instance 'estirabot_msgs-msg:Ellipse))
   (sparse
    :reader sparse
    :initarg :sparse
    :type cl:boolean
    :initform cl:nil)
   (area
    :reader area
    :initarg :area
    :type cl:fixnum
    :initform 0)
   (shape
    :reader shape
    :initarg :shape
    :type cl:fixnum
    :initform 0))
)

(cl:defclass DirtyArea (<DirtyArea>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DirtyArea>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DirtyArea)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<DirtyArea> is deprecated: use estirabot_msgs-msg:DirtyArea instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <DirtyArea>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:id-val is deprecated.  Use estirabot_msgs-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'ellipse-val :lambda-list '(m))
(cl:defmethod ellipse-val ((m <DirtyArea>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:ellipse-val is deprecated.  Use estirabot_msgs-msg:ellipse instead.")
  (ellipse m))

(cl:ensure-generic-function 'sparse-val :lambda-list '(m))
(cl:defmethod sparse-val ((m <DirtyArea>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:sparse-val is deprecated.  Use estirabot_msgs-msg:sparse instead.")
  (sparse m))

(cl:ensure-generic-function 'area-val :lambda-list '(m))
(cl:defmethod area-val ((m <DirtyArea>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:area-val is deprecated.  Use estirabot_msgs-msg:area instead.")
  (area m))

(cl:ensure-generic-function 'shape-val :lambda-list '(m))
(cl:defmethod shape-val ((m <DirtyArea>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:shape-val is deprecated.  Use estirabot_msgs-msg:shape instead.")
  (shape m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DirtyArea>) ostream)
  "Serializes a message object of type '<DirtyArea>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ellipse) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'sparse) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'area)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'shape)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DirtyArea>) istream)
  "Deserializes a message object of type '<DirtyArea>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ellipse) istream)
    (cl:setf (cl:slot-value msg 'sparse) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'area)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'shape)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DirtyArea>)))
  "Returns string type for a message object of type '<DirtyArea>"
  "estirabot_msgs/DirtyArea")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DirtyArea)))
  "Returns string type for a message object of type 'DirtyArea"
  "estirabot_msgs/DirtyArea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DirtyArea>)))
  "Returns md5sum for a message object of type '<DirtyArea>"
  "2b156136a0460cfb7965b803a38c7cc1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DirtyArea)))
  "Returns md5sum for a message object of type 'DirtyArea"
  "2b156136a0460cfb7965b803a38c7cc1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DirtyArea>)))
  "Returns full string definition for message of type '<DirtyArea>"
  (cl:format cl:nil "int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DirtyArea)))
  "Returns full string definition for message of type 'DirtyArea"
  (cl:format cl:nil "int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DirtyArea>))
  (cl:+ 0
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ellipse))
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DirtyArea>))
  "Converts a ROS message object to a list"
  (cl:list 'DirtyArea
    (cl:cons ':id (id msg))
    (cl:cons ':ellipse (ellipse msg))
    (cl:cons ':sparse (sparse msg))
    (cl:cons ':area (area msg))
    (cl:cons ':shape (shape msg))
))

; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-msg)


;//! \htmlinclude GeoVw.msg.html

(cl:defclass <GeoVw> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:integer
    :initform 0)
   (y
    :reader y
    :initarg :y
    :type cl:integer
    :initform 0)
   (word
    :reader word
    :initarg :word
    :type cl:integer
    :initform 0))
)

(cl:defclass GeoVw (<GeoVw>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GeoVw>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GeoVw)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-msg:<GeoVw> is deprecated: use iri_perception_msgs-msg:GeoVw instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <GeoVw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:x-val is deprecated.  Use iri_perception_msgs-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <GeoVw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:y-val is deprecated.  Use iri_perception_msgs-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'word-val :lambda-list '(m))
(cl:defmethod word-val ((m <GeoVw>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:word-val is deprecated.  Use iri_perception_msgs-msg:word instead.")
  (word m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GeoVw>) ostream)
  "Serializes a message object of type '<GeoVw>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'x)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'y)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'word)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'word)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'word)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'word)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GeoVw>) istream)
  "Deserializes a message object of type '<GeoVw>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'x)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'y)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'word)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'word)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'word)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'word)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GeoVw>)))
  "Returns string type for a message object of type '<GeoVw>"
  "iri_perception_msgs/GeoVw")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVw)))
  "Returns string type for a message object of type 'GeoVw"
  "iri_perception_msgs/GeoVw")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GeoVw>)))
  "Returns md5sum for a message object of type '<GeoVw>"
  "060e8b4afb3efb459a6ff75a4ab5f685")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GeoVw)))
  "Returns md5sum for a message object of type 'GeoVw"
  "060e8b4afb3efb459a6ff75a4ab5f685")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GeoVw>)))
  "Returns full string definition for message of type '<GeoVw>"
  (cl:format cl:nil "uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GeoVw)))
  "Returns full string definition for message of type 'GeoVw"
  (cl:format cl:nil "uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GeoVw>))
  (cl:+ 0
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GeoVw>))
  "Converts a ROS message object to a list"
  (cl:list 'GeoVw
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':word (word msg))
))

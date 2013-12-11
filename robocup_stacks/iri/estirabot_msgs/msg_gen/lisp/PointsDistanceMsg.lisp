; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude PointsDistanceMsg.msg.html

(cl:defclass <PointsDistanceMsg> (roslisp-msg-protocol:ros-message)
  ((origIdx
    :reader origIdx
    :initarg :origIdx
    :type cl:integer
    :initform 0)
   (dstIdx
    :reader dstIdx
    :initarg :dstIdx
    :type cl:integer
    :initform 0)
   (distance
    :reader distance
    :initarg :distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass PointsDistanceMsg (<PointsDistanceMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PointsDistanceMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PointsDistanceMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<PointsDistanceMsg> is deprecated: use estirabot_msgs-msg:PointsDistanceMsg instead.")))

(cl:ensure-generic-function 'origIdx-val :lambda-list '(m))
(cl:defmethod origIdx-val ((m <PointsDistanceMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:origIdx-val is deprecated.  Use estirabot_msgs-msg:origIdx instead.")
  (origIdx m))

(cl:ensure-generic-function 'dstIdx-val :lambda-list '(m))
(cl:defmethod dstIdx-val ((m <PointsDistanceMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:dstIdx-val is deprecated.  Use estirabot_msgs-msg:dstIdx instead.")
  (dstIdx m))

(cl:ensure-generic-function 'distance-val :lambda-list '(m))
(cl:defmethod distance-val ((m <PointsDistanceMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:distance-val is deprecated.  Use estirabot_msgs-msg:distance instead.")
  (distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PointsDistanceMsg>) ostream)
  "Serializes a message object of type '<PointsDistanceMsg>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'origIdx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'origIdx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'origIdx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'origIdx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dstIdx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'dstIdx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'dstIdx)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'dstIdx)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PointsDistanceMsg>) istream)
  "Deserializes a message object of type '<PointsDistanceMsg>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'origIdx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'origIdx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'origIdx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'origIdx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dstIdx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'dstIdx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'dstIdx)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'dstIdx)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'distance) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PointsDistanceMsg>)))
  "Returns string type for a message object of type '<PointsDistanceMsg>"
  "estirabot_msgs/PointsDistanceMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PointsDistanceMsg)))
  "Returns string type for a message object of type 'PointsDistanceMsg"
  "estirabot_msgs/PointsDistanceMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PointsDistanceMsg>)))
  "Returns md5sum for a message object of type '<PointsDistanceMsg>"
  "6f7e654975217ecc288f9361563bb698")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PointsDistanceMsg)))
  "Returns md5sum for a message object of type 'PointsDistanceMsg"
  "6f7e654975217ecc288f9361563bb698")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PointsDistanceMsg>)))
  "Returns full string definition for message of type '<PointsDistanceMsg>"
  (cl:format cl:nil "uint32 origIdx~%uint32 dstIdx~%float64 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PointsDistanceMsg)))
  "Returns full string definition for message of type 'PointsDistanceMsg"
  (cl:format cl:nil "uint32 origIdx~%uint32 dstIdx~%float64 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PointsDistanceMsg>))
  (cl:+ 0
     4
     4
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PointsDistanceMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'PointsDistanceMsg
    (cl:cons ':origIdx (origIdx msg))
    (cl:cons ':dstIdx (dstIdx msg))
    (cl:cons ':distance (distance msg))
))

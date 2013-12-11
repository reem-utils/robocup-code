; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude pose_move-request.msg.html

(cl:defclass <pose_move-request> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (vel
    :reader vel
    :initarg :vel
    :type cl:float
    :initform 0.0)
   (acc
    :reader acc
    :initarg :acc
    :type cl:float
    :initform 0.0))
)

(cl:defclass pose_move-request (<pose_move-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pose_move-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pose_move-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<pose_move-request> is deprecated: use iri_wam_common_msgs-srv:pose_move-request instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <pose_move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:pose-val is deprecated.  Use iri_wam_common_msgs-srv:pose instead.")
  (pose m))

(cl:ensure-generic-function 'vel-val :lambda-list '(m))
(cl:defmethod vel-val ((m <pose_move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:vel-val is deprecated.  Use iri_wam_common_msgs-srv:vel instead.")
  (vel m))

(cl:ensure-generic-function 'acc-val :lambda-list '(m))
(cl:defmethod acc-val ((m <pose_move-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:acc-val is deprecated.  Use iri_wam_common_msgs-srv:acc instead.")
  (acc m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pose_move-request>) ostream)
  "Serializes a message object of type '<pose_move-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'vel))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'acc))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pose_move-request>) istream)
  "Deserializes a message object of type '<pose_move-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'vel) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'acc) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pose_move-request>)))
  "Returns string type for a service object of type '<pose_move-request>"
  "iri_wam_common_msgs/pose_moveRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pose_move-request)))
  "Returns string type for a service object of type 'pose_move-request"
  "iri_wam_common_msgs/pose_moveRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pose_move-request>)))
  "Returns md5sum for a message object of type '<pose_move-request>"
  "13150f5749ba86f3ea97eb7613e22e0a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pose_move-request)))
  "Returns md5sum for a message object of type 'pose_move-request"
  "13150f5749ba86f3ea97eb7613e22e0a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pose_move-request>)))
  "Returns full string definition for message of type '<pose_move-request>"
  (cl:format cl:nil "geometry_msgs/Pose pose~%float64 vel~%float64 acc~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pose_move-request)))
  "Returns full string definition for message of type 'pose_move-request"
  (cl:format cl:nil "geometry_msgs/Pose pose~%float64 vel~%float64 acc~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pose_move-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pose_move-request>))
  "Converts a ROS message object to a list"
  (cl:list 'pose_move-request
    (cl:cons ':pose (pose msg))
    (cl:cons ':vel (vel msg))
    (cl:cons ':acc (acc msg))
))
;//! \htmlinclude pose_move-response.msg.html

(cl:defclass <pose_move-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:fixnum
    :initform 0))
)

(cl:defclass pose_move-response (<pose_move-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <pose_move-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'pose_move-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<pose_move-response> is deprecated: use iri_wam_common_msgs-srv:pose_move-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <pose_move-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:success-val is deprecated.  Use iri_wam_common_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <pose_move-response>) ostream)
  "Serializes a message object of type '<pose_move-response>"
  (cl:let* ((signed (cl:slot-value msg 'success)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <pose_move-response>) istream)
  "Deserializes a message object of type '<pose_move-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'success) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<pose_move-response>)))
  "Returns string type for a service object of type '<pose_move-response>"
  "iri_wam_common_msgs/pose_moveResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pose_move-response)))
  "Returns string type for a service object of type 'pose_move-response"
  "iri_wam_common_msgs/pose_moveResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<pose_move-response>)))
  "Returns md5sum for a message object of type '<pose_move-response>"
  "13150f5749ba86f3ea97eb7613e22e0a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'pose_move-response)))
  "Returns md5sum for a message object of type 'pose_move-response"
  "13150f5749ba86f3ea97eb7613e22e0a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<pose_move-response>)))
  "Returns full string definition for message of type '<pose_move-response>"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'pose_move-response)))
  "Returns full string definition for message of type 'pose_move-response"
  (cl:format cl:nil "int8 success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <pose_move-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <pose_move-response>))
  "Converts a ROS message object to a list"
  (cl:list 'pose_move-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'pose_move)))
  'pose_move-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'pose_move)))
  'pose_move-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'pose_move)))
  "Returns string type for a service object of type '<pose_move>"
  "iri_wam_common_msgs/pose_move")
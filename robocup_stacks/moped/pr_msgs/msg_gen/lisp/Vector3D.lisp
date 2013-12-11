; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude Vector3D.msg.html

(cl:defclass <Vector3D> (roslisp-msg-protocol:ros-message)
  ((axis1
    :reader axis1
    :initarg :axis1
    :type cl:float
    :initform 0.0)
   (axis2
    :reader axis2
    :initarg :axis2
    :type cl:float
    :initform 0.0)
   (axis3
    :reader axis3
    :initarg :axis3
    :type cl:float
    :initform 0.0))
)

(cl:defclass Vector3D (<Vector3D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Vector3D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Vector3D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<Vector3D> is deprecated: use pr_msgs-msg:Vector3D instead.")))

(cl:ensure-generic-function 'axis1-val :lambda-list '(m))
(cl:defmethod axis1-val ((m <Vector3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:axis1-val is deprecated.  Use pr_msgs-msg:axis1 instead.")
  (axis1 m))

(cl:ensure-generic-function 'axis2-val :lambda-list '(m))
(cl:defmethod axis2-val ((m <Vector3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:axis2-val is deprecated.  Use pr_msgs-msg:axis2 instead.")
  (axis2 m))

(cl:ensure-generic-function 'axis3-val :lambda-list '(m))
(cl:defmethod axis3-val ((m <Vector3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:axis3-val is deprecated.  Use pr_msgs-msg:axis3 instead.")
  (axis3 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Vector3D>) ostream)
  "Serializes a message object of type '<Vector3D>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'axis1))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'axis2))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'axis3))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Vector3D>) istream)
  "Deserializes a message object of type '<Vector3D>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'axis1) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'axis2) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'axis3) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Vector3D>)))
  "Returns string type for a message object of type '<Vector3D>"
  "pr_msgs/Vector3D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Vector3D)))
  "Returns string type for a message object of type 'Vector3D"
  "pr_msgs/Vector3D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Vector3D>)))
  "Returns md5sum for a message object of type '<Vector3D>"
  "ebd79d666ce8461ba522577a93648fee")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Vector3D)))
  "Returns md5sum for a message object of type 'Vector3D"
  "ebd79d666ce8461ba522577a93648fee")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Vector3D>)))
  "Returns full string definition for message of type '<Vector3D>"
  (cl:format cl:nil "float64 axis1~%float64 axis2~%float64 axis3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Vector3D)))
  "Returns full string definition for message of type 'Vector3D"
  (cl:format cl:nil "float64 axis1~%float64 axis2~%float64 axis3~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Vector3D>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Vector3D>))
  "Converts a ROS message object to a list"
  (cl:list 'Vector3D
    (cl:cons ':axis1 (axis1 msg))
    (cl:cons ':axis2 (axis2 msg))
    (cl:cons ':axis3 (axis3 msg))
))

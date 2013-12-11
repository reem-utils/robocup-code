; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude TraversedEllipses.msg.html

(cl:defclass <TraversedEllipses> (roslisp-msg-protocol:ros-message)
  ((idx1
    :reader idx1
    :initarg :idx1
    :type cl:integer
    :initform 0)
   (idx2
    :reader idx2
    :initarg :idx2
    :type cl:integer
    :initform 0)
   (traversedIdxs
    :reader traversedIdxs
    :initarg :traversedIdxs
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass TraversedEllipses (<TraversedEllipses>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TraversedEllipses>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TraversedEllipses)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<TraversedEllipses> is deprecated: use estirabot_msgs-msg:TraversedEllipses instead.")))

(cl:ensure-generic-function 'idx1-val :lambda-list '(m))
(cl:defmethod idx1-val ((m <TraversedEllipses>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:idx1-val is deprecated.  Use estirabot_msgs-msg:idx1 instead.")
  (idx1 m))

(cl:ensure-generic-function 'idx2-val :lambda-list '(m))
(cl:defmethod idx2-val ((m <TraversedEllipses>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:idx2-val is deprecated.  Use estirabot_msgs-msg:idx2 instead.")
  (idx2 m))

(cl:ensure-generic-function 'traversedIdxs-val :lambda-list '(m))
(cl:defmethod traversedIdxs-val ((m <TraversedEllipses>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:traversedIdxs-val is deprecated.  Use estirabot_msgs-msg:traversedIdxs instead.")
  (traversedIdxs m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TraversedEllipses>) ostream)
  "Serializes a message object of type '<TraversedEllipses>"
  (cl:let* ((signed (cl:slot-value msg 'idx1)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'idx2)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'traversedIdxs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    ))
   (cl:slot-value msg 'traversedIdxs))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TraversedEllipses>) istream)
  "Deserializes a message object of type '<TraversedEllipses>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'idx1) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'idx2) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'traversedIdxs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'traversedIdxs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TraversedEllipses>)))
  "Returns string type for a message object of type '<TraversedEllipses>"
  "estirabot_msgs/TraversedEllipses")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TraversedEllipses)))
  "Returns string type for a message object of type 'TraversedEllipses"
  "estirabot_msgs/TraversedEllipses")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TraversedEllipses>)))
  "Returns md5sum for a message object of type '<TraversedEllipses>"
  "baffdeb476b4d43dc6469d2a664bf059")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TraversedEllipses)))
  "Returns md5sum for a message object of type 'TraversedEllipses"
  "baffdeb476b4d43dc6469d2a664bf059")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TraversedEllipses>)))
  "Returns full string definition for message of type '<TraversedEllipses>"
  (cl:format cl:nil "int32 idx1~%int32 idx2~%int32[] traversedIdxs~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TraversedEllipses)))
  "Returns full string definition for message of type 'TraversedEllipses"
  (cl:format cl:nil "int32 idx1~%int32 idx2~%int32[] traversedIdxs~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TraversedEllipses>))
  (cl:+ 0
     4
     4
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'traversedIdxs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TraversedEllipses>))
  "Converts a ROS message object to a list"
  (cl:list 'TraversedEllipses
    (cl:cons ':idx1 (idx1 msg))
    (cl:cons ':idx2 (idx2 msg))
    (cl:cons ':traversedIdxs (traversedIdxs msg))
))

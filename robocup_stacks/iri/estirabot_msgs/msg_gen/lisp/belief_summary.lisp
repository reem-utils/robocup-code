; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude belief_summary.msg.html

(cl:defclass <belief_summary> (roslisp-msg-protocol:ros-message)
  ((num_objects_A
    :reader num_objects_A
    :initarg :num_objects_A
    :type cl:float
    :initform 0.0)
   (uncertainty_A
    :reader uncertainty_A
    :initarg :uncertainty_A
    :type cl:float
    :initform 0.0)
   (num_objects_B
    :reader num_objects_B
    :initarg :num_objects_B
    :type cl:float
    :initform 0.0)
   (uncertainty_B
    :reader uncertainty_B
    :initarg :uncertainty_B
    :type cl:float
    :initform 0.0)
   (uncertainty_total
    :reader uncertainty_total
    :initarg :uncertainty_total
    :type cl:float
    :initform 0.0))
)

(cl:defclass belief_summary (<belief_summary>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <belief_summary>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'belief_summary)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<belief_summary> is deprecated: use estirabot_msgs-msg:belief_summary instead.")))

(cl:ensure-generic-function 'num_objects_A-val :lambda-list '(m))
(cl:defmethod num_objects_A-val ((m <belief_summary>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:num_objects_A-val is deprecated.  Use estirabot_msgs-msg:num_objects_A instead.")
  (num_objects_A m))

(cl:ensure-generic-function 'uncertainty_A-val :lambda-list '(m))
(cl:defmethod uncertainty_A-val ((m <belief_summary>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:uncertainty_A-val is deprecated.  Use estirabot_msgs-msg:uncertainty_A instead.")
  (uncertainty_A m))

(cl:ensure-generic-function 'num_objects_B-val :lambda-list '(m))
(cl:defmethod num_objects_B-val ((m <belief_summary>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:num_objects_B-val is deprecated.  Use estirabot_msgs-msg:num_objects_B instead.")
  (num_objects_B m))

(cl:ensure-generic-function 'uncertainty_B-val :lambda-list '(m))
(cl:defmethod uncertainty_B-val ((m <belief_summary>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:uncertainty_B-val is deprecated.  Use estirabot_msgs-msg:uncertainty_B instead.")
  (uncertainty_B m))

(cl:ensure-generic-function 'uncertainty_total-val :lambda-list '(m))
(cl:defmethod uncertainty_total-val ((m <belief_summary>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:uncertainty_total-val is deprecated.  Use estirabot_msgs-msg:uncertainty_total instead.")
  (uncertainty_total m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <belief_summary>) ostream)
  "Serializes a message object of type '<belief_summary>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'num_objects_A))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'uncertainty_A))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'num_objects_B))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'uncertainty_B))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'uncertainty_total))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <belief_summary>) istream)
  "Deserializes a message object of type '<belief_summary>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'num_objects_A) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'uncertainty_A) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'num_objects_B) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'uncertainty_B) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'uncertainty_total) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<belief_summary>)))
  "Returns string type for a message object of type '<belief_summary>"
  "estirabot_msgs/belief_summary")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'belief_summary)))
  "Returns string type for a message object of type 'belief_summary"
  "estirabot_msgs/belief_summary")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<belief_summary>)))
  "Returns md5sum for a message object of type '<belief_summary>"
  "09535f079069869195fe13351686487e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'belief_summary)))
  "Returns md5sum for a message object of type 'belief_summary"
  "09535f079069869195fe13351686487e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<belief_summary>)))
  "Returns full string definition for message of type '<belief_summary>"
  (cl:format cl:nil "float32 num_objects_A~%float32 uncertainty_A~%float32 num_objects_B~%float32 uncertainty_B~%float32 uncertainty_total~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'belief_summary)))
  "Returns full string definition for message of type 'belief_summary"
  (cl:format cl:nil "float32 num_objects_A~%float32 uncertainty_A~%float32 num_objects_B~%float32 uncertainty_B~%float32 uncertainty_total~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <belief_summary>))
  (cl:+ 0
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <belief_summary>))
  "Converts a ROS message object to a list"
  (cl:list 'belief_summary
    (cl:cons ':num_objects_A (num_objects_A msg))
    (cl:cons ':uncertainty_A (uncertainty_A msg))
    (cl:cons ':num_objects_B (num_objects_B msg))
    (cl:cons ':uncertainty_B (uncertainty_B msg))
    (cl:cons ':uncertainty_total (uncertainty_total msg))
))

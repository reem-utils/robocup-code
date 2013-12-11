; Auto-generated. Do not edit!


(cl:in-package tibi_dabo_msgs-msg)


;//! \htmlinclude battery_status.msg.html

(cl:defclass <battery_status> (roslisp-msg-protocol:ros-message)
  ((voltage
    :reader voltage
    :initarg :voltage
    :type cl:float
    :initform 0.0)
   (temperature
    :reader temperature
    :initarg :temperature
    :type cl:float
    :initform 0.0)
   (status
    :reader status
    :initarg :status
    :type cl:fixnum
    :initform 0)
   (input_current
    :reader input_current
    :initarg :input_current
    :type cl:float
    :initform 0.0)
   (output_current
    :reader output_current
    :initarg :output_current
    :type cl:float
    :initform 0.0)
   (remaining_capacity
    :reader remaining_capacity
    :initarg :remaining_capacity
    :type cl:float
    :initform 0.0)
   (time_to_charged
    :reader time_to_charged
    :initarg :time_to_charged
    :type cl:float
    :initform 0.0)
   (time_to_discharged
    :reader time_to_discharged
    :initarg :time_to_discharged
    :type cl:float
    :initform 0.0))
)

(cl:defclass battery_status (<battery_status>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <battery_status>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'battery_status)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name tibi_dabo_msgs-msg:<battery_status> is deprecated: use tibi_dabo_msgs-msg:battery_status instead.")))

(cl:ensure-generic-function 'voltage-val :lambda-list '(m))
(cl:defmethod voltage-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:voltage-val is deprecated.  Use tibi_dabo_msgs-msg:voltage instead.")
  (voltage m))

(cl:ensure-generic-function 'temperature-val :lambda-list '(m))
(cl:defmethod temperature-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:temperature-val is deprecated.  Use tibi_dabo_msgs-msg:temperature instead.")
  (temperature m))

(cl:ensure-generic-function 'status-val :lambda-list '(m))
(cl:defmethod status-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:status-val is deprecated.  Use tibi_dabo_msgs-msg:status instead.")
  (status m))

(cl:ensure-generic-function 'input_current-val :lambda-list '(m))
(cl:defmethod input_current-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:input_current-val is deprecated.  Use tibi_dabo_msgs-msg:input_current instead.")
  (input_current m))

(cl:ensure-generic-function 'output_current-val :lambda-list '(m))
(cl:defmethod output_current-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:output_current-val is deprecated.  Use tibi_dabo_msgs-msg:output_current instead.")
  (output_current m))

(cl:ensure-generic-function 'remaining_capacity-val :lambda-list '(m))
(cl:defmethod remaining_capacity-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:remaining_capacity-val is deprecated.  Use tibi_dabo_msgs-msg:remaining_capacity instead.")
  (remaining_capacity m))

(cl:ensure-generic-function 'time_to_charged-val :lambda-list '(m))
(cl:defmethod time_to_charged-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:time_to_charged-val is deprecated.  Use tibi_dabo_msgs-msg:time_to_charged instead.")
  (time_to_charged m))

(cl:ensure-generic-function 'time_to_discharged-val :lambda-list '(m))
(cl:defmethod time_to_discharged-val ((m <battery_status>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader tibi_dabo_msgs-msg:time_to_discharged-val is deprecated.  Use tibi_dabo_msgs-msg:time_to_discharged instead.")
  (time_to_discharged m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <battery_status>) ostream)
  "Serializes a message object of type '<battery_status>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'voltage))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'temperature))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'input_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'output_current))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'remaining_capacity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'time_to_charged))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'time_to_discharged))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <battery_status>) istream)
  "Deserializes a message object of type '<battery_status>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'voltage) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'temperature) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'status)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'input_current) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'output_current) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'remaining_capacity) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'time_to_charged) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'time_to_discharged) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<battery_status>)))
  "Returns string type for a message object of type '<battery_status>"
  "tibi_dabo_msgs/battery_status")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'battery_status)))
  "Returns string type for a message object of type 'battery_status"
  "tibi_dabo_msgs/battery_status")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<battery_status>)))
  "Returns md5sum for a message object of type '<battery_status>"
  "9cc10a535f6582725be65cc15269919b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'battery_status)))
  "Returns md5sum for a message object of type 'battery_status"
  "9cc10a535f6582725be65cc15269919b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<battery_status>)))
  "Returns full string definition for message of type '<battery_status>"
  (cl:format cl:nil "float64 voltage~%float64 temperature~%uint8 status~%float64 input_current~%float64 output_current~%float64 remaining_capacity~%float64 time_to_charged~%float64 time_to_discharged~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'battery_status)))
  "Returns full string definition for message of type 'battery_status"
  (cl:format cl:nil "float64 voltage~%float64 temperature~%uint8 status~%float64 input_current~%float64 output_current~%float64 remaining_capacity~%float64 time_to_charged~%float64 time_to_discharged~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <battery_status>))
  (cl:+ 0
     8
     8
     1
     8
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <battery_status>))
  "Converts a ROS message object to a list"
  (cl:list 'battery_status
    (cl:cons ':voltage (voltage msg))
    (cl:cons ':temperature (temperature msg))
    (cl:cons ':status (status msg))
    (cl:cons ':input_current (input_current msg))
    (cl:cons ':output_current (output_current msg))
    (cl:cons ':remaining_capacity (remaining_capacity msg))
    (cl:cons ':time_to_charged (time_to_charged msg))
    (cl:cons ':time_to_discharged (time_to_discharged msg))
))

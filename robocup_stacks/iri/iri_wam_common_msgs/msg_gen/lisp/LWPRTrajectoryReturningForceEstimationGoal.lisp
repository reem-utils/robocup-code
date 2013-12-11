; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-msg)


;//! \htmlinclude LWPRTrajectoryReturningForceEstimationGoal.msg.html

(cl:defclass <LWPRTrajectoryReturningForceEstimationGoal> (roslisp-msg-protocol:ros-message)
  ((model_filename
    :reader model_filename
    :initarg :model_filename
    :type cl:string
    :initform "")
   (points_filename
    :reader points_filename
    :initarg :points_filename
    :type cl:string
    :initform ""))
)

(cl:defclass LWPRTrajectoryReturningForceEstimationGoal (<LWPRTrajectoryReturningForceEstimationGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LWPRTrajectoryReturningForceEstimationGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LWPRTrajectoryReturningForceEstimationGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-msg:<LWPRTrajectoryReturningForceEstimationGoal> is deprecated: use iri_wam_common_msgs-msg:LWPRTrajectoryReturningForceEstimationGoal instead.")))

(cl:ensure-generic-function 'model_filename-val :lambda-list '(m))
(cl:defmethod model_filename-val ((m <LWPRTrajectoryReturningForceEstimationGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:model_filename-val is deprecated.  Use iri_wam_common_msgs-msg:model_filename instead.")
  (model_filename m))

(cl:ensure-generic-function 'points_filename-val :lambda-list '(m))
(cl:defmethod points_filename-val ((m <LWPRTrajectoryReturningForceEstimationGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:points_filename-val is deprecated.  Use iri_wam_common_msgs-msg:points_filename instead.")
  (points_filename m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LWPRTrajectoryReturningForceEstimationGoal>) ostream)
  "Serializes a message object of type '<LWPRTrajectoryReturningForceEstimationGoal>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'model_filename))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'model_filename))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'points_filename))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'points_filename))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LWPRTrajectoryReturningForceEstimationGoal>) istream)
  "Deserializes a message object of type '<LWPRTrajectoryReturningForceEstimationGoal>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'model_filename) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'model_filename) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'points_filename) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'points_filename) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LWPRTrajectoryReturningForceEstimationGoal>)))
  "Returns string type for a message object of type '<LWPRTrajectoryReturningForceEstimationGoal>"
  "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LWPRTrajectoryReturningForceEstimationGoal)))
  "Returns string type for a message object of type 'LWPRTrajectoryReturningForceEstimationGoal"
  "iri_wam_common_msgs/LWPRTrajectoryReturningForceEstimationGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LWPRTrajectoryReturningForceEstimationGoal>)))
  "Returns md5sum for a message object of type '<LWPRTrajectoryReturningForceEstimationGoal>"
  "e44cfc1d1aa91d88d46a6e81769b3050")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LWPRTrajectoryReturningForceEstimationGoal)))
  "Returns md5sum for a message object of type 'LWPRTrajectoryReturningForceEstimationGoal"
  "e44cfc1d1aa91d88d46a6e81769b3050")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LWPRTrajectoryReturningForceEstimationGoal>)))
  "Returns full string definition for message of type '<LWPRTrajectoryReturningForceEstimationGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%string model_filename~%string points_filename~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LWPRTrajectoryReturningForceEstimationGoal)))
  "Returns full string definition for message of type 'LWPRTrajectoryReturningForceEstimationGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# goal~%string model_filename~%string points_filename~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LWPRTrajectoryReturningForceEstimationGoal>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'model_filename))
     4 (cl:length (cl:slot-value msg 'points_filename))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LWPRTrajectoryReturningForceEstimationGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'LWPRTrajectoryReturningForceEstimationGoal
    (cl:cons ':model_filename (model_filename msg))
    (cl:cons ':points_filename (points_filename msg))
))

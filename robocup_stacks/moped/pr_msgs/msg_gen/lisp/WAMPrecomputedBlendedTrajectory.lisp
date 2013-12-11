; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude WAMPrecomputedBlendedTrajectory.msg.html

(cl:defclass <WAMPrecomputedBlendedTrajectory> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:fixnum
    :initform 0)
   (HoldOnStall
    :reader HoldOnStall
    :initarg :HoldOnStall
    :type cl:boolean
    :initform cl:nil)
   (WaitForStart
    :reader WaitForStart
    :initarg :WaitForStart
    :type cl:boolean
    :initform cl:nil)
   (start_position
    :reader start_position
    :initarg :start_position
    :type pr_msgs-msg:Joints
    :initform (cl:make-instance 'pr_msgs-msg:Joints))
   (end_position
    :reader end_position
    :initarg :end_position
    :type pr_msgs-msg:Joints
    :initform (cl:make-instance 'pr_msgs-msg:Joints))
   (max_joint_vel
    :reader max_joint_vel
    :initarg :max_joint_vel
    :type pr_msgs-msg:Joints
    :initform (cl:make-instance 'pr_msgs-msg:Joints))
   (max_joint_accel
    :reader max_joint_accel
    :initarg :max_joint_accel
    :type pr_msgs-msg:Joints
    :initform (cl:make-instance 'pr_msgs-msg:Joints))
   (macpieces
    :reader macpieces
    :initarg :macpieces
    :type (cl:vector pr_msgs-msg:WAMPrecomputedBlendElement)
   :initform (cl:make-array 0 :element-type 'pr_msgs-msg:WAMPrecomputedBlendElement :initial-element (cl:make-instance 'pr_msgs-msg:WAMPrecomputedBlendElement)))
   (traj_duration
    :reader traj_duration
    :initarg :traj_duration
    :type cl:float
    :initform 0.0))
)

(cl:defclass WAMPrecomputedBlendedTrajectory (<WAMPrecomputedBlendedTrajectory>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WAMPrecomputedBlendedTrajectory>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WAMPrecomputedBlendedTrajectory)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<WAMPrecomputedBlendedTrajectory> is deprecated: use pr_msgs-msg:WAMPrecomputedBlendedTrajectory instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:id-val is deprecated.  Use pr_msgs-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'HoldOnStall-val :lambda-list '(m))
(cl:defmethod HoldOnStall-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:HoldOnStall-val is deprecated.  Use pr_msgs-msg:HoldOnStall instead.")
  (HoldOnStall m))

(cl:ensure-generic-function 'WaitForStart-val :lambda-list '(m))
(cl:defmethod WaitForStart-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:WaitForStart-val is deprecated.  Use pr_msgs-msg:WaitForStart instead.")
  (WaitForStart m))

(cl:ensure-generic-function 'start_position-val :lambda-list '(m))
(cl:defmethod start_position-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:start_position-val is deprecated.  Use pr_msgs-msg:start_position instead.")
  (start_position m))

(cl:ensure-generic-function 'end_position-val :lambda-list '(m))
(cl:defmethod end_position-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:end_position-val is deprecated.  Use pr_msgs-msg:end_position instead.")
  (end_position m))

(cl:ensure-generic-function 'max_joint_vel-val :lambda-list '(m))
(cl:defmethod max_joint_vel-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:max_joint_vel-val is deprecated.  Use pr_msgs-msg:max_joint_vel instead.")
  (max_joint_vel m))

(cl:ensure-generic-function 'max_joint_accel-val :lambda-list '(m))
(cl:defmethod max_joint_accel-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:max_joint_accel-val is deprecated.  Use pr_msgs-msg:max_joint_accel instead.")
  (max_joint_accel m))

(cl:ensure-generic-function 'macpieces-val :lambda-list '(m))
(cl:defmethod macpieces-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:macpieces-val is deprecated.  Use pr_msgs-msg:macpieces instead.")
  (macpieces m))

(cl:ensure-generic-function 'traj_duration-val :lambda-list '(m))
(cl:defmethod traj_duration-val ((m <WAMPrecomputedBlendedTrajectory>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:traj_duration-val is deprecated.  Use pr_msgs-msg:traj_duration instead.")
  (traj_duration m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WAMPrecomputedBlendedTrajectory>) ostream)
  "Serializes a message object of type '<WAMPrecomputedBlendedTrajectory>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'HoldOnStall) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'WaitForStart) 1 0)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'start_position) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'end_position) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'max_joint_vel) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'max_joint_accel) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'macpieces))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'macpieces))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'traj_duration))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WAMPrecomputedBlendedTrajectory>) istream)
  "Deserializes a message object of type '<WAMPrecomputedBlendedTrajectory>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:setf (cl:slot-value msg 'HoldOnStall) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'WaitForStart) (cl:not (cl:zerop (cl:read-byte istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'start_position) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'end_position) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'max_joint_vel) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'max_joint_accel) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'macpieces) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'macpieces)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pr_msgs-msg:WAMPrecomputedBlendElement))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'traj_duration) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WAMPrecomputedBlendedTrajectory>)))
  "Returns string type for a message object of type '<WAMPrecomputedBlendedTrajectory>"
  "pr_msgs/WAMPrecomputedBlendedTrajectory")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WAMPrecomputedBlendedTrajectory)))
  "Returns string type for a message object of type 'WAMPrecomputedBlendedTrajectory"
  "pr_msgs/WAMPrecomputedBlendedTrajectory")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WAMPrecomputedBlendedTrajectory>)))
  "Returns md5sum for a message object of type '<WAMPrecomputedBlendedTrajectory>"
  "71bcabe3695718cad854012f233bf235")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WAMPrecomputedBlendedTrajectory)))
  "Returns md5sum for a message object of type 'WAMPrecomputedBlendedTrajectory"
  "71bcabe3695718cad854012f233bf235")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WAMPrecomputedBlendedTrajectory>)))
  "Returns full string definition for message of type '<WAMPrecomputedBlendedTrajectory>"
  (cl:format cl:nil "int16 id~%bool HoldOnStall~%bool WaitForStart~%pr_msgs/Joints start_position~%pr_msgs/Joints end_position~%pr_msgs/Joints max_joint_vel~%pr_msgs/Joints max_joint_accel~%pr_msgs/WAMPrecomputedBlendElement[] macpieces~%float64 traj_duration~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%================================================================================~%MSG: pr_msgs/WAMPrecomputedBlendElement~%pr_msgs/Joints start_pos~%pr_msgs/Joints end_pos~%float64 start_time~%float64 duration~%float64 max_path_velocity~%float64 max_path_acceleration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WAMPrecomputedBlendedTrajectory)))
  "Returns full string definition for message of type 'WAMPrecomputedBlendedTrajectory"
  (cl:format cl:nil "int16 id~%bool HoldOnStall~%bool WaitForStart~%pr_msgs/Joints start_position~%pr_msgs/Joints end_position~%pr_msgs/Joints max_joint_vel~%pr_msgs/Joints max_joint_accel~%pr_msgs/WAMPrecomputedBlendElement[] macpieces~%float64 traj_duration~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%================================================================================~%MSG: pr_msgs/WAMPrecomputedBlendElement~%pr_msgs/Joints start_pos~%pr_msgs/Joints end_pos~%float64 start_time~%float64 duration~%float64 max_path_velocity~%float64 max_path_acceleration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WAMPrecomputedBlendedTrajectory>))
  (cl:+ 0
     2
     1
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'start_position))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'end_position))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'max_joint_vel))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'max_joint_accel))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'macpieces) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WAMPrecomputedBlendedTrajectory>))
  "Converts a ROS message object to a list"
  (cl:list 'WAMPrecomputedBlendedTrajectory
    (cl:cons ':id (id msg))
    (cl:cons ':HoldOnStall (HoldOnStall msg))
    (cl:cons ':WaitForStart (WaitForStart msg))
    (cl:cons ':start_position (start_position msg))
    (cl:cons ':end_position (end_position msg))
    (cl:cons ':max_joint_vel (max_joint_vel msg))
    (cl:cons ':max_joint_accel (max_joint_accel msg))
    (cl:cons ':macpieces (macpieces msg))
    (cl:cons ':traj_duration (traj_duration msg))
))

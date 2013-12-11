; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude WAMState.msg.html

(cl:defclass <WAMState> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (positions
    :reader positions
    :initarg :positions
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (jpositions
    :reader jpositions
    :initarg :jpositions
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (torques
    :reader torques
    :initarg :torques
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (trajectory_queue
    :reader trajectory_queue
    :initarg :trajectory_queue
    :type (cl:vector pr_msgs-msg:TrajInfo)
   :initform (cl:make-array 0 :element-type 'pr_msgs-msg:TrajInfo :initial-element (cl:make-instance 'pr_msgs-msg:TrajInfo)))
   (prev_trajectory
    :reader prev_trajectory
    :initarg :prev_trajectory
    :type pr_msgs-msg:TrajInfo
    :initform (cl:make-instance 'pr_msgs-msg:TrajInfo))
   (state
    :reader state
    :initarg :state
    :type cl:fixnum
    :initform 0))
)

(cl:defclass WAMState (<WAMState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <WAMState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'WAMState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<WAMState> is deprecated: use pr_msgs-msg:WAMState instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <WAMState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:header-val is deprecated.  Use pr_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'positions-val :lambda-list '(m))
(cl:defmethod positions-val ((m <WAMState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:positions-val is deprecated.  Use pr_msgs-msg:positions instead.")
  (positions m))

(cl:ensure-generic-function 'jpositions-val :lambda-list '(m))
(cl:defmethod jpositions-val ((m <WAMState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:jpositions-val is deprecated.  Use pr_msgs-msg:jpositions instead.")
  (jpositions m))

(cl:ensure-generic-function 'torques-val :lambda-list '(m))
(cl:defmethod torques-val ((m <WAMState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:torques-val is deprecated.  Use pr_msgs-msg:torques instead.")
  (torques m))

(cl:ensure-generic-function 'trajectory_queue-val :lambda-list '(m))
(cl:defmethod trajectory_queue-val ((m <WAMState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:trajectory_queue-val is deprecated.  Use pr_msgs-msg:trajectory_queue instead.")
  (trajectory_queue m))

(cl:ensure-generic-function 'prev_trajectory-val :lambda-list '(m))
(cl:defmethod prev_trajectory-val ((m <WAMState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:prev_trajectory-val is deprecated.  Use pr_msgs-msg:prev_trajectory instead.")
  (prev_trajectory m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <WAMState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:state-val is deprecated.  Use pr_msgs-msg:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<WAMState>)))
    "Constants for message type '<WAMState>"
  '((:STATE_FREE . 0)
    (:STATE_FIXED . 1)
    (:STATE_TRAJ_ACTIVE . 2)
    (:STATE_TRAJ_STALLED . 3)
    (:STATE_TRAJ_PAUSED . 4)
    (:STATE_INACTIVE . 255)
    (:STATE_MOVING . 2)
    (:STATE_STALLED . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'WAMState)))
    "Constants for message type 'WAMState"
  '((:STATE_FREE . 0)
    (:STATE_FIXED . 1)
    (:STATE_TRAJ_ACTIVE . 2)
    (:STATE_TRAJ_STALLED . 3)
    (:STATE_TRAJ_PAUSED . 4)
    (:STATE_INACTIVE . 255)
    (:STATE_MOVING . 2)
    (:STATE_STALLED . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <WAMState>) ostream)
  "Serializes a message object of type '<WAMState>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'positions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'positions))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'jpositions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'jpositions))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'torques))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'torques))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'trajectory_queue))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'trajectory_queue))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'prev_trajectory) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <WAMState>) istream)
  "Deserializes a message object of type '<WAMState>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'positions) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'positions)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'jpositions) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'jpositions)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'torques) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'torques)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'trajectory_queue) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'trajectory_queue)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pr_msgs-msg:TrajInfo))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'prev_trajectory) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<WAMState>)))
  "Returns string type for a message object of type '<WAMState>"
  "pr_msgs/WAMState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'WAMState)))
  "Returns string type for a message object of type 'WAMState"
  "pr_msgs/WAMState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<WAMState>)))
  "Returns md5sum for a message object of type '<WAMState>"
  "25cd353827aaf5484b1466979582c59d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'WAMState)))
  "Returns md5sum for a message object of type 'WAMState"
  "25cd353827aaf5484b1466979582c59d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<WAMState>)))
  "Returns full string definition for message of type '<WAMState>"
  (cl:format cl:nil "Header header~%~%float64[] positions~%float64[] jpositions~%# float64[] velocities  # not implemented yet~%float64[] torques~%pr_msgs/TrajInfo[] trajectory_queue~%pr_msgs/TrajInfo prev_trajectory~%uint8 state~%~%uint8 state_free=0~%uint8 state_fixed=1~%uint8 state_traj_active=2~%uint8 state_traj_stalled=3~%uint8 state_traj_paused=4~%uint8 state_inactive=255~%~%# Deprecated state names; please switch to the ones above~%uint8 state_moving=2 # deprecated~%uint8 state_stalled=3 # deprecated~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: pr_msgs/TrajInfo~%uint32 id~%string type~%float64[] end_position~%uint32 state~%~%uint8 state_pending=0~%uint8 state_active=1~%uint8 state_done=3~%uint8 state_aborted=4~%~%# Deprecated state names; please use the ones above~%uint8 state_running=1 # deprecated~%uint8 state_paused=2  # deprecated: look for state_traj_paused in WAMState.state~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'WAMState)))
  "Returns full string definition for message of type 'WAMState"
  (cl:format cl:nil "Header header~%~%float64[] positions~%float64[] jpositions~%# float64[] velocities  # not implemented yet~%float64[] torques~%pr_msgs/TrajInfo[] trajectory_queue~%pr_msgs/TrajInfo prev_trajectory~%uint8 state~%~%uint8 state_free=0~%uint8 state_fixed=1~%uint8 state_traj_active=2~%uint8 state_traj_stalled=3~%uint8 state_traj_paused=4~%uint8 state_inactive=255~%~%# Deprecated state names; please switch to the ones above~%uint8 state_moving=2 # deprecated~%uint8 state_stalled=3 # deprecated~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: pr_msgs/TrajInfo~%uint32 id~%string type~%float64[] end_position~%uint32 state~%~%uint8 state_pending=0~%uint8 state_active=1~%uint8 state_done=3~%uint8 state_aborted=4~%~%# Deprecated state names; please use the ones above~%uint8 state_running=1 # deprecated~%uint8 state_paused=2  # deprecated: look for state_traj_paused in WAMState.state~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <WAMState>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'positions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'jpositions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'torques) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'trajectory_queue) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'prev_trajectory))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <WAMState>))
  "Converts a ROS message object to a list"
  (cl:list 'WAMState
    (cl:cons ':header (header msg))
    (cl:cons ':positions (positions msg))
    (cl:cons ':jpositions (jpositions msg))
    (cl:cons ':torques (torques msg))
    (cl:cons ':trajectory_queue (trajectory_queue msg))
    (cl:cons ':prev_trajectory (prev_trajectory msg))
    (cl:cons ':state (state msg))
))

; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude RailsState.msg.html

(cl:defclass <RailsState> (roslisp-msg-protocol:ros-message)
  ((goal_station_name
    :reader goal_station_name
    :initarg :goal_station_name
    :type cl:string
    :initform "")
   (goal_station_distance
    :reader goal_station_distance
    :initarg :goal_station_distance
    :type cl:float
    :initform 0.0)
   (prev_station_name
    :reader prev_station_name
    :initarg :prev_station_name
    :type cl:string
    :initform "")
   (prev_station_distance
    :reader prev_station_distance
    :initarg :prev_station_distance
    :type cl:float
    :initform 0.0)
   (closest_station_name
    :reader closest_station_name
    :initarg :closest_station_name
    :type cl:string
    :initform "")
   (closest_station_distance
    :reader closest_station_distance
    :initarg :closest_station_distance
    :type cl:float
    :initform 0.0))
)

(cl:defclass RailsState (<RailsState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RailsState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RailsState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<RailsState> is deprecated: use pr_msgs-msg:RailsState instead.")))

(cl:ensure-generic-function 'goal_station_name-val :lambda-list '(m))
(cl:defmethod goal_station_name-val ((m <RailsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:goal_station_name-val is deprecated.  Use pr_msgs-msg:goal_station_name instead.")
  (goal_station_name m))

(cl:ensure-generic-function 'goal_station_distance-val :lambda-list '(m))
(cl:defmethod goal_station_distance-val ((m <RailsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:goal_station_distance-val is deprecated.  Use pr_msgs-msg:goal_station_distance instead.")
  (goal_station_distance m))

(cl:ensure-generic-function 'prev_station_name-val :lambda-list '(m))
(cl:defmethod prev_station_name-val ((m <RailsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:prev_station_name-val is deprecated.  Use pr_msgs-msg:prev_station_name instead.")
  (prev_station_name m))

(cl:ensure-generic-function 'prev_station_distance-val :lambda-list '(m))
(cl:defmethod prev_station_distance-val ((m <RailsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:prev_station_distance-val is deprecated.  Use pr_msgs-msg:prev_station_distance instead.")
  (prev_station_distance m))

(cl:ensure-generic-function 'closest_station_name-val :lambda-list '(m))
(cl:defmethod closest_station_name-val ((m <RailsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:closest_station_name-val is deprecated.  Use pr_msgs-msg:closest_station_name instead.")
  (closest_station_name m))

(cl:ensure-generic-function 'closest_station_distance-val :lambda-list '(m))
(cl:defmethod closest_station_distance-val ((m <RailsState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:closest_station_distance-val is deprecated.  Use pr_msgs-msg:closest_station_distance instead.")
  (closest_station_distance m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RailsState>) ostream)
  "Serializes a message object of type '<RailsState>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'goal_station_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'goal_station_name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'goal_station_distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'prev_station_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'prev_station_name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'prev_station_distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'closest_station_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'closest_station_name))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'closest_station_distance))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RailsState>) istream)
  "Deserializes a message object of type '<RailsState>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'goal_station_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'goal_station_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'goal_station_distance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'prev_station_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'prev_station_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'prev_station_distance) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'closest_station_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'closest_station_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'closest_station_distance) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RailsState>)))
  "Returns string type for a message object of type '<RailsState>"
  "pr_msgs/RailsState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RailsState)))
  "Returns string type for a message object of type 'RailsState"
  "pr_msgs/RailsState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RailsState>)))
  "Returns md5sum for a message object of type '<RailsState>"
  "ce17ce4ba137fd794491e233128e6635")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RailsState)))
  "Returns md5sum for a message object of type 'RailsState"
  "ce17ce4ba137fd794491e233128e6635")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RailsState>)))
  "Returns full string definition for message of type '<RailsState>"
  (cl:format cl:nil "string goal_station_name~%float64 goal_station_distance~%string prev_station_name~%float64 prev_station_distance~%string closest_station_name~%float64 closest_station_distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RailsState)))
  "Returns full string definition for message of type 'RailsState"
  (cl:format cl:nil "string goal_station_name~%float64 goal_station_distance~%string prev_station_name~%float64 prev_station_distance~%string closest_station_name~%float64 closest_station_distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RailsState>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'goal_station_name))
     8
     4 (cl:length (cl:slot-value msg 'prev_station_name))
     8
     4 (cl:length (cl:slot-value msg 'closest_station_name))
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RailsState>))
  "Converts a ROS message object to a list"
  (cl:list 'RailsState
    (cl:cons ':goal_station_name (goal_station_name msg))
    (cl:cons ':goal_station_distance (goal_station_distance msg))
    (cl:cons ':prev_station_name (prev_station_name msg))
    (cl:cons ':prev_station_distance (prev_station_distance msg))
    (cl:cons ':closest_station_name (closest_station_name msg))
    (cl:cons ':closest_station_distance (closest_station_distance msg))
))

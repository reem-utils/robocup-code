; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude AppletState.msg.html

(cl:defclass <AppletState> (roslisp-msg-protocol:ros-message)
  ((cmd_topic_name
    :reader cmd_topic_name
    :initarg :cmd_topic_name
    :type cl:string
    :initform "")
   (actions
    :reader actions
    :initarg :actions
    :type (cl:vector pr_msgs-msg:Action)
   :initform (cl:make-array 0 :element-type 'pr_msgs-msg:Action :initial-element (cl:make-instance 'pr_msgs-msg:Action)))
   (state
    :reader state
    :initarg :state
    :type cl:fixnum
    :initform 0)
   (info
    :reader info
    :initarg :info
    :type cl:string
    :initform ""))
)

(cl:defclass AppletState (<AppletState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AppletState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AppletState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<AppletState> is deprecated: use pr_msgs-msg:AppletState instead.")))

(cl:ensure-generic-function 'cmd_topic_name-val :lambda-list '(m))
(cl:defmethod cmd_topic_name-val ((m <AppletState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:cmd_topic_name-val is deprecated.  Use pr_msgs-msg:cmd_topic_name instead.")
  (cmd_topic_name m))

(cl:ensure-generic-function 'actions-val :lambda-list '(m))
(cl:defmethod actions-val ((m <AppletState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:actions-val is deprecated.  Use pr_msgs-msg:actions instead.")
  (actions m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <AppletState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:state-val is deprecated.  Use pr_msgs-msg:state instead.")
  (state m))

(cl:ensure-generic-function 'info-val :lambda-list '(m))
(cl:defmethod info-val ((m <AppletState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:info-val is deprecated.  Use pr_msgs-msg:info instead.")
  (info m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<AppletState>)))
    "Constants for message type '<AppletState>"
  '((:STATE_IDLE . 0)
    (:STATE_BUSY . 1)
    (:STATE_ERROR . 2)
    (:STATE_DYING . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'AppletState)))
    "Constants for message type 'AppletState"
  '((:STATE_IDLE . 0)
    (:STATE_BUSY . 1)
    (:STATE_ERROR . 2)
    (:STATE_DYING . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AppletState>) ostream)
  "Serializes a message object of type '<AppletState>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'cmd_topic_name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'cmd_topic_name))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'actions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'actions))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'info))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'info))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AppletState>) istream)
  "Deserializes a message object of type '<AppletState>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'cmd_topic_name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'cmd_topic_name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'actions) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'actions)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pr_msgs-msg:Action))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'state)) (cl:read-byte istream))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'info) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'info) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AppletState>)))
  "Returns string type for a message object of type '<AppletState>"
  "pr_msgs/AppletState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AppletState)))
  "Returns string type for a message object of type 'AppletState"
  "pr_msgs/AppletState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AppletState>)))
  "Returns md5sum for a message object of type '<AppletState>"
  "7c39cb5217576cbaaa8bc739f08abe33")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AppletState)))
  "Returns md5sum for a message object of type 'AppletState"
  "7c39cb5217576cbaaa8bc739f08abe33")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AppletState>)))
  "Returns full string definition for message of type '<AppletState>"
  (cl:format cl:nil "string cmd_topic_name     # The topic name to use when calling ~%                          # AppletCommand service for this node~%~%pr_msgs/Action[] actions  # the actions that this applet is ready ~%                          #   to perform NOW~%~%uint8 state               # the applet state (one of the values below)~%~%string info               # any additional human-readable information~%~%uint8 state_idle=0~%uint8 state_busy=1~%uint8 state_error=2~%uint8 state_dying=3~%~%~%================================================================================~%MSG: pr_msgs/Action~%string name         # name of this action (e.g. pickup_juice_box)~%~%string target_name  # distinguishes the target of this action from others~%                    #  (could be a global object id, world coordinates, etc)~%~%int32 prep_duration   # how long to expect before any movement commences~%~%int32 execution_duration  # how long to expect the movement to take~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AppletState)))
  "Returns full string definition for message of type 'AppletState"
  (cl:format cl:nil "string cmd_topic_name     # The topic name to use when calling ~%                          # AppletCommand service for this node~%~%pr_msgs/Action[] actions  # the actions that this applet is ready ~%                          #   to perform NOW~%~%uint8 state               # the applet state (one of the values below)~%~%string info               # any additional human-readable information~%~%uint8 state_idle=0~%uint8 state_busy=1~%uint8 state_error=2~%uint8 state_dying=3~%~%~%================================================================================~%MSG: pr_msgs/Action~%string name         # name of this action (e.g. pickup_juice_box)~%~%string target_name  # distinguishes the target of this action from others~%                    #  (could be a global object id, world coordinates, etc)~%~%int32 prep_duration   # how long to expect before any movement commences~%~%int32 execution_duration  # how long to expect the movement to take~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AppletState>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'cmd_topic_name))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'actions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     1
     4 (cl:length (cl:slot-value msg 'info))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AppletState>))
  "Converts a ROS message object to a list"
  (cl:list 'AppletState
    (cl:cons ':cmd_topic_name (cmd_topic_name msg))
    (cl:cons ':actions (actions msg))
    (cl:cons ':state (state msg))
    (cl:cons ':info (info msg))
))

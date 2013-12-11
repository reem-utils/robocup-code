; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude PomdpGraspConfig.msg.html

(cl:defclass <PomdpGraspConfig> (roslisp-msg-protocol:ros-message)
  ((best_pose_algorithm_id
    :reader best_pose_algorithm_id
    :initarg :best_pose_algorithm_id
    :type cl:fixnum
    :initform 0)
   (actiontype
    :reader actiontype
    :initarg :actiontype
    :type cl:fixnum
    :initform 0)
   (grabbing_zone
    :reader grabbing_zone
    :initarg :grabbing_zone
    :type cl:fixnum
    :initform 0)
   (approach_config
    :reader approach_config
    :initarg :approach_config
    :type estirabot_msgs-msg:GraspPointParameters
    :initform (cl:make-instance 'estirabot_msgs-msg:GraspPointParameters))
   (fingers_grasp_configs
    :reader fingers_grasp_configs
    :initarg :fingers_grasp_configs
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (place_point
    :reader place_point
    :initarg :place_point
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass PomdpGraspConfig (<PomdpGraspConfig>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PomdpGraspConfig>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PomdpGraspConfig)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<PomdpGraspConfig> is deprecated: use estirabot_msgs-msg:PomdpGraspConfig instead.")))

(cl:ensure-generic-function 'best_pose_algorithm_id-val :lambda-list '(m))
(cl:defmethod best_pose_algorithm_id-val ((m <PomdpGraspConfig>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:best_pose_algorithm_id-val is deprecated.  Use estirabot_msgs-msg:best_pose_algorithm_id instead.")
  (best_pose_algorithm_id m))

(cl:ensure-generic-function 'actiontype-val :lambda-list '(m))
(cl:defmethod actiontype-val ((m <PomdpGraspConfig>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:actiontype-val is deprecated.  Use estirabot_msgs-msg:actiontype instead.")
  (actiontype m))

(cl:ensure-generic-function 'grabbing_zone-val :lambda-list '(m))
(cl:defmethod grabbing_zone-val ((m <PomdpGraspConfig>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:grabbing_zone-val is deprecated.  Use estirabot_msgs-msg:grabbing_zone instead.")
  (grabbing_zone m))

(cl:ensure-generic-function 'approach_config-val :lambda-list '(m))
(cl:defmethod approach_config-val ((m <PomdpGraspConfig>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:approach_config-val is deprecated.  Use estirabot_msgs-msg:approach_config instead.")
  (approach_config m))

(cl:ensure-generic-function 'fingers_grasp_configs-val :lambda-list '(m))
(cl:defmethod fingers_grasp_configs-val ((m <PomdpGraspConfig>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:fingers_grasp_configs-val is deprecated.  Use estirabot_msgs-msg:fingers_grasp_configs instead.")
  (fingers_grasp_configs m))

(cl:ensure-generic-function 'place_point-val :lambda-list '(m))
(cl:defmethod place_point-val ((m <PomdpGraspConfig>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:place_point-val is deprecated.  Use estirabot_msgs-msg:place_point instead.")
  (place_point m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<PomdpGraspConfig>)))
    "Constants for message type '<PomdpGraspConfig>"
  '((:GRAB . 0)
    (:DROP . 1)
    (:BOTH_ZONES . 0)
    (:LEFT_ZONE . 1)
    (:RIGHT_ZONE . 2)
    (:MAX_HEIGHT_ALG . 0)
    (:MAX_WRINKLE_ALG . 1)
    (:FUSION_ALG . 2)
    (:APPROACH_TOP_DEEP . 0)
    (:APPROACH_TOP_SURFACE . 1)
    (:APPROACH_SIDE_DEEP . 2)
    (:APPROACH_SIDE_SURFACE . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'PomdpGraspConfig)))
    "Constants for message type 'PomdpGraspConfig"
  '((:GRAB . 0)
    (:DROP . 1)
    (:BOTH_ZONES . 0)
    (:LEFT_ZONE . 1)
    (:RIGHT_ZONE . 2)
    (:MAX_HEIGHT_ALG . 0)
    (:MAX_WRINKLE_ALG . 1)
    (:FUSION_ALG . 2)
    (:APPROACH_TOP_DEEP . 0)
    (:APPROACH_TOP_SURFACE . 1)
    (:APPROACH_SIDE_DEEP . 2)
    (:APPROACH_SIDE_SURFACE . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PomdpGraspConfig>) ostream)
  "Serializes a message object of type '<PomdpGraspConfig>"
  (cl:let* ((signed (cl:slot-value msg 'best_pose_algorithm_id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'actiontype)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'grabbing_zone)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'approach_config) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'fingers_grasp_configs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((__ros_str_len (cl:length ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) ele))
   (cl:slot-value msg 'fingers_grasp_configs))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'place_point) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PomdpGraspConfig>) istream)
  "Deserializes a message object of type '<PomdpGraspConfig>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'best_pose_algorithm_id) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'actiontype) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'grabbing_zone) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'approach_config) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'fingers_grasp_configs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'fingers_grasp_configs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'place_point) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PomdpGraspConfig>)))
  "Returns string type for a message object of type '<PomdpGraspConfig>"
  "estirabot_msgs/PomdpGraspConfig")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PomdpGraspConfig)))
  "Returns string type for a message object of type 'PomdpGraspConfig"
  "estirabot_msgs/PomdpGraspConfig")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PomdpGraspConfig>)))
  "Returns md5sum for a message object of type '<PomdpGraspConfig>"
  "38bd3d3705953515e94def1a3e168b6c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PomdpGraspConfig)))
  "Returns md5sum for a message object of type 'PomdpGraspConfig"
  "38bd3d3705953515e94def1a3e168b6c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PomdpGraspConfig>)))
  "Returns full string definition for message of type '<PomdpGraspConfig>"
  (cl:format cl:nil "# Message containing configuration for the pomdp grasping process~%~%# Define grabbing_zones~%int8 GRAB = 0~%int8 DROP = 1~%~%# Define grabbing_zones~%int8 BOTH_ZONES = 0~%int8 LEFT_ZONE = 1~%int8 RIGHT_ZONE = 2~%~%# Define best pose algorithms~%int8 MAX_HEIGHT_ALG = 0~%int8 MAX_WRINKLE_ALG = 1~%int8 FUSION_ALG = 2~%~%# Define posible approach identifiers~%int8 APPROACH_TOP_DEEP = 0~%int8 APPROACH_TOP_SURFACE = 1~%int8 APPROACH_SIDE_DEEP = 2~%int8 APPROACH_SIDE_SURFACE = 3~%~%int8 best_pose_algorithm_id~%int8 actiontype~%int8 grabbing_zone~%estirabot_msgs/GraspPointParameters approach_config~%string[] fingers_grasp_configs~%geometry_msgs/PoseStamped place_point~%~%================================================================================~%MSG: estirabot_msgs/GraspPointParameters~%# Message for parameters to modify a grasp point~%# These parameters apply on a cartesian coordinate~%# (geometry_msgs/pose).~%~%geometry_msgs/Transform pre_grasp_modifier~%geometry_msgs/Transform[] grasp_modifiers~%uint8 grasp_modifier_used~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PomdpGraspConfig)))
  "Returns full string definition for message of type 'PomdpGraspConfig"
  (cl:format cl:nil "# Message containing configuration for the pomdp grasping process~%~%# Define grabbing_zones~%int8 GRAB = 0~%int8 DROP = 1~%~%# Define grabbing_zones~%int8 BOTH_ZONES = 0~%int8 LEFT_ZONE = 1~%int8 RIGHT_ZONE = 2~%~%# Define best pose algorithms~%int8 MAX_HEIGHT_ALG = 0~%int8 MAX_WRINKLE_ALG = 1~%int8 FUSION_ALG = 2~%~%# Define posible approach identifiers~%int8 APPROACH_TOP_DEEP = 0~%int8 APPROACH_TOP_SURFACE = 1~%int8 APPROACH_SIDE_DEEP = 2~%int8 APPROACH_SIDE_SURFACE = 3~%~%int8 best_pose_algorithm_id~%int8 actiontype~%int8 grabbing_zone~%estirabot_msgs/GraspPointParameters approach_config~%string[] fingers_grasp_configs~%geometry_msgs/PoseStamped place_point~%~%================================================================================~%MSG: estirabot_msgs/GraspPointParameters~%# Message for parameters to modify a grasp point~%# These parameters apply on a cartesian coordinate~%# (geometry_msgs/pose).~%~%geometry_msgs/Transform pre_grasp_modifier~%geometry_msgs/Transform[] grasp_modifiers~%uint8 grasp_modifier_used~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PomdpGraspConfig>))
  (cl:+ 0
     1
     1
     1
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'approach_config))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'fingers_grasp_configs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'place_point))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PomdpGraspConfig>))
  "Converts a ROS message object to a list"
  (cl:list 'PomdpGraspConfig
    (cl:cons ':best_pose_algorithm_id (best_pose_algorithm_id msg))
    (cl:cons ':actiontype (actiontype msg))
    (cl:cons ':grabbing_zone (grabbing_zone msg))
    (cl:cons ':approach_config (approach_config msg))
    (cl:cons ':fingers_grasp_configs (fingers_grasp_configs msg))
    (cl:cons ':place_point (place_point msg))
))

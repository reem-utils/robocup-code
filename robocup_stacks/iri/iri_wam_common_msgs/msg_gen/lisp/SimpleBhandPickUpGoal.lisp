; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-msg)


;//! \htmlinclude SimpleBhandPickUpGoal.msg.html

(cl:defclass <SimpleBhandPickUpGoal> (roslisp-msg-protocol:ros-message)
  ((fingers_position_for_grasp
    :reader fingers_position_for_grasp
    :initarg :fingers_position_for_grasp
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (fingers_position_for_pre_grasp
    :reader fingers_position_for_pre_grasp
    :initarg :fingers_position_for_pre_grasp
    :type (cl:vector cl:string)
   :initform (cl:make-array 0 :element-type 'cl:string :initial-element ""))
   (grasp_pose
    :reader grasp_pose
    :initarg :grasp_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (pre_grasp_modifier
    :reader pre_grasp_modifier
    :initarg :pre_grasp_modifier
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (lift
    :reader lift
    :initarg :lift
    :type object_manipulation_msgs-msg:GripperTranslation
    :initform (cl:make-instance 'object_manipulation_msgs-msg:GripperTranslation)))
)

(cl:defclass SimpleBhandPickUpGoal (<SimpleBhandPickUpGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SimpleBhandPickUpGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SimpleBhandPickUpGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-msg:<SimpleBhandPickUpGoal> is deprecated: use iri_wam_common_msgs-msg:SimpleBhandPickUpGoal instead.")))

(cl:ensure-generic-function 'fingers_position_for_grasp-val :lambda-list '(m))
(cl:defmethod fingers_position_for_grasp-val ((m <SimpleBhandPickUpGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:fingers_position_for_grasp-val is deprecated.  Use iri_wam_common_msgs-msg:fingers_position_for_grasp instead.")
  (fingers_position_for_grasp m))

(cl:ensure-generic-function 'fingers_position_for_pre_grasp-val :lambda-list '(m))
(cl:defmethod fingers_position_for_pre_grasp-val ((m <SimpleBhandPickUpGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:fingers_position_for_pre_grasp-val is deprecated.  Use iri_wam_common_msgs-msg:fingers_position_for_pre_grasp instead.")
  (fingers_position_for_pre_grasp m))

(cl:ensure-generic-function 'grasp_pose-val :lambda-list '(m))
(cl:defmethod grasp_pose-val ((m <SimpleBhandPickUpGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:grasp_pose-val is deprecated.  Use iri_wam_common_msgs-msg:grasp_pose instead.")
  (grasp_pose m))

(cl:ensure-generic-function 'pre_grasp_modifier-val :lambda-list '(m))
(cl:defmethod pre_grasp_modifier-val ((m <SimpleBhandPickUpGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:pre_grasp_modifier-val is deprecated.  Use iri_wam_common_msgs-msg:pre_grasp_modifier instead.")
  (pre_grasp_modifier m))

(cl:ensure-generic-function 'lift-val :lambda-list '(m))
(cl:defmethod lift-val ((m <SimpleBhandPickUpGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-msg:lift-val is deprecated.  Use iri_wam_common_msgs-msg:lift instead.")
  (lift m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SimpleBhandPickUpGoal>) ostream)
  "Serializes a message object of type '<SimpleBhandPickUpGoal>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'fingers_position_for_grasp))))
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
   (cl:slot-value msg 'fingers_position_for_grasp))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'fingers_position_for_pre_grasp))))
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
   (cl:slot-value msg 'fingers_position_for_pre_grasp))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'grasp_pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pre_grasp_modifier) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'lift) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SimpleBhandPickUpGoal>) istream)
  "Deserializes a message object of type '<SimpleBhandPickUpGoal>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'fingers_position_for_grasp) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'fingers_position_for_grasp)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'fingers_position_for_pre_grasp) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'fingers_position_for_pre_grasp)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:aref vals i) __ros_str_idx) (cl:code-char (cl:read-byte istream))))))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'grasp_pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pre_grasp_modifier) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'lift) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SimpleBhandPickUpGoal>)))
  "Returns string type for a message object of type '<SimpleBhandPickUpGoal>"
  "iri_wam_common_msgs/SimpleBhandPickUpGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SimpleBhandPickUpGoal)))
  "Returns string type for a message object of type 'SimpleBhandPickUpGoal"
  "iri_wam_common_msgs/SimpleBhandPickUpGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SimpleBhandPickUpGoal>)))
  "Returns md5sum for a message object of type '<SimpleBhandPickUpGoal>"
  "5f90d8765528c27d77bd5b45cbdd9e78")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SimpleBhandPickUpGoal)))
  "Returns md5sum for a message object of type 'SimpleBhandPickUpGoal"
  "5f90d8765528c27d77bd5b45cbdd9e78")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SimpleBhandPickUpGoal>)))
  "Returns full string definition for message of type '<SimpleBhandPickUpGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# October 2012 - J.L Rivero, G. Alenya, D. Martinez~%#~%# This action was built after analyze previously the \"standard\" ROS message~%# PickUp. The ROS message involve a lot of action we were not consider at~%# the moment of writing and adapt that huge input for our needs was over-~%# engineer a solution.~%#~%# A translator PickUp -> SimpleBhandPickUp could be done, if needed~%~%# SimpleBhandPickUp is composed by the following phases:~%#~%# 1. Move the ARM from current to pre-grasp (planned if requested)~%# 2. Put the fingers into the pre-grasp position~%# 3. Move the ARM from pre-grasp to grasp (planned if requested)~%# 4. Put the fingers into the grasp position~%# 5. Perform the lift movement~%~%# goal~%# A vector of different GCL bhand commands~%string[] fingers_position_for_grasp~%string[] fingers_position_for_pre_grasp~%# Grasp pose is defined in the Stamped ~%geometry_msgs/PoseStamped grasp_pose~%# pre movement relative to the grasp_pose~%geometry_msgs/Pose pre_grasp_modifier~%# Direction and distance to lift from the grasp_pose~%object_manipulation_msgs/GripperTranslation lift~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: object_manipulation_msgs/GripperTranslation~%# defines a translation for the gripper, used in pickup or place tasks~%# for example for lifting an object off a table or approaching the table for placing~%~%# the direction of the translation~%geometry_msgs/Vector3Stamped direction~%~%# the desired translation distance~%float32 desired_distance~%~%# the min distance that must be considered feasible before the~%# grasp is even attempted~%float32 min_distance~%================================================================================~%MSG: geometry_msgs/Vector3Stamped~%# This represents a Vector3 with reference coordinate frame and timestamp~%Header header~%Vector3 vector~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SimpleBhandPickUpGoal)))
  "Returns full string definition for message of type 'SimpleBhandPickUpGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# October 2012 - J.L Rivero, G. Alenya, D. Martinez~%#~%# This action was built after analyze previously the \"standard\" ROS message~%# PickUp. The ROS message involve a lot of action we were not consider at~%# the moment of writing and adapt that huge input for our needs was over-~%# engineer a solution.~%#~%# A translator PickUp -> SimpleBhandPickUp could be done, if needed~%~%# SimpleBhandPickUp is composed by the following phases:~%#~%# 1. Move the ARM from current to pre-grasp (planned if requested)~%# 2. Put the fingers into the pre-grasp position~%# 3. Move the ARM from pre-grasp to grasp (planned if requested)~%# 4. Put the fingers into the grasp position~%# 5. Perform the lift movement~%~%# goal~%# A vector of different GCL bhand commands~%string[] fingers_position_for_grasp~%string[] fingers_position_for_pre_grasp~%# Grasp pose is defined in the Stamped ~%geometry_msgs/PoseStamped grasp_pose~%# pre movement relative to the grasp_pose~%geometry_msgs/Pose pre_grasp_modifier~%# Direction and distance to lift from the grasp_pose~%object_manipulation_msgs/GripperTranslation lift~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: object_manipulation_msgs/GripperTranslation~%# defines a translation for the gripper, used in pickup or place tasks~%# for example for lifting an object off a table or approaching the table for placing~%~%# the direction of the translation~%geometry_msgs/Vector3Stamped direction~%~%# the desired translation distance~%float32 desired_distance~%~%# the min distance that must be considered feasible before the~%# grasp is even attempted~%float32 min_distance~%================================================================================~%MSG: geometry_msgs/Vector3Stamped~%# This represents a Vector3 with reference coordinate frame and timestamp~%Header header~%Vector3 vector~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SimpleBhandPickUpGoal>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'fingers_position_for_grasp) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'fingers_position_for_pre_grasp) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4 (cl:length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'grasp_pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pre_grasp_modifier))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'lift))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SimpleBhandPickUpGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'SimpleBhandPickUpGoal
    (cl:cons ':fingers_position_for_grasp (fingers_position_for_grasp msg))
    (cl:cons ':fingers_position_for_pre_grasp (fingers_position_for_pre_grasp msg))
    (cl:cons ':grasp_pose (grasp_pose msg))
    (cl:cons ':pre_grasp_modifier (pre_grasp_modifier msg))
    (cl:cons ':lift (lift msg))
))

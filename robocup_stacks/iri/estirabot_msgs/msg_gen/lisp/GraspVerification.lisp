; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude GraspVerification.msg.html

(cl:defclass <GraspVerification> (roslisp-msg-protocol:ros-message)
  ((grasp_results
    :reader grasp_results
    :initarg :grasp_results
    :type (cl:vector object_manipulation_msgs-msg:GraspResult)
   :initform (cl:make-array 0 :element-type 'object_manipulation_msgs-msg:GraspResult :initial-element (cl:make-instance 'object_manipulation_msgs-msg:GraspResult)))
   (grasp_images
    :reader grasp_images
    :initarg :grasp_images
    :type (cl:vector sensor_msgs-msg:PointCloud2)
   :initform (cl:make-array 0 :element-type 'sensor_msgs-msg:PointCloud2 :initial-element (cl:make-instance 'sensor_msgs-msg:PointCloud2))))
)

(cl:defclass GraspVerification (<GraspVerification>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspVerification>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspVerification)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<GraspVerification> is deprecated: use estirabot_msgs-msg:GraspVerification instead.")))

(cl:ensure-generic-function 'grasp_results-val :lambda-list '(m))
(cl:defmethod grasp_results-val ((m <GraspVerification>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:grasp_results-val is deprecated.  Use estirabot_msgs-msg:grasp_results instead.")
  (grasp_results m))

(cl:ensure-generic-function 'grasp_images-val :lambda-list '(m))
(cl:defmethod grasp_images-val ((m <GraspVerification>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:grasp_images-val is deprecated.  Use estirabot_msgs-msg:grasp_images instead.")
  (grasp_images m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<GraspVerification>)))
    "Constants for message type '<GraspVerification>"
  '((:AFTER_LIFT . 0)
    (:AFTER_SHAKING . 1))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'GraspVerification)))
    "Constants for message type 'GraspVerification"
  '((:AFTER_LIFT . 0)
    (:AFTER_SHAKING . 1))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspVerification>) ostream)
  "Serializes a message object of type '<GraspVerification>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'grasp_results))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'grasp_results))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'grasp_images))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'grasp_images))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspVerification>) istream)
  "Deserializes a message object of type '<GraspVerification>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'grasp_results) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'grasp_results)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'object_manipulation_msgs-msg:GraspResult))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'grasp_images) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'grasp_images)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'sensor_msgs-msg:PointCloud2))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspVerification>)))
  "Returns string type for a message object of type '<GraspVerification>"
  "estirabot_msgs/GraspVerification")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspVerification)))
  "Returns string type for a message object of type 'GraspVerification"
  "estirabot_msgs/GraspVerification")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspVerification>)))
  "Returns md5sum for a message object of type '<GraspVerification>"
  "e3d204a43e7cce62c1853351b215f13e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspVerification)))
  "Returns md5sum for a message object of type 'GraspVerification"
  "e3d204a43e7cce62c1853351b215f13e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspVerification>)))
  "Returns full string definition for message of type '<GraspVerification>"
  (cl:format cl:nil "# Message containing results from a sequence of verification actions on a grasAFTER_SHAKING = 1p~%~%# Currently positions in the vector correspond to the following actions~%# 0 -> Result after basic lift movement~%# 1 -> Result after shaking the cloth when lifted~%~%int32 AFTER_LIFT = 0~%int32 AFTER_SHAKING = 1~%~%object_manipulation_msgs/GraspResult[] grasp_results~%sensor_msgs/PointCloud2[] grasp_images~%~%================================================================================~%MSG: object_manipulation_msgs/GraspResult~%int32 SUCCESS = 1~%int32 GRASP_OUT_OF_REACH = 2~%int32 GRASP_IN_COLLISION = 3~%int32 GRASP_UNFEASIBLE = 4~%int32 PREGRASP_OUT_OF_REACH = 5~%int32 PREGRASP_IN_COLLISION = 6~%int32 PREGRASP_UNFEASIBLE = 7~%int32 LIFT_OUT_OF_REACH = 8~%int32 LIFT_IN_COLLISION = 9~%int32 LIFT_UNFEASIBLE = 10~%int32 MOVE_ARM_FAILED = 11~%int32 GRASP_FAILED = 12~%int32 LIFT_FAILED = 13~%int32 RETREAT_FAILED = 14~%int32 result_code~%~%# whether the state of the world was disturbed by this attempt. generally, this flag~%# shows if another task can be attempted, or a new sensed world model is recommeded~%# before proceeding~%bool continuation_possible~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspVerification)))
  "Returns full string definition for message of type 'GraspVerification"
  (cl:format cl:nil "# Message containing results from a sequence of verification actions on a grasAFTER_SHAKING = 1p~%~%# Currently positions in the vector correspond to the following actions~%# 0 -> Result after basic lift movement~%# 1 -> Result after shaking the cloth when lifted~%~%int32 AFTER_LIFT = 0~%int32 AFTER_SHAKING = 1~%~%object_manipulation_msgs/GraspResult[] grasp_results~%sensor_msgs/PointCloud2[] grasp_images~%~%================================================================================~%MSG: object_manipulation_msgs/GraspResult~%int32 SUCCESS = 1~%int32 GRASP_OUT_OF_REACH = 2~%int32 GRASP_IN_COLLISION = 3~%int32 GRASP_UNFEASIBLE = 4~%int32 PREGRASP_OUT_OF_REACH = 5~%int32 PREGRASP_IN_COLLISION = 6~%int32 PREGRASP_UNFEASIBLE = 7~%int32 LIFT_OUT_OF_REACH = 8~%int32 LIFT_IN_COLLISION = 9~%int32 LIFT_UNFEASIBLE = 10~%int32 MOVE_ARM_FAILED = 11~%int32 GRASP_FAILED = 12~%int32 LIFT_FAILED = 13~%int32 RETREAT_FAILED = 14~%int32 result_code~%~%# whether the state of the world was disturbed by this attempt. generally, this flag~%# shows if another task can be attempted, or a new sensed world model is recommeded~%# before proceeding~%bool continuation_possible~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspVerification>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'grasp_results) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'grasp_images) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspVerification>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspVerification
    (cl:cons ':grasp_results (grasp_results msg))
    (cl:cons ':grasp_images (grasp_images msg))
))

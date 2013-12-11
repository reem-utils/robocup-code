; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude StorePointCloud2-request.msg.html

(cl:defclass <StorePointCloud2-request> (roslisp-msg-protocol:ros-message)
  ((file_name
    :reader file_name
    :initarg :file_name
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (sensor_pose
    :reader sensor_pose
    :initarg :sensor_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (point_cloud
    :reader point_cloud
    :initarg :point_cloud
    :type sensor_msgs-msg:PointCloud2
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud2)))
)

(cl:defclass StorePointCloud2-request (<StorePointCloud2-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StorePointCloud2-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StorePointCloud2-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<StorePointCloud2-request> is deprecated: use iri_perception_msgs-srv:StorePointCloud2-request instead.")))

(cl:ensure-generic-function 'file_name-val :lambda-list '(m))
(cl:defmethod file_name-val ((m <StorePointCloud2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:file_name-val is deprecated.  Use iri_perception_msgs-srv:file_name instead.")
  (file_name m))

(cl:ensure-generic-function 'sensor_pose-val :lambda-list '(m))
(cl:defmethod sensor_pose-val ((m <StorePointCloud2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:sensor_pose-val is deprecated.  Use iri_perception_msgs-srv:sensor_pose instead.")
  (sensor_pose m))

(cl:ensure-generic-function 'point_cloud-val :lambda-list '(m))
(cl:defmethod point_cloud-val ((m <StorePointCloud2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:point_cloud-val is deprecated.  Use iri_perception_msgs-srv:point_cloud instead.")
  (point_cloud m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StorePointCloud2-request>) ostream)
  "Serializes a message object of type '<StorePointCloud2-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'file_name) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'sensor_pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'point_cloud) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StorePointCloud2-request>) istream)
  "Deserializes a message object of type '<StorePointCloud2-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'file_name) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'sensor_pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'point_cloud) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StorePointCloud2-request>)))
  "Returns string type for a service object of type '<StorePointCloud2-request>"
  "iri_perception_msgs/StorePointCloud2Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StorePointCloud2-request)))
  "Returns string type for a service object of type 'StorePointCloud2-request"
  "iri_perception_msgs/StorePointCloud2Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StorePointCloud2-request>)))
  "Returns md5sum for a message object of type '<StorePointCloud2-request>"
  "620f2fb25ff410464561f8872a6e9668")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StorePointCloud2-request)))
  "Returns md5sum for a message object of type 'StorePointCloud2-request"
  "620f2fb25ff410464561f8872a6e9668")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StorePointCloud2-request>)))
  "Returns full string definition for message of type '<StorePointCloud2-request>"
  (cl:format cl:nil "~%std_msgs/String           file_name~%geometry_msgs/PoseStamped sensor_pose~%sensor_msgs/PointCloud2   point_cloud~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StorePointCloud2-request)))
  "Returns full string definition for message of type 'StorePointCloud2-request"
  (cl:format cl:nil "~%std_msgs/String           file_name~%geometry_msgs/PoseStamped sensor_pose~%sensor_msgs/PointCloud2   point_cloud~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StorePointCloud2-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'file_name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'sensor_pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'point_cloud))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StorePointCloud2-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StorePointCloud2-request
    (cl:cons ':file_name (file_name msg))
    (cl:cons ':sensor_pose (sensor_pose msg))
    (cl:cons ':point_cloud (point_cloud msg))
))
;//! \htmlinclude StorePointCloud2-response.msg.html

(cl:defclass <StorePointCloud2-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass StorePointCloud2-response (<StorePointCloud2-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StorePointCloud2-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StorePointCloud2-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<StorePointCloud2-response> is deprecated: use iri_perception_msgs-srv:StorePointCloud2-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StorePointCloud2-response>) ostream)
  "Serializes a message object of type '<StorePointCloud2-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StorePointCloud2-response>) istream)
  "Deserializes a message object of type '<StorePointCloud2-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StorePointCloud2-response>)))
  "Returns string type for a service object of type '<StorePointCloud2-response>"
  "iri_perception_msgs/StorePointCloud2Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StorePointCloud2-response)))
  "Returns string type for a service object of type 'StorePointCloud2-response"
  "iri_perception_msgs/StorePointCloud2Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StorePointCloud2-response>)))
  "Returns md5sum for a message object of type '<StorePointCloud2-response>"
  "620f2fb25ff410464561f8872a6e9668")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StorePointCloud2-response)))
  "Returns md5sum for a message object of type 'StorePointCloud2-response"
  "620f2fb25ff410464561f8872a6e9668")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StorePointCloud2-response>)))
  "Returns full string definition for message of type '<StorePointCloud2-response>"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StorePointCloud2-response)))
  "Returns full string definition for message of type 'StorePointCloud2-response"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StorePointCloud2-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StorePointCloud2-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StorePointCloud2-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StorePointCloud2)))
  'StorePointCloud2-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StorePointCloud2)))
  'StorePointCloud2-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StorePointCloud2)))
  "Returns string type for a service object of type '<StorePointCloud2>"
  "iri_perception_msgs/StorePointCloud2")
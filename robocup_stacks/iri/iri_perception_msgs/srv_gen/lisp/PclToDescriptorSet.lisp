; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude PclToDescriptorSet-request.msg.html

(cl:defclass <PclToDescriptorSet-request> (roslisp-msg-protocol:ros-message)
  ((pointcloud
    :reader pointcloud
    :initarg :pointcloud
    :type sensor_msgs-msg:PointCloud2
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud2)))
)

(cl:defclass PclToDescriptorSet-request (<PclToDescriptorSet-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PclToDescriptorSet-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PclToDescriptorSet-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<PclToDescriptorSet-request> is deprecated: use iri_perception_msgs-srv:PclToDescriptorSet-request instead.")))

(cl:ensure-generic-function 'pointcloud-val :lambda-list '(m))
(cl:defmethod pointcloud-val ((m <PclToDescriptorSet-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:pointcloud-val is deprecated.  Use iri_perception_msgs-srv:pointcloud instead.")
  (pointcloud m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PclToDescriptorSet-request>) ostream)
  "Serializes a message object of type '<PclToDescriptorSet-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pointcloud) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PclToDescriptorSet-request>) istream)
  "Deserializes a message object of type '<PclToDescriptorSet-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pointcloud) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PclToDescriptorSet-request>)))
  "Returns string type for a service object of type '<PclToDescriptorSet-request>"
  "iri_perception_msgs/PclToDescriptorSetRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToDescriptorSet-request)))
  "Returns string type for a service object of type 'PclToDescriptorSet-request"
  "iri_perception_msgs/PclToDescriptorSetRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PclToDescriptorSet-request>)))
  "Returns md5sum for a message object of type '<PclToDescriptorSet-request>"
  "f55bbc2d3d079e04fdc51edb942f1d11")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PclToDescriptorSet-request)))
  "Returns md5sum for a message object of type 'PclToDescriptorSet-request"
  "f55bbc2d3d079e04fdc51edb942f1d11")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PclToDescriptorSet-request>)))
  "Returns full string definition for message of type '<PclToDescriptorSet-request>"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 pointcloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PclToDescriptorSet-request)))
  "Returns full string definition for message of type 'PclToDescriptorSet-request"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 pointcloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PclToDescriptorSet-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pointcloud))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PclToDescriptorSet-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PclToDescriptorSet-request
    (cl:cons ':pointcloud (pointcloud msg))
))
;//! \htmlinclude PclToDescriptorSet-response.msg.html

(cl:defclass <PclToDescriptorSet-response> (roslisp-msg-protocol:ros-message)
  ((descriptor_set
    :reader descriptor_set
    :initarg :descriptor_set
    :type iri_perception_msgs-msg:DescriptorSet
    :initform (cl:make-instance 'iri_perception_msgs-msg:DescriptorSet)))
)

(cl:defclass PclToDescriptorSet-response (<PclToDescriptorSet-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PclToDescriptorSet-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PclToDescriptorSet-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<PclToDescriptorSet-response> is deprecated: use iri_perception_msgs-srv:PclToDescriptorSet-response instead.")))

(cl:ensure-generic-function 'descriptor_set-val :lambda-list '(m))
(cl:defmethod descriptor_set-val ((m <PclToDescriptorSet-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:descriptor_set-val is deprecated.  Use iri_perception_msgs-srv:descriptor_set instead.")
  (descriptor_set m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PclToDescriptorSet-response>) ostream)
  "Serializes a message object of type '<PclToDescriptorSet-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'descriptor_set) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PclToDescriptorSet-response>) istream)
  "Deserializes a message object of type '<PclToDescriptorSet-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'descriptor_set) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PclToDescriptorSet-response>)))
  "Returns string type for a service object of type '<PclToDescriptorSet-response>"
  "iri_perception_msgs/PclToDescriptorSetResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToDescriptorSet-response)))
  "Returns string type for a service object of type 'PclToDescriptorSet-response"
  "iri_perception_msgs/PclToDescriptorSetResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PclToDescriptorSet-response>)))
  "Returns md5sum for a message object of type '<PclToDescriptorSet-response>"
  "f55bbc2d3d079e04fdc51edb942f1d11")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PclToDescriptorSet-response)))
  "Returns md5sum for a message object of type 'PclToDescriptorSet-response"
  "f55bbc2d3d079e04fdc51edb942f1d11")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PclToDescriptorSet-response>)))
  "Returns full string definition for message of type '<PclToDescriptorSet-response>"
  (cl:format cl:nil "~%iri_perception_msgs/DescriptorSet descriptor_set~%~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PclToDescriptorSet-response)))
  "Returns full string definition for message of type 'PclToDescriptorSet-response"
  (cl:format cl:nil "~%iri_perception_msgs/DescriptorSet descriptor_set~%~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PclToDescriptorSet-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'descriptor_set))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PclToDescriptorSet-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PclToDescriptorSet-response
    (cl:cons ':descriptor_set (descriptor_set msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PclToDescriptorSet)))
  'PclToDescriptorSet-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PclToDescriptorSet)))
  'PclToDescriptorSet-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToDescriptorSet)))
  "Returns string type for a service object of type '<PclToDescriptorSet>"
  "iri_perception_msgs/PclToDescriptorSet")
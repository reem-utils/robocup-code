; Auto-generated. Do not edit!


(cl:in-package normal_descriptor_node-srv)


;//! \htmlinclude ndesc_pc_service-request.msg.html

(cl:defclass <ndesc_pc_service-request> (roslisp-msg-protocol:ros-message)
  ((cloth_cloud
    :reader cloth_cloud
    :initarg :cloth_cloud
    :type sensor_msgs-msg:PointCloud2
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud2)))
)

(cl:defclass ndesc_pc_service-request (<ndesc_pc_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ndesc_pc_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ndesc_pc_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name normal_descriptor_node-srv:<ndesc_pc_service-request> is deprecated: use normal_descriptor_node-srv:ndesc_pc_service-request instead.")))

(cl:ensure-generic-function 'cloth_cloud-val :lambda-list '(m))
(cl:defmethod cloth_cloud-val ((m <ndesc_pc_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-srv:cloth_cloud-val is deprecated.  Use normal_descriptor_node-srv:cloth_cloud instead.")
  (cloth_cloud m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ndesc_pc_service-request>) ostream)
  "Serializes a message object of type '<ndesc_pc_service-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'cloth_cloud) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ndesc_pc_service-request>) istream)
  "Deserializes a message object of type '<ndesc_pc_service-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'cloth_cloud) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ndesc_pc_service-request>)))
  "Returns string type for a service object of type '<ndesc_pc_service-request>"
  "normal_descriptor_node/ndesc_pc_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ndesc_pc_service-request)))
  "Returns string type for a service object of type 'ndesc_pc_service-request"
  "normal_descriptor_node/ndesc_pc_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ndesc_pc_service-request>)))
  "Returns md5sum for a message object of type '<ndesc_pc_service-request>"
  "820ec8d4b51fd678aefcb5618d6d715c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ndesc_pc_service-request)))
  "Returns md5sum for a message object of type 'ndesc_pc_service-request"
  "820ec8d4b51fd678aefcb5618d6d715c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ndesc_pc_service-request>)))
  "Returns full string definition for message of type '<ndesc_pc_service-request>"
  (cl:format cl:nil "sensor_msgs/PointCloud2 cloth_cloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ndesc_pc_service-request)))
  "Returns full string definition for message of type 'ndesc_pc_service-request"
  (cl:format cl:nil "sensor_msgs/PointCloud2 cloth_cloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ndesc_pc_service-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'cloth_cloud))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ndesc_pc_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ndesc_pc_service-request
    (cl:cons ':cloth_cloud (cloth_cloud msg))
))
;//! \htmlinclude ndesc_pc_service-response.msg.html

(cl:defclass <ndesc_pc_service-response> (roslisp-msg-protocol:ros-message)
  ((ndesc_pc_msg
    :reader ndesc_pc_msg
    :initarg :ndesc_pc_msg
    :type normal_descriptor_node-msg:ndesc_pc
    :initform (cl:make-instance 'normal_descriptor_node-msg:ndesc_pc)))
)

(cl:defclass ndesc_pc_service-response (<ndesc_pc_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ndesc_pc_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ndesc_pc_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name normal_descriptor_node-srv:<ndesc_pc_service-response> is deprecated: use normal_descriptor_node-srv:ndesc_pc_service-response instead.")))

(cl:ensure-generic-function 'ndesc_pc_msg-val :lambda-list '(m))
(cl:defmethod ndesc_pc_msg-val ((m <ndesc_pc_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader normal_descriptor_node-srv:ndesc_pc_msg-val is deprecated.  Use normal_descriptor_node-srv:ndesc_pc_msg instead.")
  (ndesc_pc_msg m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ndesc_pc_service-response>) ostream)
  "Serializes a message object of type '<ndesc_pc_service-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ndesc_pc_msg) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ndesc_pc_service-response>) istream)
  "Deserializes a message object of type '<ndesc_pc_service-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ndesc_pc_msg) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ndesc_pc_service-response>)))
  "Returns string type for a service object of type '<ndesc_pc_service-response>"
  "normal_descriptor_node/ndesc_pc_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ndesc_pc_service-response)))
  "Returns string type for a service object of type 'ndesc_pc_service-response"
  "normal_descriptor_node/ndesc_pc_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ndesc_pc_service-response>)))
  "Returns md5sum for a message object of type '<ndesc_pc_service-response>"
  "820ec8d4b51fd678aefcb5618d6d715c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ndesc_pc_service-response)))
  "Returns md5sum for a message object of type 'ndesc_pc_service-response"
  "820ec8d4b51fd678aefcb5618d6d715c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ndesc_pc_service-response>)))
  "Returns full string definition for message of type '<ndesc_pc_service-response>"
  (cl:format cl:nil "normal_descriptor_node/ndesc_pc ndesc_pc_msg~%~%~%================================================================================~%MSG: normal_descriptor_node/ndesc_pc~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%normal_descriptor_node/ndesc[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: normal_descriptor_node/ndesc~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 ori~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ndesc_pc_service-response)))
  "Returns full string definition for message of type 'ndesc_pc_service-response"
  (cl:format cl:nil "normal_descriptor_node/ndesc_pc ndesc_pc_msg~%~%~%================================================================================~%MSG: normal_descriptor_node/ndesc_pc~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%normal_descriptor_node/ndesc[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: normal_descriptor_node/ndesc~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 ori~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ndesc_pc_service-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ndesc_pc_msg))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ndesc_pc_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ndesc_pc_service-response
    (cl:cons ':ndesc_pc_msg (ndesc_pc_msg msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ndesc_pc_service)))
  'ndesc_pc_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ndesc_pc_service)))
  'ndesc_pc_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ndesc_pc_service)))
  "Returns string type for a service object of type '<ndesc_pc_service>"
  "normal_descriptor_node/ndesc_pc_service")
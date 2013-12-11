; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude PclToImg-request.msg.html

(cl:defclass <PclToImg-request> (roslisp-msg-protocol:ros-message)
  ((pointcloud
    :reader pointcloud
    :initarg :pointcloud
    :type sensor_msgs-msg:PointCloud2
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud2)))
)

(cl:defclass PclToImg-request (<PclToImg-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PclToImg-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PclToImg-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<PclToImg-request> is deprecated: use iri_perception_msgs-srv:PclToImg-request instead.")))

(cl:ensure-generic-function 'pointcloud-val :lambda-list '(m))
(cl:defmethod pointcloud-val ((m <PclToImg-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:pointcloud-val is deprecated.  Use iri_perception_msgs-srv:pointcloud instead.")
  (pointcloud m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PclToImg-request>) ostream)
  "Serializes a message object of type '<PclToImg-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pointcloud) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PclToImg-request>) istream)
  "Deserializes a message object of type '<PclToImg-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pointcloud) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PclToImg-request>)))
  "Returns string type for a service object of type '<PclToImg-request>"
  "iri_perception_msgs/PclToImgRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToImg-request)))
  "Returns string type for a service object of type 'PclToImg-request"
  "iri_perception_msgs/PclToImgRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PclToImg-request>)))
  "Returns md5sum for a message object of type '<PclToImg-request>"
  "1036a14b8c4c20601506406b1e3a4ca1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PclToImg-request)))
  "Returns md5sum for a message object of type 'PclToImg-request"
  "1036a14b8c4c20601506406b1e3a4ca1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PclToImg-request>)))
  "Returns full string definition for message of type '<PclToImg-request>"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 pointcloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PclToImg-request)))
  "Returns full string definition for message of type 'PclToImg-request"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 pointcloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PclToImg-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pointcloud))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PclToImg-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PclToImg-request
    (cl:cons ':pointcloud (pointcloud msg))
))
;//! \htmlinclude PclToImg-response.msg.html

(cl:defclass <PclToImg-response> (roslisp-msg-protocol:ros-message)
  ((image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass PclToImg-response (<PclToImg-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PclToImg-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PclToImg-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<PclToImg-response> is deprecated: use iri_perception_msgs-srv:PclToImg-response instead.")))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <PclToImg-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:image-val is deprecated.  Use iri_perception_msgs-srv:image instead.")
  (image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PclToImg-response>) ostream)
  "Serializes a message object of type '<PclToImg-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PclToImg-response>) istream)
  "Deserializes a message object of type '<PclToImg-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PclToImg-response>)))
  "Returns string type for a service object of type '<PclToImg-response>"
  "iri_perception_msgs/PclToImgResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToImg-response)))
  "Returns string type for a service object of type 'PclToImg-response"
  "iri_perception_msgs/PclToImgResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PclToImg-response>)))
  "Returns md5sum for a message object of type '<PclToImg-response>"
  "1036a14b8c4c20601506406b1e3a4ca1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PclToImg-response)))
  "Returns md5sum for a message object of type 'PclToImg-response"
  "1036a14b8c4c20601506406b1e3a4ca1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PclToImg-response>)))
  "Returns full string definition for message of type '<PclToImg-response>"
  (cl:format cl:nil "~%sensor_msgs/Image image~%~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PclToImg-response)))
  "Returns full string definition for message of type 'PclToImg-response"
  (cl:format cl:nil "~%sensor_msgs/Image image~%~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PclToImg-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PclToImg-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PclToImg-response
    (cl:cons ':image (image msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PclToImg)))
  'PclToImg-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PclToImg)))
  'PclToImg-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToImg)))
  "Returns string type for a service object of type '<PclToImg>"
  "iri_perception_msgs/PclToImg")
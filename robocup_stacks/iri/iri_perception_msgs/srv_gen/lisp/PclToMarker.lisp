; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude PclToMarker-request.msg.html

(cl:defclass <PclToMarker-request> (roslisp-msg-protocol:ros-message)
  ((pointcloud
    :reader pointcloud
    :initarg :pointcloud
    :type sensor_msgs-msg:PointCloud2
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud2)))
)

(cl:defclass PclToMarker-request (<PclToMarker-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PclToMarker-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PclToMarker-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<PclToMarker-request> is deprecated: use iri_perception_msgs-srv:PclToMarker-request instead.")))

(cl:ensure-generic-function 'pointcloud-val :lambda-list '(m))
(cl:defmethod pointcloud-val ((m <PclToMarker-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:pointcloud-val is deprecated.  Use iri_perception_msgs-srv:pointcloud instead.")
  (pointcloud m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PclToMarker-request>) ostream)
  "Serializes a message object of type '<PclToMarker-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pointcloud) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PclToMarker-request>) istream)
  "Deserializes a message object of type '<PclToMarker-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pointcloud) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PclToMarker-request>)))
  "Returns string type for a service object of type '<PclToMarker-request>"
  "iri_perception_msgs/PclToMarkerRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToMarker-request)))
  "Returns string type for a service object of type 'PclToMarker-request"
  "iri_perception_msgs/PclToMarkerRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PclToMarker-request>)))
  "Returns md5sum for a message object of type '<PclToMarker-request>"
  "e8ebdfd2bdabaf1623d8d3b6f7d39096")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PclToMarker-request)))
  "Returns md5sum for a message object of type 'PclToMarker-request"
  "e8ebdfd2bdabaf1623d8d3b6f7d39096")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PclToMarker-request>)))
  "Returns full string definition for message of type '<PclToMarker-request>"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 pointcloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PclToMarker-request)))
  "Returns full string definition for message of type 'PclToMarker-request"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 pointcloud~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PclToMarker-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pointcloud))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PclToMarker-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PclToMarker-request
    (cl:cons ':pointcloud (pointcloud msg))
))
;//! \htmlinclude PclToMarker-response.msg.html

(cl:defclass <PclToMarker-response> (roslisp-msg-protocol:ros-message)
  ((marker
    :reader marker
    :initarg :marker
    :type visualization_msgs-msg:Marker
    :initform (cl:make-instance 'visualization_msgs-msg:Marker)))
)

(cl:defclass PclToMarker-response (<PclToMarker-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PclToMarker-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PclToMarker-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<PclToMarker-response> is deprecated: use iri_perception_msgs-srv:PclToMarker-response instead.")))

(cl:ensure-generic-function 'marker-val :lambda-list '(m))
(cl:defmethod marker-val ((m <PclToMarker-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:marker-val is deprecated.  Use iri_perception_msgs-srv:marker instead.")
  (marker m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PclToMarker-response>) ostream)
  "Serializes a message object of type '<PclToMarker-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'marker) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PclToMarker-response>) istream)
  "Deserializes a message object of type '<PclToMarker-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'marker) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PclToMarker-response>)))
  "Returns string type for a service object of type '<PclToMarker-response>"
  "iri_perception_msgs/PclToMarkerResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToMarker-response)))
  "Returns string type for a service object of type 'PclToMarker-response"
  "iri_perception_msgs/PclToMarkerResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PclToMarker-response>)))
  "Returns md5sum for a message object of type '<PclToMarker-response>"
  "e8ebdfd2bdabaf1623d8d3b6f7d39096")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PclToMarker-response)))
  "Returns md5sum for a message object of type 'PclToMarker-response"
  "e8ebdfd2bdabaf1623d8d3b6f7d39096")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PclToMarker-response>)))
  "Returns full string definition for message of type '<PclToMarker-response>"
  (cl:format cl:nil "~%visualization_msgs/Marker marker~%~%~%================================================================================~%MSG: visualization_msgs/Marker~%# See http://www.ros.org/wiki/rviz/DisplayTypes/Marker and http://www.ros.org/wiki/rviz/Tutorials/Markers%3A%20Basic%20Shapes for more information on using this message with rviz~%~%uint8 ARROW=0~%uint8 CUBE=1~%uint8 SPHERE=2~%uint8 CYLINDER=3~%uint8 LINE_STRIP=4~%uint8 LINE_LIST=5~%uint8 CUBE_LIST=6~%uint8 SPHERE_LIST=7~%uint8 POINTS=8~%uint8 TEXT_VIEW_FACING=9~%uint8 MESH_RESOURCE=10~%uint8 TRIANGLE_LIST=11~%~%uint8 ADD=0~%uint8 MODIFY=0~%uint8 DELETE=2~%~%Header header                        # header for time/frame information~%string ns                            # Namespace to place this object in... used in conjunction with id to create a unique name for the object~%int32 id 		                         # object ID useful in conjunction with the namespace for manipulating and deleting the object later~%int32 type 		                       # Type of object~%int32 action 	                       # 0 add/modify an object, 1 (deprecated), 2 deletes an object~%geometry_msgs/Pose pose                 # Pose of the object~%geometry_msgs/Vector3 scale             # Scale of the object 1,1,1 means default (usually 1 meter square)~%std_msgs/ColorRGBA color             # Color [0.0-1.0]~%duration lifetime                    # How long the object should last before being automatically deleted.  0 means forever~%bool frame_locked                    # If this marker should be frame-locked, i.e. retransformed into its frame every timestep~%~%#Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)~%geometry_msgs/Point[] points~%#Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)~%#number of colors must either be 0 or equal to the number of points~%#NOTE: alpha is not yet used~%std_msgs/ColorRGBA[] colors~%~%# NOTE: only used for text markers~%string text~%~%# NOTE: only used for MESH_RESOURCE markers~%string mesh_resource~%bool mesh_use_embedded_materials~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: std_msgs/ColorRGBA~%float32 r~%float32 g~%float32 b~%float32 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PclToMarker-response)))
  "Returns full string definition for message of type 'PclToMarker-response"
  (cl:format cl:nil "~%visualization_msgs/Marker marker~%~%~%================================================================================~%MSG: visualization_msgs/Marker~%# See http://www.ros.org/wiki/rviz/DisplayTypes/Marker and http://www.ros.org/wiki/rviz/Tutorials/Markers%3A%20Basic%20Shapes for more information on using this message with rviz~%~%uint8 ARROW=0~%uint8 CUBE=1~%uint8 SPHERE=2~%uint8 CYLINDER=3~%uint8 LINE_STRIP=4~%uint8 LINE_LIST=5~%uint8 CUBE_LIST=6~%uint8 SPHERE_LIST=7~%uint8 POINTS=8~%uint8 TEXT_VIEW_FACING=9~%uint8 MESH_RESOURCE=10~%uint8 TRIANGLE_LIST=11~%~%uint8 ADD=0~%uint8 MODIFY=0~%uint8 DELETE=2~%~%Header header                        # header for time/frame information~%string ns                            # Namespace to place this object in... used in conjunction with id to create a unique name for the object~%int32 id 		                         # object ID useful in conjunction with the namespace for manipulating and deleting the object later~%int32 type 		                       # Type of object~%int32 action 	                       # 0 add/modify an object, 1 (deprecated), 2 deletes an object~%geometry_msgs/Pose pose                 # Pose of the object~%geometry_msgs/Vector3 scale             # Scale of the object 1,1,1 means default (usually 1 meter square)~%std_msgs/ColorRGBA color             # Color [0.0-1.0]~%duration lifetime                    # How long the object should last before being automatically deleted.  0 means forever~%bool frame_locked                    # If this marker should be frame-locked, i.e. retransformed into its frame every timestep~%~%#Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)~%geometry_msgs/Point[] points~%#Only used if the type specified has some use for them (eg. POINTS, LINE_STRIP, ...)~%#number of colors must either be 0 or equal to the number of points~%#NOTE: alpha is not yet used~%std_msgs/ColorRGBA[] colors~%~%# NOTE: only used for text markers~%string text~%~%# NOTE: only used for MESH_RESOURCE markers~%string mesh_resource~%bool mesh_use_embedded_materials~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: std_msgs/ColorRGBA~%float32 r~%float32 g~%float32 b~%float32 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PclToMarker-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'marker))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PclToMarker-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PclToMarker-response
    (cl:cons ':marker (marker msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PclToMarker)))
  'PclToMarker-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PclToMarker)))
  'PclToMarker-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PclToMarker)))
  "Returns string type for a service object of type '<PclToMarker>"
  "iri_perception_msgs/PclToMarker")
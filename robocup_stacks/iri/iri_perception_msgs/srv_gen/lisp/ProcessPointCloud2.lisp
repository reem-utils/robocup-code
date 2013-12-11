; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude ProcessPointCloud2-request.msg.html

(cl:defclass <ProcessPointCloud2-request> (roslisp-msg-protocol:ros-message)
  ((input
    :reader input
    :initarg :input
    :type sensor_msgs-msg:PointCloud2
    :initform (cl:make-instance 'sensor_msgs-msg:PointCloud2)))
)

(cl:defclass ProcessPointCloud2-request (<ProcessPointCloud2-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ProcessPointCloud2-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ProcessPointCloud2-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<ProcessPointCloud2-request> is deprecated: use iri_perception_msgs-srv:ProcessPointCloud2-request instead.")))

(cl:ensure-generic-function 'input-val :lambda-list '(m))
(cl:defmethod input-val ((m <ProcessPointCloud2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:input-val is deprecated.  Use iri_perception_msgs-srv:input instead.")
  (input m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ProcessPointCloud2-request>) ostream)
  "Serializes a message object of type '<ProcessPointCloud2-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'input) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ProcessPointCloud2-request>) istream)
  "Deserializes a message object of type '<ProcessPointCloud2-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'input) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ProcessPointCloud2-request>)))
  "Returns string type for a service object of type '<ProcessPointCloud2-request>"
  "iri_perception_msgs/ProcessPointCloud2Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ProcessPointCloud2-request)))
  "Returns string type for a service object of type 'ProcessPointCloud2-request"
  "iri_perception_msgs/ProcessPointCloud2Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ProcessPointCloud2-request>)))
  "Returns md5sum for a message object of type '<ProcessPointCloud2-request>"
  "55c5f2a1ba5379341fa496de58e8d437")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ProcessPointCloud2-request)))
  "Returns md5sum for a message object of type 'ProcessPointCloud2-request"
  "55c5f2a1ba5379341fa496de58e8d437")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ProcessPointCloud2-request>)))
  "Returns full string definition for message of type '<ProcessPointCloud2-request>"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 input~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ProcessPointCloud2-request)))
  "Returns full string definition for message of type 'ProcessPointCloud2-request"
  (cl:format cl:nil "~%sensor_msgs/PointCloud2 input~%~%================================================================================~%MSG: sensor_msgs/PointCloud2~%# This message holds a collection of N-dimensional points, which may~%# contain additional information such as normals, intensity, etc. The~%# point data is stored as a binary blob, its layout described by the~%# contents of the \"fields\" array.~%~%# The point cloud data may be organized 2d (image-like) or 1d~%# (unordered). Point clouds organized as 2d images may be produced by~%# camera depth sensors such as stereo or time-of-flight.~%~%# Time of sensor data acquisition, and the coordinate frame ID (for 3d~%# points).~%Header header~%~%# 2D structure of the point cloud. If the cloud is unordered, height is~%# 1 and width is the length of the point cloud.~%uint32 height~%uint32 width~%~%# Describes the channels and their layout in the binary data blob.~%PointField[] fields~%~%bool    is_bigendian # Is this data bigendian?~%uint32  point_step   # Length of a point in bytes~%uint32  row_step     # Length of a row in bytes~%uint8[] data         # Actual point data, size is (row_step*height)~%~%bool is_dense        # True if there are no invalid points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: sensor_msgs/PointField~%# This message holds the description of one point entry in the~%# PointCloud2 message format.~%uint8 INT8    = 1~%uint8 UINT8   = 2~%uint8 INT16   = 3~%uint8 UINT16  = 4~%uint8 INT32   = 5~%uint8 UINT32  = 6~%uint8 FLOAT32 = 7~%uint8 FLOAT64 = 8~%~%string name      # Name of field~%uint32 offset    # Offset from start of point struct~%uint8  datatype  # Datatype enumeration, see above~%uint32 count     # How many elements in the field~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ProcessPointCloud2-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'input))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ProcessPointCloud2-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ProcessPointCloud2-request
    (cl:cons ':input (input msg))
))
;//! \htmlinclude ProcessPointCloud2-response.msg.html

(cl:defclass <ProcessPointCloud2-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ProcessPointCloud2-response (<ProcessPointCloud2-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ProcessPointCloud2-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ProcessPointCloud2-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<ProcessPointCloud2-response> is deprecated: use iri_perception_msgs-srv:ProcessPointCloud2-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ProcessPointCloud2-response>) ostream)
  "Serializes a message object of type '<ProcessPointCloud2-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ProcessPointCloud2-response>) istream)
  "Deserializes a message object of type '<ProcessPointCloud2-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ProcessPointCloud2-response>)))
  "Returns string type for a service object of type '<ProcessPointCloud2-response>"
  "iri_perception_msgs/ProcessPointCloud2Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ProcessPointCloud2-response)))
  "Returns string type for a service object of type 'ProcessPointCloud2-response"
  "iri_perception_msgs/ProcessPointCloud2Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ProcessPointCloud2-response>)))
  "Returns md5sum for a message object of type '<ProcessPointCloud2-response>"
  "55c5f2a1ba5379341fa496de58e8d437")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ProcessPointCloud2-response)))
  "Returns md5sum for a message object of type 'ProcessPointCloud2-response"
  "55c5f2a1ba5379341fa496de58e8d437")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ProcessPointCloud2-response>)))
  "Returns full string definition for message of type '<ProcessPointCloud2-response>"
  (cl:format cl:nil "~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ProcessPointCloud2-response)))
  "Returns full string definition for message of type 'ProcessPointCloud2-response"
  (cl:format cl:nil "~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ProcessPointCloud2-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ProcessPointCloud2-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ProcessPointCloud2-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ProcessPointCloud2)))
  'ProcessPointCloud2-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ProcessPointCloud2)))
  'ProcessPointCloud2-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ProcessPointCloud2)))
  "Returns string type for a service object of type '<ProcessPointCloud2>"
  "iri_perception_msgs/ProcessPointCloud2")
; Auto-generated. Do not edit!


(cl:in-package iri_sift-srv)


;//! \htmlinclude GeoVwSetSrv-request.msg.html

(cl:defclass <GeoVwSetSrv-request> (roslisp-msg-protocol:ros-message)
  ((image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass GeoVwSetSrv-request (<GeoVwSetSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GeoVwSetSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GeoVwSetSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_sift-srv:<GeoVwSetSrv-request> is deprecated: use iri_sift-srv:GeoVwSetSrv-request instead.")))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <GeoVwSetSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_sift-srv:image-val is deprecated.  Use iri_sift-srv:image instead.")
  (image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GeoVwSetSrv-request>) ostream)
  "Serializes a message object of type '<GeoVwSetSrv-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GeoVwSetSrv-request>) istream)
  "Deserializes a message object of type '<GeoVwSetSrv-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GeoVwSetSrv-request>)))
  "Returns string type for a service object of type '<GeoVwSetSrv-request>"
  "iri_sift/GeoVwSetSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVwSetSrv-request)))
  "Returns string type for a service object of type 'GeoVwSetSrv-request"
  "iri_sift/GeoVwSetSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GeoVwSetSrv-request>)))
  "Returns md5sum for a message object of type '<GeoVwSetSrv-request>"
  "daa8e81549d2bfdca961b9581eed855d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GeoVwSetSrv-request)))
  "Returns md5sum for a message object of type 'GeoVwSetSrv-request"
  "daa8e81549d2bfdca961b9581eed855d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GeoVwSetSrv-request>)))
  "Returns full string definition for message of type '<GeoVwSetSrv-request>"
  (cl:format cl:nil "sensor_msgs/Image image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GeoVwSetSrv-request)))
  "Returns full string definition for message of type 'GeoVwSetSrv-request"
  (cl:format cl:nil "sensor_msgs/Image image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GeoVwSetSrv-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GeoVwSetSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GeoVwSetSrv-request
    (cl:cons ':image (image msg))
))
;//! \htmlinclude GeoVwSetSrv-response.msg.html

(cl:defclass <GeoVwSetSrv-response> (roslisp-msg-protocol:ros-message)
  ((geo_vw_set
    :reader geo_vw_set
    :initarg :geo_vw_set
    :type iri_perception_msgs-msg:GeoVwSet
    :initform (cl:make-instance 'iri_perception_msgs-msg:GeoVwSet)))
)

(cl:defclass GeoVwSetSrv-response (<GeoVwSetSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GeoVwSetSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GeoVwSetSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_sift-srv:<GeoVwSetSrv-response> is deprecated: use iri_sift-srv:GeoVwSetSrv-response instead.")))

(cl:ensure-generic-function 'geo_vw_set-val :lambda-list '(m))
(cl:defmethod geo_vw_set-val ((m <GeoVwSetSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_sift-srv:geo_vw_set-val is deprecated.  Use iri_sift-srv:geo_vw_set instead.")
  (geo_vw_set m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GeoVwSetSrv-response>) ostream)
  "Serializes a message object of type '<GeoVwSetSrv-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'geo_vw_set) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GeoVwSetSrv-response>) istream)
  "Deserializes a message object of type '<GeoVwSetSrv-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'geo_vw_set) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GeoVwSetSrv-response>)))
  "Returns string type for a service object of type '<GeoVwSetSrv-response>"
  "iri_sift/GeoVwSetSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVwSetSrv-response)))
  "Returns string type for a service object of type 'GeoVwSetSrv-response"
  "iri_sift/GeoVwSetSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GeoVwSetSrv-response>)))
  "Returns md5sum for a message object of type '<GeoVwSetSrv-response>"
  "daa8e81549d2bfdca961b9581eed855d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GeoVwSetSrv-response)))
  "Returns md5sum for a message object of type 'GeoVwSetSrv-response"
  "daa8e81549d2bfdca961b9581eed855d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GeoVwSetSrv-response>)))
  "Returns full string definition for message of type '<GeoVwSetSrv-response>"
  (cl:format cl:nil "iri_perception_msgs/GeoVwSet geo_vw_set~%~%~%================================================================================~%MSG: iri_perception_msgs/GeoVwSet~%iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GeoVwSetSrv-response)))
  "Returns full string definition for message of type 'GeoVwSetSrv-response"
  (cl:format cl:nil "iri_perception_msgs/GeoVwSet geo_vw_set~%~%~%================================================================================~%MSG: iri_perception_msgs/GeoVwSet~%iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GeoVwSetSrv-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'geo_vw_set))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GeoVwSetSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GeoVwSetSrv-response
    (cl:cons ':geo_vw_set (geo_vw_set msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GeoVwSetSrv)))
  'GeoVwSetSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GeoVwSetSrv)))
  'GeoVwSetSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVwSetSrv)))
  "Returns string type for a service object of type '<GeoVwSetSrv>"
  "iri_sift/GeoVwSetSrv")
; Auto-generated. Do not edit!


(cl:in-package iri_sift-srv)


;//! \htmlinclude DescriptorsFromImage-request.msg.html

(cl:defclass <DescriptorsFromImage-request> (roslisp-msg-protocol:ros-message)
  ((image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass DescriptorsFromImage-request (<DescriptorsFromImage-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DescriptorsFromImage-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DescriptorsFromImage-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_sift-srv:<DescriptorsFromImage-request> is deprecated: use iri_sift-srv:DescriptorsFromImage-request instead.")))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <DescriptorsFromImage-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_sift-srv:image-val is deprecated.  Use iri_sift-srv:image instead.")
  (image m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DescriptorsFromImage-request>) ostream)
  "Serializes a message object of type '<DescriptorsFromImage-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DescriptorsFromImage-request>) istream)
  "Deserializes a message object of type '<DescriptorsFromImage-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DescriptorsFromImage-request>)))
  "Returns string type for a service object of type '<DescriptorsFromImage-request>"
  "iri_sift/DescriptorsFromImageRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DescriptorsFromImage-request)))
  "Returns string type for a service object of type 'DescriptorsFromImage-request"
  "iri_sift/DescriptorsFromImageRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DescriptorsFromImage-request>)))
  "Returns md5sum for a message object of type '<DescriptorsFromImage-request>"
  "3f84e2bbe8799c8c0db43a5ff96da0c4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DescriptorsFromImage-request)))
  "Returns md5sum for a message object of type 'DescriptorsFromImage-request"
  "3f84e2bbe8799c8c0db43a5ff96da0c4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DescriptorsFromImage-request>)))
  "Returns full string definition for message of type '<DescriptorsFromImage-request>"
  (cl:format cl:nil "~%sensor_msgs/Image image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DescriptorsFromImage-request)))
  "Returns full string definition for message of type 'DescriptorsFromImage-request"
  (cl:format cl:nil "~%sensor_msgs/Image image~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DescriptorsFromImage-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DescriptorsFromImage-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DescriptorsFromImage-request
    (cl:cons ':image (image msg))
))
;//! \htmlinclude DescriptorsFromImage-response.msg.html

(cl:defclass <DescriptorsFromImage-response> (roslisp-msg-protocol:ros-message)
  ((descriptor_set
    :reader descriptor_set
    :initarg :descriptor_set
    :type iri_perception_msgs-msg:DescriptorSet
    :initform (cl:make-instance 'iri_perception_msgs-msg:DescriptorSet)))
)

(cl:defclass DescriptorsFromImage-response (<DescriptorsFromImage-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DescriptorsFromImage-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DescriptorsFromImage-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_sift-srv:<DescriptorsFromImage-response> is deprecated: use iri_sift-srv:DescriptorsFromImage-response instead.")))

(cl:ensure-generic-function 'descriptor_set-val :lambda-list '(m))
(cl:defmethod descriptor_set-val ((m <DescriptorsFromImage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_sift-srv:descriptor_set-val is deprecated.  Use iri_sift-srv:descriptor_set instead.")
  (descriptor_set m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DescriptorsFromImage-response>) ostream)
  "Serializes a message object of type '<DescriptorsFromImage-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'descriptor_set) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DescriptorsFromImage-response>) istream)
  "Deserializes a message object of type '<DescriptorsFromImage-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'descriptor_set) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DescriptorsFromImage-response>)))
  "Returns string type for a service object of type '<DescriptorsFromImage-response>"
  "iri_sift/DescriptorsFromImageResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DescriptorsFromImage-response)))
  "Returns string type for a service object of type 'DescriptorsFromImage-response"
  "iri_sift/DescriptorsFromImageResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DescriptorsFromImage-response>)))
  "Returns md5sum for a message object of type '<DescriptorsFromImage-response>"
  "3f84e2bbe8799c8c0db43a5ff96da0c4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DescriptorsFromImage-response)))
  "Returns md5sum for a message object of type 'DescriptorsFromImage-response"
  "3f84e2bbe8799c8c0db43a5ff96da0c4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DescriptorsFromImage-response>)))
  "Returns full string definition for message of type '<DescriptorsFromImage-response>"
  (cl:format cl:nil "~%iri_perception_msgs/DescriptorSet descriptor_set~%~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DescriptorsFromImage-response)))
  "Returns full string definition for message of type 'DescriptorsFromImage-response"
  (cl:format cl:nil "~%iri_perception_msgs/DescriptorSet descriptor_set~%~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DescriptorsFromImage-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'descriptor_set))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DescriptorsFromImage-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DescriptorsFromImage-response
    (cl:cons ':descriptor_set (descriptor_set msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DescriptorsFromImage)))
  'DescriptorsFromImage-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DescriptorsFromImage)))
  'DescriptorsFromImage-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DescriptorsFromImage)))
  "Returns string type for a service object of type '<DescriptorsFromImage>"
  "iri_sift/DescriptorsFromImage")
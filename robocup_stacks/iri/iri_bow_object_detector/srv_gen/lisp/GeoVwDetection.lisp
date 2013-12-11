; Auto-generated. Do not edit!


(cl:in-package iri_bow_object_detector-srv)


;//! \htmlinclude GeoVwDetection-request.msg.html

(cl:defclass <GeoVwDetection-request> (roslisp-msg-protocol:ros-message)
  ((geo_vw_sets
    :reader geo_vw_sets
    :initarg :geo_vw_sets
    :type (cl:vector iri_perception_msgs-msg:GeoVwSet)
   :initform (cl:make-array 0 :element-type 'iri_perception_msgs-msg:GeoVwSet :initial-element (cl:make-instance 'iri_perception_msgs-msg:GeoVwSet)))
   (image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (mask
    :reader mask
    :initarg :mask
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass GeoVwDetection-request (<GeoVwDetection-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GeoVwDetection-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GeoVwDetection-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_bow_object_detector-srv:<GeoVwDetection-request> is deprecated: use iri_bow_object_detector-srv:GeoVwDetection-request instead.")))

(cl:ensure-generic-function 'geo_vw_sets-val :lambda-list '(m))
(cl:defmethod geo_vw_sets-val ((m <GeoVwDetection-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:geo_vw_sets-val is deprecated.  Use iri_bow_object_detector-srv:geo_vw_sets instead.")
  (geo_vw_sets m))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <GeoVwDetection-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:image-val is deprecated.  Use iri_bow_object_detector-srv:image instead.")
  (image m))

(cl:ensure-generic-function 'mask-val :lambda-list '(m))
(cl:defmethod mask-val ((m <GeoVwDetection-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:mask-val is deprecated.  Use iri_bow_object_detector-srv:mask instead.")
  (mask m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GeoVwDetection-request>) ostream)
  "Serializes a message object of type '<GeoVwDetection-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'geo_vw_sets))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'geo_vw_sets))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'mask) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GeoVwDetection-request>) istream)
  "Deserializes a message object of type '<GeoVwDetection-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'geo_vw_sets) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'geo_vw_sets)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'iri_perception_msgs-msg:GeoVwSet))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'mask) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GeoVwDetection-request>)))
  "Returns string type for a service object of type '<GeoVwDetection-request>"
  "iri_bow_object_detector/GeoVwDetectionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVwDetection-request)))
  "Returns string type for a service object of type 'GeoVwDetection-request"
  "iri_bow_object_detector/GeoVwDetectionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GeoVwDetection-request>)))
  "Returns md5sum for a message object of type '<GeoVwDetection-request>"
  "a9527c0fdb9971ff28f08c026548c643")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GeoVwDetection-request)))
  "Returns md5sum for a message object of type 'GeoVwDetection-request"
  "a9527c0fdb9971ff28f08c026548c643")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GeoVwDetection-request>)))
  "Returns full string definition for message of type '<GeoVwDetection-request>"
  (cl:format cl:nil "iri_perception_msgs/GeoVwSet[] geo_vw_sets~%sensor_msgs/Image image~%sensor_msgs/Image mask~%~%================================================================================~%MSG: iri_perception_msgs/GeoVwSet~%iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GeoVwDetection-request)))
  "Returns full string definition for message of type 'GeoVwDetection-request"
  (cl:format cl:nil "iri_perception_msgs/GeoVwSet[] geo_vw_sets~%sensor_msgs/Image image~%sensor_msgs/Image mask~%~%================================================================================~%MSG: iri_perception_msgs/GeoVwSet~%iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GeoVwDetection-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'geo_vw_sets) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'mask))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GeoVwDetection-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GeoVwDetection-request
    (cl:cons ':geo_vw_sets (geo_vw_sets msg))
    (cl:cons ':image (image msg))
    (cl:cons ':mask (mask msg))
))
;//! \htmlinclude GeoVwDetection-response.msg.html

(cl:defclass <GeoVwDetection-response> (roslisp-msg-protocol:ros-message)
  ((posible_solutions
    :reader posible_solutions
    :initarg :posible_solutions
    :type (cl:vector iri_bow_object_detector-msg:ObjectBox)
   :initform (cl:make-array 0 :element-type 'iri_bow_object_detector-msg:ObjectBox :initial-element (cl:make-instance 'iri_bow_object_detector-msg:ObjectBox))))
)

(cl:defclass GeoVwDetection-response (<GeoVwDetection-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GeoVwDetection-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GeoVwDetection-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_bow_object_detector-srv:<GeoVwDetection-response> is deprecated: use iri_bow_object_detector-srv:GeoVwDetection-response instead.")))

(cl:ensure-generic-function 'posible_solutions-val :lambda-list '(m))
(cl:defmethod posible_solutions-val ((m <GeoVwDetection-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:posible_solutions-val is deprecated.  Use iri_bow_object_detector-srv:posible_solutions instead.")
  (posible_solutions m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GeoVwDetection-response>) ostream)
  "Serializes a message object of type '<GeoVwDetection-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'posible_solutions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'posible_solutions))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GeoVwDetection-response>) istream)
  "Deserializes a message object of type '<GeoVwDetection-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'posible_solutions) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'posible_solutions)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'iri_bow_object_detector-msg:ObjectBox))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GeoVwDetection-response>)))
  "Returns string type for a service object of type '<GeoVwDetection-response>"
  "iri_bow_object_detector/GeoVwDetectionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVwDetection-response)))
  "Returns string type for a service object of type 'GeoVwDetection-response"
  "iri_bow_object_detector/GeoVwDetectionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GeoVwDetection-response>)))
  "Returns md5sum for a message object of type '<GeoVwDetection-response>"
  "a9527c0fdb9971ff28f08c026548c643")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GeoVwDetection-response)))
  "Returns md5sum for a message object of type 'GeoVwDetection-response"
  "a9527c0fdb9971ff28f08c026548c643")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GeoVwDetection-response>)))
  "Returns full string definition for message of type '<GeoVwDetection-response>"
  (cl:format cl:nil "iri_bow_object_detector/ObjectBox[] posible_solutions~%~%~%================================================================================~%MSG: iri_bow_object_detector/ObjectBox~%iri_perception_msgs/ImagePoint point1~%iri_perception_msgs/ImagePoint point2~%float32 value~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GeoVwDetection-response)))
  "Returns full string definition for message of type 'GeoVwDetection-response"
  (cl:format cl:nil "iri_bow_object_detector/ObjectBox[] posible_solutions~%~%~%================================================================================~%MSG: iri_bow_object_detector/ObjectBox~%iri_perception_msgs/ImagePoint point1~%iri_perception_msgs/ImagePoint point2~%float32 value~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GeoVwDetection-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'posible_solutions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GeoVwDetection-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GeoVwDetection-response
    (cl:cons ':posible_solutions (posible_solutions msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GeoVwDetection)))
  'GeoVwDetection-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GeoVwDetection)))
  'GeoVwDetection-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GeoVwDetection)))
  "Returns string type for a service object of type '<GeoVwDetection>"
  "iri_bow_object_detector/GeoVwDetection")
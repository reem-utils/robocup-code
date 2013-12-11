; Auto-generated. Do not edit!


(cl:in-package iri_bow_object_detector-srv)


;//! \htmlinclude RefineGraspPoint-request.msg.html

(cl:defclass <RefineGraspPoint-request> (roslisp-msg-protocol:ros-message)
  ((posible_solutions
    :reader posible_solutions
    :initarg :posible_solutions
    :type (cl:vector iri_bow_object_detector-msg:ObjectBox)
   :initform (cl:make-array 0 :element-type 'iri_bow_object_detector-msg:ObjectBox :initial-element (cl:make-instance 'iri_bow_object_detector-msg:ObjectBox)))
   (image
    :reader image
    :initarg :image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (descriptor_set
    :reader descriptor_set
    :initarg :descriptor_set
    :type iri_perception_msgs-msg:DescriptorSet
    :initform (cl:make-instance 'iri_perception_msgs-msg:DescriptorSet)))
)

(cl:defclass RefineGraspPoint-request (<RefineGraspPoint-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RefineGraspPoint-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RefineGraspPoint-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_bow_object_detector-srv:<RefineGraspPoint-request> is deprecated: use iri_bow_object_detector-srv:RefineGraspPoint-request instead.")))

(cl:ensure-generic-function 'posible_solutions-val :lambda-list '(m))
(cl:defmethod posible_solutions-val ((m <RefineGraspPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:posible_solutions-val is deprecated.  Use iri_bow_object_detector-srv:posible_solutions instead.")
  (posible_solutions m))

(cl:ensure-generic-function 'image-val :lambda-list '(m))
(cl:defmethod image-val ((m <RefineGraspPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:image-val is deprecated.  Use iri_bow_object_detector-srv:image instead.")
  (image m))

(cl:ensure-generic-function 'descriptor_set-val :lambda-list '(m))
(cl:defmethod descriptor_set-val ((m <RefineGraspPoint-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:descriptor_set-val is deprecated.  Use iri_bow_object_detector-srv:descriptor_set instead.")
  (descriptor_set m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RefineGraspPoint-request>) ostream)
  "Serializes a message object of type '<RefineGraspPoint-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'posible_solutions))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'posible_solutions))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'descriptor_set) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RefineGraspPoint-request>) istream)
  "Deserializes a message object of type '<RefineGraspPoint-request>"
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'descriptor_set) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RefineGraspPoint-request>)))
  "Returns string type for a service object of type '<RefineGraspPoint-request>"
  "iri_bow_object_detector/RefineGraspPointRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RefineGraspPoint-request)))
  "Returns string type for a service object of type 'RefineGraspPoint-request"
  "iri_bow_object_detector/RefineGraspPointRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RefineGraspPoint-request>)))
  "Returns md5sum for a message object of type '<RefineGraspPoint-request>"
  "4df81184ea52bef77e8b614f35924fb4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RefineGraspPoint-request)))
  "Returns md5sum for a message object of type 'RefineGraspPoint-request"
  "4df81184ea52bef77e8b614f35924fb4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RefineGraspPoint-request>)))
  "Returns full string definition for message of type '<RefineGraspPoint-request>"
  (cl:format cl:nil "~%~%iri_bow_object_detector/ObjectBox[] posible_solutions~%sensor_msgs/Image image~%iri_perception_msgs/DescriptorSet descriptor_set~%~%================================================================================~%MSG: iri_bow_object_detector/ObjectBox~%iri_perception_msgs/ImagePoint point1~%iri_perception_msgs/ImagePoint point2~%float32 value~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RefineGraspPoint-request)))
  "Returns full string definition for message of type 'RefineGraspPoint-request"
  (cl:format cl:nil "~%~%iri_bow_object_detector/ObjectBox[] posible_solutions~%sensor_msgs/Image image~%iri_perception_msgs/DescriptorSet descriptor_set~%~%================================================================================~%MSG: iri_bow_object_detector/ObjectBox~%iri_perception_msgs/ImagePoint point1~%iri_perception_msgs/ImagePoint point2~%float32 value~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RefineGraspPoint-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'posible_solutions) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'descriptor_set))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RefineGraspPoint-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RefineGraspPoint-request
    (cl:cons ':posible_solutions (posible_solutions msg))
    (cl:cons ':image (image msg))
    (cl:cons ':descriptor_set (descriptor_set msg))
))
;//! \htmlinclude RefineGraspPoint-response.msg.html

(cl:defclass <RefineGraspPoint-response> (roslisp-msg-protocol:ros-message)
  ((grasp_point
    :reader grasp_point
    :initarg :grasp_point
    :type iri_perception_msgs-msg:ImagePoint
    :initform (cl:make-instance 'iri_perception_msgs-msg:ImagePoint)))
)

(cl:defclass RefineGraspPoint-response (<RefineGraspPoint-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RefineGraspPoint-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RefineGraspPoint-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_bow_object_detector-srv:<RefineGraspPoint-response> is deprecated: use iri_bow_object_detector-srv:RefineGraspPoint-response instead.")))

(cl:ensure-generic-function 'grasp_point-val :lambda-list '(m))
(cl:defmethod grasp_point-val ((m <RefineGraspPoint-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_bow_object_detector-srv:grasp_point-val is deprecated.  Use iri_bow_object_detector-srv:grasp_point instead.")
  (grasp_point m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RefineGraspPoint-response>) ostream)
  "Serializes a message object of type '<RefineGraspPoint-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'grasp_point) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RefineGraspPoint-response>) istream)
  "Deserializes a message object of type '<RefineGraspPoint-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'grasp_point) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RefineGraspPoint-response>)))
  "Returns string type for a service object of type '<RefineGraspPoint-response>"
  "iri_bow_object_detector/RefineGraspPointResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RefineGraspPoint-response)))
  "Returns string type for a service object of type 'RefineGraspPoint-response"
  "iri_bow_object_detector/RefineGraspPointResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RefineGraspPoint-response>)))
  "Returns md5sum for a message object of type '<RefineGraspPoint-response>"
  "4df81184ea52bef77e8b614f35924fb4")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RefineGraspPoint-response)))
  "Returns md5sum for a message object of type 'RefineGraspPoint-response"
  "4df81184ea52bef77e8b614f35924fb4")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RefineGraspPoint-response>)))
  "Returns full string definition for message of type '<RefineGraspPoint-response>"
  (cl:format cl:nil "~%iri_perception_msgs/ImagePoint grasp_point~%~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RefineGraspPoint-response)))
  "Returns full string definition for message of type 'RefineGraspPoint-response"
  (cl:format cl:nil "~%iri_perception_msgs/ImagePoint grasp_point~%~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RefineGraspPoint-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'grasp_point))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RefineGraspPoint-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RefineGraspPoint-response
    (cl:cons ':grasp_point (grasp_point msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RefineGraspPoint)))
  'RefineGraspPoint-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RefineGraspPoint)))
  'RefineGraspPoint-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RefineGraspPoint)))
  "Returns string type for a service object of type '<RefineGraspPoint>"
  "iri_bow_object_detector/RefineGraspPoint")
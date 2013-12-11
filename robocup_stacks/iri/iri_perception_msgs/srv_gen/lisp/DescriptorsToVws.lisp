; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude DescriptorsToVws-request.msg.html

(cl:defclass <DescriptorsToVws-request> (roslisp-msg-protocol:ros-message)
  ((descriptor_set
    :reader descriptor_set
    :initarg :descriptor_set
    :type iri_perception_msgs-msg:DescriptorSet
    :initform (cl:make-instance 'iri_perception_msgs-msg:DescriptorSet)))
)

(cl:defclass DescriptorsToVws-request (<DescriptorsToVws-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DescriptorsToVws-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DescriptorsToVws-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<DescriptorsToVws-request> is deprecated: use iri_perception_msgs-srv:DescriptorsToVws-request instead.")))

(cl:ensure-generic-function 'descriptor_set-val :lambda-list '(m))
(cl:defmethod descriptor_set-val ((m <DescriptorsToVws-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:descriptor_set-val is deprecated.  Use iri_perception_msgs-srv:descriptor_set instead.")
  (descriptor_set m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DescriptorsToVws-request>) ostream)
  "Serializes a message object of type '<DescriptorsToVws-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'descriptor_set) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DescriptorsToVws-request>) istream)
  "Deserializes a message object of type '<DescriptorsToVws-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'descriptor_set) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DescriptorsToVws-request>)))
  "Returns string type for a service object of type '<DescriptorsToVws-request>"
  "iri_perception_msgs/DescriptorsToVwsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DescriptorsToVws-request)))
  "Returns string type for a service object of type 'DescriptorsToVws-request"
  "iri_perception_msgs/DescriptorsToVwsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DescriptorsToVws-request>)))
  "Returns md5sum for a message object of type '<DescriptorsToVws-request>"
  "22b3d75b6de6a8033e791170a75fab55")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DescriptorsToVws-request)))
  "Returns md5sum for a message object of type 'DescriptorsToVws-request"
  "22b3d75b6de6a8033e791170a75fab55")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DescriptorsToVws-request>)))
  "Returns full string definition for message of type '<DescriptorsToVws-request>"
  (cl:format cl:nil "~%iri_perception_msgs/DescriptorSet descriptor_set~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DescriptorsToVws-request)))
  "Returns full string definition for message of type 'DescriptorsToVws-request"
  (cl:format cl:nil "~%iri_perception_msgs/DescriptorSet descriptor_set~%~%================================================================================~%MSG: iri_perception_msgs/DescriptorSet~%Header header~%int32 num_orient_bins~%int32 num_spa_bins~%int32 num~%int32 len~%int32 width~%int32 height~%iri_perception_msgs/Descriptor[] descriptors~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/Descriptor~%float32[] descriptor~%geometry_msgs/Vector3 point3d~%int32 u~%int32 v~%float32 orientation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DescriptorsToVws-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'descriptor_set))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DescriptorsToVws-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DescriptorsToVws-request
    (cl:cons ':descriptor_set (descriptor_set msg))
))
;//! \htmlinclude DescriptorsToVws-response.msg.html

(cl:defclass <DescriptorsToVws-response> (roslisp-msg-protocol:ros-message)
  ((geo_vw_set
    :reader geo_vw_set
    :initarg :geo_vw_set
    :type iri_perception_msgs-msg:GeoVwSet
    :initform (cl:make-instance 'iri_perception_msgs-msg:GeoVwSet)))
)

(cl:defclass DescriptorsToVws-response (<DescriptorsToVws-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DescriptorsToVws-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DescriptorsToVws-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<DescriptorsToVws-response> is deprecated: use iri_perception_msgs-srv:DescriptorsToVws-response instead.")))

(cl:ensure-generic-function 'geo_vw_set-val :lambda-list '(m))
(cl:defmethod geo_vw_set-val ((m <DescriptorsToVws-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:geo_vw_set-val is deprecated.  Use iri_perception_msgs-srv:geo_vw_set instead.")
  (geo_vw_set m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DescriptorsToVws-response>) ostream)
  "Serializes a message object of type '<DescriptorsToVws-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'geo_vw_set) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DescriptorsToVws-response>) istream)
  "Deserializes a message object of type '<DescriptorsToVws-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'geo_vw_set) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DescriptorsToVws-response>)))
  "Returns string type for a service object of type '<DescriptorsToVws-response>"
  "iri_perception_msgs/DescriptorsToVwsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DescriptorsToVws-response)))
  "Returns string type for a service object of type 'DescriptorsToVws-response"
  "iri_perception_msgs/DescriptorsToVwsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DescriptorsToVws-response>)))
  "Returns md5sum for a message object of type '<DescriptorsToVws-response>"
  "22b3d75b6de6a8033e791170a75fab55")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DescriptorsToVws-response)))
  "Returns md5sum for a message object of type 'DescriptorsToVws-response"
  "22b3d75b6de6a8033e791170a75fab55")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DescriptorsToVws-response>)))
  "Returns full string definition for message of type '<DescriptorsToVws-response>"
  (cl:format cl:nil "~%iri_perception_msgs/GeoVwSet geo_vw_set~%~%~%================================================================================~%MSG: iri_perception_msgs/GeoVwSet~%iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DescriptorsToVws-response)))
  "Returns full string definition for message of type 'DescriptorsToVws-response"
  (cl:format cl:nil "~%iri_perception_msgs/GeoVwSet geo_vw_set~%~%~%================================================================================~%MSG: iri_perception_msgs/GeoVwSet~%iri_perception_msgs/GeoVw[] geo_vws~%~%================================================================================~%MSG: iri_perception_msgs/GeoVw~%uint32 x~%uint32 y~%uint32 word~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DescriptorsToVws-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'geo_vw_set))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DescriptorsToVws-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DescriptorsToVws-response
    (cl:cons ':geo_vw_set (geo_vw_set msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DescriptorsToVws)))
  'DescriptorsToVws-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DescriptorsToVws)))
  'DescriptorsToVws-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DescriptorsToVws)))
  "Returns string type for a service object of type '<DescriptorsToVws>"
  "iri_perception_msgs/DescriptorsToVws")
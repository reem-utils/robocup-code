; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude SetImage-request.msg.html

(cl:defclass <SetImage-request> (roslisp-msg-protocol:ros-message)
  ((image_in
    :reader image_in
    :initarg :image_in
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image)))
)

(cl:defclass SetImage-request (<SetImage-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetImage-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetImage-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<SetImage-request> is deprecated: use iri_perception_msgs-srv:SetImage-request instead.")))

(cl:ensure-generic-function 'image_in-val :lambda-list '(m))
(cl:defmethod image_in-val ((m <SetImage-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:image_in-val is deprecated.  Use iri_perception_msgs-srv:image_in instead.")
  (image_in m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetImage-request>) ostream)
  "Serializes a message object of type '<SetImage-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'image_in) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetImage-request>) istream)
  "Deserializes a message object of type '<SetImage-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'image_in) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetImage-request>)))
  "Returns string type for a service object of type '<SetImage-request>"
  "iri_perception_msgs/SetImageRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetImage-request)))
  "Returns string type for a service object of type 'SetImage-request"
  "iri_perception_msgs/SetImageRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetImage-request>)))
  "Returns md5sum for a message object of type '<SetImage-request>"
  "3c9d3f37fa6b00d25eaac8ccbaa373ab")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetImage-request)))
  "Returns md5sum for a message object of type 'SetImage-request"
  "3c9d3f37fa6b00d25eaac8ccbaa373ab")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetImage-request>)))
  "Returns full string definition for message of type '<SetImage-request>"
  (cl:format cl:nil "~%sensor_msgs/Image image_in~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetImage-request)))
  "Returns full string definition for message of type 'SetImage-request"
  (cl:format cl:nil "~%sensor_msgs/Image image_in~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetImage-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'image_in))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetImage-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetImage-request
    (cl:cons ':image_in (image_in msg))
))
;//! \htmlinclude SetImage-response.msg.html

(cl:defclass <SetImage-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass SetImage-response (<SetImage-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetImage-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetImage-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<SetImage-response> is deprecated: use iri_perception_msgs-srv:SetImage-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <SetImage-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:success-val is deprecated.  Use iri_perception_msgs-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetImage-response>) ostream)
  "Serializes a message object of type '<SetImage-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetImage-response>) istream)
  "Deserializes a message object of type '<SetImage-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetImage-response>)))
  "Returns string type for a service object of type '<SetImage-response>"
  "iri_perception_msgs/SetImageResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetImage-response)))
  "Returns string type for a service object of type 'SetImage-response"
  "iri_perception_msgs/SetImageResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetImage-response>)))
  "Returns md5sum for a message object of type '<SetImage-response>"
  "3c9d3f37fa6b00d25eaac8ccbaa373ab")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetImage-response)))
  "Returns md5sum for a message object of type 'SetImage-response"
  "3c9d3f37fa6b00d25eaac8ccbaa373ab")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetImage-response>)))
  "Returns full string definition for message of type '<SetImage-response>"
  (cl:format cl:nil "~%bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetImage-response)))
  "Returns full string definition for message of type 'SetImage-response"
  (cl:format cl:nil "~%bool success~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetImage-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetImage-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetImage-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetImage)))
  'SetImage-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetImage)))
  'SetImage-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetImage)))
  "Returns string type for a service object of type '<SetImage>"
  "iri_perception_msgs/SetImage")
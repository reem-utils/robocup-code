; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-msg)


;//! \htmlinclude img_detection.msg.html

(cl:defclass <img_detection> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (dets
    :reader dets
    :initarg :dets
    :type (cl:vector iri_perception_msgs-msg:single_img_detection)
   :initform (cl:make-array 0 :element-type 'iri_perception_msgs-msg:single_img_detection :initial-element (cl:make-instance 'iri_perception_msgs-msg:single_img_detection))))
)

(cl:defclass img_detection (<img_detection>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <img_detection>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'img_detection)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-msg:<img_detection> is deprecated: use iri_perception_msgs-msg:img_detection instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <img_detection>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:header-val is deprecated.  Use iri_perception_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'dets-val :lambda-list '(m))
(cl:defmethod dets-val ((m <img_detection>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:dets-val is deprecated.  Use iri_perception_msgs-msg:dets instead.")
  (dets m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <img_detection>) ostream)
  "Serializes a message object of type '<img_detection>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'dets))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'dets))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <img_detection>) istream)
  "Deserializes a message object of type '<img_detection>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'dets) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'dets)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'iri_perception_msgs-msg:single_img_detection))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<img_detection>)))
  "Returns string type for a message object of type '<img_detection>"
  "iri_perception_msgs/img_detection")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'img_detection)))
  "Returns string type for a message object of type 'img_detection"
  "iri_perception_msgs/img_detection")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<img_detection>)))
  "Returns md5sum for a message object of type '<img_detection>"
  "e9e8bbe61df18ff990a99d2579e484a0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'img_detection)))
  "Returns md5sum for a message object of type 'img_detection"
  "e9e8bbe61df18ff990a99d2579e484a0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<img_detection>)))
  "Returns full string definition for message of type '<img_detection>"
  (cl:format cl:nil "# timestamp, frame id~%Header header~%~%# detections vector~%single_img_detection[] dets~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/single_img_detection~%# detection identifier~%uint32 id~%~%# OpenCV cv::Rect structure~%# upper-left corner and width+height from the detection~%float32 x~%float32 y~%float32 width~%float32 height~%~%# detection score~%float32 score~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'img_detection)))
  "Returns full string definition for message of type 'img_detection"
  (cl:format cl:nil "# timestamp, frame id~%Header header~%~%# detections vector~%single_img_detection[] dets~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/single_img_detection~%# detection identifier~%uint32 id~%~%# OpenCV cv::Rect structure~%# upper-left corner and width+height from the detection~%float32 x~%float32 y~%float32 width~%float32 height~%~%# detection score~%float32 score~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <img_detection>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'dets) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <img_detection>))
  "Converts a ROS message object to a list"
  (cl:list 'img_detection
    (cl:cons ':header (header msg))
    (cl:cons ':dets (dets msg))
))

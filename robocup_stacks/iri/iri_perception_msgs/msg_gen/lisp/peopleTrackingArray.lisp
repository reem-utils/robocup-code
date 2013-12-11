; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-msg)


;//! \htmlinclude peopleTrackingArray.msg.html

(cl:defclass <peopleTrackingArray> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (peopleSet
    :reader peopleSet
    :initarg :peopleSet
    :type (cl:vector iri_perception_msgs-msg:peopleTracking)
   :initform (cl:make-array 0 :element-type 'iri_perception_msgs-msg:peopleTracking :initial-element (cl:make-instance 'iri_perception_msgs-msg:peopleTracking))))
)

(cl:defclass peopleTrackingArray (<peopleTrackingArray>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <peopleTrackingArray>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'peopleTrackingArray)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-msg:<peopleTrackingArray> is deprecated: use iri_perception_msgs-msg:peopleTrackingArray instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <peopleTrackingArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:header-val is deprecated.  Use iri_perception_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'peopleSet-val :lambda-list '(m))
(cl:defmethod peopleSet-val ((m <peopleTrackingArray>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-msg:peopleSet-val is deprecated.  Use iri_perception_msgs-msg:peopleSet instead.")
  (peopleSet m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <peopleTrackingArray>) ostream)
  "Serializes a message object of type '<peopleTrackingArray>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'peopleSet))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'peopleSet))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <peopleTrackingArray>) istream)
  "Deserializes a message object of type '<peopleTrackingArray>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'peopleSet) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'peopleSet)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'iri_perception_msgs-msg:peopleTracking))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<peopleTrackingArray>)))
  "Returns string type for a message object of type '<peopleTrackingArray>"
  "iri_perception_msgs/peopleTrackingArray")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'peopleTrackingArray)))
  "Returns string type for a message object of type 'peopleTrackingArray"
  "iri_perception_msgs/peopleTrackingArray")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<peopleTrackingArray>)))
  "Returns md5sum for a message object of type '<peopleTrackingArray>"
  "35cdc779914b5346377962145609933e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'peopleTrackingArray)))
  "Returns md5sum for a message object of type 'peopleTrackingArray"
  "35cdc779914b5346377962145609933e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<peopleTrackingArray>)))
  "Returns full string definition for message of type '<peopleTrackingArray>"
  (cl:format cl:nil "# timestamp, frame id~%Header header~%~%#set of targets being tracked~%peopleTracking[] peopleSet~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/peopleTracking~%#target id~%int32 targetId~%~%#target status is a bitwise OR of the following values~%#      TO_BE_REMOVED = 0x01,~%#      OCCLUDDED = 0x02,~%#      CANDIDATE = 0x04,~%#      LEGGED_TARGET = 0x08,~%#      VISUALLY_CONFIRMED = 0x10,~%#      FRIEND_IN_SIGHT = 0x20,~%#      BACK_LEARNT = 0x40,~%#      FACE_LEARNT = 0x80~%int32 targetStatus~%~%#target 2D position~%float64 x~%float64 y~%~%#target 2D linear velocity~%float64 vx~%float64 vy~%~%#(x,y,vx,vy) covariance matrix~%float64[16] covariances~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'peopleTrackingArray)))
  "Returns full string definition for message of type 'peopleTrackingArray"
  (cl:format cl:nil "# timestamp, frame id~%Header header~%~%#set of targets being tracked~%peopleTracking[] peopleSet~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/peopleTracking~%#target id~%int32 targetId~%~%#target status is a bitwise OR of the following values~%#      TO_BE_REMOVED = 0x01,~%#      OCCLUDDED = 0x02,~%#      CANDIDATE = 0x04,~%#      LEGGED_TARGET = 0x08,~%#      VISUALLY_CONFIRMED = 0x10,~%#      FRIEND_IN_SIGHT = 0x20,~%#      BACK_LEARNT = 0x40,~%#      FACE_LEARNT = 0x80~%int32 targetStatus~%~%#target 2D position~%float64 x~%float64 y~%~%#target 2D linear velocity~%float64 vx~%float64 vy~%~%#(x,y,vx,vy) covariance matrix~%float64[16] covariances~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <peopleTrackingArray>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'peopleSet) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <peopleTrackingArray>))
  "Converts a ROS message object to a list"
  (cl:list 'peopleTrackingArray
    (cl:cons ':header (header msg))
    (cl:cons ':peopleSet (peopleSet msg))
))

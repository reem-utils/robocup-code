; Auto-generated. Do not edit!


(cl:in-package iri_perception_msgs-srv)


;//! \htmlinclude peopleTrackingService-request.msg.html

(cl:defclass <peopleTrackingService-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass peopleTrackingService-request (<peopleTrackingService-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <peopleTrackingService-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'peopleTrackingService-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<peopleTrackingService-request> is deprecated: use iri_perception_msgs-srv:peopleTrackingService-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <peopleTrackingService-request>) ostream)
  "Serializes a message object of type '<peopleTrackingService-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <peopleTrackingService-request>) istream)
  "Deserializes a message object of type '<peopleTrackingService-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<peopleTrackingService-request>)))
  "Returns string type for a service object of type '<peopleTrackingService-request>"
  "iri_perception_msgs/peopleTrackingServiceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'peopleTrackingService-request)))
  "Returns string type for a service object of type 'peopleTrackingService-request"
  "iri_perception_msgs/peopleTrackingServiceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<peopleTrackingService-request>)))
  "Returns md5sum for a message object of type '<peopleTrackingService-request>"
  "fe22c69eec47e5d3de106e176d235190")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'peopleTrackingService-request)))
  "Returns md5sum for a message object of type 'peopleTrackingService-request"
  "fe22c69eec47e5d3de106e176d235190")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<peopleTrackingService-request>)))
  "Returns full string definition for message of type '<peopleTrackingService-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'peopleTrackingService-request)))
  "Returns full string definition for message of type 'peopleTrackingService-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <peopleTrackingService-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <peopleTrackingService-request>))
  "Converts a ROS message object to a list"
  (cl:list 'peopleTrackingService-request
))
;//! \htmlinclude peopleTrackingService-response.msg.html

(cl:defclass <peopleTrackingService-response> (roslisp-msg-protocol:ros-message)
  ((peopleSet
    :reader peopleSet
    :initarg :peopleSet
    :type iri_perception_msgs-msg:peopleTrackingArray
    :initform (cl:make-instance 'iri_perception_msgs-msg:peopleTrackingArray)))
)

(cl:defclass peopleTrackingService-response (<peopleTrackingService-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <peopleTrackingService-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'peopleTrackingService-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_perception_msgs-srv:<peopleTrackingService-response> is deprecated: use iri_perception_msgs-srv:peopleTrackingService-response instead.")))

(cl:ensure-generic-function 'peopleSet-val :lambda-list '(m))
(cl:defmethod peopleSet-val ((m <peopleTrackingService-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_perception_msgs-srv:peopleSet-val is deprecated.  Use iri_perception_msgs-srv:peopleSet instead.")
  (peopleSet m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <peopleTrackingService-response>) ostream)
  "Serializes a message object of type '<peopleTrackingService-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'peopleSet) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <peopleTrackingService-response>) istream)
  "Deserializes a message object of type '<peopleTrackingService-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'peopleSet) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<peopleTrackingService-response>)))
  "Returns string type for a service object of type '<peopleTrackingService-response>"
  "iri_perception_msgs/peopleTrackingServiceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'peopleTrackingService-response)))
  "Returns string type for a service object of type 'peopleTrackingService-response"
  "iri_perception_msgs/peopleTrackingServiceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<peopleTrackingService-response>)))
  "Returns md5sum for a message object of type '<peopleTrackingService-response>"
  "fe22c69eec47e5d3de106e176d235190")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'peopleTrackingService-response)))
  "Returns md5sum for a message object of type 'peopleTrackingService-response"
  "fe22c69eec47e5d3de106e176d235190")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<peopleTrackingService-response>)))
  "Returns full string definition for message of type '<peopleTrackingService-response>"
  (cl:format cl:nil "~%peopleTrackingArray peopleSet~%~%~%================================================================================~%MSG: iri_perception_msgs/peopleTrackingArray~%# timestamp, frame id~%Header header~%~%#set of targets being tracked~%peopleTracking[] peopleSet~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/peopleTracking~%#target id~%int32 targetId~%~%#target status is a bitwise OR of the following values~%#      TO_BE_REMOVED = 0x01,~%#      OCCLUDDED = 0x02,~%#      CANDIDATE = 0x04,~%#      LEGGED_TARGET = 0x08,~%#      VISUALLY_CONFIRMED = 0x10,~%#      FRIEND_IN_SIGHT = 0x20,~%#      BACK_LEARNT = 0x40,~%#      FACE_LEARNT = 0x80~%int32 targetStatus~%~%#target 2D position~%float64 x~%float64 y~%~%#target 2D linear velocity~%float64 vx~%float64 vy~%~%#(x,y,vx,vy) covariance matrix~%float64[16] covariances~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'peopleTrackingService-response)))
  "Returns full string definition for message of type 'peopleTrackingService-response"
  (cl:format cl:nil "~%peopleTrackingArray peopleSet~%~%~%================================================================================~%MSG: iri_perception_msgs/peopleTrackingArray~%# timestamp, frame id~%Header header~%~%#set of targets being tracked~%peopleTracking[] peopleSet~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: iri_perception_msgs/peopleTracking~%#target id~%int32 targetId~%~%#target status is a bitwise OR of the following values~%#      TO_BE_REMOVED = 0x01,~%#      OCCLUDDED = 0x02,~%#      CANDIDATE = 0x04,~%#      LEGGED_TARGET = 0x08,~%#      VISUALLY_CONFIRMED = 0x10,~%#      FRIEND_IN_SIGHT = 0x20,~%#      BACK_LEARNT = 0x40,~%#      FACE_LEARNT = 0x80~%int32 targetStatus~%~%#target 2D position~%float64 x~%float64 y~%~%#target 2D linear velocity~%float64 vx~%float64 vy~%~%#(x,y,vx,vy) covariance matrix~%float64[16] covariances~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <peopleTrackingService-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'peopleSet))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <peopleTrackingService-response>))
  "Converts a ROS message object to a list"
  (cl:list 'peopleTrackingService-response
    (cl:cons ':peopleSet (peopleSet msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'peopleTrackingService)))
  'peopleTrackingService-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'peopleTrackingService)))
  'peopleTrackingService-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'peopleTrackingService)))
  "Returns string type for a service object of type '<peopleTrackingService>"
  "iri_perception_msgs/peopleTrackingService")
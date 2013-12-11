; Auto-generated. Do not edit!


(cl:in-package person_detector_mock-srv)


;//! \htmlinclude DetectPeople-request.msg.html

(cl:defclass <DetectPeople-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass DetectPeople-request (<DetectPeople-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectPeople-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectPeople-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name person_detector_mock-srv:<DetectPeople-request> is deprecated: use person_detector_mock-srv:DetectPeople-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectPeople-request>) ostream)
  "Serializes a message object of type '<DetectPeople-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectPeople-request>) istream)
  "Deserializes a message object of type '<DetectPeople-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectPeople-request>)))
  "Returns string type for a service object of type '<DetectPeople-request>"
  "person_detector_mock/DetectPeopleRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectPeople-request)))
  "Returns string type for a service object of type 'DetectPeople-request"
  "person_detector_mock/DetectPeopleRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectPeople-request>)))
  "Returns md5sum for a message object of type '<DetectPeople-request>"
  "fb55709fde01cfa26cd33335972baf09")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectPeople-request)))
  "Returns md5sum for a message object of type 'DetectPeople-request"
  "fb55709fde01cfa26cd33335972baf09")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectPeople-request>)))
  "Returns full string definition for message of type '<DetectPeople-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectPeople-request)))
  "Returns full string definition for message of type 'DetectPeople-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectPeople-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectPeople-request>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectPeople-request
))
;//! \htmlinclude DetectPeople-response.msg.html

(cl:defclass <DetectPeople-response> (roslisp-msg-protocol:ros-message)
  ((peopleSet
    :reader peopleSet
    :initarg :peopleSet
    :type person_detector_mock-msg:peopleTrackingArray
    :initform (cl:make-instance 'person_detector_mock-msg:peopleTrackingArray)))
)

(cl:defclass DetectPeople-response (<DetectPeople-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DetectPeople-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DetectPeople-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name person_detector_mock-srv:<DetectPeople-response> is deprecated: use person_detector_mock-srv:DetectPeople-response instead.")))

(cl:ensure-generic-function 'peopleSet-val :lambda-list '(m))
(cl:defmethod peopleSet-val ((m <DetectPeople-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader person_detector_mock-srv:peopleSet-val is deprecated.  Use person_detector_mock-srv:peopleSet instead.")
  (peopleSet m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DetectPeople-response>) ostream)
  "Serializes a message object of type '<DetectPeople-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'peopleSet) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DetectPeople-response>) istream)
  "Deserializes a message object of type '<DetectPeople-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'peopleSet) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DetectPeople-response>)))
  "Returns string type for a service object of type '<DetectPeople-response>"
  "person_detector_mock/DetectPeopleResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectPeople-response)))
  "Returns string type for a service object of type 'DetectPeople-response"
  "person_detector_mock/DetectPeopleResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DetectPeople-response>)))
  "Returns md5sum for a message object of type '<DetectPeople-response>"
  "fb55709fde01cfa26cd33335972baf09")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DetectPeople-response)))
  "Returns md5sum for a message object of type 'DetectPeople-response"
  "fb55709fde01cfa26cd33335972baf09")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DetectPeople-response>)))
  "Returns full string definition for message of type '<DetectPeople-response>"
  (cl:format cl:nil "peopleTrackingArray peopleSet~%~%~%================================================================================~%MSG: person_detector_mock/peopleTrackingArray~%# timestamp, frame id~%Header header~%~%#set of targets being tracked~%peopleTracking[] peopleSet~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: person_detector_mock/peopleTracking~%int32 targetId~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64[16] covariances~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DetectPeople-response)))
  "Returns full string definition for message of type 'DetectPeople-response"
  (cl:format cl:nil "peopleTrackingArray peopleSet~%~%~%================================================================================~%MSG: person_detector_mock/peopleTrackingArray~%# timestamp, frame id~%Header header~%~%#set of targets being tracked~%peopleTracking[] peopleSet~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: person_detector_mock/peopleTracking~%int32 targetId~%float64 x~%float64 y~%float64 vx~%float64 vy~%float64[16] covariances~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DetectPeople-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'peopleSet))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DetectPeople-response>))
  "Converts a ROS message object to a list"
  (cl:list 'DetectPeople-response
    (cl:cons ':peopleSet (peopleSet msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'DetectPeople)))
  'DetectPeople-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'DetectPeople)))
  'DetectPeople-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DetectPeople)))
  "Returns string type for a service object of type '<DetectPeople>"
  "person_detector_mock/DetectPeople")
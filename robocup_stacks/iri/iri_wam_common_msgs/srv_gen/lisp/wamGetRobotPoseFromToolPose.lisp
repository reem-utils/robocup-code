; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude wamGetRobotPoseFromToolPose-request.msg.html

(cl:defclass <wamGetRobotPoseFromToolPose-request> (roslisp-msg-protocol:ros-message)
  ((tool_pose
    :reader tool_pose
    :initarg :tool_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass wamGetRobotPoseFromToolPose-request (<wamGetRobotPoseFromToolPose-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamGetRobotPoseFromToolPose-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamGetRobotPoseFromToolPose-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamGetRobotPoseFromToolPose-request> is deprecated: use iri_wam_common_msgs-srv:wamGetRobotPoseFromToolPose-request instead.")))

(cl:ensure-generic-function 'tool_pose-val :lambda-list '(m))
(cl:defmethod tool_pose-val ((m <wamGetRobotPoseFromToolPose-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:tool_pose-val is deprecated.  Use iri_wam_common_msgs-srv:tool_pose instead.")
  (tool_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamGetRobotPoseFromToolPose-request>) ostream)
  "Serializes a message object of type '<wamGetRobotPoseFromToolPose-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'tool_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamGetRobotPoseFromToolPose-request>) istream)
  "Deserializes a message object of type '<wamGetRobotPoseFromToolPose-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'tool_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamGetRobotPoseFromToolPose-request>)))
  "Returns string type for a service object of type '<wamGetRobotPoseFromToolPose-request>"
  "iri_wam_common_msgs/wamGetRobotPoseFromToolPoseRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamGetRobotPoseFromToolPose-request)))
  "Returns string type for a service object of type 'wamGetRobotPoseFromToolPose-request"
  "iri_wam_common_msgs/wamGetRobotPoseFromToolPoseRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamGetRobotPoseFromToolPose-request>)))
  "Returns md5sum for a message object of type '<wamGetRobotPoseFromToolPose-request>"
  "9bc33b41fd06e0cc64ed1e05be1d2898")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamGetRobotPoseFromToolPose-request)))
  "Returns md5sum for a message object of type 'wamGetRobotPoseFromToolPose-request"
  "9bc33b41fd06e0cc64ed1e05be1d2898")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamGetRobotPoseFromToolPose-request>)))
  "Returns full string definition for message of type '<wamGetRobotPoseFromToolPose-request>"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped tool_pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamGetRobotPoseFromToolPose-request)))
  "Returns full string definition for message of type 'wamGetRobotPoseFromToolPose-request"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped tool_pose~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamGetRobotPoseFromToolPose-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'tool_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamGetRobotPoseFromToolPose-request>))
  "Converts a ROS message object to a list"
  (cl:list 'wamGetRobotPoseFromToolPose-request
    (cl:cons ':tool_pose (tool_pose msg))
))
;//! \htmlinclude wamGetRobotPoseFromToolPose-response.msg.html

(cl:defclass <wamGetRobotPoseFromToolPose-response> (roslisp-msg-protocol:ros-message)
  ((robot_pose
    :reader robot_pose
    :initarg :robot_pose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass wamGetRobotPoseFromToolPose-response (<wamGetRobotPoseFromToolPose-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <wamGetRobotPoseFromToolPose-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'wamGetRobotPoseFromToolPose-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<wamGetRobotPoseFromToolPose-response> is deprecated: use iri_wam_common_msgs-srv:wamGetRobotPoseFromToolPose-response instead.")))

(cl:ensure-generic-function 'robot_pose-val :lambda-list '(m))
(cl:defmethod robot_pose-val ((m <wamGetRobotPoseFromToolPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:robot_pose-val is deprecated.  Use iri_wam_common_msgs-srv:robot_pose instead.")
  (robot_pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <wamGetRobotPoseFromToolPose-response>) ostream)
  "Serializes a message object of type '<wamGetRobotPoseFromToolPose-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'robot_pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <wamGetRobotPoseFromToolPose-response>) istream)
  "Deserializes a message object of type '<wamGetRobotPoseFromToolPose-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'robot_pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<wamGetRobotPoseFromToolPose-response>)))
  "Returns string type for a service object of type '<wamGetRobotPoseFromToolPose-response>"
  "iri_wam_common_msgs/wamGetRobotPoseFromToolPoseResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamGetRobotPoseFromToolPose-response)))
  "Returns string type for a service object of type 'wamGetRobotPoseFromToolPose-response"
  "iri_wam_common_msgs/wamGetRobotPoseFromToolPoseResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<wamGetRobotPoseFromToolPose-response>)))
  "Returns md5sum for a message object of type '<wamGetRobotPoseFromToolPose-response>"
  "9bc33b41fd06e0cc64ed1e05be1d2898")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'wamGetRobotPoseFromToolPose-response)))
  "Returns md5sum for a message object of type 'wamGetRobotPoseFromToolPose-response"
  "9bc33b41fd06e0cc64ed1e05be1d2898")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<wamGetRobotPoseFromToolPose-response>)))
  "Returns full string definition for message of type '<wamGetRobotPoseFromToolPose-response>"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped robot_pose~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'wamGetRobotPoseFromToolPose-response)))
  "Returns full string definition for message of type 'wamGetRobotPoseFromToolPose-response"
  (cl:format cl:nil "~%geometry_msgs/PoseStamped robot_pose~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <wamGetRobotPoseFromToolPose-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'robot_pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <wamGetRobotPoseFromToolPose-response>))
  "Converts a ROS message object to a list"
  (cl:list 'wamGetRobotPoseFromToolPose-response
    (cl:cons ':robot_pose (robot_pose msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'wamGetRobotPoseFromToolPose)))
  'wamGetRobotPoseFromToolPose-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'wamGetRobotPoseFromToolPose)))
  'wamGetRobotPoseFromToolPose-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'wamGetRobotPoseFromToolPose)))
  "Returns string type for a service object of type '<wamGetRobotPoseFromToolPose>"
  "iri_wam_common_msgs/wamGetRobotPoseFromToolPose")
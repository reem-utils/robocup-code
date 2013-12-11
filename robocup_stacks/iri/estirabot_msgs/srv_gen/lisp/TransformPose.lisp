; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-srv)


;//! \htmlinclude TransformPose-request.msg.html

(cl:defclass <TransformPose-request> (roslisp-msg-protocol:ros-message)
  ((orig_pose_st
    :reader orig_pose_st
    :initarg :orig_pose_st
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (target_frame
    :reader target_frame
    :initarg :target_frame
    :type cl:string
    :initform ""))
)

(cl:defclass TransformPose-request (<TransformPose-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TransformPose-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TransformPose-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<TransformPose-request> is deprecated: use estirabot_msgs-srv:TransformPose-request instead.")))

(cl:ensure-generic-function 'orig_pose_st-val :lambda-list '(m))
(cl:defmethod orig_pose_st-val ((m <TransformPose-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:orig_pose_st-val is deprecated.  Use estirabot_msgs-srv:orig_pose_st instead.")
  (orig_pose_st m))

(cl:ensure-generic-function 'target_frame-val :lambda-list '(m))
(cl:defmethod target_frame-val ((m <TransformPose-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:target_frame-val is deprecated.  Use estirabot_msgs-srv:target_frame instead.")
  (target_frame m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TransformPose-request>) ostream)
  "Serializes a message object of type '<TransformPose-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'orig_pose_st) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'target_frame))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'target_frame))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TransformPose-request>) istream)
  "Deserializes a message object of type '<TransformPose-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'orig_pose_st) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'target_frame) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'target_frame) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TransformPose-request>)))
  "Returns string type for a service object of type '<TransformPose-request>"
  "estirabot_msgs/TransformPoseRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TransformPose-request)))
  "Returns string type for a service object of type 'TransformPose-request"
  "estirabot_msgs/TransformPoseRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TransformPose-request>)))
  "Returns md5sum for a message object of type '<TransformPose-request>"
  "d970a793ffec2eaf87d550a3deb0c796")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TransformPose-request)))
  "Returns md5sum for a message object of type 'TransformPose-request"
  "d970a793ffec2eaf87d550a3deb0c796")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TransformPose-request>)))
  "Returns full string definition for message of type '<TransformPose-request>"
  (cl:format cl:nil "geometry_msgs/PoseStamped orig_pose_st~%string target_frame~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TransformPose-request)))
  "Returns full string definition for message of type 'TransformPose-request"
  (cl:format cl:nil "geometry_msgs/PoseStamped orig_pose_st~%string target_frame~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TransformPose-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'orig_pose_st))
     4 (cl:length (cl:slot-value msg 'target_frame))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TransformPose-request>))
  "Converts a ROS message object to a list"
  (cl:list 'TransformPose-request
    (cl:cons ':orig_pose_st (orig_pose_st msg))
    (cl:cons ':target_frame (target_frame msg))
))
;//! \htmlinclude TransformPose-response.msg.html

(cl:defclass <TransformPose-response> (roslisp-msg-protocol:ros-message)
  ((target_pose_st
    :reader target_pose_st
    :initarg :target_pose_st
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass TransformPose-response (<TransformPose-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TransformPose-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TransformPose-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<TransformPose-response> is deprecated: use estirabot_msgs-srv:TransformPose-response instead.")))

(cl:ensure-generic-function 'target_pose_st-val :lambda-list '(m))
(cl:defmethod target_pose_st-val ((m <TransformPose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:target_pose_st-val is deprecated.  Use estirabot_msgs-srv:target_pose_st instead.")
  (target_pose_st m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TransformPose-response>) ostream)
  "Serializes a message object of type '<TransformPose-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'target_pose_st) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TransformPose-response>) istream)
  "Deserializes a message object of type '<TransformPose-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'target_pose_st) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TransformPose-response>)))
  "Returns string type for a service object of type '<TransformPose-response>"
  "estirabot_msgs/TransformPoseResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TransformPose-response)))
  "Returns string type for a service object of type 'TransformPose-response"
  "estirabot_msgs/TransformPoseResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TransformPose-response>)))
  "Returns md5sum for a message object of type '<TransformPose-response>"
  "d970a793ffec2eaf87d550a3deb0c796")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TransformPose-response)))
  "Returns md5sum for a message object of type 'TransformPose-response"
  "d970a793ffec2eaf87d550a3deb0c796")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TransformPose-response>)))
  "Returns full string definition for message of type '<TransformPose-response>"
  (cl:format cl:nil "geometry_msgs/PoseStamped target_pose_st~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TransformPose-response)))
  "Returns full string definition for message of type 'TransformPose-response"
  (cl:format cl:nil "geometry_msgs/PoseStamped target_pose_st~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TransformPose-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'target_pose_st))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TransformPose-response>))
  "Converts a ROS message object to a list"
  (cl:list 'TransformPose-response
    (cl:cons ':target_pose_st (target_pose_st msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'TransformPose)))
  'TransformPose-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'TransformPose)))
  'TransformPose-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TransformPose)))
  "Returns string type for a service object of type '<TransformPose>"
  "estirabot_msgs/TransformPose")
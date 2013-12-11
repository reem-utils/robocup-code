; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude ObjectPoseList.msg.html

(cl:defclass <ObjectPoseList> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (object_list
    :reader object_list
    :initarg :object_list
    :type (cl:vector pr_msgs-msg:ObjectPose)
   :initform (cl:make-array 0 :element-type 'pr_msgs-msg:ObjectPose :initial-element (cl:make-instance 'pr_msgs-msg:ObjectPose)))
   (originalTimeStamp
    :reader originalTimeStamp
    :initarg :originalTimeStamp
    :type cl:real
    :initform 0)
   (requestTimeStamp
    :reader requestTimeStamp
    :initarg :requestTimeStamp
    :type cl:real
    :initform 0))
)

(cl:defclass ObjectPoseList (<ObjectPoseList>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectPoseList>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectPoseList)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<ObjectPoseList> is deprecated: use pr_msgs-msg:ObjectPoseList instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ObjectPoseList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:header-val is deprecated.  Use pr_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'object_list-val :lambda-list '(m))
(cl:defmethod object_list-val ((m <ObjectPoseList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:object_list-val is deprecated.  Use pr_msgs-msg:object_list instead.")
  (object_list m))

(cl:ensure-generic-function 'originalTimeStamp-val :lambda-list '(m))
(cl:defmethod originalTimeStamp-val ((m <ObjectPoseList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:originalTimeStamp-val is deprecated.  Use pr_msgs-msg:originalTimeStamp instead.")
  (originalTimeStamp m))

(cl:ensure-generic-function 'requestTimeStamp-val :lambda-list '(m))
(cl:defmethod requestTimeStamp-val ((m <ObjectPoseList>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:requestTimeStamp-val is deprecated.  Use pr_msgs-msg:requestTimeStamp instead.")
  (requestTimeStamp m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectPoseList>) ostream)
  "Serializes a message object of type '<ObjectPoseList>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'object_list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'object_list))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'originalTimeStamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'originalTimeStamp) (cl:floor (cl:slot-value msg 'originalTimeStamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'requestTimeStamp)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'requestTimeStamp) (cl:floor (cl:slot-value msg 'requestTimeStamp)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectPoseList>) istream)
  "Deserializes a message object of type '<ObjectPoseList>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'object_list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'object_list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pr_msgs-msg:ObjectPose))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'originalTimeStamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'requestTimeStamp) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectPoseList>)))
  "Returns string type for a message object of type '<ObjectPoseList>"
  "pr_msgs/ObjectPoseList")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectPoseList)))
  "Returns string type for a message object of type 'ObjectPoseList"
  "pr_msgs/ObjectPoseList")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectPoseList>)))
  "Returns md5sum for a message object of type '<ObjectPoseList>"
  "418ab919a68374930e8c523eaea185d2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectPoseList)))
  "Returns md5sum for a message object of type 'ObjectPoseList"
  "418ab919a68374930e8c523eaea185d2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectPoseList>)))
  "Returns full string definition for message of type '<ObjectPoseList>"
  (cl:format cl:nil "Header header~%~%ObjectPose[] object_list~%~%time originalTimeStamp~%~%time requestTimeStamp~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: pr_msgs/ObjectPose~%string name~%~%geometry_msgs/Pose pose~%geometry_msgs/Point32 pose2D~%~%int16[] convex_hull_x~%int16[] convex_hull_y~%~%float32 mean_quality~%int16 used_points~%~%NameTypeValue[] properties~%~%geometry_msgs/Pose[] pose_uncertainty_list~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: pr_msgs/NameTypeValue~%string name~%string type~%string value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectPoseList)))
  "Returns full string definition for message of type 'ObjectPoseList"
  (cl:format cl:nil "Header header~%~%ObjectPose[] object_list~%~%time originalTimeStamp~%~%time requestTimeStamp~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: pr_msgs/ObjectPose~%string name~%~%geometry_msgs/Pose pose~%geometry_msgs/Point32 pose2D~%~%int16[] convex_hull_x~%int16[] convex_hull_y~%~%float32 mean_quality~%int16 used_points~%~%NameTypeValue[] properties~%~%geometry_msgs/Pose[] pose_uncertainty_list~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: pr_msgs/NameTypeValue~%string name~%string type~%string value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectPoseList>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'object_list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectPoseList>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectPoseList
    (cl:cons ':header (header msg))
    (cl:cons ':object_list (object_list msg))
    (cl:cons ':originalTimeStamp (originalTimeStamp msg))
    (cl:cons ':requestTimeStamp (requestTimeStamp msg))
))

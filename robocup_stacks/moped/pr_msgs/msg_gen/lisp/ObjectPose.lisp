; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude ObjectPose.msg.html

(cl:defclass <ObjectPose> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (pose2D
    :reader pose2D
    :initarg :pose2D
    :type geometry_msgs-msg:Point32
    :initform (cl:make-instance 'geometry_msgs-msg:Point32))
   (convex_hull_x
    :reader convex_hull_x
    :initarg :convex_hull_x
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (convex_hull_y
    :reader convex_hull_y
    :initarg :convex_hull_y
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 0 :element-type 'cl:fixnum :initial-element 0))
   (mean_quality
    :reader mean_quality
    :initarg :mean_quality
    :type cl:float
    :initform 0.0)
   (used_points
    :reader used_points
    :initarg :used_points
    :type cl:fixnum
    :initform 0)
   (properties
    :reader properties
    :initarg :properties
    :type (cl:vector pr_msgs-msg:NameTypeValue)
   :initform (cl:make-array 0 :element-type 'pr_msgs-msg:NameTypeValue :initial-element (cl:make-instance 'pr_msgs-msg:NameTypeValue)))
   (pose_uncertainty_list
    :reader pose_uncertainty_list
    :initarg :pose_uncertainty_list
    :type (cl:vector geometry_msgs-msg:Pose)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Pose :initial-element (cl:make-instance 'geometry_msgs-msg:Pose))))
)

(cl:defclass ObjectPose (<ObjectPose>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ObjectPose>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ObjectPose)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<ObjectPose> is deprecated: use pr_msgs-msg:ObjectPose instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:name-val is deprecated.  Use pr_msgs-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:pose-val is deprecated.  Use pr_msgs-msg:pose instead.")
  (pose m))

(cl:ensure-generic-function 'pose2D-val :lambda-list '(m))
(cl:defmethod pose2D-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:pose2D-val is deprecated.  Use pr_msgs-msg:pose2D instead.")
  (pose2D m))

(cl:ensure-generic-function 'convex_hull_x-val :lambda-list '(m))
(cl:defmethod convex_hull_x-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:convex_hull_x-val is deprecated.  Use pr_msgs-msg:convex_hull_x instead.")
  (convex_hull_x m))

(cl:ensure-generic-function 'convex_hull_y-val :lambda-list '(m))
(cl:defmethod convex_hull_y-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:convex_hull_y-val is deprecated.  Use pr_msgs-msg:convex_hull_y instead.")
  (convex_hull_y m))

(cl:ensure-generic-function 'mean_quality-val :lambda-list '(m))
(cl:defmethod mean_quality-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:mean_quality-val is deprecated.  Use pr_msgs-msg:mean_quality instead.")
  (mean_quality m))

(cl:ensure-generic-function 'used_points-val :lambda-list '(m))
(cl:defmethod used_points-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:used_points-val is deprecated.  Use pr_msgs-msg:used_points instead.")
  (used_points m))

(cl:ensure-generic-function 'properties-val :lambda-list '(m))
(cl:defmethod properties-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:properties-val is deprecated.  Use pr_msgs-msg:properties instead.")
  (properties m))

(cl:ensure-generic-function 'pose_uncertainty_list-val :lambda-list '(m))
(cl:defmethod pose_uncertainty_list-val ((m <ObjectPose>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:pose_uncertainty_list-val is deprecated.  Use pr_msgs-msg:pose_uncertainty_list instead.")
  (pose_uncertainty_list m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ObjectPose>) ostream)
  "Serializes a message object of type '<ObjectPose>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose2D) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'convex_hull_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'convex_hull_x))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'convex_hull_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'convex_hull_y))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'mean_quality))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'used_points)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'properties))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'properties))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pose_uncertainty_list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'pose_uncertainty_list))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ObjectPose>) istream)
  "Deserializes a message object of type '<ObjectPose>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose2D) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'convex_hull_x) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'convex_hull_x)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'convex_hull_y) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'convex_hull_y)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536)))))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'mean_quality) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'used_points) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'properties) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'properties)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'pr_msgs-msg:NameTypeValue))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pose_uncertainty_list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pose_uncertainty_list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Pose))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ObjectPose>)))
  "Returns string type for a message object of type '<ObjectPose>"
  "pr_msgs/ObjectPose")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ObjectPose)))
  "Returns string type for a message object of type 'ObjectPose"
  "pr_msgs/ObjectPose")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ObjectPose>)))
  "Returns md5sum for a message object of type '<ObjectPose>"
  "a1a9ddd9cdd7cb9b07994b75cc08bdcc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ObjectPose)))
  "Returns md5sum for a message object of type 'ObjectPose"
  "a1a9ddd9cdd7cb9b07994b75cc08bdcc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ObjectPose>)))
  "Returns full string definition for message of type '<ObjectPose>"
  (cl:format cl:nil "string name~%~%geometry_msgs/Pose pose~%geometry_msgs/Point32 pose2D~%~%int16[] convex_hull_x~%int16[] convex_hull_y~%~%float32 mean_quality~%int16 used_points~%~%NameTypeValue[] properties~%~%geometry_msgs/Pose[] pose_uncertainty_list~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: pr_msgs/NameTypeValue~%string name~%string type~%string value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ObjectPose)))
  "Returns full string definition for message of type 'ObjectPose"
  (cl:format cl:nil "string name~%~%geometry_msgs/Pose pose~%geometry_msgs/Point32 pose2D~%~%int16[] convex_hull_x~%int16[] convex_hull_y~%~%float32 mean_quality~%int16 used_points~%~%NameTypeValue[] properties~%~%geometry_msgs/Pose[] pose_uncertainty_list~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%================================================================================~%MSG: pr_msgs/NameTypeValue~%string name~%string type~%string value~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ObjectPose>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose2D))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'convex_hull_x) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'convex_hull_y) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     4
     2
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'properties) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pose_uncertainty_list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ObjectPose>))
  "Converts a ROS message object to a list"
  (cl:list 'ObjectPose
    (cl:cons ':name (name msg))
    (cl:cons ':pose (pose msg))
    (cl:cons ':pose2D (pose2D msg))
    (cl:cons ':convex_hull_x (convex_hull_x msg))
    (cl:cons ':convex_hull_y (convex_hull_y msg))
    (cl:cons ':mean_quality (mean_quality msg))
    (cl:cons ':used_points (used_points msg))
    (cl:cons ':properties (properties msg))
    (cl:cons ':pose_uncertainty_list (pose_uncertainty_list msg))
))

; Auto-generated. Do not edit!


(cl:in-package pr_msgs-msg)


;//! \htmlinclude OccGrid3D.msg.html

(cl:defclass <OccGrid3D> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (resolution
    :reader resolution
    :initarg :resolution
    :type cl:float
    :initform 0.0)
   (num_x_voxels
    :reader num_x_voxels
    :initarg :num_x_voxels
    :type cl:integer
    :initform 0)
   (num_y_voxels
    :reader num_y_voxels
    :initarg :num_y_voxels
    :type cl:integer
    :initform 0)
   (num_z_voxels
    :reader num_z_voxels
    :initarg :num_z_voxels
    :type cl:integer
    :initform 0)
   (origin
    :reader origin
    :initarg :origin
    :type geometry_msgs-msg:Point32
    :initform (cl:make-instance 'geometry_msgs-msg:Point32))
   (data
    :reader data
    :initarg :data
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass OccGrid3D (<OccGrid3D>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <OccGrid3D>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'OccGrid3D)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-msg:<OccGrid3D> is deprecated: use pr_msgs-msg:OccGrid3D instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <OccGrid3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:header-val is deprecated.  Use pr_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'resolution-val :lambda-list '(m))
(cl:defmethod resolution-val ((m <OccGrid3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:resolution-val is deprecated.  Use pr_msgs-msg:resolution instead.")
  (resolution m))

(cl:ensure-generic-function 'num_x_voxels-val :lambda-list '(m))
(cl:defmethod num_x_voxels-val ((m <OccGrid3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:num_x_voxels-val is deprecated.  Use pr_msgs-msg:num_x_voxels instead.")
  (num_x_voxels m))

(cl:ensure-generic-function 'num_y_voxels-val :lambda-list '(m))
(cl:defmethod num_y_voxels-val ((m <OccGrid3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:num_y_voxels-val is deprecated.  Use pr_msgs-msg:num_y_voxels instead.")
  (num_y_voxels m))

(cl:ensure-generic-function 'num_z_voxels-val :lambda-list '(m))
(cl:defmethod num_z_voxels-val ((m <OccGrid3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:num_z_voxels-val is deprecated.  Use pr_msgs-msg:num_z_voxels instead.")
  (num_z_voxels m))

(cl:ensure-generic-function 'origin-val :lambda-list '(m))
(cl:defmethod origin-val ((m <OccGrid3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:origin-val is deprecated.  Use pr_msgs-msg:origin instead.")
  (origin m))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <OccGrid3D>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-msg:data-val is deprecated.  Use pr_msgs-msg:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <OccGrid3D>) ostream)
  "Serializes a message object of type '<OccGrid3D>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'resolution))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_x_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_x_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_x_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_x_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_y_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_y_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_y_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_y_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_z_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_z_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_z_voxels)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_z_voxels)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'origin) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:write-byte (cl:ldb (cl:byte 8 0) ele) ostream))
   (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <OccGrid3D>) istream)
  "Deserializes a message object of type '<OccGrid3D>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'resolution) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_x_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_x_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_x_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_x_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_y_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_y_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_y_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_y_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'num_z_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'num_z_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'num_z_voxels)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'num_z_voxels)) (cl:read-byte istream))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'origin) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'data) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'data)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:aref vals i)) (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<OccGrid3D>)))
  "Returns string type for a message object of type '<OccGrid3D>"
  "pr_msgs/OccGrid3D")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'OccGrid3D)))
  "Returns string type for a message object of type 'OccGrid3D"
  "pr_msgs/OccGrid3D")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<OccGrid3D>)))
  "Returns md5sum for a message object of type '<OccGrid3D>"
  "3c71e0896dd3dc42f5341886fcc48fd1")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'OccGrid3D)))
  "Returns md5sum for a message object of type 'OccGrid3D"
  "3c71e0896dd3dc42f5341886fcc48fd1")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<OccGrid3D>)))
  "Returns full string definition for message of type '<OccGrid3D>"
  (cl:format cl:nil "#a 3-D grid map, modeled after the OccGrid.msg type~%Header header~%~%#resolution of cells [m/side] ~%float32 resolution~%~%# num cells in {x,y,z} direction~%uint32 num_x_voxels~%uint32 num_y_voxels~%uint32 num_z_voxels~%~%# exact center of map (always an odd number of voxels in each dimension)~%geometry_msgs/Point32 origin~%~%# the map data. 0-100, representing probability: ceil(100*p_occupied-0.5)~%# index =  kk * num_y_voxels * num_x_voxels + jj * num_x_voxels + ii~%byte[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'OccGrid3D)))
  "Returns full string definition for message of type 'OccGrid3D"
  (cl:format cl:nil "#a 3-D grid map, modeled after the OccGrid.msg type~%Header header~%~%#resolution of cells [m/side] ~%float32 resolution~%~%# num cells in {x,y,z} direction~%uint32 num_x_voxels~%uint32 num_y_voxels~%uint32 num_z_voxels~%~%# exact center of map (always an odd number of voxels in each dimension)~%geometry_msgs/Point32 origin~%~%# the map data. 0-100, representing probability: ceil(100*p_occupied-0.5)~%# index =  kk * num_y_voxels * num_x_voxels + jj * num_x_voxels + ii~%byte[] data~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Point32~%# This contains the position of a point in free space(with 32 bits of precision).~%# It is recommeded to use Point wherever possible instead of Point32.  ~%# ~%# This recommendation is to promote interoperability.  ~%#~%# This message is designed to take up less space when sending~%# lots of points at once, as in the case of a PointCloud.  ~%~%float32 x~%float32 y~%float32 z~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <OccGrid3D>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'origin))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'data) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 1)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <OccGrid3D>))
  "Converts a ROS message object to a list"
  (cl:list 'OccGrid3D
    (cl:cons ':header (header msg))
    (cl:cons ':resolution (resolution msg))
    (cl:cons ':num_x_voxels (num_x_voxels msg))
    (cl:cons ':num_y_voxels (num_y_voxels msg))
    (cl:cons ':num_z_voxels (num_z_voxels msg))
    (cl:cons ':origin (origin msg))
    (cl:cons ':data (data msg))
))

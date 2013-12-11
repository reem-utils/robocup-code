; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-srv)


;//! \htmlinclude StateRepresentationChanges-request.msg.html

(cl:defclass <StateRepresentationChanges-request> (roslisp-msg-protocol:ros-message)
  ((prev_image
    :reader prev_image
    :initarg :prev_image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (current_image
    :reader current_image
    :initarg :current_image
    :type sensor_msgs-msg:Image
    :initform (cl:make-instance 'sensor_msgs-msg:Image))
   (ignored_dirty_areas
    :reader ignored_dirty_areas
    :initarg :ignored_dirty_areas
    :type (cl:vector estirabot_msgs-msg:DirtyArea)
   :initform (cl:make-array 0 :element-type 'estirabot_msgs-msg:DirtyArea :initial-element (cl:make-instance 'estirabot_msgs-msg:DirtyArea))))
)

(cl:defclass StateRepresentationChanges-request (<StateRepresentationChanges-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StateRepresentationChanges-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StateRepresentationChanges-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<StateRepresentationChanges-request> is deprecated: use estirabot_msgs-srv:StateRepresentationChanges-request instead.")))

(cl:ensure-generic-function 'prev_image-val :lambda-list '(m))
(cl:defmethod prev_image-val ((m <StateRepresentationChanges-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:prev_image-val is deprecated.  Use estirabot_msgs-srv:prev_image instead.")
  (prev_image m))

(cl:ensure-generic-function 'current_image-val :lambda-list '(m))
(cl:defmethod current_image-val ((m <StateRepresentationChanges-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:current_image-val is deprecated.  Use estirabot_msgs-srv:current_image instead.")
  (current_image m))

(cl:ensure-generic-function 'ignored_dirty_areas-val :lambda-list '(m))
(cl:defmethod ignored_dirty_areas-val ((m <StateRepresentationChanges-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:ignored_dirty_areas-val is deprecated.  Use estirabot_msgs-srv:ignored_dirty_areas instead.")
  (ignored_dirty_areas m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StateRepresentationChanges-request>) ostream)
  "Serializes a message object of type '<StateRepresentationChanges-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'prev_image) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'current_image) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'ignored_dirty_areas))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'ignored_dirty_areas))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StateRepresentationChanges-request>) istream)
  "Deserializes a message object of type '<StateRepresentationChanges-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'prev_image) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'current_image) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'ignored_dirty_areas) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'ignored_dirty_areas)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'estirabot_msgs-msg:DirtyArea))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StateRepresentationChanges-request>)))
  "Returns string type for a service object of type '<StateRepresentationChanges-request>"
  "estirabot_msgs/StateRepresentationChangesRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StateRepresentationChanges-request)))
  "Returns string type for a service object of type 'StateRepresentationChanges-request"
  "estirabot_msgs/StateRepresentationChangesRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StateRepresentationChanges-request>)))
  "Returns md5sum for a message object of type '<StateRepresentationChanges-request>"
  "b297ec3f6ef61c64fcfbb64052d30c6d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StateRepresentationChanges-request)))
  "Returns md5sum for a message object of type 'StateRepresentationChanges-request"
  "b297ec3f6ef61c64fcfbb64052d30c6d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StateRepresentationChanges-request>)))
  "Returns full string definition for message of type '<StateRepresentationChanges-request>"
  (cl:format cl:nil "sensor_msgs/Image prev_image~%sensor_msgs/Image current_image~%estirabot_msgs/DirtyArea[] ignored_dirty_areas~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: estirabot_msgs/DirtyArea~%int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StateRepresentationChanges-request)))
  "Returns full string definition for message of type 'StateRepresentationChanges-request"
  (cl:format cl:nil "sensor_msgs/Image prev_image~%sensor_msgs/Image current_image~%estirabot_msgs/DirtyArea[] ignored_dirty_areas~%~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of cameara~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in src/image_encodings.cpp~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: estirabot_msgs/DirtyArea~%int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StateRepresentationChanges-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'prev_image))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'current_image))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'ignored_dirty_areas) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StateRepresentationChanges-request>))
  "Converts a ROS message object to a list"
  (cl:list 'StateRepresentationChanges-request
    (cl:cons ':prev_image (prev_image msg))
    (cl:cons ':current_image (current_image msg))
    (cl:cons ':ignored_dirty_areas (ignored_dirty_areas msg))
))
;//! \htmlinclude StateRepresentationChanges-response.msg.html

(cl:defclass <StateRepresentationChanges-response> (roslisp-msg-protocol:ros-message)
  ((changed_ellipses
    :reader changed_ellipses
    :initarg :changed_ellipses
    :type cl:integer
    :initform 0)
   (differences_string
    :reader differences_string
    :initarg :differences_string
    :type cl:string
    :initform "")
   (pre_state_string
    :reader pre_state_string
    :initarg :pre_state_string
    :type cl:string
    :initform ""))
)

(cl:defclass StateRepresentationChanges-response (<StateRepresentationChanges-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <StateRepresentationChanges-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'StateRepresentationChanges-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<StateRepresentationChanges-response> is deprecated: use estirabot_msgs-srv:StateRepresentationChanges-response instead.")))

(cl:ensure-generic-function 'changed_ellipses-val :lambda-list '(m))
(cl:defmethod changed_ellipses-val ((m <StateRepresentationChanges-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:changed_ellipses-val is deprecated.  Use estirabot_msgs-srv:changed_ellipses instead.")
  (changed_ellipses m))

(cl:ensure-generic-function 'differences_string-val :lambda-list '(m))
(cl:defmethod differences_string-val ((m <StateRepresentationChanges-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:differences_string-val is deprecated.  Use estirabot_msgs-srv:differences_string instead.")
  (differences_string m))

(cl:ensure-generic-function 'pre_state_string-val :lambda-list '(m))
(cl:defmethod pre_state_string-val ((m <StateRepresentationChanges-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:pre_state_string-val is deprecated.  Use estirabot_msgs-srv:pre_state_string instead.")
  (pre_state_string m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <StateRepresentationChanges-response>) ostream)
  "Serializes a message object of type '<StateRepresentationChanges-response>"
  (cl:let* ((signed (cl:slot-value msg 'changed_ellipses)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'differences_string))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'differences_string))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'pre_state_string))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'pre_state_string))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <StateRepresentationChanges-response>) istream)
  "Deserializes a message object of type '<StateRepresentationChanges-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'changed_ellipses) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'differences_string) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'differences_string) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'pre_state_string) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'pre_state_string) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<StateRepresentationChanges-response>)))
  "Returns string type for a service object of type '<StateRepresentationChanges-response>"
  "estirabot_msgs/StateRepresentationChangesResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StateRepresentationChanges-response)))
  "Returns string type for a service object of type 'StateRepresentationChanges-response"
  "estirabot_msgs/StateRepresentationChangesResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<StateRepresentationChanges-response>)))
  "Returns md5sum for a message object of type '<StateRepresentationChanges-response>"
  "b297ec3f6ef61c64fcfbb64052d30c6d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'StateRepresentationChanges-response)))
  "Returns md5sum for a message object of type 'StateRepresentationChanges-response"
  "b297ec3f6ef61c64fcfbb64052d30c6d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<StateRepresentationChanges-response>)))
  "Returns full string definition for message of type '<StateRepresentationChanges-response>"
  (cl:format cl:nil "~%int32 changed_ellipses~%string differences_string~%string pre_state_string~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'StateRepresentationChanges-response)))
  "Returns full string definition for message of type 'StateRepresentationChanges-response"
  (cl:format cl:nil "~%int32 changed_ellipses~%string differences_string~%string pre_state_string~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <StateRepresentationChanges-response>))
  (cl:+ 0
     4
     4 (cl:length (cl:slot-value msg 'differences_string))
     4 (cl:length (cl:slot-value msg 'pre_state_string))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <StateRepresentationChanges-response>))
  "Converts a ROS message object to a list"
  (cl:list 'StateRepresentationChanges-response
    (cl:cons ':changed_ellipses (changed_ellipses msg))
    (cl:cons ':differences_string (differences_string msg))
    (cl:cons ':pre_state_string (pre_state_string msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'StateRepresentationChanges)))
  'StateRepresentationChanges-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'StateRepresentationChanges)))
  'StateRepresentationChanges-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'StateRepresentationChanges)))
  "Returns string type for a service object of type '<StateRepresentationChanges>"
  "estirabot_msgs/StateRepresentationChanges")
; Auto-generated. Do not edit!


(cl:in-package door_detector_pal-msg)


;//! \htmlinclude DoorDetectorResult.msg.html

(cl:defclass <DoorDetectorResult> (roslisp-msg-protocol:ros-message)
  ((handle_side
    :reader handle_side
    :initarg :handle_side
    :type cl:string
    :initform "")
   (door_status
    :reader door_status
    :initarg :door_status
    :type cl:string
    :initform "")
   (door_handle
    :reader door_handle
    :initarg :door_handle
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (door_position
    :reader door_position
    :initarg :door_position
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped)))
)

(cl:defclass DoorDetectorResult (<DoorDetectorResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DoorDetectorResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DoorDetectorResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name door_detector_pal-msg:<DoorDetectorResult> is deprecated: use door_detector_pal-msg:DoorDetectorResult instead.")))

(cl:ensure-generic-function 'handle_side-val :lambda-list '(m))
(cl:defmethod handle_side-val ((m <DoorDetectorResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader door_detector_pal-msg:handle_side-val is deprecated.  Use door_detector_pal-msg:handle_side instead.")
  (handle_side m))

(cl:ensure-generic-function 'door_status-val :lambda-list '(m))
(cl:defmethod door_status-val ((m <DoorDetectorResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader door_detector_pal-msg:door_status-val is deprecated.  Use door_detector_pal-msg:door_status instead.")
  (door_status m))

(cl:ensure-generic-function 'door_handle-val :lambda-list '(m))
(cl:defmethod door_handle-val ((m <DoorDetectorResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader door_detector_pal-msg:door_handle-val is deprecated.  Use door_detector_pal-msg:door_handle instead.")
  (door_handle m))

(cl:ensure-generic-function 'door_position-val :lambda-list '(m))
(cl:defmethod door_position-val ((m <DoorDetectorResult>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader door_detector_pal-msg:door_position-val is deprecated.  Use door_detector_pal-msg:door_position instead.")
  (door_position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DoorDetectorResult>) ostream)
  "Serializes a message object of type '<DoorDetectorResult>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'handle_side))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'handle_side))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'door_status))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'door_status))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'door_handle) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'door_position) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DoorDetectorResult>) istream)
  "Deserializes a message object of type '<DoorDetectorResult>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'handle_side) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'handle_side) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'door_status) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'door_status) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'door_handle) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'door_position) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DoorDetectorResult>)))
  "Returns string type for a message object of type '<DoorDetectorResult>"
  "door_detector_pal/DoorDetectorResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DoorDetectorResult)))
  "Returns string type for a message object of type 'DoorDetectorResult"
  "door_detector_pal/DoorDetectorResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DoorDetectorResult>)))
  "Returns md5sum for a message object of type '<DoorDetectorResult>"
  "5769294bcaaeb780153856a9d6238a27")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DoorDetectorResult)))
  "Returns md5sum for a message object of type 'DoorDetectorResult"
  "5769294bcaaeb780153856a9d6238a27")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DoorDetectorResult>)))
  "Returns full string definition for message of type '<DoorDetectorResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%# side of the handle \"left\" or \"right\"~%string handle_side~%# status of the door \"open\" or \"closed\"~%string door_status~%# if it's closed and we have the position of the handle~%geometry_msgs/PoseStamped door_handle~%# if it's open and we have the position of the door centroid~%geometry_msgs/PoseStamped door_position~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DoorDetectorResult)))
  "Returns full string definition for message of type 'DoorDetectorResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%# Result~%# side of the handle \"left\" or \"right\"~%string handle_side~%# status of the door \"open\" or \"closed\"~%string door_status~%# if it's closed and we have the position of the handle~%geometry_msgs/PoseStamped door_handle~%# if it's open and we have the position of the door centroid~%geometry_msgs/PoseStamped door_position~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DoorDetectorResult>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'handle_side))
     4 (cl:length (cl:slot-value msg 'door_status))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'door_handle))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'door_position))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DoorDetectorResult>))
  "Converts a ROS message object to a list"
  (cl:list 'DoorDetectorResult
    (cl:cons ':handle_side (handle_side msg))
    (cl:cons ':door_status (door_status msg))
    (cl:cons ':door_handle (door_handle msg))
    (cl:cons ':door_position (door_position msg))
))

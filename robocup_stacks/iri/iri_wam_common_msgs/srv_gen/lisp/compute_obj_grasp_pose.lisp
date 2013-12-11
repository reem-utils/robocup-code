; Auto-generated. Do not edit!


(cl:in-package iri_wam_common_msgs-srv)


;//! \htmlinclude compute_obj_grasp_pose-request.msg.html

(cl:defclass <compute_obj_grasp_pose-request> (roslisp-msg-protocol:ros-message)
  ((filterID
    :reader filterID
    :initarg :filterID
    :type cl:integer
    :initform 0))
)

(cl:defclass compute_obj_grasp_pose-request (<compute_obj_grasp_pose-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <compute_obj_grasp_pose-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'compute_obj_grasp_pose-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<compute_obj_grasp_pose-request> is deprecated: use iri_wam_common_msgs-srv:compute_obj_grasp_pose-request instead.")))

(cl:ensure-generic-function 'filterID-val :lambda-list '(m))
(cl:defmethod filterID-val ((m <compute_obj_grasp_pose-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:filterID-val is deprecated.  Use iri_wam_common_msgs-srv:filterID instead.")
  (filterID m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <compute_obj_grasp_pose-request>) ostream)
  "Serializes a message object of type '<compute_obj_grasp_pose-request>"
  (cl:let* ((signed (cl:slot-value msg 'filterID)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <compute_obj_grasp_pose-request>) istream)
  "Deserializes a message object of type '<compute_obj_grasp_pose-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'filterID) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<compute_obj_grasp_pose-request>)))
  "Returns string type for a service object of type '<compute_obj_grasp_pose-request>"
  "iri_wam_common_msgs/compute_obj_grasp_poseRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'compute_obj_grasp_pose-request)))
  "Returns string type for a service object of type 'compute_obj_grasp_pose-request"
  "iri_wam_common_msgs/compute_obj_grasp_poseRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<compute_obj_grasp_pose-request>)))
  "Returns md5sum for a message object of type '<compute_obj_grasp_pose-request>"
  "a4372bd3edc1254ae3d8c932f3655620")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'compute_obj_grasp_pose-request)))
  "Returns md5sum for a message object of type 'compute_obj_grasp_pose-request"
  "a4372bd3edc1254ae3d8c932f3655620")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<compute_obj_grasp_pose-request>)))
  "Returns full string definition for message of type '<compute_obj_grasp_pose-request>"
  (cl:format cl:nil "int32 filterID~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'compute_obj_grasp_pose-request)))
  "Returns full string definition for message of type 'compute_obj_grasp_pose-request"
  (cl:format cl:nil "int32 filterID~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <compute_obj_grasp_pose-request>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <compute_obj_grasp_pose-request>))
  "Converts a ROS message object to a list"
  (cl:list 'compute_obj_grasp_pose-request
    (cl:cons ':filterID (filterID msg))
))
;//! \htmlinclude compute_obj_grasp_pose-response.msg.html

(cl:defclass <compute_obj_grasp_pose-response> (roslisp-msg-protocol:ros-message)
  ((graspPose
    :reader graspPose
    :initarg :graspPose
    :type geometry_msgs-msg:PoseStamped
    :initform (cl:make-instance 'geometry_msgs-msg:PoseStamped))
   (wrinkleness
    :reader wrinkleness
    :initarg :wrinkleness
    :type cl:float
    :initform 0.0))
)

(cl:defclass compute_obj_grasp_pose-response (<compute_obj_grasp_pose-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <compute_obj_grasp_pose-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'compute_obj_grasp_pose-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_wam_common_msgs-srv:<compute_obj_grasp_pose-response> is deprecated: use iri_wam_common_msgs-srv:compute_obj_grasp_pose-response instead.")))

(cl:ensure-generic-function 'graspPose-val :lambda-list '(m))
(cl:defmethod graspPose-val ((m <compute_obj_grasp_pose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:graspPose-val is deprecated.  Use iri_wam_common_msgs-srv:graspPose instead.")
  (graspPose m))

(cl:ensure-generic-function 'wrinkleness-val :lambda-list '(m))
(cl:defmethod wrinkleness-val ((m <compute_obj_grasp_pose-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_wam_common_msgs-srv:wrinkleness-val is deprecated.  Use iri_wam_common_msgs-srv:wrinkleness instead.")
  (wrinkleness m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <compute_obj_grasp_pose-response>) ostream)
  "Serializes a message object of type '<compute_obj_grasp_pose-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'graspPose) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'wrinkleness))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <compute_obj_grasp_pose-response>) istream)
  "Deserializes a message object of type '<compute_obj_grasp_pose-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'graspPose) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'wrinkleness) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<compute_obj_grasp_pose-response>)))
  "Returns string type for a service object of type '<compute_obj_grasp_pose-response>"
  "iri_wam_common_msgs/compute_obj_grasp_poseResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'compute_obj_grasp_pose-response)))
  "Returns string type for a service object of type 'compute_obj_grasp_pose-response"
  "iri_wam_common_msgs/compute_obj_grasp_poseResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<compute_obj_grasp_pose-response>)))
  "Returns md5sum for a message object of type '<compute_obj_grasp_pose-response>"
  "a4372bd3edc1254ae3d8c932f3655620")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'compute_obj_grasp_pose-response)))
  "Returns md5sum for a message object of type 'compute_obj_grasp_pose-response"
  "a4372bd3edc1254ae3d8c932f3655620")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<compute_obj_grasp_pose-response>)))
  "Returns full string definition for message of type '<compute_obj_grasp_pose-response>"
  (cl:format cl:nil "geometry_msgs/PoseStamped graspPose~%float32 wrinkleness~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'compute_obj_grasp_pose-response)))
  "Returns full string definition for message of type 'compute_obj_grasp_pose-response"
  (cl:format cl:nil "geometry_msgs/PoseStamped graspPose~%float32 wrinkleness~%~%~%================================================================================~%MSG: geometry_msgs/PoseStamped~%# A Pose with reference coordinate frame and timestamp~%Header header~%Pose pose~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <compute_obj_grasp_pose-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'graspPose))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <compute_obj_grasp_pose-response>))
  "Converts a ROS message object to a list"
  (cl:list 'compute_obj_grasp_pose-response
    (cl:cons ':graspPose (graspPose msg))
    (cl:cons ':wrinkleness (wrinkleness msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'compute_obj_grasp_pose)))
  'compute_obj_grasp_pose-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'compute_obj_grasp_pose)))
  'compute_obj_grasp_pose-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'compute_obj_grasp_pose)))
  "Returns string type for a service object of type '<compute_obj_grasp_pose>"
  "iri_wam_common_msgs/compute_obj_grasp_pose")
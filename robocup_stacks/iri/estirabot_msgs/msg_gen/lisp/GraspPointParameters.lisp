; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-msg)


;//! \htmlinclude GraspPointParameters.msg.html

(cl:defclass <GraspPointParameters> (roslisp-msg-protocol:ros-message)
  ((pre_grasp_modifier
    :reader pre_grasp_modifier
    :initarg :pre_grasp_modifier
    :type geometry_msgs-msg:Transform
    :initform (cl:make-instance 'geometry_msgs-msg:Transform))
   (grasp_modifiers
    :reader grasp_modifiers
    :initarg :grasp_modifiers
    :type (cl:vector geometry_msgs-msg:Transform)
   :initform (cl:make-array 0 :element-type 'geometry_msgs-msg:Transform :initial-element (cl:make-instance 'geometry_msgs-msg:Transform)))
   (grasp_modifier_used
    :reader grasp_modifier_used
    :initarg :grasp_modifier_used
    :type cl:fixnum
    :initform 0))
)

(cl:defclass GraspPointParameters (<GraspPointParameters>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspPointParameters>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspPointParameters)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-msg:<GraspPointParameters> is deprecated: use estirabot_msgs-msg:GraspPointParameters instead.")))

(cl:ensure-generic-function 'pre_grasp_modifier-val :lambda-list '(m))
(cl:defmethod pre_grasp_modifier-val ((m <GraspPointParameters>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:pre_grasp_modifier-val is deprecated.  Use estirabot_msgs-msg:pre_grasp_modifier instead.")
  (pre_grasp_modifier m))

(cl:ensure-generic-function 'grasp_modifiers-val :lambda-list '(m))
(cl:defmethod grasp_modifiers-val ((m <GraspPointParameters>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:grasp_modifiers-val is deprecated.  Use estirabot_msgs-msg:grasp_modifiers instead.")
  (grasp_modifiers m))

(cl:ensure-generic-function 'grasp_modifier_used-val :lambda-list '(m))
(cl:defmethod grasp_modifier_used-val ((m <GraspPointParameters>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-msg:grasp_modifier_used-val is deprecated.  Use estirabot_msgs-msg:grasp_modifier_used instead.")
  (grasp_modifier_used m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspPointParameters>) ostream)
  "Serializes a message object of type '<GraspPointParameters>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pre_grasp_modifier) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'grasp_modifiers))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'grasp_modifiers))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_modifier_used)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspPointParameters>) istream)
  "Deserializes a message object of type '<GraspPointParameters>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pre_grasp_modifier) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'grasp_modifiers) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'grasp_modifiers)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'geometry_msgs-msg:Transform))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_modifier_used)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspPointParameters>)))
  "Returns string type for a message object of type '<GraspPointParameters>"
  "estirabot_msgs/GraspPointParameters")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspPointParameters)))
  "Returns string type for a message object of type 'GraspPointParameters"
  "estirabot_msgs/GraspPointParameters")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspPointParameters>)))
  "Returns md5sum for a message object of type '<GraspPointParameters>"
  "4a7fd3c439b5601709521f9ae1410df2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspPointParameters)))
  "Returns md5sum for a message object of type 'GraspPointParameters"
  "4a7fd3c439b5601709521f9ae1410df2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspPointParameters>)))
  "Returns full string definition for message of type '<GraspPointParameters>"
  (cl:format cl:nil "# Message for parameters to modify a grasp point~%# These parameters apply on a cartesian coordinate~%# (geometry_msgs/pose).~%~%geometry_msgs/Transform pre_grasp_modifier~%geometry_msgs/Transform[] grasp_modifiers~%uint8 grasp_modifier_used~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspPointParameters)))
  "Returns full string definition for message of type 'GraspPointParameters"
  (cl:format cl:nil "# Message for parameters to modify a grasp point~%# These parameters apply on a cartesian coordinate~%# (geometry_msgs/pose).~%~%geometry_msgs/Transform pre_grasp_modifier~%geometry_msgs/Transform[] grasp_modifiers~%uint8 grasp_modifier_used~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspPointParameters>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pre_grasp_modifier))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'grasp_modifiers) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspPointParameters>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspPointParameters
    (cl:cons ':pre_grasp_modifier (pre_grasp_modifier msg))
    (cl:cons ':grasp_modifiers (grasp_modifiers msg))
    (cl:cons ':grasp_modifier_used (grasp_modifier_used msg))
))

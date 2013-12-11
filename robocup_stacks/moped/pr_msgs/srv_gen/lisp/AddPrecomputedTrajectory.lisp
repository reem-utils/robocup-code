; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude AddPrecomputedTrajectory-request.msg.html

(cl:defclass <AddPrecomputedTrajectory-request> (roslisp-msg-protocol:ros-message)
  ((traj
    :reader traj
    :initarg :traj
    :type pr_msgs-msg:WAMPrecomputedBlendedTrajectory
    :initform (cl:make-instance 'pr_msgs-msg:WAMPrecomputedBlendedTrajectory)))
)

(cl:defclass AddPrecomputedTrajectory-request (<AddPrecomputedTrajectory-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddPrecomputedTrajectory-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddPrecomputedTrajectory-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<AddPrecomputedTrajectory-request> is deprecated: use pr_msgs-srv:AddPrecomputedTrajectory-request instead.")))

(cl:ensure-generic-function 'traj-val :lambda-list '(m))
(cl:defmethod traj-val ((m <AddPrecomputedTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:traj-val is deprecated.  Use pr_msgs-srv:traj instead.")
  (traj m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddPrecomputedTrajectory-request>) ostream)
  "Serializes a message object of type '<AddPrecomputedTrajectory-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'traj) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddPrecomputedTrajectory-request>) istream)
  "Deserializes a message object of type '<AddPrecomputedTrajectory-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'traj) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddPrecomputedTrajectory-request>)))
  "Returns string type for a service object of type '<AddPrecomputedTrajectory-request>"
  "pr_msgs/AddPrecomputedTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddPrecomputedTrajectory-request)))
  "Returns string type for a service object of type 'AddPrecomputedTrajectory-request"
  "pr_msgs/AddPrecomputedTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddPrecomputedTrajectory-request>)))
  "Returns md5sum for a message object of type '<AddPrecomputedTrajectory-request>"
  "df6b014b3af6aad7a3a7cf42649684a6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddPrecomputedTrajectory-request)))
  "Returns md5sum for a message object of type 'AddPrecomputedTrajectory-request"
  "df6b014b3af6aad7a3a7cf42649684a6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddPrecomputedTrajectory-request>)))
  "Returns full string definition for message of type '<AddPrecomputedTrajectory-request>"
  (cl:format cl:nil "pr_msgs/WAMPrecomputedBlendedTrajectory traj~%~%================================================================================~%MSG: pr_msgs/WAMPrecomputedBlendedTrajectory~%int16 id~%bool HoldOnStall~%bool WaitForStart~%pr_msgs/Joints start_position~%pr_msgs/Joints end_position~%pr_msgs/Joints max_joint_vel~%pr_msgs/Joints max_joint_accel~%pr_msgs/WAMPrecomputedBlendElement[] macpieces~%float64 traj_duration~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%================================================================================~%MSG: pr_msgs/WAMPrecomputedBlendElement~%pr_msgs/Joints start_pos~%pr_msgs/Joints end_pos~%float64 start_time~%float64 duration~%float64 max_path_velocity~%float64 max_path_acceleration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddPrecomputedTrajectory-request)))
  "Returns full string definition for message of type 'AddPrecomputedTrajectory-request"
  (cl:format cl:nil "pr_msgs/WAMPrecomputedBlendedTrajectory traj~%~%================================================================================~%MSG: pr_msgs/WAMPrecomputedBlendedTrajectory~%int16 id~%bool HoldOnStall~%bool WaitForStart~%pr_msgs/Joints start_position~%pr_msgs/Joints end_position~%pr_msgs/Joints max_joint_vel~%pr_msgs/Joints max_joint_accel~%pr_msgs/WAMPrecomputedBlendElement[] macpieces~%float64 traj_duration~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%================================================================================~%MSG: pr_msgs/WAMPrecomputedBlendElement~%pr_msgs/Joints start_pos~%pr_msgs/Joints end_pos~%float64 start_time~%float64 duration~%float64 max_path_velocity~%float64 max_path_acceleration~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddPrecomputedTrajectory-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'traj))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddPrecomputedTrajectory-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AddPrecomputedTrajectory-request
    (cl:cons ':traj (traj msg))
))
;//! \htmlinclude AddPrecomputedTrajectory-response.msg.html

(cl:defclass <AddPrecomputedTrajectory-response> (roslisp-msg-protocol:ros-message)
  ((ok
    :reader ok
    :initarg :ok
    :type cl:boolean
    :initform cl:nil)
   (reason
    :reader reason
    :initarg :reason
    :type cl:string
    :initform "")
   (id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0))
)

(cl:defclass AddPrecomputedTrajectory-response (<AddPrecomputedTrajectory-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddPrecomputedTrajectory-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddPrecomputedTrajectory-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<AddPrecomputedTrajectory-response> is deprecated: use pr_msgs-srv:AddPrecomputedTrajectory-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <AddPrecomputedTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:ok-val is deprecated.  Use pr_msgs-srv:ok instead.")
  (ok m))

(cl:ensure-generic-function 'reason-val :lambda-list '(m))
(cl:defmethod reason-val ((m <AddPrecomputedTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:reason-val is deprecated.  Use pr_msgs-srv:reason instead.")
  (reason m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <AddPrecomputedTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:id-val is deprecated.  Use pr_msgs-srv:id instead.")
  (id m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddPrecomputedTrajectory-response>) ostream)
  "Serializes a message object of type '<AddPrecomputedTrajectory-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'ok) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'reason))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'reason))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddPrecomputedTrajectory-response>) istream)
  "Deserializes a message object of type '<AddPrecomputedTrajectory-response>"
    (cl:setf (cl:slot-value msg 'ok) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'reason) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'reason) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddPrecomputedTrajectory-response>)))
  "Returns string type for a service object of type '<AddPrecomputedTrajectory-response>"
  "pr_msgs/AddPrecomputedTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddPrecomputedTrajectory-response)))
  "Returns string type for a service object of type 'AddPrecomputedTrajectory-response"
  "pr_msgs/AddPrecomputedTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddPrecomputedTrajectory-response>)))
  "Returns md5sum for a message object of type '<AddPrecomputedTrajectory-response>"
  "df6b014b3af6aad7a3a7cf42649684a6")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddPrecomputedTrajectory-response)))
  "Returns md5sum for a message object of type 'AddPrecomputedTrajectory-response"
  "df6b014b3af6aad7a3a7cf42649684a6")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddPrecomputedTrajectory-response>)))
  "Returns full string definition for message of type '<AddPrecomputedTrajectory-response>"
  (cl:format cl:nil "bool ok~%string reason~%uint32 id~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddPrecomputedTrajectory-response)))
  "Returns full string definition for message of type 'AddPrecomputedTrajectory-response"
  (cl:format cl:nil "bool ok~%string reason~%uint32 id~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddPrecomputedTrajectory-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'reason))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddPrecomputedTrajectory-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AddPrecomputedTrajectory-response
    (cl:cons ':ok (ok msg))
    (cl:cons ':reason (reason msg))
    (cl:cons ':id (id msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AddPrecomputedTrajectory)))
  'AddPrecomputedTrajectory-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AddPrecomputedTrajectory)))
  'AddPrecomputedTrajectory-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddPrecomputedTrajectory)))
  "Returns string type for a service object of type '<AddPrecomputedTrajectory>"
  "pr_msgs/AddPrecomputedTrajectory")
; Auto-generated. Do not edit!


(cl:in-package pr_msgs-srv)


;//! \htmlinclude AddTrajectory-request.msg.html

(cl:defclass <AddTrajectory-request> (roslisp-msg-protocol:ros-message)
  ((traj
    :reader traj
    :initarg :traj
    :type pr_msgs-msg:JointTraj
    :initform (cl:make-instance 'pr_msgs-msg:JointTraj)))
)

(cl:defclass AddTrajectory-request (<AddTrajectory-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddTrajectory-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddTrajectory-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<AddTrajectory-request> is deprecated: use pr_msgs-srv:AddTrajectory-request instead.")))

(cl:ensure-generic-function 'traj-val :lambda-list '(m))
(cl:defmethod traj-val ((m <AddTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:traj-val is deprecated.  Use pr_msgs-srv:traj instead.")
  (traj m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddTrajectory-request>) ostream)
  "Serializes a message object of type '<AddTrajectory-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'traj) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddTrajectory-request>) istream)
  "Deserializes a message object of type '<AddTrajectory-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'traj) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddTrajectory-request>)))
  "Returns string type for a service object of type '<AddTrajectory-request>"
  "pr_msgs/AddTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddTrajectory-request)))
  "Returns string type for a service object of type 'AddTrajectory-request"
  "pr_msgs/AddTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddTrajectory-request>)))
  "Returns md5sum for a message object of type '<AddTrajectory-request>"
  "718f35ed3e678fbf88689fadd359050d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddTrajectory-request)))
  "Returns md5sum for a message object of type 'AddTrajectory-request"
  "718f35ed3e678fbf88689fadd359050d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddTrajectory-request>)))
  "Returns full string definition for message of type '<AddTrajectory-request>"
  (cl:format cl:nil "pr_msgs/JointTraj traj~%~%================================================================================~%MSG: pr_msgs/JointTraj~%pr_msgs/Joints[] positions~%float32[] blend_radius~%uint32 options~%~%# options should be powers of 2, so that they can be OR'd together~%uint32 opt_WaitForStart=1~%uint32 opt_CancelOnStall=2~%uint32 opt_CancelOnForceInput=4~%uint32 opt_CancelOnTactileInput=8~%#uint32 opt_          =16  # placeholder for next value~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddTrajectory-request)))
  "Returns full string definition for message of type 'AddTrajectory-request"
  (cl:format cl:nil "pr_msgs/JointTraj traj~%~%================================================================================~%MSG: pr_msgs/JointTraj~%pr_msgs/Joints[] positions~%float32[] blend_radius~%uint32 options~%~%# options should be powers of 2, so that they can be OR'd together~%uint32 opt_WaitForStart=1~%uint32 opt_CancelOnStall=2~%uint32 opt_CancelOnForceInput=4~%uint32 opt_CancelOnTactileInput=8~%#uint32 opt_          =16  # placeholder for next value~%~%================================================================================~%MSG: pr_msgs/Joints~%float64[] j~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddTrajectory-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'traj))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddTrajectory-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AddTrajectory-request
    (cl:cons ':traj (traj msg))
))
;//! \htmlinclude AddTrajectory-response.msg.html

(cl:defclass <AddTrajectory-response> (roslisp-msg-protocol:ros-message)
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

(cl:defclass AddTrajectory-response (<AddTrajectory-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddTrajectory-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddTrajectory-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pr_msgs-srv:<AddTrajectory-response> is deprecated: use pr_msgs-srv:AddTrajectory-response instead.")))

(cl:ensure-generic-function 'ok-val :lambda-list '(m))
(cl:defmethod ok-val ((m <AddTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:ok-val is deprecated.  Use pr_msgs-srv:ok instead.")
  (ok m))

(cl:ensure-generic-function 'reason-val :lambda-list '(m))
(cl:defmethod reason-val ((m <AddTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:reason-val is deprecated.  Use pr_msgs-srv:reason instead.")
  (reason m))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <AddTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pr_msgs-srv:id-val is deprecated.  Use pr_msgs-srv:id instead.")
  (id m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddTrajectory-response>) ostream)
  "Serializes a message object of type '<AddTrajectory-response>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddTrajectory-response>) istream)
  "Deserializes a message object of type '<AddTrajectory-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddTrajectory-response>)))
  "Returns string type for a service object of type '<AddTrajectory-response>"
  "pr_msgs/AddTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddTrajectory-response)))
  "Returns string type for a service object of type 'AddTrajectory-response"
  "pr_msgs/AddTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddTrajectory-response>)))
  "Returns md5sum for a message object of type '<AddTrajectory-response>"
  "718f35ed3e678fbf88689fadd359050d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddTrajectory-response)))
  "Returns md5sum for a message object of type 'AddTrajectory-response"
  "718f35ed3e678fbf88689fadd359050d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddTrajectory-response>)))
  "Returns full string definition for message of type '<AddTrajectory-response>"
  (cl:format cl:nil "bool ok~%string reason~%uint32 id~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddTrajectory-response)))
  "Returns full string definition for message of type 'AddTrajectory-response"
  (cl:format cl:nil "bool ok~%string reason~%uint32 id~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddTrajectory-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'reason))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddTrajectory-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AddTrajectory-response
    (cl:cons ':ok (ok msg))
    (cl:cons ':reason (reason msg))
    (cl:cons ':id (id msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AddTrajectory)))
  'AddTrajectory-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AddTrajectory)))
  'AddTrajectory-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddTrajectory)))
  "Returns string type for a service object of type '<AddTrajectory>"
  "pr_msgs/AddTrajectory")
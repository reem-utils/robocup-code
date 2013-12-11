; Auto-generated. Do not edit!


(cl:in-package gpsr-msg)


;//! \htmlinclude action_list.msg.html

(cl:defclass <action_list> (roslisp-msg-protocol:ros-message)
  ((actionList
    :reader actionList
    :initarg :actionList
    :type (cl:vector gpsr-msg:action)
   :initform (cl:make-array 0 :element-type 'gpsr-msg:action :initial-element (cl:make-instance 'gpsr-msg:action))))
)

(cl:defclass action_list (<action_list>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <action_list>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'action_list)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gpsr-msg:<action_list> is deprecated: use gpsr-msg:action_list instead.")))

(cl:ensure-generic-function 'actionList-val :lambda-list '(m))
(cl:defmethod actionList-val ((m <action_list>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsr-msg:actionList-val is deprecated.  Use gpsr-msg:actionList instead.")
  (actionList m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <action_list>) ostream)
  "Serializes a message object of type '<action_list>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'actionList))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'actionList))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <action_list>) istream)
  "Deserializes a message object of type '<action_list>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'actionList) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'actionList)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'gpsr-msg:action))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<action_list>)))
  "Returns string type for a message object of type '<action_list>"
  "gpsr/action_list")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'action_list)))
  "Returns string type for a message object of type 'action_list"
  "gpsr/action_list")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<action_list>)))
  "Returns md5sum for a message object of type '<action_list>"
  "787e44f80e004f43718f2db3eba127b0")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'action_list)))
  "Returns md5sum for a message object of type 'action_list"
  "787e44f80e004f43718f2db3eba127b0")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<action_list>)))
  "Returns full string definition for message of type '<action_list>"
  (cl:format cl:nil "action[] actionList~%================================================================================~%MSG: gpsr/action~%string action~%string person~%string location~%string item~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'action_list)))
  "Returns full string definition for message of type 'action_list"
  (cl:format cl:nil "action[] actionList~%================================================================================~%MSG: gpsr/action~%string action~%string person~%string location~%string item~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <action_list>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'actionList) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <action_list>))
  "Converts a ROS message object to a list"
  (cl:list 'action_list
    (cl:cons ':actionList (actionList msg))
))

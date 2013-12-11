; Auto-generated. Do not edit!


(cl:in-package gpsr-msg)


;//! \htmlinclude order_list.msg.html

(cl:defclass <order_list> (roslisp-msg-protocol:ros-message)
  ((actionSet
    :reader actionSet
    :initarg :actionSet
    :type (cl:vector gpsr-msg:order)
   :initform (cl:make-array 0 :element-type 'gpsr-msg:order :initial-element (cl:make-instance 'gpsr-msg:order))))
)

(cl:defclass order_list (<order_list>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <order_list>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'order_list)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gpsr-msg:<order_list> is deprecated: use gpsr-msg:order_list instead.")))

(cl:ensure-generic-function 'actionSet-val :lambda-list '(m))
(cl:defmethod actionSet-val ((m <order_list>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gpsr-msg:actionSet-val is deprecated.  Use gpsr-msg:actionSet instead.")
  (actionSet m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <order_list>) ostream)
  "Serializes a message object of type '<order_list>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'actionSet))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'actionSet))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <order_list>) istream)
  "Deserializes a message object of type '<order_list>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'actionSet) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'actionSet)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'gpsr-msg:order))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<order_list>)))
  "Returns string type for a message object of type '<order_list>"
  "gpsr/order_list")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'order_list)))
  "Returns string type for a message object of type 'order_list"
  "gpsr/order_list")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<order_list>)))
  "Returns md5sum for a message object of type '<order_list>"
  "4056d793c91331c5f484bd54042199ea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'order_list)))
  "Returns md5sum for a message object of type 'order_list"
  "4056d793c91331c5f484bd54042199ea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<order_list>)))
  "Returns full string definition for message of type '<order_list>"
  (cl:format cl:nil "order[] actionSet~%~%================================================================================~%MSG: gpsr/order~%string action~%string person~%string location~%string item~%string[] other~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'order_list)))
  "Returns full string definition for message of type 'order_list"
  (cl:format cl:nil "order[] actionSet~%~%================================================================================~%MSG: gpsr/order~%string action~%string person~%string location~%string item~%string[] other~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <order_list>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'actionSet) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <order_list>))
  "Converts a ROS message object to a list"
  (cl:list 'order_list
    (cl:cons ':actionSet (actionSet msg))
))

; Auto-generated. Do not edit!


(cl:in-package iri_publish_params-msg)


;//! \htmlinclude classifier_params.msg.html

(cl:defclass <classifier_params> (roslisp-msg-protocol:ros-message)
  ((params
    :reader params
    :initarg :params
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass classifier_params (<classifier_params>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <classifier_params>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'classifier_params)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_publish_params-msg:<classifier_params> is deprecated: use iri_publish_params-msg:classifier_params instead.")))

(cl:ensure-generic-function 'params-val :lambda-list '(m))
(cl:defmethod params-val ((m <classifier_params>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_publish_params-msg:params-val is deprecated.  Use iri_publish_params-msg:params instead.")
  (params m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <classifier_params>) ostream)
  "Serializes a message object of type '<classifier_params>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'params))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'params))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <classifier_params>) istream)
  "Deserializes a message object of type '<classifier_params>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'params) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'params)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<classifier_params>)))
  "Returns string type for a message object of type '<classifier_params>"
  "iri_publish_params/classifier_params")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'classifier_params)))
  "Returns string type for a message object of type 'classifier_params"
  "iri_publish_params/classifier_params")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<classifier_params>)))
  "Returns md5sum for a message object of type '<classifier_params>"
  "8e22f8c3368a715022fd214d9775704d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'classifier_params)))
  "Returns md5sum for a message object of type 'classifier_params"
  "8e22f8c3368a715022fd214d9775704d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<classifier_params>)))
  "Returns full string definition for message of type '<classifier_params>"
  (cl:format cl:nil "float32[] params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'classifier_params)))
  "Returns full string definition for message of type 'classifier_params"
  (cl:format cl:nil "float32[] params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <classifier_params>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'params) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <classifier_params>))
  "Converts a ROS message object to a list"
  (cl:list 'classifier_params
    (cl:cons ':params (params msg))
))

; Auto-generated. Do not edit!


(cl:in-package iri_publish_params-msg)


;//! \htmlinclude classifier_update.msg.html

(cl:defclass <classifier_update> (roslisp-msg-protocol:ros-message)
  ((update_params
    :reader update_params
    :initarg :update_params
    :type (cl:vector iri_publish_params-msg:classifier_params)
   :initform (cl:make-array 0 :element-type 'iri_publish_params-msg:classifier_params :initial-element (cl:make-instance 'iri_publish_params-msg:classifier_params)))
   (selected_centroid
    :reader selected_centroid
    :initarg :selected_centroid
    :type cl:integer
    :initform 0)
   (filter_method
    :reader filter_method
    :initarg :filter_method
    :type cl:integer
    :initform 0))
)

(cl:defclass classifier_update (<classifier_update>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <classifier_update>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'classifier_update)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_publish_params-msg:<classifier_update> is deprecated: use iri_publish_params-msg:classifier_update instead.")))

(cl:ensure-generic-function 'update_params-val :lambda-list '(m))
(cl:defmethod update_params-val ((m <classifier_update>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_publish_params-msg:update_params-val is deprecated.  Use iri_publish_params-msg:update_params instead.")
  (update_params m))

(cl:ensure-generic-function 'selected_centroid-val :lambda-list '(m))
(cl:defmethod selected_centroid-val ((m <classifier_update>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_publish_params-msg:selected_centroid-val is deprecated.  Use iri_publish_params-msg:selected_centroid instead.")
  (selected_centroid m))

(cl:ensure-generic-function 'filter_method-val :lambda-list '(m))
(cl:defmethod filter_method-val ((m <classifier_update>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_publish_params-msg:filter_method-val is deprecated.  Use iri_publish_params-msg:filter_method instead.")
  (filter_method m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <classifier_update>) ostream)
  "Serializes a message object of type '<classifier_update>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'update_params))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'update_params))
  (cl:let* ((signed (cl:slot-value msg 'selected_centroid)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'filter_method)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <classifier_update>) istream)
  "Deserializes a message object of type '<classifier_update>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'update_params) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'update_params)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'iri_publish_params-msg:classifier_params))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'selected_centroid) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'filter_method) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<classifier_update>)))
  "Returns string type for a message object of type '<classifier_update>"
  "iri_publish_params/classifier_update")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'classifier_update)))
  "Returns string type for a message object of type 'classifier_update"
  "iri_publish_params/classifier_update")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<classifier_update>)))
  "Returns md5sum for a message object of type '<classifier_update>"
  "a27aec3298bbdcd2bd8ad5da8e997b16")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'classifier_update)))
  "Returns md5sum for a message object of type 'classifier_update"
  "a27aec3298bbdcd2bd8ad5da8e997b16")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<classifier_update>)))
  "Returns full string definition for message of type '<classifier_update>"
  (cl:format cl:nil "classifier_params[] update_params~%int32 selected_centroid~%int32 filter_method~%~%================================================================================~%MSG: iri_publish_params/classifier_params~%float32[] params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'classifier_update)))
  "Returns full string definition for message of type 'classifier_update"
  (cl:format cl:nil "classifier_params[] update_params~%int32 selected_centroid~%int32 filter_method~%~%================================================================================~%MSG: iri_publish_params/classifier_params~%float32[] params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <classifier_update>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'update_params) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <classifier_update>))
  "Converts a ROS message object to a list"
  (cl:list 'classifier_update
    (cl:cons ':update_params (update_params msg))
    (cl:cons ':selected_centroid (selected_centroid msg))
    (cl:cons ':filter_method (filter_method msg))
))

; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-srv)


;//! \htmlinclude RepresentationToString-request.msg.html

(cl:defclass <RepresentationToString-request> (roslisp-msg-protocol:ros-message)
  ((dirty_areas
    :reader dirty_areas
    :initarg :dirty_areas
    :type (cl:vector estirabot_msgs-msg:DirtyArea)
   :initform (cl:make-array 0 :element-type 'estirabot_msgs-msg:DirtyArea :initial-element (cl:make-instance 'estirabot_msgs-msg:DirtyArea)))
   (distances
    :reader distances
    :initarg :distances
    :type (cl:vector estirabot_msgs-msg:PointsDistanceMsg)
   :initform (cl:make-array 0 :element-type 'estirabot_msgs-msg:PointsDistanceMsg :initial-element (cl:make-instance 'estirabot_msgs-msg:PointsDistanceMsg)))
   (traversed_ellipses
    :reader traversed_ellipses
    :initarg :traversed_ellipses
    :type (cl:vector estirabot_msgs-msg:TraversedEllipses)
   :initform (cl:make-array 0 :element-type 'estirabot_msgs-msg:TraversedEllipses :initial-element (cl:make-instance 'estirabot_msgs-msg:TraversedEllipses))))
)

(cl:defclass RepresentationToString-request (<RepresentationToString-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RepresentationToString-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RepresentationToString-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<RepresentationToString-request> is deprecated: use estirabot_msgs-srv:RepresentationToString-request instead.")))

(cl:ensure-generic-function 'dirty_areas-val :lambda-list '(m))
(cl:defmethod dirty_areas-val ((m <RepresentationToString-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:dirty_areas-val is deprecated.  Use estirabot_msgs-srv:dirty_areas instead.")
  (dirty_areas m))

(cl:ensure-generic-function 'distances-val :lambda-list '(m))
(cl:defmethod distances-val ((m <RepresentationToString-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:distances-val is deprecated.  Use estirabot_msgs-srv:distances instead.")
  (distances m))

(cl:ensure-generic-function 'traversed_ellipses-val :lambda-list '(m))
(cl:defmethod traversed_ellipses-val ((m <RepresentationToString-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:traversed_ellipses-val is deprecated.  Use estirabot_msgs-srv:traversed_ellipses instead.")
  (traversed_ellipses m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RepresentationToString-request>) ostream)
  "Serializes a message object of type '<RepresentationToString-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'dirty_areas))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'dirty_areas))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'distances))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'distances))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'traversed_ellipses))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'traversed_ellipses))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RepresentationToString-request>) istream)
  "Deserializes a message object of type '<RepresentationToString-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'dirty_areas) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'dirty_areas)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'estirabot_msgs-msg:DirtyArea))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'distances) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'distances)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'estirabot_msgs-msg:PointsDistanceMsg))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'traversed_ellipses) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'traversed_ellipses)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'estirabot_msgs-msg:TraversedEllipses))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RepresentationToString-request>)))
  "Returns string type for a service object of type '<RepresentationToString-request>"
  "estirabot_msgs/RepresentationToStringRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RepresentationToString-request)))
  "Returns string type for a service object of type 'RepresentationToString-request"
  "estirabot_msgs/RepresentationToStringRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RepresentationToString-request>)))
  "Returns md5sum for a message object of type '<RepresentationToString-request>"
  "a1b22891042192e0316f71d2c67c0d87")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RepresentationToString-request)))
  "Returns md5sum for a message object of type 'RepresentationToString-request"
  "a1b22891042192e0316f71d2c67c0d87")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RepresentationToString-request>)))
  "Returns full string definition for message of type '<RepresentationToString-request>"
  (cl:format cl:nil "estirabot_msgs/DirtyArea[] dirty_areas~%estirabot_msgs/PointsDistanceMsg[] distances~%estirabot_msgs/TraversedEllipses[] traversed_ellipses~%~%================================================================================~%MSG: estirabot_msgs/DirtyArea~%int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%================================================================================~%MSG: estirabot_msgs/PointsDistanceMsg~%uint32 origIdx~%uint32 dstIdx~%float64 distance~%~%================================================================================~%MSG: estirabot_msgs/TraversedEllipses~%int32 idx1~%int32 idx2~%int32[] traversedIdxs~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RepresentationToString-request)))
  "Returns full string definition for message of type 'RepresentationToString-request"
  (cl:format cl:nil "estirabot_msgs/DirtyArea[] dirty_areas~%estirabot_msgs/PointsDistanceMsg[] distances~%estirabot_msgs/TraversedEllipses[] traversed_ellipses~%~%================================================================================~%MSG: estirabot_msgs/DirtyArea~%int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%================================================================================~%MSG: estirabot_msgs/PointsDistanceMsg~%uint32 origIdx~%uint32 dstIdx~%float64 distance~%~%================================================================================~%MSG: estirabot_msgs/TraversedEllipses~%int32 idx1~%int32 idx2~%int32[] traversedIdxs~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RepresentationToString-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'dirty_areas) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'distances) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'traversed_ellipses) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RepresentationToString-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RepresentationToString-request
    (cl:cons ':dirty_areas (dirty_areas msg))
    (cl:cons ':distances (distances msg))
    (cl:cons ':traversed_ellipses (traversed_ellipses msg))
))
;//! \htmlinclude RepresentationToString-response.msg.html

(cl:defclass <RepresentationToString-response> (roslisp-msg-protocol:ros-message)
  ((state_string
    :reader state_string
    :initarg :state_string
    :type cl:string
    :initform ""))
)

(cl:defclass RepresentationToString-response (<RepresentationToString-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RepresentationToString-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RepresentationToString-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<RepresentationToString-response> is deprecated: use estirabot_msgs-srv:RepresentationToString-response instead.")))

(cl:ensure-generic-function 'state_string-val :lambda-list '(m))
(cl:defmethod state_string-val ((m <RepresentationToString-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:state_string-val is deprecated.  Use estirabot_msgs-srv:state_string instead.")
  (state_string m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RepresentationToString-response>) ostream)
  "Serializes a message object of type '<RepresentationToString-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_string))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_string))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RepresentationToString-response>) istream)
  "Deserializes a message object of type '<RepresentationToString-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_string) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_string) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RepresentationToString-response>)))
  "Returns string type for a service object of type '<RepresentationToString-response>"
  "estirabot_msgs/RepresentationToStringResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RepresentationToString-response)))
  "Returns string type for a service object of type 'RepresentationToString-response"
  "estirabot_msgs/RepresentationToStringResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RepresentationToString-response>)))
  "Returns md5sum for a message object of type '<RepresentationToString-response>"
  "a1b22891042192e0316f71d2c67c0d87")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RepresentationToString-response)))
  "Returns md5sum for a message object of type 'RepresentationToString-response"
  "a1b22891042192e0316f71d2c67c0d87")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RepresentationToString-response>)))
  "Returns full string definition for message of type '<RepresentationToString-response>"
  (cl:format cl:nil "string state_string~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RepresentationToString-response)))
  "Returns full string definition for message of type 'RepresentationToString-response"
  (cl:format cl:nil "string state_string~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RepresentationToString-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'state_string))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RepresentationToString-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RepresentationToString-response
    (cl:cons ':state_string (state_string msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RepresentationToString)))
  'RepresentationToString-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RepresentationToString)))
  'RepresentationToString-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RepresentationToString)))
  "Returns string type for a service object of type '<RepresentationToString>"
  "estirabot_msgs/RepresentationToString")
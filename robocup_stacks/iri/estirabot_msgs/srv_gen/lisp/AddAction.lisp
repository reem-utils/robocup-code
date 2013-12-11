; Auto-generated. Do not edit!


(cl:in-package estirabot_msgs-srv)


;//! \htmlinclude AddAction-request.msg.html

(cl:defclass <AddAction-request> (roslisp-msg-protocol:ros-message)
  ((action
    :reader action
    :initarg :action
    :type cl:string
    :initform "")
   (dirty_areas
    :reader dirty_areas
    :initarg :dirty_areas
    :type (cl:vector estirabot_msgs-msg:DirtyArea)
   :initform (cl:make-array 0 :element-type 'estirabot_msgs-msg:DirtyArea :initial-element (cl:make-instance 'estirabot_msgs-msg:DirtyArea)))
   (target_dirty_areas
    :reader target_dirty_areas
    :initarg :target_dirty_areas
    :type estirabot_msgs-msg:ArrayIndexes
    :initform (cl:make-instance 'estirabot_msgs-msg:ArrayIndexes))
   (distances
    :reader distances
    :initarg :distances
    :type (cl:vector estirabot_msgs-msg:PointsDistanceMsg)
   :initform (cl:make-array 0 :element-type 'estirabot_msgs-msg:PointsDistanceMsg :initial-element (cl:make-instance 'estirabot_msgs-msg:PointsDistanceMsg)))
   (state_string
    :reader state_string
    :initarg :state_string
    :type cl:string
    :initform "")
   (action_movements_successful
    :reader action_movements_successful
    :initarg :action_movements_successful
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass AddAction-request (<AddAction-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddAction-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddAction-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<AddAction-request> is deprecated: use estirabot_msgs-srv:AddAction-request instead.")))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <AddAction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:action-val is deprecated.  Use estirabot_msgs-srv:action instead.")
  (action m))

(cl:ensure-generic-function 'dirty_areas-val :lambda-list '(m))
(cl:defmethod dirty_areas-val ((m <AddAction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:dirty_areas-val is deprecated.  Use estirabot_msgs-srv:dirty_areas instead.")
  (dirty_areas m))

(cl:ensure-generic-function 'target_dirty_areas-val :lambda-list '(m))
(cl:defmethod target_dirty_areas-val ((m <AddAction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:target_dirty_areas-val is deprecated.  Use estirabot_msgs-srv:target_dirty_areas instead.")
  (target_dirty_areas m))

(cl:ensure-generic-function 'distances-val :lambda-list '(m))
(cl:defmethod distances-val ((m <AddAction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:distances-val is deprecated.  Use estirabot_msgs-srv:distances instead.")
  (distances m))

(cl:ensure-generic-function 'state_string-val :lambda-list '(m))
(cl:defmethod state_string-val ((m <AddAction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:state_string-val is deprecated.  Use estirabot_msgs-srv:state_string instead.")
  (state_string m))

(cl:ensure-generic-function 'action_movements_successful-val :lambda-list '(m))
(cl:defmethod action_movements_successful-val ((m <AddAction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:action_movements_successful-val is deprecated.  Use estirabot_msgs-srv:action_movements_successful instead.")
  (action_movements_successful m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddAction-request>) ostream)
  "Serializes a message object of type '<AddAction-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'action))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'dirty_areas))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'dirty_areas))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'target_dirty_areas) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'distances))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'distances))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'state_string))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'state_string))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'action_movements_successful) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddAction-request>) istream)
  "Deserializes a message object of type '<AddAction-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'action) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'action) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
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
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'target_dirty_areas) istream)
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
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'state_string) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'state_string) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:setf (cl:slot-value msg 'action_movements_successful) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddAction-request>)))
  "Returns string type for a service object of type '<AddAction-request>"
  "estirabot_msgs/AddActionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddAction-request)))
  "Returns string type for a service object of type 'AddAction-request"
  "estirabot_msgs/AddActionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddAction-request>)))
  "Returns md5sum for a message object of type '<AddAction-request>"
  "3ef83f1df6473e149ff74e23eea70811")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddAction-request)))
  "Returns md5sum for a message object of type 'AddAction-request"
  "3ef83f1df6473e149ff74e23eea70811")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddAction-request>)))
  "Returns full string definition for message of type '<AddAction-request>"
  (cl:format cl:nil "string action~%estirabot_msgs/DirtyArea[] dirty_areas~%estirabot_msgs/ArrayIndexes target_dirty_areas~%estirabot_msgs/PointsDistanceMsg[] distances~%string state_string~%bool action_movements_successful~%~%================================================================================~%MSG: estirabot_msgs/DirtyArea~%int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%================================================================================~%MSG: estirabot_msgs/ArrayIndexes~%uint32[] indexes~%================================================================================~%MSG: estirabot_msgs/PointsDistanceMsg~%uint32 origIdx~%uint32 dstIdx~%float64 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddAction-request)))
  "Returns full string definition for message of type 'AddAction-request"
  (cl:format cl:nil "string action~%estirabot_msgs/DirtyArea[] dirty_areas~%estirabot_msgs/ArrayIndexes target_dirty_areas~%estirabot_msgs/PointsDistanceMsg[] distances~%string state_string~%bool action_movements_successful~%~%================================================================================~%MSG: estirabot_msgs/DirtyArea~%int32 id~%estirabot_msgs/Ellipse ellipse~%bool sparse~%uint8 area~%uint8 shape~%~%================================================================================~%MSG: estirabot_msgs/Ellipse~%iri_perception_msgs/ImagePoint center~%iri_perception_msgs/ImageSize size~%float64 angle~%~%================================================================================~%MSG: iri_perception_msgs/ImagePoint~%uint32 x~%uint32 y~%================================================================================~%MSG: iri_perception_msgs/ImageSize~%uint32 width~%uint32 height~%================================================================================~%MSG: estirabot_msgs/ArrayIndexes~%uint32[] indexes~%================================================================================~%MSG: estirabot_msgs/PointsDistanceMsg~%uint32 origIdx~%uint32 dstIdx~%float64 distance~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddAction-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'action))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'dirty_areas) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'target_dirty_areas))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'distances) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:length (cl:slot-value msg 'state_string))
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddAction-request>))
  "Converts a ROS message object to a list"
  (cl:list 'AddAction-request
    (cl:cons ':action (action msg))
    (cl:cons ':dirty_areas (dirty_areas msg))
    (cl:cons ':target_dirty_areas (target_dirty_areas msg))
    (cl:cons ':distances (distances msg))
    (cl:cons ':state_string (state_string msg))
    (cl:cons ':action_movements_successful (action_movements_successful msg))
))
;//! \htmlinclude AddAction-response.msg.html

(cl:defclass <AddAction-response> (roslisp-msg-protocol:ros-message)
  ((needs_learning
    :reader needs_learning
    :initarg :needs_learning
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass AddAction-response (<AddAction-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <AddAction-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'AddAction-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name estirabot_msgs-srv:<AddAction-response> is deprecated: use estirabot_msgs-srv:AddAction-response instead.")))

(cl:ensure-generic-function 'needs_learning-val :lambda-list '(m))
(cl:defmethod needs_learning-val ((m <AddAction-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader estirabot_msgs-srv:needs_learning-val is deprecated.  Use estirabot_msgs-srv:needs_learning instead.")
  (needs_learning m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <AddAction-response>) ostream)
  "Serializes a message object of type '<AddAction-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'needs_learning) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <AddAction-response>) istream)
  "Deserializes a message object of type '<AddAction-response>"
    (cl:setf (cl:slot-value msg 'needs_learning) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<AddAction-response>)))
  "Returns string type for a service object of type '<AddAction-response>"
  "estirabot_msgs/AddActionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddAction-response)))
  "Returns string type for a service object of type 'AddAction-response"
  "estirabot_msgs/AddActionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<AddAction-response>)))
  "Returns md5sum for a message object of type '<AddAction-response>"
  "3ef83f1df6473e149ff74e23eea70811")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'AddAction-response)))
  "Returns md5sum for a message object of type 'AddAction-response"
  "3ef83f1df6473e149ff74e23eea70811")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<AddAction-response>)))
  "Returns full string definition for message of type '<AddAction-response>"
  (cl:format cl:nil "bool needs_learning~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'AddAction-response)))
  "Returns full string definition for message of type 'AddAction-response"
  (cl:format cl:nil "bool needs_learning~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <AddAction-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <AddAction-response>))
  "Converts a ROS message object to a list"
  (cl:list 'AddAction-response
    (cl:cons ':needs_learning (needs_learning msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'AddAction)))
  'AddAction-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'AddAction)))
  'AddAction-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'AddAction)))
  "Returns string type for a service object of type '<AddAction>"
  "estirabot_msgs/AddAction")
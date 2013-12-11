; Auto-generated. Do not edit!


(cl:in-package next_location_provider-srv)


;//! \htmlinclude NextProbableLocation-request.msg.html

(cl:defclass <NextProbableLocation-request> (roslisp-msg-protocol:ros-message)
  ((room
    :reader room
    :initarg :room
    :type cl:string
    :initform ""))
)

(cl:defclass NextProbableLocation-request (<NextProbableLocation-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NextProbableLocation-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NextProbableLocation-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name next_location_provider-srv:<NextProbableLocation-request> is deprecated: use next_location_provider-srv:NextProbableLocation-request instead.")))

(cl:ensure-generic-function 'room-val :lambda-list '(m))
(cl:defmethod room-val ((m <NextProbableLocation-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader next_location_provider-srv:room-val is deprecated.  Use next_location_provider-srv:room instead.")
  (room m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NextProbableLocation-request>) ostream)
  "Serializes a message object of type '<NextProbableLocation-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'room))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'room))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NextProbableLocation-request>) istream)
  "Deserializes a message object of type '<NextProbableLocation-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'room) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'room) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NextProbableLocation-request>)))
  "Returns string type for a service object of type '<NextProbableLocation-request>"
  "next_location_provider/NextProbableLocationRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NextProbableLocation-request)))
  "Returns string type for a service object of type 'NextProbableLocation-request"
  "next_location_provider/NextProbableLocationRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NextProbableLocation-request>)))
  "Returns md5sum for a message object of type '<NextProbableLocation-request>"
  "4b161fd3eae8ce85c6fdfdca1a4229bc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NextProbableLocation-request)))
  "Returns md5sum for a message object of type 'NextProbableLocation-request"
  "4b161fd3eae8ce85c6fdfdca1a4229bc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NextProbableLocation-request>)))
  "Returns full string definition for message of type '<NextProbableLocation-request>"
  (cl:format cl:nil "string room~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NextProbableLocation-request)))
  "Returns full string definition for message of type 'NextProbableLocation-request"
  (cl:format cl:nil "string room~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NextProbableLocation-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'room))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NextProbableLocation-request>))
  "Converts a ROS message object to a list"
  (cl:list 'NextProbableLocation-request
    (cl:cons ':room (room msg))
))
;//! \htmlinclude NextProbableLocation-response.msg.html

(cl:defclass <NextProbableLocation-response> (roslisp-msg-protocol:ros-message)
  ((location
    :reader location
    :initarg :location
    :type cl:string
    :initform "")
   (loc_position
    :reader loc_position
    :initarg :loc_position
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass NextProbableLocation-response (<NextProbableLocation-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NextProbableLocation-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NextProbableLocation-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name next_location_provider-srv:<NextProbableLocation-response> is deprecated: use next_location_provider-srv:NextProbableLocation-response instead.")))

(cl:ensure-generic-function 'location-val :lambda-list '(m))
(cl:defmethod location-val ((m <NextProbableLocation-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader next_location_provider-srv:location-val is deprecated.  Use next_location_provider-srv:location instead.")
  (location m))

(cl:ensure-generic-function 'loc_position-val :lambda-list '(m))
(cl:defmethod loc_position-val ((m <NextProbableLocation-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader next_location_provider-srv:loc_position-val is deprecated.  Use next_location_provider-srv:loc_position instead.")
  (loc_position m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NextProbableLocation-response>) ostream)
  "Serializes a message object of type '<NextProbableLocation-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'location))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'location))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'loc_position) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NextProbableLocation-response>) istream)
  "Deserializes a message object of type '<NextProbableLocation-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'location) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'location) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'loc_position) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NextProbableLocation-response>)))
  "Returns string type for a service object of type '<NextProbableLocation-response>"
  "next_location_provider/NextProbableLocationResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NextProbableLocation-response)))
  "Returns string type for a service object of type 'NextProbableLocation-response"
  "next_location_provider/NextProbableLocationResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NextProbableLocation-response>)))
  "Returns md5sum for a message object of type '<NextProbableLocation-response>"
  "4b161fd3eae8ce85c6fdfdca1a4229bc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NextProbableLocation-response)))
  "Returns md5sum for a message object of type 'NextProbableLocation-response"
  "4b161fd3eae8ce85c6fdfdca1a4229bc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NextProbableLocation-response>)))
  "Returns full string definition for message of type '<NextProbableLocation-response>"
  (cl:format cl:nil "string location~%geometry_msgs/Pose loc_position~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NextProbableLocation-response)))
  "Returns full string definition for message of type 'NextProbableLocation-response"
  (cl:format cl:nil "string location~%geometry_msgs/Pose loc_position~%~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of postion and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NextProbableLocation-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'location))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'loc_position))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NextProbableLocation-response>))
  "Converts a ROS message object to a list"
  (cl:list 'NextProbableLocation-response
    (cl:cons ':location (location msg))
    (cl:cons ':loc_position (loc_position msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'NextProbableLocation)))
  'NextProbableLocation-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'NextProbableLocation)))
  'NextProbableLocation-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NextProbableLocation)))
  "Returns string type for a service object of type '<NextProbableLocation>"
  "next_location_provider/NextProbableLocation")
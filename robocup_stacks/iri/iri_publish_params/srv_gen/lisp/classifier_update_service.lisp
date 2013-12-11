; Auto-generated. Do not edit!


(cl:in-package iri_publish_params-srv)


;//! \htmlinclude classifier_update_service-request.msg.html

(cl:defclass <classifier_update_service-request> (roslisp-msg-protocol:ros-message)
  ((params
    :reader params
    :initarg :params
    :type iri_publish_params-msg:classifier_update
    :initform (cl:make-instance 'iri_publish_params-msg:classifier_update)))
)

(cl:defclass classifier_update_service-request (<classifier_update_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <classifier_update_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'classifier_update_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_publish_params-srv:<classifier_update_service-request> is deprecated: use iri_publish_params-srv:classifier_update_service-request instead.")))

(cl:ensure-generic-function 'params-val :lambda-list '(m))
(cl:defmethod params-val ((m <classifier_update_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_publish_params-srv:params-val is deprecated.  Use iri_publish_params-srv:params instead.")
  (params m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <classifier_update_service-request>) ostream)
  "Serializes a message object of type '<classifier_update_service-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'params) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <classifier_update_service-request>) istream)
  "Deserializes a message object of type '<classifier_update_service-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'params) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<classifier_update_service-request>)))
  "Returns string type for a service object of type '<classifier_update_service-request>"
  "iri_publish_params/classifier_update_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'classifier_update_service-request)))
  "Returns string type for a service object of type 'classifier_update_service-request"
  "iri_publish_params/classifier_update_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<classifier_update_service-request>)))
  "Returns md5sum for a message object of type '<classifier_update_service-request>"
  "b7540e46e50484b76ac974e85c69cb86")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'classifier_update_service-request)))
  "Returns md5sum for a message object of type 'classifier_update_service-request"
  "b7540e46e50484b76ac974e85c69cb86")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<classifier_update_service-request>)))
  "Returns full string definition for message of type '<classifier_update_service-request>"
  (cl:format cl:nil "classifier_update params~%~%================================================================================~%MSG: iri_publish_params/classifier_update~%classifier_params[] update_params~%int32 selected_centroid~%int32 filter_method~%~%================================================================================~%MSG: iri_publish_params/classifier_params~%float32[] params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'classifier_update_service-request)))
  "Returns full string definition for message of type 'classifier_update_service-request"
  (cl:format cl:nil "classifier_update params~%~%================================================================================~%MSG: iri_publish_params/classifier_update~%classifier_params[] update_params~%int32 selected_centroid~%int32 filter_method~%~%================================================================================~%MSG: iri_publish_params/classifier_params~%float32[] params~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <classifier_update_service-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'params))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <classifier_update_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'classifier_update_service-request
    (cl:cons ':params (params msg))
))
;//! \htmlinclude classifier_update_service-response.msg.html

(cl:defclass <classifier_update_service-response> (roslisp-msg-protocol:ros-message)
  ((result
    :reader result
    :initarg :result
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass classifier_update_service-response (<classifier_update_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <classifier_update_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'classifier_update_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name iri_publish_params-srv:<classifier_update_service-response> is deprecated: use iri_publish_params-srv:classifier_update_service-response instead.")))

(cl:ensure-generic-function 'result-val :lambda-list '(m))
(cl:defmethod result-val ((m <classifier_update_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader iri_publish_params-srv:result-val is deprecated.  Use iri_publish_params-srv:result instead.")
  (result m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <classifier_update_service-response>) ostream)
  "Serializes a message object of type '<classifier_update_service-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'result) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <classifier_update_service-response>) istream)
  "Deserializes a message object of type '<classifier_update_service-response>"
    (cl:setf (cl:slot-value msg 'result) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<classifier_update_service-response>)))
  "Returns string type for a service object of type '<classifier_update_service-response>"
  "iri_publish_params/classifier_update_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'classifier_update_service-response)))
  "Returns string type for a service object of type 'classifier_update_service-response"
  "iri_publish_params/classifier_update_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<classifier_update_service-response>)))
  "Returns md5sum for a message object of type '<classifier_update_service-response>"
  "b7540e46e50484b76ac974e85c69cb86")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'classifier_update_service-response)))
  "Returns md5sum for a message object of type 'classifier_update_service-response"
  "b7540e46e50484b76ac974e85c69cb86")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<classifier_update_service-response>)))
  "Returns full string definition for message of type '<classifier_update_service-response>"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'classifier_update_service-response)))
  "Returns full string definition for message of type 'classifier_update_service-response"
  (cl:format cl:nil "bool result~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <classifier_update_service-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <classifier_update_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'classifier_update_service-response
    (cl:cons ':result (result msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'classifier_update_service)))
  'classifier_update_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'classifier_update_service)))
  'classifier_update_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'classifier_update_service)))
  "Returns string type for a service object of type '<classifier_update_service>"
  "iri_publish_params/classifier_update_service")
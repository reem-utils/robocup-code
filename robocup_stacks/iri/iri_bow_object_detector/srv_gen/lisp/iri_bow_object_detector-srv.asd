
(cl:in-package :asdf)

(defsystem "iri_bow_object_detector-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :iri_bow_object_detector-msg
               :iri_perception_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "GeoVwDetection" :depends-on ("_package_GeoVwDetection"))
    (:file "_package_GeoVwDetection" :depends-on ("_package"))
    (:file "RefineGraspPoint" :depends-on ("_package_RefineGraspPoint"))
    (:file "_package_RefineGraspPoint" :depends-on ("_package"))
  ))
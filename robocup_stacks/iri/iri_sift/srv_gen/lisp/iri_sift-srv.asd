
(cl:in-package :asdf)

(defsystem "iri_sift-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :iri_perception_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "DescriptorsFromImage" :depends-on ("_package_DescriptorsFromImage"))
    (:file "_package_DescriptorsFromImage" :depends-on ("_package"))
    (:file "GeoVwSetSrv" :depends-on ("_package_GeoVwSetSrv"))
    (:file "_package_GeoVwSetSrv" :depends-on ("_package"))
  ))
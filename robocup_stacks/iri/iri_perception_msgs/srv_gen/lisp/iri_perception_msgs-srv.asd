
(cl:in-package :asdf)

(defsystem "iri_perception_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :iri_perception_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
               :visualization_msgs-msg
)
  :components ((:file "_package")
    (:file "DescriptorsToVws" :depends-on ("_package_DescriptorsToVws"))
    (:file "_package_DescriptorsToVws" :depends-on ("_package"))
    (:file "SetImage" :depends-on ("_package_SetImage"))
    (:file "_package_SetImage" :depends-on ("_package"))
    (:file "StorePointCloud2" :depends-on ("_package_StorePointCloud2"))
    (:file "_package_StorePointCloud2" :depends-on ("_package"))
    (:file "PclToImg" :depends-on ("_package_PclToImg"))
    (:file "_package_PclToImg" :depends-on ("_package"))
    (:file "peopleTrackingService" :depends-on ("_package_peopleTrackingService"))
    (:file "_package_peopleTrackingService" :depends-on ("_package"))
    (:file "ProcessPointCloud2" :depends-on ("_package_ProcessPointCloud2"))
    (:file "_package_ProcessPointCloud2" :depends-on ("_package"))
    (:file "PclToDescriptorSet" :depends-on ("_package_PclToDescriptorSet"))
    (:file "_package_PclToDescriptorSet" :depends-on ("_package"))
    (:file "PclToMarker" :depends-on ("_package_PclToMarker"))
    (:file "_package_PclToMarker" :depends-on ("_package"))
    (:file "GetPointCloud2" :depends-on ("_package_GetPointCloud2"))
    (:file "_package_GetPointCloud2" :depends-on ("_package"))
  ))
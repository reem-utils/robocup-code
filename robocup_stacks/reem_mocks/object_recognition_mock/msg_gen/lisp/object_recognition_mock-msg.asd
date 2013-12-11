
(cl:in-package :asdf)

(defsystem "object_recognition_mock-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "DetectionResult" :depends-on ("_package_DetectionResult"))
    (:file "_package_DetectionResult" :depends-on ("_package"))
    (:file "DetectedObject" :depends-on ("_package_DetectedObject"))
    (:file "_package_DetectedObject" :depends-on ("_package"))
    (:file "Pixel" :depends-on ("_package_Pixel"))
    (:file "_package_Pixel" :depends-on ("_package"))
  ))
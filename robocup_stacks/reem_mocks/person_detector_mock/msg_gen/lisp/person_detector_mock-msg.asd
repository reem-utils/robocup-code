
(cl:in-package :asdf)

(defsystem "person_detector_mock-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "peopleTrackingArray" :depends-on ("_package_peopleTrackingArray"))
    (:file "_package_peopleTrackingArray" :depends-on ("_package"))
    (:file "peopleTracking" :depends-on ("_package_peopleTracking"))
    (:file "_package_peopleTracking" :depends-on ("_package"))
  ))
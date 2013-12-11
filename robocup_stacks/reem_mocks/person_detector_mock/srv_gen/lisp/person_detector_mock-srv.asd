
(cl:in-package :asdf)

(defsystem "person_detector_mock-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :person_detector_mock-msg
)
  :components ((:file "_package")
    (:file "DetectPeople" :depends-on ("_package_DetectPeople"))
    (:file "_package_DetectPeople" :depends-on ("_package"))
  ))
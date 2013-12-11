
(cl:in-package :asdf)

(defsystem "next_location_provider-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "NextProbableLocation" :depends-on ("_package_NextProbableLocation"))
    (:file "_package_NextProbableLocation" :depends-on ("_package"))
  ))
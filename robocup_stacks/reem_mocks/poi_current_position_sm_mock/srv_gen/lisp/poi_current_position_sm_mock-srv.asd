
(cl:in-package :asdf)

(defsystem "poi_current_position_sm_mock-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "lookupTransform" :depends-on ("_package_lookupTransform"))
    (:file "_package_lookupTransform" :depends-on ("_package"))
  ))
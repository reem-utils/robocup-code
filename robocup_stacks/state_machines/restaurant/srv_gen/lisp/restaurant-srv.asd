
(cl:in-package :asdf)

(defsystem "restaurant-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "lookupTransform" :depends-on ("_package_lookupTransform"))
    (:file "_package_lookupTransform" :depends-on ("_package"))
  ))
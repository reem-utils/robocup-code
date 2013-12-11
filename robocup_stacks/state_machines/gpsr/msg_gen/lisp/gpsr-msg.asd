
(cl:in-package :asdf)

(defsystem "gpsr-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "order" :depends-on ("_package_order"))
    (:file "_package_order" :depends-on ("_package"))
    (:file "action" :depends-on ("_package_action"))
    (:file "_package_action" :depends-on ("_package"))
    (:file "order_list" :depends-on ("_package_order_list"))
    (:file "_package_order_list" :depends-on ("_package"))
    (:file "action_list" :depends-on ("_package_action_list"))
    (:file "_package_action_list" :depends-on ("_package"))
  ))
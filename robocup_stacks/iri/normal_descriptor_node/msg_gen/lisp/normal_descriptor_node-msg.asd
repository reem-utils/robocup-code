
(cl:in-package :asdf)

(defsystem "normal_descriptor_node-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ndesc_pc" :depends-on ("_package_ndesc_pc"))
    (:file "_package_ndesc_pc" :depends-on ("_package"))
    (:file "ndesc" :depends-on ("_package_ndesc"))
    (:file "_package_ndesc" :depends-on ("_package"))
  ))
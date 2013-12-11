
(cl:in-package :asdf)

(defsystem "normal_descriptor_node-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :normal_descriptor_node-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "ndesc_pc_service" :depends-on ("_package_ndesc_pc_service"))
    (:file "_package_ndesc_pc_service" :depends-on ("_package"))
  ))
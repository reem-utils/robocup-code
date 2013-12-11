
(cl:in-package :asdf)

(defsystem "iri_publish_params-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :iri_publish_params-msg
)
  :components ((:file "_package")
    (:file "classifier_update_service" :depends-on ("_package_classifier_update_service"))
    (:file "_package_classifier_update_service" :depends-on ("_package"))
  ))

(cl:in-package :asdf)

(defsystem "iri_publish_params-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "classifier_update" :depends-on ("_package_classifier_update"))
    (:file "_package_classifier_update" :depends-on ("_package"))
    (:file "classifier_params" :depends-on ("_package_classifier_params"))
    (:file "_package_classifier_params" :depends-on ("_package"))
  ))
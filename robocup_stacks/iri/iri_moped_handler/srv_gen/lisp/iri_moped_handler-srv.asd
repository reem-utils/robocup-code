
(cl:in-package :asdf)

(defsystem "iri_moped_handler-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "enable" :depends-on ("_package_enable"))
    (:file "_package_enable" :depends-on ("_package"))
  ))
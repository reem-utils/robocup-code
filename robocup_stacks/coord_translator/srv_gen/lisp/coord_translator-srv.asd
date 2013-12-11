
(cl:in-package :asdf)

(defsystem "coord_translator-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "ObjectTranslatorDataBase" :depends-on ("_package_ObjectTranslatorDataBase"))
    (:file "_package_ObjectTranslatorDataBase" :depends-on ("_package"))
    (:file "LocationTranslator" :depends-on ("_package_LocationTranslator"))
    (:file "_package_LocationTranslator" :depends-on ("_package"))
    (:file "ObjectTranslator" :depends-on ("_package_ObjectTranslator"))
    (:file "_package_ObjectTranslator" :depends-on ("_package"))
  ))
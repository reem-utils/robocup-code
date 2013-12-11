
(cl:in-package :asdf)

(defsystem "gpsrSoar-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "gpsrActionActionFeedback" :depends-on ("_package_gpsrActionActionFeedback"))
    (:file "_package_gpsrActionActionFeedback" :depends-on ("_package"))
    (:file "gpsrActionActionResult" :depends-on ("_package_gpsrActionActionResult"))
    (:file "_package_gpsrActionActionResult" :depends-on ("_package"))
    (:file "gpsrActionResult" :depends-on ("_package_gpsrActionResult"))
    (:file "_package_gpsrActionResult" :depends-on ("_package"))
    (:file "order" :depends-on ("_package_order"))
    (:file "_package_order" :depends-on ("_package"))
    (:file "gpsrActionAction" :depends-on ("_package_gpsrActionAction"))
    (:file "_package_gpsrActionAction" :depends-on ("_package"))
    (:file "gpsrActionActionGoal" :depends-on ("_package_gpsrActionActionGoal"))
    (:file "_package_gpsrActionActionGoal" :depends-on ("_package"))
    (:file "gpsrActionGoal" :depends-on ("_package_gpsrActionGoal"))
    (:file "_package_gpsrActionGoal" :depends-on ("_package"))
    (:file "gpsrActionFeedback" :depends-on ("_package_gpsrActionFeedback"))
    (:file "_package_gpsrActionFeedback" :depends-on ("_package"))
  ))
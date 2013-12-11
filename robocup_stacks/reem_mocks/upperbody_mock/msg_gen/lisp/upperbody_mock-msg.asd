
(cl:in-package :asdf)

(defsystem "upperbody_mock-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "UpperBodyGoal" :depends-on ("_package_UpperBodyGoal"))
    (:file "_package_UpperBodyGoal" :depends-on ("_package"))
    (:file "UpperBodyResult" :depends-on ("_package_UpperBodyResult"))
    (:file "_package_UpperBodyResult" :depends-on ("_package"))
    (:file "UpperBodyActionResult" :depends-on ("_package_UpperBodyActionResult"))
    (:file "_package_UpperBodyActionResult" :depends-on ("_package"))
    (:file "UpperBodyActionFeedback" :depends-on ("_package_UpperBodyActionFeedback"))
    (:file "_package_UpperBodyActionFeedback" :depends-on ("_package"))
    (:file "UpperBodyActionGoal" :depends-on ("_package_UpperBodyActionGoal"))
    (:file "_package_UpperBodyActionGoal" :depends-on ("_package"))
    (:file "UpperBodyFeedback" :depends-on ("_package_UpperBodyFeedback"))
    (:file "_package_UpperBodyFeedback" :depends-on ("_package"))
    (:file "UpperBodyAction" :depends-on ("_package_UpperBodyAction"))
    (:file "_package_UpperBodyAction" :depends-on ("_package"))
  ))
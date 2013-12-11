
(cl:in-package :asdf)

(defsystem "iri_motion_detector-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "MotionDetectorActionResult" :depends-on ("_package_MotionDetectorActionResult"))
    (:file "_package_MotionDetectorActionResult" :depends-on ("_package"))
    (:file "MotionDetectorActionFeedback" :depends-on ("_package_MotionDetectorActionFeedback"))
    (:file "_package_MotionDetectorActionFeedback" :depends-on ("_package"))
    (:file "MotionDetectorActionActionResult" :depends-on ("_package_MotionDetectorActionActionResult"))
    (:file "_package_MotionDetectorActionActionResult" :depends-on ("_package"))
    (:file "MotionDetectorActionActionGoal" :depends-on ("_package_MotionDetectorActionActionGoal"))
    (:file "_package_MotionDetectorActionActionGoal" :depends-on ("_package"))
    (:file "MotionDetectorActionActionFeedback" :depends-on ("_package_MotionDetectorActionActionFeedback"))
    (:file "_package_MotionDetectorActionActionFeedback" :depends-on ("_package"))
    (:file "MotionDetectorActionGoal" :depends-on ("_package_MotionDetectorActionGoal"))
    (:file "_package_MotionDetectorActionGoal" :depends-on ("_package"))
    (:file "MotionDetectorActionAction" :depends-on ("_package_MotionDetectorActionAction"))
    (:file "_package_MotionDetectorActionAction" :depends-on ("_package"))
  ))
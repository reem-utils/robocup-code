
(cl:in-package :asdf)

(defsystem "iri_bow_object_detector-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :actionlib_msgs-msg
               :geometry_msgs-msg
               :iri_perception_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "WrinkledMap" :depends-on ("_package_WrinkledMap"))
    (:file "_package_WrinkledMap" :depends-on ("_package"))
    (:file "GetGraspingPointFeedback" :depends-on ("_package_GetGraspingPointFeedback"))
    (:file "_package_GetGraspingPointFeedback" :depends-on ("_package"))
    (:file "GetGraspingPointAction" :depends-on ("_package_GetGraspingPointAction"))
    (:file "_package_GetGraspingPointAction" :depends-on ("_package"))
    (:file "ObjectBox" :depends-on ("_package_ObjectBox"))
    (:file "_package_ObjectBox" :depends-on ("_package"))
    (:file "GetGraspingPointGoal" :depends-on ("_package_GetGraspingPointGoal"))
    (:file "_package_GetGraspingPointGoal" :depends-on ("_package"))
    (:file "GetGraspingPointResult" :depends-on ("_package_GetGraspingPointResult"))
    (:file "_package_GetGraspingPointResult" :depends-on ("_package"))
    (:file "GetGraspingPointActionResult" :depends-on ("_package_GetGraspingPointActionResult"))
    (:file "_package_GetGraspingPointActionResult" :depends-on ("_package"))
    (:file "GetGraspingPointActionGoal" :depends-on ("_package_GetGraspingPointActionGoal"))
    (:file "_package_GetGraspingPointActionGoal" :depends-on ("_package"))
    (:file "GetGraspingPointActionFeedback" :depends-on ("_package_GetGraspingPointActionFeedback"))
    (:file "_package_GetGraspingPointActionFeedback" :depends-on ("_package"))
  ))

(cl:in-package :asdf)

(defsystem "estirabot_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :iri_perception_msgs-msg
               :object_manipulation_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "belief_summary" :depends-on ("_package_belief_summary"))
    (:file "_package_belief_summary" :depends-on ("_package"))
    (:file "TraversedEllipses" :depends-on ("_package_TraversedEllipses"))
    (:file "_package_TraversedEllipses" :depends-on ("_package"))
    (:file "belief" :depends-on ("_package_belief"))
    (:file "_package_belief" :depends-on ("_package"))
    (:file "DirtyArea" :depends-on ("_package_DirtyArea"))
    (:file "_package_DirtyArea" :depends-on ("_package"))
    (:file "ArrayIndexes" :depends-on ("_package_ArrayIndexes"))
    (:file "_package_ArrayIndexes" :depends-on ("_package"))
    (:file "GraspVerification" :depends-on ("_package_GraspVerification"))
    (:file "_package_GraspVerification" :depends-on ("_package"))
    (:file "PointsDistanceMsg" :depends-on ("_package_PointsDistanceMsg"))
    (:file "_package_PointsDistanceMsg" :depends-on ("_package"))
    (:file "Ellipse" :depends-on ("_package_Ellipse"))
    (:file "_package_Ellipse" :depends-on ("_package"))
    (:file "GraspPointParameters" :depends-on ("_package_GraspPointParameters"))
    (:file "_package_GraspPointParameters" :depends-on ("_package"))
    (:file "PomdpGraspConfig" :depends-on ("_package_PomdpGraspConfig"))
    (:file "_package_PomdpGraspConfig" :depends-on ("_package"))
  ))
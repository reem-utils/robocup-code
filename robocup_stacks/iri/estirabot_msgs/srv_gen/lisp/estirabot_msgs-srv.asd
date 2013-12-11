
(cl:in-package :asdf)

(defsystem "estirabot_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :estirabot_msgs-msg
               :geometry_msgs-msg
               :sensor_msgs-msg
)
  :components ((:file "_package")
    (:file "obs2action" :depends-on ("_package_obs2action"))
    (:file "_package_obs2action" :depends-on ("_package"))
    (:file "StateRepresentationChanges" :depends-on ("_package_StateRepresentationChanges"))
    (:file "_package_StateRepresentationChanges" :depends-on ("_package"))
    (:file "ArmMovementsPosesSrv" :depends-on ("_package_ArmMovementsPosesSrv"))
    (:file "_package_ArmMovementsPosesSrv" :depends-on ("_package"))
    (:file "RepresentationToString" :depends-on ("_package_RepresentationToString"))
    (:file "_package_RepresentationToString" :depends-on ("_package"))
    (:file "AddAction" :depends-on ("_package_AddAction"))
    (:file "_package_AddAction" :depends-on ("_package"))
    (:file "TransformPose" :depends-on ("_package_TransformPose"))
    (:file "_package_TransformPose" :depends-on ("_package"))
    (:file "AddState" :depends-on ("_package_AddState"))
    (:file "_package_AddState" :depends-on ("_package"))
  ))
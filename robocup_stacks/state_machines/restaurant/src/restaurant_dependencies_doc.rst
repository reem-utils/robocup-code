THIS IS A RESTAURANT DEPENDENCIES DOCUMENT
==========================================

This is a list of the States and StateMachines, what actions or topic do they use.
Note that there are only the ones that dont repeat, because most of the repeat throughout
most of them.

#. from speech.sound_action import SpeakActionState
ACTIONS=['/sound']

#. from speech.listen_general_command import RecogCommand
	TOPICS = ['usersaid']
	from grammar_state import GrammarState
	SERVICES = ['asrservice']

#. from navigation.navigation_state import ChangeNavigationMode
	SERVICES = ['pal_navigation_sm']
	TOPICS = ['/pal_navigation_sm/state']

#. from navigation.learn_person import LearnPerson
	TOPICS = ['/iri_people_tracking_rai/peopleSet']
	ACTIONS = ['face_recognition']

#. from navigation.follow_and_stop import FollowAndStop
	from navigation.follow_operator import FollowOperator
	TOPICS = ["/move_by/move_base_simple/goal"]
	from speech.sm_hear_voice_commands_and_pois import SM_MemorisePois
	SERVICES = ['lookupTransform']

#. from navigation.listen_and_satisfy_delivery_order import ListenAndSatisfyDeliveryOrderSM
	from grasp.fetch_object import FetchObject
	SERVICES = ['object_translator', 'loc_translator']
	from grasp.deliver_object import DeliverObject
	ACTIONS = ['/head_traj_controller/head_scan_snapshot_action', 'move_right_arm_torso',
	           '/right_hand_controller/follow_joint_trajectory']
	SERVICES = ['/approachToGoal']
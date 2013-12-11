import rospy
from smach_ros import SimpleActionState, ServiceState

from geometry_msgs.msg import Pose
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib import GoalStatus

from pal_smach_utils.utils.global_common import succeeded
from pal_smach_utils.utils.pose_at_distance import pose_at_distance
from reem_final_approach.srv import FinalApproachPose, FinalApproachPoseRequest
from pal_smach_utils.utils.colors import colors as C

# Constants
MOVE_BASE_ACTION_NAME = '/move_base'
MOVE_BY_ACTION_NAME = "/move_by/move_base"
FRAME_BASE_LINK = "/base_link"
DISTANCE_TO_RETRY = 0.5  # This variable is used if MoveActionState aborts


class MoveActionState(SimpleActionState):
    """MoveActionState State.

    Use this State to move the robot.

    The input data you give has to be of type Pose

    """
    def __init__(self, frame_id="/base_link", move_base_action_name=MOVE_BASE_ACTION_NAME, pose=None, goal_cb=None,
            goal_key=None, **kwargs):
        """Constructor for MoveActionState

        @type frame_id: string
        @param frame_id: The fame_id of the pose object. By default is "/base_link"

        @type move_base_action_name: string
        @param move_base_action_name: The action name. By default is the action name defined on the MOVE_BASE_ACTION_NAME variable.

        @type pose: geometry_msgs.Pose
        @param pose: The pose where the robot should move to on frame_id link.

        @type goal_cb: callable
        @param goal_cb: The function that will be called to get the pose. You can set only one of 'pose, goal_cb and goal_key' variables.

        @type goal_key: input_key on userdata.
        @param goal_key: The key on userdata variable that contains the pose.

        """

        if (pose and goal_cb) or (pose and goal_key) or (goal_cb and goal_key):
            raise ValueError("You've set more than one of `pose', " \
                "`goal_cb' and `goal_key'!")
        if not goal_cb and not goal_key and not pose:
            raise ValueError("Neither `pose' nor `goal_cb' nor `goal_key' were set!")

        if goal_key:
            if not 'input_keys' in kwargs:
                kwargs['input_keys'] = []
            kwargs['input_keys'].append(goal_key)

        def generic_goal_cb(userdata, old_goal):
            """ Send a goal to the action """
            self.nav_goal = MoveBaseGoal()
            self.nav_goal.target_pose.header.stamp = rospy.Time.now()
            self.nav_goal.target_pose.header.frame_id = frame_id
            if pose:
                self.nav_goal.target_pose.pose = pose
                return self.nav_goal
            elif goal_key:
                self.nav_goal.target_pose.pose = getattr(userdata, goal_key)
                return self.nav_goal
            else:
                self.nav_goal.target_pose.pose = Pose()
                return goal_cb(userdata, self.nav_goal)

        def _result_cb(userdata, status, result):
            """ This function will analize the status of the response
            If the status is aborted, will call the action again with the same
            orientation, but with the distance -0,5. If the status now is succeeded,
            then call the move_by with x=0.5 in front.

            :type status: actionlib.GoalStatus
            :type result: MoveBaseResult
            """

            if status != GoalStatus.SUCCEEDED:
                rospy.loginfo(C.BACKGROUND_YELLOW  + "Retrying go to the target goal" + C.NATIVE_COLOR)
                new_pose = pose_at_distance(self.nav_goal.target_pose.pose, DISTANCE_TO_RETRY )
                self.nav_goal.target_pose.pose = new_pose
                self.nav_goal.target_pose.header.stamp = rospy.Time.now()

                move_action = SimpleActionState(move_base_action_name, MoveBaseAction, goal=self.nav_goal)

                result_status = move_action.execute(userdata)
                if result_status == succeeded:
                    new_goal = MoveBaseGoal()
                    new_goal.target_pose.header.frame_id = FRAME_BASE_LINK
                    new_goal.target_pose.pose.position.x = DISTANCE_TO_RETRY
                    new_goal.target_pose.header.stamp = rospy.Time.now()

                    move_action = SimpleActionState(MOVE_BY_ACTION_NAME , MoveBaseAction, goal=new_goal)
                    return move_action.execute(userdata)
#                    THE PART BELOW WAS 'REMOVED' BECAUSE FINAL_APPROACH IS NOT RUNNING BY DEFAULT.
#                    final_approach_goal = FinalApproachPoseRequest()
#                    final_approach_goal.pose.position.x = DISTANCE_TO_RETRY - 0.1 # -0.1 Just because final_approach don't check if is secure to move
#                    final_approach_goal.pose.orientation.w = 0.0
#                    rospy.loginfo("Calling /approachToGoal with message:\n" + str(final_approach_goal))
#                    final_approach = ServiceState('/approachToGoal', FinalApproachPose, request=final_approach_goal)
#                    return final_approach.execute(userdata)



        SimpleActionState.__init__(self,
            move_base_action_name, MoveBaseAction,
            goal_cb=generic_goal_cb, result_cb=_result_cb, **kwargs)

# vim: expandtab ts=4 sw=4

#! /usr/bin/env python
import roslib
roslib.load_manifest('pal_smach_utils')
import smach

from pal_smach_utils.utils.global_common import succeeded, aborted, transform_pose
from geometry_msgs.msg import Pose
from pal_smach_utils.object_finding_algorithms.tsp import TSP


class TSPState(smach.State):

    '''
    Smach node to solve the TSP problem.
    The HC parameter in the constructor specifies if it'll be solved with a Hill Climbing (True)
    or with a Simulated Annealing(False)
    The add_start_pose parameter in the constructor specifies whether the actual position of the robot should be
    adedd as the start position of the route or not. If True, the resulting route doesn't contain the initial as a route.

    Userdata keys:
        - in_nodes is expected to be a list of pairs representing the points to visit.
        - out_route is a list of pairs in order of visiting, optimizing the distance of the total route.
    '''

    def __init__(self, HC=False, add_start_pose=True, indices=False):
        smach.State.__init__(self, outcomes=[succeeded, aborted], input_keys=['in_nodes'],
                             output_keys=['out_route'])
        self.HC = HC
        self.start_pose = add_start_pose
        self.indices = indices

    def execute(self, userdata):
        nodes = userdata.in_nodes
        print 'Calculating the TSP route with %d nodes' % len(nodes)

        if len(nodes) < 2:  # There's no point in calculating it
            if self.indices:
                userdata.out_route = range(len(nodes))
            else:
                userdata.out_route = nodes  # The same result
            return succeeded

        if self.start_pose:
            robot_pose = Pose()
            robot_pose.position.x = 0
            robot_pose.position.y = 0
            robot_pose.position.z = 0
            # Get robot's pose in /map coordinates
            robot_pose = transform_pose(robot_pose, '/base_link', '/map', timeout=3)
            initial = (robot_pose.position.x, robot_pose.position.y)
            nodes = [initial] + nodes

        tsp = TSP(nodes)
        in_qual = tsp._best_qual
        if self.HC:
            route = userdata.out_route = tsp.hill_climbing(self.indices)
        else:
            route = tsp.simulated_annealing(self.indices)

        if self.start_pose:
            route = route[1:]
            if self.indices:
                route = map(lambda x: x-1, route)

        userdata.out_route = route

        print "\n\nTSP's route", route, len(route)  # FIXME
        print 'Initial: %f, End: %f, Difference: %f' % (in_qual, tsp._best_qual, in_qual-tsp._best_qual), '\n\n'  # FIXME

        return succeeded

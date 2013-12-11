import rospy
import pal_smach_utils.object_finding_algorithms.ofb_utils as ofb_utils
from nav_msgs.srv import GetPlan
from rospy import ROSException
import math
import random
import numpy.random
#random.seed(54321)
#numpy.random.seed(54321)


class TSP(object):

    N_RHC_TRIES = 50    # Number of tries of the randomized hill climbing
    INITIAL_TEMP = 20   # 20 Starting temp for the simulated annealing
    N_ITER_SA = 10      # 10 Number of iterations for the simulated annealing
    ALPHA_SA = 0.99     # Decreasing factor for the temp of the simulated annealing. Must be < 1.0
    TEMP_TRESH = 0.001  # Value at which the SA temperature is assumed to be 0

    '''
    Class that tries to solve a TSP with a local search approach.
    It recieves a list of nodes (x, y) in the nodes parameter.
    with_plan specifies if the navigation planner is going to be used to calculate the distance or not.
    '''

    def __init__(self, nodes, with_plan=True):
        self._nodes = nodes  # Expected to be a list of pair tuples or something similar
        self._with_plan = with_plan
        self._n = len(nodes)
        self._route = range(self._n)  # Route (list that contains the indices of the nodes ordered in the order of the visiting)
        self._min = [(0, -1)]
        self._create_distance_matrix()
        self._best_qual = self.quality(self._route)

    def _create_distance_matrix(self):
        n = self._n
        make_plan = None
        if self._with_plan:
            try:
                rospy.wait_for_service('/move_base/make_plan', 0.1)
                make_plan = rospy.ServiceProxy('/move_base/make_plan', GetPlan)
            except ROSException:
                pass  # We already have make_plan set to None

        # i is the row, j the column
        #self._dist_mat = [[(self._distance(i, j, make_plan) if i != j else -1) for j in range(n)] for i in range(n)]
        self._dist_mat = [[ofb_utils.distance(self._nodes[i], self._nodes[j], make_plan) for j in range(n) if j < i] for i in range(n)]

    def _print_mat(self):
        for i in range(len(self._dist_mat)):
            print self._dist_mat[i]

    def successors(self, route):
        # To use with the hill climbing. It could also be used with the simulated annealing
        s = random.randrange(1, self._n)  # Position to swap
        new_routes = []
        for i in xrange(1, self._n):
            if i != s:
                r = route[:]
                r[s] = route[i]
                r[i] = route[s]
                new_routes.append(r)
        return new_routes

    def random_swap(self, route):
        # To use with the simulated annealing
        samp = random.sample(xrange(1, self._n), 2)  # The first node is the initial pose and the route must begin there
        swapped = route[:]
        swapped[samp[0]] = route[samp[1]]
        swapped[samp[1]] = route[samp[0]]
        return swapped

    def quality(self, route):
        total_dist = 0
        for i in range(1, self._n):
            ri = route[i]
            rj = route[i-1]
            if ri > rj:
                total_dist += self._dist_mat[ri][rj]
                # print rj, ri
            else:
                total_dist += self._dist_mat[rj][ri]
                # print rj, ri
        return total_dist

    def hill_climbing(self, indices=False):
        i = 0
        while i < self.N_RHC_TRIES:
            curr_route = self._route[:]
            if i == 0:
                curr_qual = self._best_qual
            else:
                curr_route[1:] = numpy.random.permutation(curr_route[1:])  # Random restart of the route (the first node must be the same)
                curr_qual = self.quality(curr_route)
            finished = False
            while not finished:
                succ = self.successors(curr_route)
                updated = False
                for s in succ:
                    qual = self.quality(s)
                    if qual < curr_qual:  # We want to minimize the distance
                        curr_qual = qual
                        curr_route = s
                        updated = True
                finished = not updated
            if curr_qual < self._best_qual:
                self._best_qual = curr_qual
                self._route = curr_route
                i = 0
            else:
                i += 1
        if indices:
            return self._route
        return [self._nodes[node_index] for node_index in self._route]

    def simulated_annealing(self, indices=False):
        temp = self.INITIAL_TEMP
        curr_route = self._route[:]
        curr_qual = self._best_qual
        while temp > self.TEMP_TRESH:
            for _ in range(self.N_ITER_SA):
                new_state = self.random_swap(curr_route)  # newS <- generate_random_successors(currS)
                new_qual = self.quality(new_state)
                delta_energy = curr_qual - new_qual
                if delta_energy > 0:
                    curr_qual = new_qual
                    curr_route = new_state
                    if curr_qual < self._best_qual:
                        self._best_qual = curr_qual
                        self._route = curr_route[:]
                elif numpy.random.random() < math.exp(delta_energy/temp):  # Probability of moving to a worse state
                    # with probability e ^(deltaE/T) : currS <- newS
                    curr_route = new_state
                    curr_qual = curr_qual
            # Reduce temperature
            temp *= self.ALPHA_SA  # alpha < 1
        if indices:
            return self._route
        # Return a list of nodes ordered with the route
        return [self._nodes[node_index] for node_index in self._route]

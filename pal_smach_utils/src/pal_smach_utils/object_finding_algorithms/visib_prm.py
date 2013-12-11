import pal_smach_utils.object_finding_algorithms.ofb_utils as ofb_utils
import math
#import random
import numpy.random as random  # Is said to be more efficient than the standard random module
#random.seed(54321)


class Visib_PRM(object):

    M = 300
    MAX_DIST_MTRS = 1.5  # Maximum distance in metres to consider something visible
    MIN_DIST_MTRS = 0.1  # Minimum distance in metres to consider something visible
    # Values of the occupancy grid
    FREE = 0
    OCCUPIED = 100
    UNKNOWN = -1
    PRM_POINT = 3  # Point inserted by the algorithm
    # Values to identify inner corners (corner ids)
    UL = 1  # Up Left
    UR = 2  # Up Right
    DL = 3  # Down Left
    DR = 4  # Down Right
    # Size of the region (Nx*Ny) to look for occupied pixels
    Nx = 7
    Ny = 7

    def __init__(self, occupancy_grid, c1, c2, c3, c4, inn_corners=[]):
        ''' It recieves the occupancy grid (an object of type nav_msgs/OccupancyGrid),
            the four corners of the room and a list of inner corners (i.e the room is not rectangular) '''

        # To make the class get the map. Remove occupancy_grid parameter if used
        # print "Waiting for service..."
        # rospy.wait_for_service('/static_map')
        # print "Connected to /static_map"
        # try:
        #     getmap = rospy.ServiceProxy('/static_map', GetMap)
        #     occupancy_grid = getmap().map
        # except rospy.ServiceException, e:
        #     print "Service call failed: %s" % e

        self._grid = list(occupancy_grid.data)
        self._NCOL = occupancy_grid.info.width
        self._NFIL = occupancy_grid.info.height
        self._resolution = occupancy_grid.info.resolution  # m/cell

        origin = occupancy_grid.info.origin
        self._origin = (origin.position.x, origin.position.y)

        # Save corner coordinates and adjust them
        (self._minc, self._maxc) = ofb_utils.get_corners(c1, c2, c3, c4)
        self._minc = self.met2pix(self._minc)  # From meters to pixels
        self._maxc = self.met2pix(self._maxc)  # From meters to pixels
        self._maxc = (min((self._maxc[0], self._NCOL-1)), min((self._maxc[1], self._NFIL-1)))  # To avoid an indexError

        # Mark the zones that doesn't belong to the room as occupied
        for l in inn_corners:
            corner_id = l[2] if type(l[2]) is int else self.str2corner(l[2])
            self.occupy_zone(self.met2pix((l[0], l[1])), corner_id)  # l[2] indicates which corner the point belongs to

    def met2pix(self, a_tuple):
        #return tuple([int(round(x/self._resolution)) for x in a_tuple])
        px = int(math.floor((a_tuple[0] - self._origin[0]) / self._resolution))
        py = int(math.floor((a_tuple[1] - self._origin[1]) / self._resolution))
        return (px, py)

    def pix2met(self, a_tuple):
        #return tuple([x*self._resolution for x in a_tuple])
        mx = self._origin[0] + a_tuple[0] * self._resolution
        my = self._origin[1] + a_tuple[1] * self._resolution
        return (mx, my)

    def str2corner(self, string):
        if string == 'UR':
            return self.UR
        if string == 'UL':
            return self.UL
        if string == 'DR':
            return self.DR
        return self.DL

    def mat_elem(self, l, fil, col):
        # Returns the element of the list l at position (fil, col) in a matrix accessing form. NCOL is the number of columns.
        return l[col+fil*self._NCOL]

    def mat_index(self, fil, col):
        # Returns the element of the list l at position (fil, col) in a matrix accessing form. NCOL is the number of columns.
        return col+fil*self._NCOL

    def is_free(self, x, y, check_PRM=True):
        # Returns True if point at grid(x,y) contains free space. x is the horizontal coordinate and y is the vertical one.
        # NCOL is the number of columns in the grid.
        # 0 is free. 100 is occupied and -1 is unknown
        # check_PRM tells if it has to consider points added by the algorithm as free (True) or occupied (False)

        # nx = int((self.Nx-(self.Nx/3))/2)
        # ny = int((self.Ny-(self.Ny/3))/2)
        # for i in xrange(x-nx, x+nx+1):
        #     for j in xrange(y-ny, y+ny+1):
        #         elem = self.mat_elem(self._grid, j, i)
        #         if elem != self.FREE and elem != self.PRM_POINT:
        #             return False
        # return True

        elem = self.mat_elem(self._grid, y, x)
        if elem == self.FREE or (check_PRM and elem == self.PRM_POINT):
            return True
        return False

    def is_free_region(self, x, y, check_PRM=False):
        # Returns True if the region of Nx x Ny with center at grid(x,y) contains free space.
        # x is the horizontal coordinate and y is the vertical one.
        # NCOL is the number of columns in the grid.
        # 0 is free. 100 is occupied and -1 is unknown
        # check_PRM tells if it has to consider points added by the algorithm as free (True) or occupied (False)

        nx = int(self.Nx/2)
        ny = int(self.Ny/2)
        for j in range(y-ny, y+ny+1):
            line = self._grid[self.mat_index(j, x-nx):self.mat_index(j, x+nx)+1]
            if not reduce(lambda acc, l: acc and l, map(lambda p: p == self.FREE or (check_PRM and p == self.PRM_POINT), line)):
                return False
        return True

    def bresenham_supercover_visibility(self, x1, y1, x2, y2, corners=True):
        # Returns True if point (x1, y1) in grid sees point (x2, y2) in grid. grid is assumed to have NCOL columns.
        # Point1 sees point2 if there exist a straight line between them that goes entirely on free cells. Otherwise False is returned.
        # from http://lifc.univ-fcomte.fr/~dedu/projects/bresenham/index.html
        y = y1
        x = x1
        dx = x2 - x1
        dy = y2 - y1
        if not self.is_free(x1, y1):  # Primer punt
            return False
        ystep = 1
        if dy < 0:
            ystep = -1
            dy = -dy
        xstep = 1
        if dx < 0:
            xstep = -1
            dx = -dx
        ddx = 2 * dx
        ddy = 2 * dy
        if ddx >= ddy:
            errorprev = error = dx
            for i in range(0, dx):
                x += xstep
                error += ddy
                if error > ddx:
                    y += ystep
                    error -= ddx
                    if error + errorprev < ddx:
                        if not self.is_free(x, y-ystep):
                            return False
                    elif error + errorprev > ddx:
                        if not self.is_free(x-xstep, y):
                            return False
                    elif corners:
                        if (not self.is_free(x, y-ystep)) or (not self.is_free(x-xstep, y)):
                            return False
                if not self.is_free(x, y):
                    return False
                errorprev = error
        else:
            errorprev = error = dy
            for i in range(0, dy):
                y += ystep
                error += ddx
                if error > ddy:
                    x += xstep
                    error -= ddy
                    if error + errorprev < ddy:
                        if not self.is_free(x-xstep, y):
                            return False
                    elif error + errorprev > ddy:
                        if not self.is_free(x, y-ystep):
                            return False
                    elif corners:
                        if (not self.is_free(x-xstep, y)) or (not self.is_free(x, y-ystep)):
                            return False
                if not self.is_free(x, y):
                    return False
                errorprev = error
        return True

    def occupy_point(self, p):
        nx = int(self.Nx/2)
        ny = int(self.Ny/2)
        x = p[0]
        y = p[1]
        line = [self.PRM_POINT] * (2*nx+1)
        for j in range(y-ny, y+ny+1):
            self._grid[self.mat_index(j, x-nx):self.mat_index(j, x+nx)+1] = line

    def random_config(self):
        # Creates a random free configuration in the map
        r = (random.randint(self._minc[0], self._maxc[0]), random.randint(self._minc[1], self._maxc[1]))
        while not self.is_free_region(r[0], r[1], False):  # FIXME maybe we need a max num of iterations here
            r = (random.randint(self._minc[0], self._maxc[0]), random.randint(self._minc[1], self._maxc[1]))
        return r

    def visible(self, g, q):
        dist_mtrs = ofb_utils.euclidean_distance(g, q)*self._resolution
        if dist_mtrs > self.MAX_DIST_MTRS or dist_mtrs < self.MIN_DIST_MTRS:
            return False
        return self.bresenham_supercover_visibility(g[0], g[1], q[0], q[1])

    def visib_prm(self, in_mtrs=True):
        Guard = []  # List of lists
        Connection = []
        ntry = 0
        while ntry < self.M:
            q = self.random_config()
            g_vis = None  # Last guard viewed
            G_vis = None  # Last connex component viewed
            i = 0
            while i < len(Guard):  # A for could be used but we would miss iterations if a connection node is reused
                Gi = Guard[i]
                found = False
                connected = False
                for g in Gi:
                    if self.visible(g, q):  # q belongs to Vis(g)
                        found = True
                        if g_vis is None:
                            g_vis = g
                            G_vis = i
                        else:  # q is a connection node
                            Connection.append((q, (q, g), (q, g_vis)))
                            # Create edges (q, g) and (q, gvis)
                            Guard[i].extend(Guard.pop(G_vis))  # Merge components Gvis and Gi
                            #Mark the point in the map
                            self.occupy_point(q)
                            connected = True
                    if found:
                        break
                if not connected:  # If connected the Guard list is smaller so the current i is in fact the next one
                    i += 1
            if g_vis is None:  # q is a guard node
                Guard.append([q])
                # Mark the point in the map.
                self.occupy_point(q)
                ntry = 0
            else:
                ntry += 1
        # We return the guards in a plain list (as in the algorithm is a list of lists)
        #plain_guards = reduce(lambda x, y: x + y, Guard)
        #We get the connected component with the highest number of nodes
        n_max_g = -1
        plain_guards = []
        for guards in Guard:
            n_guards = len(guards)
            if n_guards > n_max_g:
                n_max_g = n_guards
                plain_guards = guards

        if in_mtrs:
            conn_mtrs = map(lambda c: (self.pix2met(c[0]), (self.pix2met(c[1][0]), self.pix2met(c[1][1]))), Connection)
            return (map(self.pix2met, plain_guards), conn_mtrs)
        return (plain_guards, Connection)

    def occupy_zone(self, point, direction):
        # Get the region
        if direction == self.UL:
            xi = self._minc[0]
            yi = self._minc[1]
            xf = point[0]
            yf = point[1]
        elif direction == self.UR:
            xi = point[0]
            yi = self._minc[1]
            xf = self._maxc[0]
            yf = point[1]
        elif direction == self.DL:
            xi = self._minc[0]
            yi = point[1]
            xf = point[0]
            yf = self._maxc[1]
        else:  # direction == self.DR
            xi = point[0]
            yi = point[1]
            xf = self._maxc[0]
            yf = self._maxc[1]
        # Mark the zone as occupied
        occupied_line = [self.OCCUPIED] * (int(xf-xi)+1)
        for y in range(yi, yf+1):
            self._grid[self.mat_index(y, xi):self.mat_index(y, xf)+1] = occupied_line

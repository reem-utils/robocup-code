# This message defines a named location.  Coordinates reference the
# global map.  The robot can be asked to go to locations by their
# name.  How the robot goes to a location depends on its type--a
# place or a thing.  In the latter case, something can be expected
# to occupy the defined coordinates.  However, the robot should get
# as close as possible.

Header header

# How the location is known
string name

# Pose of the location
float32 xx
float32 yy
float32 th

# Desired precision with which the pose must be attained.
float32 dist_thresh
float32 angle_thresh

# One of the below types, which identifies how to go to this place.
uint8 type

uint8 type_place=1	# The pose can be attained by the robot
uint8 type_thing=2	# Something is at this pose; just get close.

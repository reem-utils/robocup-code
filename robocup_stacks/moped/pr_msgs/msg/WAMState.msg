Header header

float64[] positions
float64[] jpositions
# float64[] velocities  # not implemented yet
float64[] torques
pr_msgs/TrajInfo[] trajectory_queue
pr_msgs/TrajInfo prev_trajectory
uint8 state

uint8 state_free=0
uint8 state_fixed=1
uint8 state_traj_active=2
uint8 state_traj_stalled=3
uint8 state_traj_paused=4
uint8 state_inactive=255

# Deprecated state names; please switch to the ones above
uint8 state_moving=2 # deprecated
uint8 state_stalled=3 # deprecated

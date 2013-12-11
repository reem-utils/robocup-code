uint32 id
string type
float64[] end_position
uint32 state

uint8 state_pending=0
uint8 state_active=1
uint8 state_done=3
uint8 state_aborted=4

# Deprecated state names; please use the ones above
uint8 state_running=1 # deprecated
uint8 state_paused=2  # deprecated: look for state_traj_paused in WAMState.state




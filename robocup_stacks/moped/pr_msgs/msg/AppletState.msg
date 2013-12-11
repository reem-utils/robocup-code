string cmd_topic_name     # The topic name to use when calling 
                          # AppletCommand service for this node

pr_msgs/Action[] actions  # the actions that this applet is ready 
                          #   to perform NOW

uint8 state               # the applet state (one of the values below)

string info               # any additional human-readable information

uint8 state_idle=0
uint8 state_busy=1
uint8 state_error=2
uint8 state_dying=3


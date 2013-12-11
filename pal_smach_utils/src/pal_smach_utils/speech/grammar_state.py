from smach_ros import ServiceState

from pal_interaction_msgs.msg import asrupdate
from pal_interaction_msgs.srv import recognizerService

# Constants
GRAMMAR_ACTION_NAME = 'asrservice'


class GrammarState(ServiceState):
    """GrammarState.

    Use this State to enable and disable grammar.
    """

    def __init__(self, grammar, enabled):
        """Constructor for GrammarState.

        @type grammar: string
        @param grammar: The grammar name that you want enabled or disable.

        @type enabled: boolean
        @param enabled: If False, 0 or None, the grammar will be disabled. Enabled otherwise.

        """

        def asr_request_cb(userdata, old_request):
            if enabled:
                print "ASR: Enabling grammar '%s'" % grammar
            else:
                print "ASR: Disabling grammar '%s'" % grammar
            update = asrupdate()
            update.enable_grammar = grammar
            update.active = bool(enabled)

            return update

        ServiceState.__init__(self,
            GRAMMAR_ACTION_NAME, recognizerService,
            request_cb=asr_request_cb)

# vim: expandtab ts=4 sw=4

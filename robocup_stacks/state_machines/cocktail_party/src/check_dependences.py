#! /usr/bin/env python
# -.- coding: utf-8 -.-
""" Contains calls the State that check all depencences of Cocktail Party. """

import roslib
roslib.load_manifest('cocktail_party')
import smach
import rospy
import smach_ros

from pal_smach_utils.utils.global_common import succeeded, aborted, preempted
from pal_smach_utils.utils.cocktail_party_variables import cocktail_party_variables as cp_vars
from pal_smach_utils.utils.check_dependences import CheckDependencesState

class CocktailPartyCheckDependences(CheckDependencesState):
    """Check the dependences of the CocktailPartyStateMachine and check
    the 'consistence'"""
    def __init__(self):
        CheckDependencesState.__init__(self,
            topic_names=cp_vars.TOPICS,
            service_names=cp_vars.SERVICES,
            action_names=cp_vars.ACTIONS,
            map_locations=cp_vars.MAP_LOCATIONS,
            object_names=cp_vars.ALLOWED_DRINKS)


    def __check_drinks(self):
        """Check if the number of ALLOWED_DRINKS is equals of bigger than
        the NUMBER_PERSONS variable"""
        len_drinks = len(cp_vars.ALLOWED_DRINKS)

        if len_drinks < cp_vars.NUMBER_PERSONS:
            self._print_fatal(
            "Failed: The size (%s) of the list ALLOWED_DRINKS '%s' is smaller than number_persons (%s). Check the cocktail_party.yaml file and/or the grammar '%s'."
            % (str(len_drinks), str(cp_vars.ALLOWED_DRINKS), str(cp_vars.NUMBER_PERSONS), str(cp_vars.DRINKS_GRAMMAR_NAME)))

            return aborted

        self._print_info("Checking number_persons and ALLOWED_DRINKS list size: OK")
        return succeeded


    def __check_person_names(self):
        """Check if the lenght of the list PERSON_NAMES is bigger or equal
        the NUMBER_PERSONS variable"""
        self._print_title("CHECKING CONSISTENCE")
        len_persons_name = len(cp_vars.PERSONS_NAME)

        if len_persons_name < cp_vars.NUMBER_PERSONS:
            self._print_fatal(
            "Failed: The size (%s) of the list of people '%s' is smaller than number_persons (%s). Check the cocktail_party.yaml file and/or the grammar '%s'."
            % (str(len_persons_name), str(cp_vars.PERSONS_NAME), str(cp_vars.NUMBER_PERSONS), str(cp_vars.PEOPLE_GRAMMAR_NAME)))

            return aborted

        self._print_info("Checking number_persons and PERSONS_NAME list size: OK")
        return succeeded


    def __check_consistence(self):
        """Check the consistence of the variables that will be used by CocktailPartyStateMachine"""
        out_1 = self.__check_person_names()
        out_2 = self.__check_drinks()

        return aborted if out_1 == aborted or out_2 == aborted else succeeded

    def __mandatory_warning(self):
        self._print_title("MANDATORY WARNING")
        """Warning about the grammars that should be identical on the two robot computers, because the
        person and drink names are loaded from the reemh3c, but the robot will hear according with the
        grammars on the reemh3m."""
        self._print_warning("Important: The grammars '%s.gram' and '%s.gram' should be identical with the grammar "
            % (str(cp_vars.PEOPLE_GRAMMAR_NAME), str(cp_vars.DRINKS_GRAMMAR_NAME))
            + "with the same name on reemh3c and reemh3m computers.")

    def execute(self, userdata):
        """The main function."""
        main_outcome = super(CocktailPartyCheckDependences, self).execute(userdata)
        consistence_outcome = self.__check_consistence()

        self.__mandatory_warning()

        return aborted if main_outcome == aborted or consistence_outcome == aborted else succeeded


def main():
    """ Main function """
    rospy.init_node('check_dependences')
    s_m = smach.StateMachine(outcomes=[succeeded, aborted, preempted])
    with s_m:

        smach.StateMachine.add(
            "CHECK_DEPENDENCES",
            CocktailPartyCheckDependences(),
            transitions={succeeded: succeeded, aborted: aborted}
            )

    sis = smach_ros.IntrospectionServer(
        'check_dependences_introspection', s_m, '/SM_ROOT')
    sis.start()

    s_m.execute()

    rospy.spin()
    sis.stop()

if __name__ == '__main__':
    main()

#! /usr/bin/env python

# import roslib; roslib.load_manifest('gpsrSoar')
# import rospy
import sys
# import smach
# import smach_ros
# import actionlib

# sys.path.append("/home/jy/reem_at_iri/state_machines/common/src")
# from pal_smach_utils.utils.find_and_recognize_people import FindAndRecognizeParticularPersonStateMachine as FindAndRecognizeParticularPersonSM
# from pal_smach_utils.object_finding_algorithms.ofb_first_approach import OFBFirstApproach as OFBFirstApproachSM
# from pal_smach_utils.grasping.sm_grasp import GraspStateMachine as GraspSM
# from pal_smach_utils.navigation.move_to_room import MoveToRoomStateMachine as MoveToRoomSM
# from follow_me import FollowMe as FollowMeSM
# from follow_me import LearnPerson as LearnPersonSM

sys.path.append("/home/jy/iSOAR/bin")
import Python_sml_ClientInterface as sml
# /home/jy/reem_at_iri/state_machines/gpsr_applyOrder
SOAR_GP_PATH = "/home/jy/testbench/SOARagents/REEM01.soar"

# def call_go_to(loc_name):
#     print "SM : go_to %s" % (loc_name)
#     move_to_drinks = MoveToRoomSM()
#     move_to_drinks.userdata.room_name = loc_name 
#     out = move_to_drinks.execute()
#     return out

# def call_exit(): #TODO 
#     print "SM : exit"
#     return call_go_to("exit")

# def call_learn_person():
#     print "SM : learn_person"
#     lp = LearnPersonSM()
#     out = lp.execute()
#     PT_id_of_person = lp.userdata.PT_Id_of_person
#     LP_all_person_data = lp.userdata.LP_all_person_data
#     return (out, PT_id_of_person, LP_all_person_data)

# def call_recognize_person(): #TODO
#     print "SM : recognize_person" 

# def call_introduce(): #TODO
#     print "SM : introduce" 

# def call_point_at(): #TODO
#     print "SM : point_at" 

# def call_follow(): #TODO
#     print "SM : follow" 
#     f = FollowMeSM()
#     out = f.execute()
#     return out

# def call_find_object(object_name, loc_name):
#     print "SM : find_object %s" % (object_name)
#     fo = OFBFirstApproachSM(target_object_key='target_obj')
#     fo.userdata.target_obj = object_name
#     fo.userdata.in_room_name= loc_name
#     out = fo.execute()
#     found_object = fo.userdata.out_object_found
#     return (out, found_object)

# def call_grasp(obj):
#     print "SM : grasp %s" % (obj)
#     grasp = GraspSM()
#     grasp.userdata.pose_object = obj
#     out = grasp.execute()
#     return out

# def call_find_person(person_name):
#     print "SM : find_person %s" % (person_name)
#        fp = FindAndRecognizeParticularPersonSM()
#        fp.userdata.name_key = person_name
#        out = fp.execute()
#        return out

# def call_bring_to(person_name): #TODO
#     print "SM : bring_to %s" % (person_name)


# def trad_obj(obj):
#     if obj == 0:
#         return "coke"
#     else:
#         return "NULL"

# def trad_pers(pers):
#     if pers==0:
#         return "John"
#     else:
#         return "NULL"

# def trad_loc(loc):
#     if loc == 0:
#         return "asd"
#     elif loc == 1:
#         return "kitchen"
#     elif loc == 2:
#         return "bethroom"
#     else:
#         return "NULL"

def define_prohibitions(): #TODO
    pass

def create_kernel():
    kernel = sml.Kernel.CreateKernelInCurrentThread()
    if not kernel or kernel.HadError():
        print kernel.GetLastErrorDescription()
        exit(1)
    return kernel

def create_agent(kernel, name):
    agent = kernel.CreateAgent("agent")
    if not agent:
        print kernel.GetLastErrorDescription()
        exit(1)
    return agent

def agent_load_productions(agent, path):
    agent.LoadProductions(path)
    if agent.HadError():
        print agent.GetLastErrorDescription()
        exit(1)

def main():
    kernel = create_kernel()
    agent = create_agent(kernel, "agent")
    agent_load_productions(agent,SOAR_GP_PATH)        

    goal_achived = False
    i=0
    while not goal_achived:

        agent.Commit()
        agent.ClearOutputLinkChanges()


        agent.RunSelfTilOutput()
        print "El agente ha generado comandos de salida"

        agent.Commands()
        numberCommands = agent.GetNumberCommands();
        print "Numero de comandos recibidos del agente: %s" % (numberCommands)

        # i=0;  #sisi.. esto es una guarrada... se tiene que ver como borrar los comandos anteriores correctamente...
        while i<numberCommands:

            command = agent.GetCommand(i)
            print i
            print command
            command_name = command.GetCommandName()
            print command_name
            i += 1
            print "El nombre del commando %d/%d es %s" % (i,numberCommands,command_name)

            out = "NULL"
            if command_name == "go-to":
                loc_to_navigate = command.GetParameterValue("destination")
                loc = loc_to_navigate
                out = "succeeded"
                # agent.DestroyWME(agent.GetOutputLink())
                agent.GetOutputLink().DestroyWME()
                # print loc
                if (loc =="NULL"):
                    print "ERROR: la loacalizacion %s no existe" % (loc_to_navigate)

                agent.GetInputLink().CreateStringWME("location", loc)
                agent.GetInputLink().CreateStringWME("performed", command_name)


            # elif command_name == "grasp":
            #     obj_to_grasp = command.GetParameterValue("obj")
            #     obj = trad_obj(obj_to_grasp)
            #     if (obj =="NULL"):
            #         print "ERROR: el objeto %s no existe" % (obj_to_grasp)

            #     out = call_grasp(obj)

            # elif command_name == "deliver":
            #     to_pers = command.GetParameterValue("pers")
            #     pers = trad_pers(to_pers)
            #     if (pers =="NULL"):
            #         print "ERROR: la persona %s no existe" % (to_pers)

            #     out = call_bring_to(pers)

            # elif command_name == "search-object":
            #     obj_to_search = command.GetParameterValue("obj")
            #     obj = trad_obj(obj_to_search)
            #     if (obj =="NULL"):
            #         print "ERROR: el objeto %s no existe" % (obj_to_search)

            #     out,obj = call_find_object(obj)

            # elif command_name == "search-person":
            #     pers_to_search = command.GetParameterValue("pers")
            #     pers = trad_pers(pers_to_search)
            #     if (pers =="NULL"):
            #         print "ERROR: la persona %s no existe" % (pers_to_search)

            #     out = call_find_person(pers)

            # elif command_name == "follow":
            #     out = call_follow()

            elif command_name == "result":
                goal_achived = True
                print 'goal achieved!!'
                out == "succeeded"

            else:
                print "ERROR: El commando %s no existe" % (command_name)
                command.AddStatusComplete()

            
            print "SM return: %s" % (out)
            if out=="succeeded": 
                command.AddStatusComplete()
        agent.ClearOutputLinkChanges()

        kernel.CheckForIncomingCommands()
    command.AddStatusComplete()


    kernel.DestroyAgent(agent)
    kernel.Shutdown()
    del kernel


if __name__ == "__main__":
    main()

#! /usr/bin/env python
import roslib
roslib.load_manifest('tts_mock')
import rospy
import actionlib

from text_to_speech.msg import SoundAction as TTSAction
from pal_smach_utils.utils.play_sound_sm import SpeakText

ROS_TALK = rospy.get_param('/params_tts/ros_talk')


class SpeakingText():

    def __init__(self):
        self.setTxt()

    def setTxt(self):
        self.text_to_say = ""


class TextToSpeechServer:

    """
    Note that we are using a State called SpeakText.
    To use a State, you call the execute method. The input of
    it must be a userdata structure that has the same structure
    as the userdata of that State.
    Eg: SpeakText has input_keys=['text_to_say'], that means
    that your userdata object that you feed SpeakText(userdata_object)
    has to be of the structure userdata_object.text_to_say. Thats
    why I've build a constructor called SpeakingText.

    To enable or disable this function you just have to go to the config
    file in the tts_mock pkg named tts.yaml and change the state of the variable
    ros_talk.
    rostalk : True --> the tts_mock will talk apart from writing the messages.

    In order to use it you have to:
    1)Install the audio-commons of ROS.
    http://www.ros.org/wiki/audio_common/Tutorials/

    """

    def __init__(self, name):
        self._server = actionlib.SimpleActionServer(name,
                                                    TTSAction,
                                                    self._execute,
                                                    auto_start=False)
        self._server.start()

    def _execute(self, goal):
        if ROS_TALK:
            t = SpeakingText()
            t.text_to_say = goal.text
            speakSM = SpeakText()
            speakSM.execute(t)
        print "Goal received ============"
        print goal
        print "=========================="
        self._server.set_succeeded()


def tts_service():
    rospy.init_node('sound')
    server = TextToSpeechServer('sound')
    print "TextToSpeechServer started... waiting for goals"
    rospy.spin()

if __name__ == '__main__':
    tts_service()

#! /usr/bin/env python
# -*- encoding: utf-8 -*-

"""
This module alows us to play and stop any kind of sound in ogg or wav format,
and it also gives as an auxiliary Text to Speach module.

In order to use it you have to:
1)Install the audio-commons of ROS.
http://www.ros.org/wiki/audio_common/Tutorials/

2)Launch soundplay_node.launch, add the following line to your launch.
<include file="$(find sound_play)/soundplay_node.launch" />

3) To add more voices, just do the following:
    #. $sudo apt-get install festival festlex-cmu festlex-poslex festlex-oald libestools1.2 unzip
    #. $apt-cache search festvox-* (to see which voices are available for download)
    #. $sudo apt-get install name_of_voice ( Eg:festvox-don )

4) Then you just have to give it as input in the SpeakText(VOICE_NAME)

5) These are some that you could have:
el_diphone
suo_fi_lj_diphone
hy_fi_mv_diphone
rab_diphone
don_diphone
ked_diphone
kal_diphone
czech_ph
czech_krb
pc_diphone
lp_diphone

"""


import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach

from pal_smach_utils.utils.mp3_to_wav_converter import Mp3ToWavConverter, SoundFileIsMp3
from pal_smach_utils.utils.bpm_conversions import BpmToFreq
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted
from sound_play.libsoundplay import SoundClient


class PlaySoundOnceState(smach.State):

    """
    Plays an .OGG or .WAV file. The path to the file should be absolute,
    and be valid on the computer on which sound_play is running.
    Bare in mind that only one sound at a time can be reproduced.
    If you are playing one sound and then another it will probably
    stop the first one and start the second one.
    IMPORTANT: When executing bare in mind that when executing in Reem,
    the to_execute_sound_file_path has to be the path in the m PC, which has to have
    the pkg sound_play soundplay_node.launch launched.
    """

    def __init__(self, to_execute_sound_file_path="/tmp/tmp_sound_file.wav"):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['sound_file_path'])
        self._to_execute_sound_file_path = to_execute_sound_file_path

    def execute(self, userdata):

        if SoundFileIsMp3(userdata.sound_file_path):
            print "CONVERTING MP3 TO WAV"
            sound_path = Mp3ToWavConverter(input_mp3_absolute_path=userdata.sound_file_path, output_wav_absolute_path=self._to_execute_sound_file_path)
        else:
            print "ALREADY WAV, NO CONVERSION NEEDED"
            sound_path = self._to_execute_sound_file_path
        print "@@@11"
        soundhandle = SoundClient()
        print "@@@11"
        rospy.sleep(1)
        print "@@@11"
        soundhandle.playWave(sound_path)
        print "@@@11"
        rospy.sleep(1)

        return succeeded


class PlaySoundAtRateGiven(smach.State):

    """
    This state playes a sound at a given rate in beats per minute
    bpm: is the rate at which you want the given sound to be played
    sound_path: this is the absolute sound path of the .wav or .ogg that
                you want to play. In case you give an mp3 file this will be converted
                to .wav.
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['sound_file_path', 'bpm'])

    def execute(self, userdata):

        sound_path = Mp3ToWavConverter(userdata.sound_file_path)
        frequency = BpmToFreq(userdata.bpm)
        soundhandle = SoundClient()

        rospy.sleep(1)

        r = rospy.Rate(frequency)
        rospy.loginfo("Playing the sound in this path ==> " + sound_path)
        while not rospy.is_shutdown():
            soundhandle.playWave(sound_path)
            r.sleep()

        return succeeded


class ShutUp(smach.State):

    """
    This state makes that no sound is produced antil CTRL + C is pressed.
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['sound_file_path'])

    def execute(self, userdata):

        soundhandle = SoundClient()
        #let ROS get started...
        rospy.sleep(0.5)

        print "Sending stopAll commande every 100 ms."
        print "Note: This will not prevent a node that is continuing to issue commands"
        print "from producing sound."
        print "Press Ctrl+C to exit."

        while not rospy.is_shutdown():
            soundhandle.stopAll()
            try:
                rospy.sleep(.1)
            except:
                pass

        return succeeded


class StopSoundState(smach.State):

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['sound_file_path'])

    def execute(self, userdata):

        soundhandle = SoundClient()
        #let ROS get started...
        rospy.sleep(0.5)

        soundhandle.stopAll()

        return succeeded


class SpeakText(smach.State):

    def __init__(self, voice_name='voice_kal_diphone'):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['text_to_say'])
        self._voice_name = voice_name

    def execute(self, userdata):

        soundhandle = SoundClient()
        rospy.sleep(1)

        #voice = 'voice_kal_diphone'
        print 'Saying: %s' % userdata.text_to_say
        print 'Voice: %s' % self._voice_name
        rospy.loginfo("SAYING ==>%s" % userdata.text_to_say)

        soundhandle.say(userdata.text_to_say, self._voice_name)
        rospy.sleep(1)

        return succeeded

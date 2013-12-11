# -*- encoding: utf-8 -*-

import roslib
roslib.load_manifest('pal_smach_utils')
import rospy
import smach
import wave

from pal_smach_utils.utils.mp3_to_wav_converter import Mp3ToWavConverter
from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

#Time in seconds to avoid being dancing when the sonf finishes.
SECURITY_TIME = 10.0
#Put to zero if you want the real duration in seconds of the song.
TIME_YOU_WANT_FOR_SONG = 60

def SoundFileDuration(file_absolute_path):
    """
    Returns the duration of a sound file in milliseconds.
    The input file can be .wav or .mp3. If its an .mp3 file
    it will be converted in order to make the analysis.
    If you put the TIME_YOU_WANT_FOR_SONG to a value different 
    from zero, it will instead put that duration.
    It comes in handy when you want a song to last a determinate
    amount of time.
    """

    if TIME_YOU_WANT_FOR_SONG != 0:
        time = TIME_YOU_WANT_FOR_SONG
    else:
        wavfile = Mp3ToWavConverter(file_absolute_path)
        myfile = wave.open(wavfile, "r")
        frames = (1.0 * myfile.getnframes())
        sr = myfile.getframerate()
        time = (1.0 * (frames/sr)) - SECURITY_TIME

    print "Security Seconds ===> " + str(SECURITY_TIME)
    print "DURATION OF THE SOOONG in seconds ===> " + str(time)
    print "DURATION IN MINUTES ===> " + str(time/60.0)

    return int(round(time * 1000))


class SongDurationState(smach.State):

    """
    Given a song path that can be an mp3 file or a wav,
    it gives you the duration of that file in milliseconds
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['in_song_path'], output_keys=['song_duration_out'])

    def execute(self, userdata):

        userdata.song_duration_out = SoundFileDuration(userdata.in_song_path)

        return succeeded

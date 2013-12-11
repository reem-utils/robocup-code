# -*- encoding: utf-8 -*-

import roslib; roslib.load_manifest('dancing_reem')
import rospy
import smach
import os
import pipes
from random import randint
from roslib import packages

from pal_smach_utils.utils.global_common import succeeded, preempted, aborted

from jorgen_bpm import analyze_mp3


DANCING_REEM_PKG = 'dancing_reem'
NAME_MP3_LIBRARY_DIR = 'mp3_lib'
# 12 bpm is very slow movements, like one beat every 5 seconds
BPM_MINIMUM = 12.0


class BpmAnalysisSM(smach.StateMachine):

    """
    SM that selects a random mp3 file from the dancing_reem/mp3_lib
    and extracts its BPM.
    If no song is found, it will keep looking until one is introduced in
    the mp3_lib or the program is terminated.
    """

    def __init__(self):

        smach.StateMachine.__init__(self, [succeeded, preempted, aborted], input_keys=[], output_keys=['bpm_out', 'song_path_out'])

        with self:

            smach.StateMachine.add('SELECT_RANDOM_MP3_FILE_FROM_MP3LIB',
                                    SelectRandomMP3FileFromMp3LibState(),
                                    transitions={'song_found': 'EXTRACT_BPM_FROM_MP3',
                                                'no_song_found': 'SELECT_RANDOM_MP3_FILE_FROM_MP3LIB',
                                                preempted: preempted,
                                                aborted: aborted},
                                    remapping={'song_path_out': 'song_path_out'})

            smach.StateMachine.add('EXTRACT_BPM_FROM_MP3',
                                   ExtractBpmFromMp3State(),
                                   transitions={succeeded: succeeded,
                                                preempted: preempted,
                                                aborted: aborted},
                                    remapping={'in_song_path': 'song_path_out',
                                                'bpm_out': 'bpm_out'})


def SelectRandomMP3FileFromMp3Lib():

    """
    Selects radomly a song in the mp3_lib dir in the dancing_reem package.
    It now take mp3 files and wav files. We dont get .ogg because soundstretch doesnt.
    """

    base = packages.get_pkg_dir(DANCING_REEM_PKG)
    path_to_mp3_lib = os.path.join(base, NAME_MP3_LIBRARY_DIR)

    list_mp3_songs_in_mp3lib = filter(lambda x: x.endswith('.mp3'), os.listdir(path_to_mp3_lib))
    list_wav_songs_in_mp3lib = filter(lambda x: x.endswith('.wav'), os.listdir(path_to_mp3_lib))
    list_songs_in_mp3lib = list_mp3_songs_in_mp3lib + list_wav_songs_in_mp3lib

    print "Song LIST" + str(list_songs_in_mp3lib)

    if len(list_songs_in_mp3lib) == 0:
        rospy.loginfo("###### The MP3 Library is EMPTY ######")
        song_path = 'None'
    else:
        random_song_name = list_songs_in_mp3lib[randint(0, len(list_songs_in_mp3lib) - 1)]
        print "SELECTED SONG: " + str(random_song_name)
        song_path = os.path.join(path_to_mp3_lib, random_song_name)

    return song_path


class SelectRandomMP3FileFromMp3LibState(smach.State):

    """
    This State looks for the Dancing Reem PKG and picks randomly in the mp3_lib
    a song.
    If no song has been found, it return 'no song found'
    """

    def __init__(self):

        smach.State.__init__(self, outcomes=['song_found', 'no_song_found', preempted, aborted],
                                    input_keys=[],
                                    output_keys=['song_path_out'])

    def execute(self, userdata):

        music_path = SelectRandomMP3FileFromMp3Lib()
        userdata.song_path_out = music_path
        if music_path == 'None':
            return 'no_song_found'
        else:
            return 'song_found'


def SlowDancing(bpm):
    """
    When we have a slow song, without noticeable beats,
    we will get bpm = 0.0. This is unaccetable because the robots has to know
    how to dance slow music. Thats why in case bpm is very low ( lower tha BPM_MINIMUM)
    we will always give it the BPM_MINIMUM.
    If its higher then the bpm isnt modified.
    """
    if bpm < BPM_MINIMUM:
        return BPM_MINIMUM
    return bpm


def ExtractBpmFromMp3(mp3filespec):

    """
    This Function extracts the BPM ( Beats Per Minute) of a given song
        mp3filespec : Absolute Path to the mp3 file.
    In case no BPM is found, we will evaluate bpm to 0.0
    """

    bpm_suggestion = analyze_mp3(pipes.quote(mp3filespec))
    if bpm_suggestion is None:
        print "Unable to detect bpm for file %s" % mp3filespec
        bpm_suggestion = 0.0
    else:
        print "BPM rate for %s is estimated to be %s" % (mp3filespec, bpm_suggestion)

    return SlowDancing(bpm_suggestion)


class ExtractBpmFromMp3State(smach.State):

    def __init__(self):

        smach.State.__init__(self, outcomes=[succeeded, preempted, aborted], input_keys=['in_song_path'], output_keys=['bpm_out'])

    def execute(self, userdata):

        mp3filespec = os.path.abspath(userdata.in_song_path)
        bpm = ExtractBpmFromMp3(mp3filespec)
        print "THIS IS THE REAL BEAT " + str(bpm)
        userdata.bpm_out = bpm
        return succeeded

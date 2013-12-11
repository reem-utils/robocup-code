#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import subprocess


def Mp3ToWavConverter(input_mp3_absolute_path, output_wav_absolute_path="/tmp/tmp_sound_file.wav"):

    """
    To use this function you need to have installed lame
    $sudo apt-get install lame
    If output_wav_absolute_path is not given , then the output file will be placed
    $/tmp/tmp_sound_file.wav. If its a wav file it just copeies it to the output_wav_absolute_path.
    """
    print "SONG TO BE CONVERTED PATH" + str(input_mp3_absolute_path)

    # Use lame to make a wav representation of the mp3 file to be analyzed
    wav_command = 'lame --decode %s %s' % (input_mp3_absolute_path, output_wav_absolute_path)
    subprocess.call([wav_command], shell=True, stderr=open(os.devnull, 'w'))

    print "CONVERTED SONG OUTPUT PATH" + str(output_wav_absolute_path)
    return output_wav_absolute_path


def SoundFileIsMp3(sound_file_Name):

    extension = sound_file_Name.rsplit('.', 1)[1]
    print "THE FILE HAS EXTENSION ==> " + str(extension)
    if extension == 'mp3':
        print "SOUND FILE IS MP3"
        return True

    return False

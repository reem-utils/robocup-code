#!/usr/bin/python
DOC = ''' This program detects bpm for mp3 files. It relies on lame and soundstretch being
installed on your system. 


Usage: 

    %s <filename>
    
-or pipe filenames to it.

Example:

    find . -name "*.mp3"| %s\n''' % (__file__, __file__)

import os
import pipes
import select
import shutil
import subprocess
import sys
import tempfile

## Define the window for sane bpm values. This may depend on genre of music. ##
BPM_WINDOW_MAX = 240
# Do not change this one
BPM_WINDOW_MIN = BPM_WINDOW_MAX/2
###############################################################################


def _get_bpm_from_soundstretch(output):
    """Gets bpm value from soundstretch output"""

    output = output.split("\n")
    for line in output:
        if 'Detected BPM rate ' in line:
            bpm = line[18:]
            return float(bpm)
    return None  # Could not parse output


def fit_bpm_in_window(bpm_suggestion):
    """Double or halve a bpm suggestion until it fits inside the bpm window"""

    if bpm_suggestion is not None:
        while bpm_suggestion < (BPM_WINDOW_MIN):
            bpm_suggestion = bpm_suggestion * 2
        while bpm_suggestion > (BPM_WINDOW_MAX):
            bpm_suggestion = bpm_suggestion / 2
    return bpm_suggestion


def analyze_mp3(mp3filespec):
    """
    Uses lame and soundstretch to analyze an mp3 file for its bpm rate.
    If the input file mp3filespec is a .wav file, it doesnt matter
    because lame detects it and just copies the file to the temporal file.
    """

    # Make a temporary working directory for storing the wav file
    # that soundstretch should analyze
    workingdir = tempfile.mkdtemp()
    wavfilespec = workingdir + "/tempwavfile.wav"

    # Use lame to make a wav representation of the mp3 file to be analyzed
    wav_command = 'lame --decode %s %s' % (mp3filespec, wavfilespec)
    subprocess.call([wav_command], shell=True, stderr=open(os.devnull, 'w'))

    # Call soundstretch to analyze the wav file
    p = subprocess.Popen(['soundstretch', wavfilespec, '-bpm'], stderr=subprocess.PIPE)
    output = p.communicate()[1]

    # Delete temporary working directory and its contents
    shutil.rmtree(workingdir)

    bpm_suggestion = _get_bpm_from_soundstretch(output)
    print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

    return fit_bpm_in_window(bpm_suggestion)


def process_input(mp3filespec):
    bpm_suggestion = analyze_mp3(pipes.quote(mp3filespec))
    if bpm_suggestion is None:
        print "Unable to detect bpm for file %s" % mp3filespec
    else:
        print "BPM rate for %s is estimated to be %s" % (mp3filespec, bpm_suggestion)

if __name__ == "__main__":
    argv = sys.argv[1:]
    # input is piped to program
    if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
        mp3filespecs = sys.stdin.readlines()
        for mp3filespec in mp3filespecs:
            process_input(mp3filespec.rstrip('\n'))
    elif len(argv) < 1:  # No pipe and no input file, print help text and exit
        print DOC
        sys.exit()
    else:  # Input file present
        mp3filespec = os.path.abspath(argv[0])
        process_input(mp3filespec)

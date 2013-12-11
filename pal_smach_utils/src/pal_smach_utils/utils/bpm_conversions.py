#! /usr/bin/env python
# -*- encoding: utf-8 -*-


def BpmToPeriod(bpm, multiplier=1.0):

    """
    Turns BPM to seconds between beats. Period between one neat and the next.
    The second variable is a multiplier to allow us to
    have multiples of the basic period. Its default value is 1.0.
    """
    print "BPM INPUT = " + str(bpm)
    beat_period = ((1.0 / (bpm / 60.0)) * multiplier)
    print "BPM PERIOD = " + str(beat_period)
    print (beat_period)
    return beat_period


def BpmToFreq(bpm, multiplier=1.0):

    """
    Turns BPM into Hz.
    """
    print "BPM INPUT = " + str(bpm)
    beat_freq_Hz = bpm / 60
    print "FREQUENCY OUTPUT = " + str(beat_freq_Hz)
    return beat_freq_Hz

def PeriodToBpm(period):

    """
    Turns Perod to beats per minute. Period between one beat and the next.
    """
    print "PERIOD INPUT = " + str(period)
    bpm = ((1.0 / period ) * 60.0)
    print "BPM = " + str(bpm)
    return bpm

#!/usr/bin/env python3

'''Cozmo sings an original monster-catching adventure tune.

This is an original melody and original lyrics in the same playful
"let's go catch them all" spirit as a certain monster-catching show's
theme song - not a reproduction of that (or any other existing) song.

Cozmo plays the melody for ~5 seconds, then "sings" original lyrics via
text-to-speech for ~5 seconds. Throughout both phases, a random animation
from the full cozmo.anim.Triggers list plays continuously alongside.
'''

import random
import time

import cozmo
from cozmo.song import SongNote, NoteTypes, NoteDurations


# An original short, upbeat melody (not a transcription of any existing song).
MELODY = [
    SongNote(NoteTypes.C2, NoteDurations.Quarter),
    SongNote(NoteTypes.E2, NoteDurations.Quarter),
    SongNote(NoteTypes.G2, NoteDurations.Quarter),
    SongNote(NoteTypes.C3, NoteDurations.Quarter),
    SongNote(NoteTypes.G2, NoteDurations.Quarter),
    SongNote(NoteTypes.E2, NoteDurations.Quarter),
    SongNote(NoteTypes.F2, NoteDurations.Quarter),
    SongNote(NoteTypes.A2, NoteDurations.Quarter),
]

# Original lyrics, not from any existing song.
LYRICS = ("Little robot on the go, gotta find them high and low! "
          "Every friend, near and far, Cozmo knows just who you are!")


def play_random_animations_for(robot: cozmo.robot.Robot, duration_s):
    '''Play random animation triggers back-to-back until duration_s has elapsed.'''
    deadline = time.time() + duration_s
    triggers = cozmo.anim.Triggers.trigger_list  # pyright: ignore[reportAttributeAccessIssue]

    while True:
        remaining = deadline - time.time()
        if remaining <= 0:
            break

        trigger = random.choice(triggers)
        action = robot.play_anim_trigger(trigger, ignore_body_track=True, in_parallel=True)
        try:
            action.wait_for_completed(timeout=remaining)
        except (TimeoutError, cozmo.exceptions.CozmoSDKException):
            action.abort()


def cozmo_program(robot: cozmo.robot.Robot):
    print("Phase 1: melody (~5s) + random animations")
    song_action = robot.play_song(MELODY, loop_count=3, in_parallel=True)
    play_random_animations_for(robot, 5.0)
    song_action.abort()

    print("Phase 2: original lyrics (~5s) + random animations")
    say_action = robot.say_text(LYRICS, in_parallel=True)
    play_random_animations_for(robot, 5.0)
    say_action.abort()


cozmo.run_program(cozmo_program)

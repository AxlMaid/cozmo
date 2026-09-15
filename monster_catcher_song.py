#!/usr/bin/env python3

'''Cozmo sings an original monster-catching adventure tune.

This is an original melody and original lyrics in the same playful
"let's go catch them all" spirit as a certain monster-catching show's
theme song - not a reproduction of that (or any other existing) song.

Sequence: random animation, then the melody, then another random
animation, then the lyrics (spoken), then one last random animation.

Note: singing/speaking and a triggered animation's own sound effect can't
play at once - Cozmo only has one audio channel, and confirmed on real
hardware, starting an animation trigger while the song/speech action is
still running actively aborts it rather than being silenced or queued.
That's why these run one at a time instead of "in parallel".
'''

import random

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


def play_random_animation(robot: cozmo.robot.Robot):
    '''Play a single random animation trigger and wait for it to complete.'''
    trigger = random.choice(cozmo.anim.Triggers.trigger_list)  # pyright: ignore[reportAttributeAccessIssue]
    robot.play_anim_trigger(trigger, ignore_body_track=True).wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]


def say_long_text(robot: cozmo.robot.Robot, text, max_len=255):
    '''Speak text via say_text(), splitting it into whole-word chunks first if
    needed - Cozmo's SayText protocol message hard-caps text at 255 characters
    and raises ValueError rather than truncating it for you.'''
    words = text.split()
    chunk = ""
    for word in words:
        candidate = (chunk + " " + word).strip()
        if len(candidate) > max_len:
            robot.say_text(chunk).wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]
            chunk = word
        else:
            chunk = candidate
    if chunk:
        robot.say_text(chunk).wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]


def cozmo_program(robot: cozmo.robot.Robot):
    print("Random animation")
    play_random_animation(robot)

    print("Melody")
    robot.play_song(MELODY, loop_count=3).wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]

    print("Random animation")
    play_random_animation(robot)

    print("Lyrics")
    say_long_text(robot, LYRICS)

    print("Random animation")
    play_random_animation(robot)


cozmo.run_program(cozmo_program)

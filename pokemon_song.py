#!/usr/bin/env python3

'''Cozmo sings an original monster-catching adventure tune.

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


# Pokemon song melody
MELODY = [
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.C2, NoteDurations.Quarter),
	SongNote(NoteTypes.A2, NoteDurations.Quarter),
	SongNote(NoteTypes.F2, NoteDurations.Half),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.C2, NoteDurations.Whole),
	SongNote(NoteTypes.F2, NoteDurations.Half),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.F2, NoteDurations.Half),
	SongNote(NoteTypes.Rest, NoteDurations.Half),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.C2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Half),
	SongNote(NoteTypes.Rest, NoteDurations.Half),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.D2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.F2, NoteDurations.Quarter),
	SongNote(NoteTypes.G2, NoteDurations.Quarter),
	SongNote(NoteTypes.A2, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.C2, NoteDurations.Quarter),
	SongNote(NoteTypes.F2, NoteDurations.Half),
	SongNote(NoteTypes.Rest, NoteDurations.Half),
	SongNote(NoteTypes.G2, NoteDurations.Half),
	SongNote(NoteTypes.F2, NoteDurations.Quarter),
	SongNote(NoteTypes.A2, NoteDurations.Quarter),
	SongNote(NoteTypes.A2_Sharp, NoteDurations.Quarter),
	SongNote(NoteTypes.C2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Quarter),
	SongNote(NoteTypes.D2, NoteDurations.Half)
]


# Pokemon song lyrics
LYRICS = ("Un jour je serai le meilleur dresseur"
          "Je me battrai sans répit"
          "Je ferai tout pour être vainqueur"
          "Et gagner les défis"
          "Je parcourerai la terre entière"
          "Traquant avec espoir"
          "Les pokémon et leurs mystères"
          "Le secret de leurs pouvoirs"
          "Pokémon !"
          "Attrapez les tous"
          "C'est notre histoire"
          "Ensemble pour la victoire"
          "Pokémon !"
          "Rien ne nous arrêtera"
          "Notre amitié triomphera"
          "Pokémon !"
          "Attrapez les tous"
          "Même à notre âge !"
          "Un voyage d'apprentissage"
          "Ça demande du courage !"
          "Po-ké-mon !"
          "Attrapez-les tous! Attrapez-les tous!"
          "Pokémon !")


def play_random_animation(robot: cozmo.robot.Robot):
    '''Play a single random animation trigger and wait for it to complete.'''
    trigger = random.choice(cozmo.anim.Triggers.trigger_list)  # pyright: ignore[reportAttributeAccessIssue]
    print("Random animation (" + trigger.name + ")")
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
    play_random_animation(robot)

    print("Melody")
    robot.play_song(MELODY, loop_count=3).wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]

    play_random_animation(robot)

    print("Lyrics")
    say_long_text(robot, LYRICS)

    play_random_animation(robot)


cozmo.run_program(cozmo_program)

#!/usr/bin/env python3

# Copyright (c) 2026 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Investigate the SdkTextToSpeech animation trigger.

cozmo.anim.Triggers.SdkTextToSpeech is named as though it should be the
"talking" animation that plays alongside robot.say_text(). It isn't. The
SDK's own source (cozmo/robot.py, class SayText) never uses it:

    if play_excited_animation:
        self.play_event = _clad_to_engine_cozmo.AnimationTrigger.OnSawNewNamedFace
    else:
        # TODO: Switch to use AnimationTrigger.SdkTextToSpeech when that works correctly
        self.play_event = _clad_to_engine_cozmo.AnimationTrigger.Count

Anki's own engineers left that TODO in place, meaning SdkTextToSpeech shipped
broken, and say_text() instead falls back to AnimationTrigger.Count (an
essentially blank placeholder) or, when play_excited_animation=True, reuses
the unrelated OnSawNewNamedFace trigger (meant for greeting a recognized
face).

This tutorial plays all three back to back so you can hear/see the
difference for yourself:
    1) Plain say_text()                      -> AnimationTrigger.Count
    2) say_text(play_excited_animation=True)  -> AnimationTrigger.OnSawNewNamedFace
    3) SdkTextToSpeech triggered directly     -> whatever it actually does today

Trigger (3) is unsupported and was never finished. Confirmed on real
hardware: it completes without error (has_failed is never set) but produces
no sound and no animation at all - a true dead trigger, not just an unusual
one. This tutorial still checks has_failed/failure_reason afterwards since
that's the only signal the SDK gives you; it won't tell you the trigger did
nothing.

See anim_triggers.md at the repo root for the full list of available
triggers (the official docs site, cozmosdk.anki.bot, is offline).

The two say_text() calls below speak French and use use_cozmo_voice=False
(the generic human voice instead of Cozmo's robot-filtered one). Note this
only swaps the voice *style* - it does not change the language/accent, which
is fixed by the Cozmo app itself and not exposed anywhere in the SDK.
'''

import cozmo


def cozmo_program(robot: cozmo.robot.Robot):
    # 1) Plain say_text(): internally uses AnimationTrigger.Count as its
    # "talking" animation, which is essentially a no-op placeholder.
    print("1) Plain say_text() - uses AnimationTrigger.Count internally:")
    robot.say_text("Bonjour, j'utilise la fonction de synthèse vocale normale.",
                    use_cozmo_voice=False).wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]

    # 2) Excited say_text(): internally reuses OnSawNewNamedFace, a trigger
    # meant for greeting a recognized face, not for talking.
    print("2) Excited say_text() - reuses the OnSawNewNamedFace trigger:")
    robot.say_text("Maintenant, j'utilise plutôt la version excitée !",
                    play_excited_animation=True,
                    use_cozmo_voice=False).wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]

    # 3) Play SdkTextToSpeech directly. This is the trigger that was clearly
    # *meant* to power say_text(), but never worked and was never wired up.
    print("3) Playing AnimationTrigger.SdkTextToSpeech directly (unsupported):")
    action = robot.play_anim_trigger(cozmo.anim.Triggers.SdkTextToSpeech)  # pyright: ignore[reportAttributeAccessIssue]
    action.wait_for_completed()  # pyright: ignore[reportUnusedCoroutine]
    if action.has_failed:
        code, reason = action.failure_reason
        print("   -> Failed: code=%s reason='%s'" % (code, reason))
    else:
        print("   -> Completed without error, but confirmed on hardware to do nothing: "
              "no sound, no animation. A true dead trigger.")


cozmo.run_program(cozmo_program)

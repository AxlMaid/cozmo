# Cozmo SDK examples (patched for a modern toolchain)

This is Anki's official [Cozmo Python SDK](https://github.com/anki/cozmo-python-sdk) example
repository — tutorials, apps, and IFTTT integrations for the Cozmo robot. Anki shut down in
2019 and the SDK (last updated ~2018) was never touched again, so running it today means
bridging an 8-year gap against a current Python, Pillow, numpy, and Flask. This fork tracks
the fixes needed to make that gap disappear.

## What's fixed here

### Real, crash-causing bugs

- **`asyncio.sleep(..., loop=...)`** — the `loop=` keyword argument to `asyncio.sleep()` and
  `asyncio.Future()` was removed in Python 3.10+. This broke Cozmo's charger-docking behavior
  (`cozmo/robot.py`'s `backup_onto_charger()`), iOS USB pairing (`cozmo/usbmux/usbmux.py`),
  and the cube light-chaser animation in [apps/quick_tap.py](apps/quick_tap.py) — all patched
  to drop the dead argument.
- **`apps/remote_control_cozmo.py`** had a video-stream fallback branch calling
  `asyncio.sleep(.1)` with no `await` inside a function that isn't even `async` (a plain Flask
  streaming generator) — meaning it silently did nothing and busy-looped instead of pausing.
  Replaced with a real blocking `time.sleep(.1)`.
- **`if_this_then_that/ifttt_gmail.py`** parsed the sender's email address with `re.search()`
  and called `.group(1)` on the result with no null check — a malformed webhook payload from
  IFTTT would have crashed the handler. Added a proper fallback.
- **`lib/flask_helpers.py`** called `send_file(..., add_etags=False)` — Flask renamed that
  parameter to `etag` years ago; modern Flask rejects the old name outright. Fixed, and
  verified the resulting response actually omits the ETag header as intended.
- **`apps/quizmaster_cozmo.py`** had a handful of type hints that were flatly wrong (a
  non-`Optional` parameter for a value the class's own code already null-checked everywhere,
  a return type that didn't account for the function's own `return None` branch) — these
  weren't just satisfying a linter, they were documentation bugs that made the code harder to
  trust.

### Deprecated / removed APIs, swapped for their modern equivalents

- `asyncio.iscoroutinefunction` → `inspect.iscoroutinefunction` (`cozmo/run.py`, `cozmo/base.py`)
- `pkg_resources` → `importlib.resources` (`cozmo/opengl.py`, used by the 3D viewer)
- `PIL.Image.BICUBIC` / `.NEAREST` / `.LANCZOS` / `.FLIP_LEFT_RIGHT` → `Image.Resampling.*` /
  `Image.Transpose.*` (Pillow 10+ removed the old top-level aliases from its type stubs)
- `Image.getdata()` → `Image.get_flattened_data()` (deprecated, slated for removal in Pillow 14)
- `numpy.uint8(array)` used as a dtype cast → `array.astype(numpy.uint8)` (the correct,
  unambiguous numpy API for that)
- Flask's `send_file(add_etags=...)` → `send_file(etag=...)`

### Editor / type-checker cleanup

Every tutorial and app now passes Pylance/pyright with zero diagnostics. Two different things
were going on under the hood, handled differently:

- **Genuine gaps** (old-style broken `# type: X Y` comments, `Optional` values with no
  annotation hiding a real crash path, mistyped parameters) got *real* fixes — either a correct
  type annotation or, where a value can legitimately be `None` at a real system boundary
  (external webhook input, a browser hitting a Flask route before the robot connects), an
  actual guard.
- **False positives** — mostly the SDK's own dual sync/async dispatch magic (`cozmo/base.py`'s
  `_SyncProxy`/`_Factory` descriptors let the same code run as blocking calls or real
  coroutines depending on context, which static analysis can't see through) and
  `cozmo.anim.Triggers`' ~576 attributes being populated dynamically at import time rather than
  declared in the class body — got suppressed with a `# pyright: ignore[...]` and a comment
  explaining why, rather than rewritten.

### Reference

- **[anim_triggers.md](anim_triggers.md)** — the full list of all 576 `cozmo.anim.Triggers`
  names, generated from the installed SDK and grouped by theme. Anki's official docs site
  (`cozmosdk.anki.bot/docs`) is offline, so this replaces it.
- **[tutorials/01_basics/13_sdk_text_to_speech.py](tutorials/01_basics/13_sdk_text_to_speech.py)** —
  a small investigation confirming `cozmo.anim.Triggers.SdkTextToSpeech` (named as though it
  should be the "talking" animation for `say_text()`) was shipped broken and never wired up —
  Anki's own source has a TODO admitting as much. Verified on real hardware: it completes
  without error but does nothing at all.

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
./install_sdk_patches.sh
```

A virtual environment isn't required (`pip3 install --user -r requirements.txt` works fine
too), but it keeps this project's dependencies isolated from anything else on your machine, and
it's what's actually been tested. Either way, run `install_sdk_patches.sh` with that same
environment active — it patches whatever `python3` resolves to at the time. If you create
another venv later, or reinstall `requirements.txt` into an existing one, re-run it there too.

See [requirements.txt](requirements.txt) for why `cozmo`/`cozmoclad` are pulled from a direct
URL rather than PyPI (PyPI's public releases are older than what's tested here), and why
`setuptools<81` is currently required for a fresh install.

`pip install` gives you Anki's original, unpatched SDK — the five bugs described above live in
the actual pip-installed package, not in this repo, so they'd otherwise come back on every fresh
install. [install_sdk_patches.sh](install_sdk_patches.sh) copies this repo's patched
[cozmo_sdk/](cozmo_sdk) directory over your installed copy to fix that.

## Layout

- [tutorials/](tutorials) — a graduated course from `hello_world` through vision, cube/object
  handling, async patterns, and parallel actions.
- [apps/](apps) — fuller demos: a browser-based remote control, a desk security guard, color
  chasing, a trivia quiz, a reaction-tap game, a 3D pose viewer.
- [if_this_then_that/](if_this_then_that) — webhook-triggered reactions (Gmail, sports scores,
  stock prices) via IFTTT.
- [multi_robot/](multi_robot) — controlling more than one Cozmo/cube from a single script.
- [tools/cubes/](tools/cubes) — standalone cube connect/disconnect/battery-check utilities.
- [cozmo_sdk/](cozmo_sdk) — a vendored, patched copy of the installed `cozmo` package (see
  [install_sdk_patches.sh](install_sdk_patches.sh)). Not imported directly by anything here; it
  exists so the SDK-level fixes travel with the repo instead of living only on one machine.
  Named `cozmo_sdk` rather than `cozmo` on purpose — Python checks the current directory before
  site-packages, so a folder literally named `cozmo` sitting at the repo root would silently
  shadow the real installed package for anything run from here.

More to come as we build our own programs on top of this.

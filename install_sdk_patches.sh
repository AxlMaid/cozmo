#!/bin/sh
# Overlays this repo's patched cozmo_sdk/ package on top of the pip-installed one.
#
# The wheel pulled by requirements.txt is Anki's original, unpatched cozmo SDK.
# This repo's cozmo_sdk/ directory is that same SDK with the fixes described in
# README.md applied (dead asyncio loop= kwargs, deprecated asyncio.iscoroutinefunction,
# pkg_resources -> importlib.resources). Run this after `pip3 install -r requirements.txt`
# to apply those fixes to your installed copy.

set -e

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
DEST=$(python3 -c "import cozmo, os; print(os.path.dirname(cozmo.__file__))")

cp -r "$SCRIPT_DIR/cozmo_sdk/." "$DEST/"
echo "Patched cozmo SDK installed to $DEST"

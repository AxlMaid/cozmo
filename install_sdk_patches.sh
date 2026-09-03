#!/bin/sh
# Overlays this repo's patched cozmo/ package on top of the pip-installed one.
#
# The wheel pulled by requirements.txt is Anki's original, unpatched cozmo SDK.
# This repo's cozmo/ directory is that same SDK with the fixes described in
# README.md applied (dead asyncio loop= kwargs, deprecated asyncio.iscoroutinefunction,
# pkg_resources -> importlib.resources). Run this after `pip3 install -r requirements.txt`
# to apply those fixes to your installed copy.
#
# Requires Python 3.11+ (for the -P flag, which resolves the real install path
# instead of accidentally finding this repo's own cozmo/ folder when run from here).

set -e

SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
DEST=$(python3 -P -c "import cozmo, os; print(os.path.dirname(cozmo.__file__))")

cp -r "$SCRIPT_DIR/cozmo/." "$DEST/"
echo "Patched cozmo SDK installed to $DEST"

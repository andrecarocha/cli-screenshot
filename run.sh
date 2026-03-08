#!/bin/bash
# Launch the Screenshot to Clipboard menu bar app
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec /usr/local/bin/python3 "$SCRIPT_DIR/screenshot.py"

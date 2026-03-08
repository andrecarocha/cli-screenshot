# Screenshot to Clipboard

A lightweight macOS menu bar app that captures screenshots directly to the clipboard — no files saved.

## Features

- **Capture Region** — drag to select any area of the screen
- **Capture Window** — click any window to capture it
- **Capture Fullscreen** — grabs all screens
- Lives in the menu bar, no Dock icon
- Zero dependencies beyond Python 3 + PyObjC (ships with macOS dev tools)

## Requirements

- macOS
- Python 3 with PyObjC (`/usr/local/bin/python3` or adjust path)

Check if PyObjC is available:
```bash
python3 -c "import objc; print('ok')"
```

If not, install it:
```bash
pip3 install pyobjc-framework-Cocoa
```

## Install & Run

### Run manually
```bash
./run.sh
```

### Auto-start on login (LaunchAgent)
```bash
# Install
cp com.andrecarocha.screenshot.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.andrecarocha.screenshot.plist

# Stop
launchctl unload ~/Library/LaunchAgents/com.andrecarocha.screenshot.plist
```

> **Note:** Edit the Python path in `run.sh` and the `.plist` file if your `python3` is not at `/usr/local/bin/python3`.

## How it works

Uses macOS's built-in `screencapture` command with the `-c` flag (clipboard) and `-i` flag (interactive selection). No temp files are written.

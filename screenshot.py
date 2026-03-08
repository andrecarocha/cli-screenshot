#!/usr/bin/env python3
"""
Screenshot to Clipboard — macOS Menu Bar App
Captures region or window and copies directly to clipboard (no file saved).
"""

import subprocess
import sys
import os

import objc
from AppKit import (
    NSApplication,
    NSStatusBar,
    NSMenu,
    NSMenuItem,
    NSImage,
    NSVariableStatusItemLength,
)
from Foundation import NSObject, NSLog


class AppDelegate(NSObject):
    statusitem = None

    def applicationDidFinishLaunching_(self, notification):
        bar = NSStatusBar.systemStatusBar()
        self.statusitem = bar.statusItemWithLength_(NSVariableStatusItemLength)

        # Use camera emoji as the icon (simple, no image file needed)
        btn = self.statusitem.button()
        btn.setTitle_("⌘⇧4")

        menu = NSMenu.new()
        menu.setAutoenablesItems_(False)

        self._add_item(menu, "Capture Region  ⌘⇧4", "captureRegion:", "")
        self._add_item(menu, "Capture Window  ⌘⇧5", "captureWindow:", "")
        self._add_item(menu, "Capture Fullscreen", "captureFullscreen:", "")
        menu.addItem_(NSMenuItem.separatorItem())
        self._add_item(menu, "Quit", "quitApp:", "q")

        self.statusitem.setMenu_(menu)

    def _add_item(self, menu, title, action, key):
        item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            title, action, key
        )
        item.setTarget_(self)
        item.setEnabled_(True)
        menu.addItem_(item)
        return item

    def captureRegion_(self, sender):
        # -i = interactive, -c = clipboard (no file)
        subprocess.Popen(["screencapture", "-ic"])

    def captureWindow_(self, sender):
        # -i = interactive, -W = window mode, -c = clipboard
        subprocess.Popen(["screencapture", "-iWc"])

    def captureFullscreen_(self, sender):
        # -c = clipboard, captures all screens
        subprocess.Popen(["screencapture", "-c"])

    def quitApp_(self, sender):
        NSApplication.sharedApplication().terminate_(self)


def main():
    app = NSApplication.sharedApplication()
    # Accessory policy = no Dock icon, lives only in menu bar
    app.setActivationPolicy_(1)

    delegate = AppDelegate.new()
    app.setDelegate_(delegate)
    app.run()


if __name__ == "__main__":
    main()

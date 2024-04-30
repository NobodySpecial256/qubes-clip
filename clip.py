#!/usr/bin/env python3

from sys import argv, stderr
# Refer to /usr/lib/python3.11/site-packages/qui/clipboard.py
from qui.clipboard import pyinotify, qubesadmin, NotificationApp, Gtk, Gdk

if len(argv) != 2:
	print("Usage: %s <text>" %(argv[0]), file=stderr)
	raise SystemExit

wm = pyinotify.WatchManager()
qubes_app = qubesadmin.Qubes()
dispatcher = qubesadmin.events.EventsDispatcher(qubes_app)
gtk_app = NotificationApp(wm, qubes_app, dispatcher)
clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
text = clipboard.wait_for_text() # Save dom0's old clipboard

clipboard.set_text(argv[1], -1)
gtk_app.copy_dom0_clipboard()

if text != None:
	clipboard.set_text(text, -1) # Revert dom0's clipboard

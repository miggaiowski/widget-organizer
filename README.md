widget-organizer
================

Mac OS X Dashboard Widget Organizer

Everytime I switch from my laptop display to an external monitor
and back, the widgets' positions I had chosen get messed up.
This is my attempt to automate the positioning of the widgets.

Instructions
------------

1. Kill the Dock (Dashboard's parent process)
2. Run the organizer 

That is:

        $ sudo killall dock
		$ ./organizer.py ~/Library/Preferences/com.apple.dashboard.plist


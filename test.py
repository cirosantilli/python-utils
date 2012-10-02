#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
My curses cheatsheet/template!
"""

import curses

def init(screen):
    """
    Startup functions that make the terminal work like a gui app.
    """
    screen.border(0)
    screen.clear() #clears the screen
    curses.noecho() #don't echo user input
    curses.cbreak() #no enter to process key
    screen.keypad(1) #accept special keys such as directionals

def cleanup(screen):
    """
    Cleanup actions in case of an exception (typically KeyboardInterrupt),
    or terminal may be left in a messy state.
    """
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin() 

def main(screen):

    i=1

    while 1:

        c = screen.getch()

        screen.addstr(i, i, "hello world") 

        if c == ord('p'): i=i+1
        elif c == ord('q'): break
        elif c == curses.KEY_HOME: x = y = 0

if __name__ == "__main__":
    screen = curses.initscr() #creates the screen object
    try:
        init(screen)
        curses.wrapper(main)
    except KeyboardInterrupt:
        print "interrupt"
    finally:
        cleanup(screen)

#!/usr/bin/python

## AntNest.py
##
## Written by Matthew Egan
## License: MIT License
##
## https://github.com/tolo137/AntNest

import sys
import pygame
from pygame.locals import *

import gameLoop

VER_NUM = "v0.1"

def main():
    # Initialise the PyGame engine
    pygame.init()

    # Instanstiate the applications window
    screen = makeWindow()

    # Begin the application loop
    app = gameLoop.Game(VER_NUM, screen)
    app.runApplication()

    # Exit the application
    pygame.quit()
    sys.exit(0)

def makeWindow():
    # Get command line args
    args = sys.argv

    # Attempt to set resolution using args, otherwise default to 480x360
    try:
        width = int(sys.argv[1])
        height = int(sys.argv[2])
    except:
        width = 480
        height = 360

    screen = pygame.display.set_mode((width, height))

    # Check fonts work
    if not pygame.font: print "Warning: Font disabled"

    pygame.display.set_caption("AntNest " + VER_NUM)

    return screen


if __name__ == "__main__": main()
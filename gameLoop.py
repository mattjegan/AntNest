import sys
import pygame
from pygame.locals import *

class Game:
    def __init__(self, versionNum, screen):
        self.VER_NUM = versionNum
        self.screen = screen

    def runApplication(self):
        self.running = True
        screen = self.screen

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            screen.fill((0,0,0))

            pygame.display.update()
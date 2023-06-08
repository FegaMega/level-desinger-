import pygame
class main:
    def __init__(self):
        self.screenSize = [700, 700]
        self.screen = pygame.display.set_mode(self.screenSize)
    def newScreen(self):
        self.screen = pygame.display.set_mode(self.screenSize)
import pygame
from screeninfo import get_monitors
for m in get_monitors():
    if m.is_primary == True:
        Primary_screen = m
class main:
    def __init__(self):
        self.user_primary_display_size = [Primary_screen.width, Primary_screen.height]
        self.screenSize = [700, 700]
        self.screen = pygame.display.set_mode(self.screenSize)
    def newScreen(self):
        self.screen = pygame.display.set_mode(self.screenSize)
        print(self.screenSize, pygame.display.get_window_size())
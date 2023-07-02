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
        self.Key = [
            ["Q", False, 0],
            ["W", False, 1],
            ["E", False, 2],
            ["R", False, 3],
            ["T", False, 4],
            ["Y", False, 5],
            ["U", False, 6],
            ["I", False, 7],
            ["O", False, 8],
            ["P", False, 9],
            ["A", False, 10],
            ["S", False, 11],
            ["D", False, 12],
            ["F", False, 13],
            ["G", False, 14],
            ["H", False, 15],
            ["J", False, 16],
            ["K", False, 17],
            ["L", False, 18],
            ["Z", False, 19],
            ["X", False, 20],
            ["C", False, 21],
            ["V", False, 22],
            ["B", False, 23],
            ["N", False, 24],
            ["M", False, 25], 
            ["UP", False, 26],
            ["LEFT", False, 27],
            ["DOWN", False, 28],
            ["RIGHT", False, 29],
        ]
    def newScreen(self):
        self.screen = pygame.display.set_mode(self.screenSize)

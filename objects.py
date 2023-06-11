import pygame

from utils import main
U = main()

class cube:
    def __init__(self, x, y, xsize, ysize, color=(0, 0, 0), extra_info=[]):
        self.extra_info = extra_info
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
    def draw(self, scroll=[0, 0]):
        self.rect = pygame.Rect(self.x - scroll[0], self.y - scroll[1], self.xsize, self.ysize)
        pygame.draw.rect(U.screen, self.color, self.rect)
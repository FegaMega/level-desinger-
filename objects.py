import pygame

from utils import utils
U = utils()

class cube:
    def __init__(self, x, y, xsize, ysize, color=(0, 0, 0), extra_info=[]):
        self.extra_info = extra_info
        self.pos : int= [x, y]
        self.size : int = [xsize, ysize]
        self.color = color
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    def draw(self, scroll=[0, 0]):
        self.rect = pygame.Rect(self.pos[0] - scroll[0], self.pos[1] - scroll[1], self.size[0], self.size[1])
        pygame.draw.rect(U.screen, self.color, self.rect)
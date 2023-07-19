import pygame

from utils import utils
U = utils()

class cube:
    def __init__(self, x, y, xsize, ysize, color=(0, 0, 0)):
        #color is a pointer and if not changed during init of construction will be linked to every other object not changed during constrution
        #it can only be changed localy with "color = (info/new pointer)" and never with something like color.(func) 
        self.extra_info:list = [0, 0, 0, 0]
        self.pos : int= [x, y]
        self.size : int = [xsize, ysize]
        self.color = color
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    def draw(self, scroll=[0, 0]):
        self.rect = pygame.Rect(self.pos[0] - scroll[0], self.pos[1] - scroll[1], self.size[0], self.size[1])
        pygame.draw.rect(U.screen, self.color, self.rect)
        try:
            index = self.extra_info.index("drawRightGreen")
            if True == self.extra_info[index+1]:
                pygame.draw.rect(U.screen, (0, 255, 0), pygame.Rect(self.pos[0] + self.size[0] - U.tolerance - scroll[0], self.pos[1] - scroll[1], U.tolerance, self.size[1]))
        except:
            TypeError
        try:
            index = self.extra_info.index("drawDownGreen")
            if True == self.extra_info[index+1]:
                pygame.draw.rect(U.screen, (0, 255, 0), pygame.Rect(self.pos[0] - scroll[0], self.pos[1] + self.size[1] - U.tolerance - scroll[1], self.size[0], U.tolerance))
        except:
            TypeError
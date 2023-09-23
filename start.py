import pygame

from utils import utils
U = utils()

class startBlock:
    def __init__(self, x, y, xsize, ysize, color=(0, 0, 255)):
        #color is a pointer and if not changed during init of construction will be linked to every other object not changed during constrution
        #it can only be changed localy with "color = (info/new pointer)" and never with something like color.(func) 
        self.pos : int= [x, y]
        self.size : int = [xsize, ysize]
        self.color = color
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.extra_info = []
    def rANDwExtra_info(self, extra_info, rORw:str):
        if rORw == "w":
            self.extra_info = extra_info
        elif rORw == "r":
            return self.extra_info
    def rANDwPos(self, pos, rORw:str):
        if rORw == "w":
            self.pos = pos
        elif rORw == "r":
            return self.pos
    def rANDwSize(self, size, rORw:str):
        if rORw == "w":
            self.size = size
        elif rORw == "r":
            return self.size
    def rANDwColor(self, color, rORw:str):
        if rORw == "w":
            self.color = color
        elif rORw == "r":
            return self.color
    def draw(self, rANDwScroll):
        scroll = rANDwScroll(0, "r")
        self.rect = pygame.Rect(self.pos[0] - scroll[0], self.pos[1] - scroll[1], self.size[0], self.size[1])
        pygame.draw.rect(U.screen, self.color, self.rect)
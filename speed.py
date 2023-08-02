import pygame
import utils
U = utils.utils()

class speed:
    def __init__(self, x, y, xsize, ysize, color):
        self.extra_info = "collecteble"
        self.pos = [x, y]
        self.size = [xsize, ysize]
        self.color = color
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
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
                
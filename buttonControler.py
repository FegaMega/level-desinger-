import pygame, sys, collision, utils
class button:
    def __init__(self, pos:list, size:list, img:str, Type):
        self.pos = pos
        self.size = size
        self.img = img
        self.type = Type
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
    def draw(self, rANDwScreen):
        screen = rANDwScreen(0, "r")
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        img = pygame.image.load(self.img)
        screen.blit(img, (self.pos[0], self.pos[1]))
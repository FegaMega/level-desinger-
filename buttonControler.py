import pygame, sys, collision, utils
class button:
    def __init__(self, pos:list, size:list, img:str, Type, index):
        self.size = size
        self.inputpos = pos
        self.pos = [self.inputpos[0]-self.size[0], self.inputpos[1]]
        self.TrueSize = self.size
        self.scale = 1
        self.img = img
        self.type = Type
        self.index = index
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
    def draw(self, rANDwScreen, rANDwScreenSize):
        screen = rANDwScreen(0, "r")
        screenSize = rANDwScreenSize(0, "r")
        self.TrueSize = [screenSize[0]/700 * self.size[0], screenSize[1]/700 * self.size[1]]
        self.pos = [self.inputpos[0]-self.TrueSize[0], (self.inputpos[1]+self.TrueSize[1])*self.index + self.inputpos[1]]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.TrueSize[0], self.TrueSize[1])
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, self.TrueSize)
        screen.blit(img, (self.pos[0], self.pos[1]))
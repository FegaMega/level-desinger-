import pygame, sys, collision, utils
class button:
    def __init__(self, pos:list, size:list, img:str, Type):
        self.pos = pos
        self.size = size
        self.TrueSize = self.size
        self.scale = 1
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
    def draw(self, rANDwScreen, rANDwScreenSize):
        screen = rANDwScreen(0, "r")
        screenSize = rANDwScreenSize(0, "r")
        print(screenSize)
        self.TrueSize = [screenSize[0]/self.size[0] - 700/self.size[0] + 1*self.size[0], screenSize[1]/self.size[1] - 700/self.size[1] + 1*self.size[1]]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.TrueSize[0], self.TrueSize[1])
        print(self.TrueSize)
        img = pygame.image.load(self.img)
        img = pygame.transform.scale(img, self.TrueSize)
        screen.blit(img, (self.pos[0], self.pos[1]))
import pygame, utils

U = utils.utils()

class camera:
    def __init__(self):
        self.pos = [U.screenSize[0]/2, U.screenSize[1]/2]
        self.size = [0, 0]
        self.speed = [0.0, 0.0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    def rANDwPos(self, pos, rORw:str):
        if rORw == "w":
            self.pos = pos
        elif rORw == "r":
            pos == self.pos
    def rANDwSize(self, size, rORw:str):
        if rORw == "w":
            self.size = size
        elif rORw == "r":
            size == self.size
    def rANDwColor(self, speed, rORw:str):
        if rORw == "w":
            self.speed = speed
        elif rORw == "r":
            speed == self.speed    
    def draw(self, scroll=[0, 0]):
        playe = pygame.Rect(self.pos[0] - scroll[0], self.pos[1] - scroll[1], 50, 50)
        pygame.draw.rect(U.screen, (0, 255, 0), playe)
    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
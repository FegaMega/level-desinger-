import pygame, utils

U = utils.main()

class camera:
    def __init__(self):
        self.pos = [0, 0]
        self.xsize = 50
        self.ysize = 50
        self.speed = [0, 0]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.xsize, self.ysize)
    def draw(self, scroll=[0, 0]):
        playe = pygame.Rect(self.pos[0] - scroll[0], self.pos[1] - scroll[1], 50, 50)
        pygame.draw.rect(U.screen, (0, 255, 0), playe)
    def move(self):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.pos[0] = round(self.pos[0])
        self.pos[1] = round(self.pos[1])
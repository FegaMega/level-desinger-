import pygame, utils

U = utils.main()

class camera:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.xsize = 50
        self.ysize = 50
        self.xspeed: float = 0
        self.yspeed: float = 0
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
    def draw(self, scroll=[0, 0]):
        playe = pygame.Rect(self.x - scroll[0], self.y - scroll[1], 50, 50)
        pygame.draw.rect(U.screen, (0, 255, 0), playe)
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.x = round(self.x)
        self.y = round(self.y)
import pygame



class tunnel:
    def __init__(self, x, y, xsize, ysize, color, extra_info=[]):
        self.extra_info = extra_info
        self.x = x
        self.y = y
        self.xsize = xsize
        self.ysize = ysize
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.xsize, self.ysize)
        self.clas = "Tunnel"
    def draw(self, scroll_x, scroll_y, screen):
        self.rect = pygame.Rect(self.x - scroll_x, self.y - scroll_y, self.xsize, self.ysize)
        pygame.draw.rect(screen, self.color, self.rect)
                
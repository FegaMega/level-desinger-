import pygame, math
from datetime import datetime, timedelta

class bullet:
    def __init__(self, x, y, speed, angle):
        self.pos = [x, y]
        self.speed: float = speed
        self.angle: float = angle
        self.size = [6, 3]
        self.frames_drawn = 0
        self.og_surf = pygame.transform.smoothscale(pygame.image.load("data/img/bullet.png").convert_alpha(), (self.size[0], self.size[1]))
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.TPallow: bool = True
    def move(self):
        self.pos[0] += (math.cos(math.radians(self.angle))) * self.speed
        self.pos[1] -= (math.sin(math.radians(self.angle))) * self.speed
    def draw(self, screen, rANDwScroll):
        scroll = rANDwScroll(0, "r")
        self.rect = pygame.Rect(self.pos[0]  - scroll[0], self.pos[1] - scroll[1], self.size[0], self.size[1])
        screen.blit(self.surf, (self.pos[0] - scroll[0], self.pos[1]- scroll[1]))
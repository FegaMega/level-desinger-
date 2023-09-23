import pygame
from pygame.locals import *
from pistol import Pistol


class Player:
    def __init__(self, x, y):
        self.gun = Pistol(0, 0, 0)
        self.size = [50, 50]
        self.pos = [x, y]
        self.speed:list = [0, 0]
        self.ml: bool = False
        self.mr: bool = False
        self.mu: bool = False
        self.jumps = 0
        self.TPallow: bool = True
        self.on_floor: bool = False
        self.max_jumps = 2
        self.max_speed = .3
        self.in_tunnel = False
        self.hitbox: bool = [True, True]
        self.playe = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    def draw(self, scrollx, scrolly, screen):
        playe = pygame.Rect(self.pos[0]- scrollx, self.pos[1]- scrolly, 50, 50)
        pygame.draw.rect(screen, (0, 255, 0), playe)
    def movement(self):
        if self.ml:
            self.speed[0] -= self.max_speed/(60)
            if self.speed[0] < -self.max_speed:
                self.speed[0] = -self.max_speed
        if self.mr:
            self.speed[0] += self.max_speed/(60)
            if self.speed[0] > self.max_speed:
                self.speed[0] = self.max_speed
        if self.mr == self.ml:
            if self.speed[0] > 0.05:
                self.speed[0] -= self.speed[0]/60 
            elif self.speed[0] < -0.05:
                self.speed[0] -= self.speed[0]/60
            else:
                self.speed[0] = 0
        if self.mu == True:
            self.speed[1]= -15/10
        self.pos[0]+= self.speed[0]
        self.pos[1]+= self.speed[1]
        self.bottom:float = self.pos[1]+ self.size[1]
        self.right: float = self.pos[0]+ self.size[0] 
        self.collision_lines = [[self.right - 5, self.pos[1]+ 5, 10, 1, "right"], [self.pos[0]- 5, self.bottom - 5, 10, 1, "left"], [self.pos[0]+ 5, self.bottom - 5, 1, 10, "down"], [self.right - 5, self.bottom - 5, 1, 10, "down"], [self.right - 5, self.bottom - 5, 10, 1, "right"], [self.pos[0]- 5, self.pos[1]+ 5, 10, 1, "left"], [self.pos[0]+ 5, self.pos[1] - 5, 1, 10, "up"], [self.right - 5, self.pos[1] - 5, 1, 10, "up"]]
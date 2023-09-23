import pygame
from bullet import bullet
import math



class Pistol:
    def __init__(self, x, y, angle):
        self.pos = [x, y]
        self.size = [25, 15]
        self.angle = angle
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.rotateleft = False
        self.rotateright = False
        self.change_angle = 0
        self.og_surf = pygame.transform.smoothscale(pygame.image.load("data/img/gun.png").convert_alpha(), (self.size[0], self.size[1]))
        self.surf = self.og_surf
        self.bullets = []
        self.bullet_spawn_pos = [0, 0]
    def rot(self):
        self.angle += self.change_angle
        self.angle = self.angle % 360
        self.rect = self.surf.get_rect(center=self.rect.center)
        self.surf = pygame.transform.rotate(self.og_surf, self.angle)
    def shoot(self):
        self.bullet_spawn_pos[0] = (self.pos[0] + self.rect.height/2 + ((math.cos(math.radians(self.angle+30))) * self.rect.height/2))
        self.bullet_spawn_pos[1] = (self.pos[1] + self.rect.width/2 + ((math.sin(math.radians(self.angle+30))) * -self.rect.width/2))
        self.bullets.append(bullet(self.bullet_spawn_pos[0], self.bullet_spawn_pos[1], 5, self.angle))
    def draw(self, scroll_x, scroll_y, screen):
        screen.blit(self.surf, (self.pos[0] - scroll_x, self.pos[1] - scroll_y))



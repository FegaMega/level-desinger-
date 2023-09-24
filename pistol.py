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
        self.flip_surf = self.surf
        self.flipped = False
        self.bullets = []
        self.bullet_spawn_pos = [0, 0]
    def rot(self, mousePos, rANDwScroll):
        scroll = rANDwScroll(0, "r")
        x = mousePos[0] + scroll[0] - self.pos[0]
        y = mousePos[1] + scroll[1] - self.pos[1]
        self.angle = math.atan2(y, -x) * (180/math.pi) + 180
        
        if self.angle < 270 and self.angle > 90 and self.flipped == False:
            self.rect = self.surf.get_rect(center=self.rect.center)
            self.flip_surf = pygame.transform.flip(self.flip_surf, True, False)
            self.flipped = True
        if self.angle > 270 and self.flipped == True or self.angle < 90 and self.flipped == True:
            self.rect = self.surf.get_rect(center=self.rect.center)
            self.flip_surf = pygame.transform.flip(self.flip_surf, True, False)
            self.flipped = False
        self.rect = self.surf.get_rect(center=self.rect.center)
        if self.flipped == False:
            self.surf = pygame.transform.rotate(self.flip_surf, self.angle)
        else:
            self.surf = pygame.transform.rotate(self.flip_surf, self.angle-180)
    def shoot(self):
        if self.flipped == False:
            self.bullet_spawn_pos[0] = (self.pos[0] + self.rect.height/2 + ((math.cos(math.radians(self.angle+30))) * self.rect.height/2))
            self.bullet_spawn_pos[1] = (self.pos[1] + self.rect.width/2 + ((math.sin(math.radians(self.angle+30))) * -self.rect.width/2))
        else:
            self.bullet_spawn_pos[0] = (self.pos[0] + self.rect.height/2 + -((math.cos(math.radians(self.angle+30))) * self.rect.height/2))
            self.bullet_spawn_pos[1] = (self.pos[1] + self.rect.width/2 + -((math.sin(math.radians(self.angle+30))) * -self.rect.width/2))
        self.bullets.append(bullet(self.bullet_spawn_pos[0], self.bullet_spawn_pos[1], 5, self.angle))
    def draw(self, scroll_x, scroll_y, screen):
        screen.blit(self.surf, (self.pos[0] - scroll_x, self.pos[1] - scroll_y))
        



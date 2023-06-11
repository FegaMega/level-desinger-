import pygame
from pygame.locals import *

YACCELERATION = .1
YDECELERATION = .1
YMAX = 3

def eventW(KEYUPorKEYDOWN: str, player):
    if KEYUPorKEYDOWN == "KEYDOWN":
        if player.yspeed != YMAX:
            player.yspeed += YACCELERATION
    if KEYUPorKEYDOWN == "KEYUP":
        if player.yspeed > YDECELERATION:   
            player.yspeed -= YDECELERATION
        elif player.yspeed > 0:
            player.yspeed = 0
def eventS(KEYUPorKEYDOWN: str, player):
    if KEYUPorKEYDOWN == "KEYDOWN":
        if player.yspeed != -YMAX:
            player.yspeed -= YACCELERATION
    if KEYUPorKEYDOWN == "KEYUP":
        if player.yspeed < YDECELERATION:   
            player.yspeed += YDECELERATION
        elif player.yspeed < 0:
            player.yspeed = 0
def inputHandler(player, event):
    if event.type == pygame.KEYDOWN:
        if event.key == K_w:
            eventW("KEYDOWN", player)
        if event.key == K_s:
            eventS("KEYDOWN", player)
    if event.type == pygame.KEYUP:
        if event.key == K_w:
            eventW("KEYUP", player)
        if event.key == K_s:
            eventS("KEYUP", player)
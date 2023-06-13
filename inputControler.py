import pygame
from pygame.locals import *

YACCELERATION = .1
YDECELERATION = .1
YMAX = 3

def eventW(KEYUPorKEYDOWN: str, player):
    if KEYUPorKEYDOWN == "KEYDOWN":
        if player.speed[1] != YMAX:
            player.speed[1] += YACCELERATION
    if KEYUPorKEYDOWN == "KEYUP":
        if player.speed[1] > YDECELERATION:   
            player.speed[1] -= YDECELERATION
        elif player.speed[1] > 0:
            player.speed[1] = 0
    return [player.speed, "playerSpeed"]
def eventS(KEYUPorKEYDOWN: str, player):
    if KEYUPorKEYDOWN == "KEYDOWN":
        if player.speed[1] != -YMAX:
            player.speed[1] -= YACCELERATION
    if KEYUPorKEYDOWN == "KEYUP":
        if player.speed[1] < YDECELERATION:   
            player.speed[1] += YDECELERATION
        elif player.speed[1] < 0:
            player.speed[1] = 0
    return [player.speed, "playerSpeed"]
def inputHandler(player, event):
    if event.type == pygame.KEYDOWN:
        if event.key == K_w:
            info = eventW("KEYDOWN", player)
        if event.key == K_s:
            info = eventS("KEYDOWN", player)
    if event.type == pygame.KEYUP:
        if event.key == K_w:
            info = eventW("KEYUP", player)
        if event.key == K_s:
            info = eventS("KEYUP", player)
    return info
import pygame, objects, collision, speed
from pygame.locals import *

YACCELERATION = .1
YDECELERATION = .1
YMAX = 3
XACCELERATION = .1
XDECELERATION = .1
XMAX = 3




def inputSaver(event, rANDwKey, rANDwMouse):
    Key = rANDwKey(0, "r")
    Mouse = rANDwMouse(0, "r")
    
    
    #Keyboard saver
    if event.type == pygame.KEYDOWN: 
        for key in Key:
            if key.__class__ == list:
                if event.key == key[1]:
                    key[0] = True
                    

    if event.type == pygame.KEYUP:     
        for key in Key:
            if key.__class__ == list:
                if event.key == key[1]:
                    key[0] = False
    rANDwKey(Key, "w")

    #mouse saver
    MouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    MouseRight = Mouse[Mouse.index("MOUSERIGHT")+1]
    MouseVar = Mouse[Mouse.index("MOUSE")+1]
    MouseSrollDown = Mouse[Mouse.index("MOUSESCROLLDOWN")+1]
    MouseSrollUp = Mouse[Mouse.index("MOUSESCROLLUP")+1]
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            MouseLeft[0] = True
            MouseVar[1] = pygame.mouse.get_pos()
        if event.button == 3:
            MouseRight[0] = True
            MouseVar[1] = pygame.mouse.get_pos()
        if event.button == 4:
            MouseSrollUp[0] = True
        if event.button == 5:
            MouseSrollDown[0] = True
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            MouseLeft[0] = False
        if event.button == 3:
            MouseRight[0] = False
        if event.button == 4:
            MouseSrollUp[0] = False
        if event.button == 5:
            MouseSrollDown[0] = False
    rANDwMouse(Mouse, "w") 


def inputHandler(app):
    1+1
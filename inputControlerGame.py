import pygame, objects, collision, speed
from pygame.locals import *
from bullet import bullet

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
    for key in Key:
        if event.type == pygame.KEYDOWN: 
            if key.__class__ == list:
                if event.key == key[1]:
                        key[0] = True
        if event.type == pygame.KEYUP:     
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

def eventMOVELEFT(rANDwKey, player):
    Key = rANDwKey(0, "r") 
    A = Key[Key.index("A")+1]
    if A[0] == True:
        player.ml = True
    else:
        player.ml = False

def eventMOVEUP(rANDwKey, player):
    Key = rANDwKey(0, "r") 
    W = Key[Key.index("W")+1]
    if W[0] == True and W[2]%43 == 1 and player.jumps > 0:
        player.mu = True
        player.jumps -= 1
        if player.on_wall == True and player.on_floor == False:
            player.on_wall_object_left = player.on_wall_object
            player.on_wall = False
#            if player.on_wall_left == True:
 #               player.speed[0] = .05
#            if player.on_wall_right == True:
  #              player.speed[0] = -.05
    else:
        player.mu = False

def eventMOVERIGHT(rANDwKey, player):
    Key = rANDwKey(0, "r") 
    D = Key[Key.index("D")+1]
    if D[0] == True:
        player.mr = True
    else:
        player.mr = False

def eventROTATEGUN(rANDwKey, gun):
    Key = rANDwKey(0, "r") 
    LEFT = Key[Key.index("LEFT")+1]
    RIGHT = Key[Key.index("RIGHT")+1]
    if LEFT[0] == True:
        gun.change_angle = 10
    elif RIGHT[0] == True:
            gun.change_angle = -10
    else:
        gun.change_angle = 0
    
    

def eventSHOOTGUN(rANDwMouse, gun):
    Mouse = rANDwMouse(0, "r") 
    MOUSELEFT = Mouse[Mouse.index("MOUSELEFT")+1]
    if MOUSELEFT[0] == True and MOUSELEFT[2]%10 == 1:
        gun.shoot()

def eventsMOVING(rANDwKey, player):
    eventMOVELEFT(rANDwKey, player)
    eventMOVERIGHT(rANDwKey, player)
    eventMOVEUP(rANDwKey, player)      

def eventsGUN(rANDwKey, rANDwMouse,  gun):
    eventROTATEGUN(rANDwKey, gun)
    eventSHOOTGUN(rANDwMouse, gun)


def inputHandler(game):    
    for key in game.u.Key:
        if key.__class__ == list:
            if key[0] == True:
                key[2] += 1
            else:
                key[2] = 0
    Mouse = game.u.rANDwMouse(0, "r")
    MouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    MouseRight = Mouse[Mouse.index("MOUSERIGHT")+1]
    
    if MouseLeft[0] == True:
        MouseLeft[2] += 1
    else:
        MouseLeft[2] = 0
    if MouseRight[0] == True:
        MouseRight[2] += 1
    else:
        MouseRight[2] = 0
    eventsMOVING(game.u.rANDwKey, game.player)
    eventsGUN(game.u.rANDwKey, game.u.rANDwMouse,  game.player.gun)
    
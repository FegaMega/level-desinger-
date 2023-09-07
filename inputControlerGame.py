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
    if event.type == pygame.KEYDOWN: 
        for key in Key:
            if key.__class__ == list:
                if key == "SPACE":
                    if Key[Key.index(key)+1][0] == False:
                        Key[Key.index(key)+1][2] = False
                    else:
                        Key[Key.index(key)+1][2] = True
                if event.key == key[1]:
                        key[0] = True
            

    if event.type == pygame.KEYUP:     
        for key in Key:
            if key.__class__ == list:
                if event.key == key[1]:
                    key[0] = False
                if key == "SPACE":
                    Key[Key.index(key)+1][2] = False
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
        player.ml == True
    else:
        player.ml == False

def eventMOVEUP(rANDwKey, player):
    Key = rANDwKey(0, "r") 
    W = Key[Key.index("W")+1]
    if W[0] == True:
        player.mu == True
    else:
        player.mu == False

def eventMOVERIGHT(rANDwKey, player):
    Key = rANDwKey(0, "r") 
    D = Key[Key.index("D")+1]
    if D[0] == True:
        player.mr == True
    else:
        player.mr == False

def eventROTATEGUNLEFT(rANDwKey, gun):
    Key = rANDwKey(0, "r") 
    LEFT = Key[Key.index("LEFT")+1]
    if LEFT[0] == True:
        gun.change_angle = 10
    else:
        gun.chage_angle = 0

def eventROTATEGUNRIGHT(rANDwKey, gun):
    Key = rANDwKey(0, "r") 
    RIGHT = Key[Key.index("RIGHT")+1]
    if RIGHT[0] == True:
        gun.change_angle = -10
    else:
        gun.chage_angle = 0

def eventSHOOTGUN(rANDwKey, gun, rANDwBullets):
    Key = rANDwKey(0, "r") 
    SPACE = Key[Key.index("SPACE")+1]
    bullets = rANDwBullets(0, "r")    
    if SPACE[0] == True:
        bullets.append(bullet(gun.pos[0], gun.pos[1] + 3, 5, gun.angle))

def eventsMOVING(rANDwKey, player):
    eventMOVELEFT(rANDwKey, player)
    eventMOVERIGHT(rANDwKey, player)
    eventMOVEUP(rANDwKey, player)      

def eventsGUN(rANDwKey, gun, rANDwBullets):
    eventROTATEGUNLEFT(rANDwKey, gun)
    eventROTATEGUNRIGHT(rANDwKey, gun)
    eventSHOOTGUN(rANDwKey, gun, rANDwBullets)


def inputHandler(game):    
    eventsMOVING(game.u.rANDwKey, game.player)
    eventsGUN(game.u.rANDwKey, game.gun, game.rANDwBullets)
    
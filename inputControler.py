import pygame, objects, collision
from pygame.locals import *

YACCELERATION = .1
YDECELERATION = .1
YMAX = 3
XACCELERATION = .1
XDECELERATION = .1
XMAX = 3


def eventDOWN(speed, Key):
    S = Key[Key.index("S")+1]
    DOWN = Key[Key.index("DOWN")+1]
    if S[0] == True or DOWN[0] == True:
        if speed[1] < YMAX:
            speed[1] += YACCELERATION
        if speed[1] > YMAX:
            speed[1] = YMAX
    if S[0] == False and DOWN[0] == False: 
        if speed[1] > 0:
            if speed[1] < YDECELERATION:
                speed[1] = 0
            else:
                speed[1] -= YDECELERATION
    return [speed, "playerSpeed"]

def eventUP(speed, Key):
    W = Key[Key.index("W")+1]
    UP = Key[Key.index("UP")+1]
    if W[0] == True or UP[0] == True:
        if speed[1] > -YMAX:
            speed[1] -= YACCELERATION
        if speed[1] < -YMAX:
            speed[1] = -YMAX
    if W[0] == False and UP[0] == False:
        if speed[1] < 0:
            if speed[1] > YDECELERATION:
                speed[1] = 0
            else:
                speed[1] += YDECELERATION
    return [speed, "playerSpeed"]

def eventLEFT(speed, Key:list):
    A = Key[Key.index("A")+1]
    LEFT = Key[Key.index("LEFT")+1]
    if A[0] == True or LEFT[0] == True:
        if speed[0] > -XMAX:
            speed[0] -= XACCELERATION
        if speed[0] < -XMAX:
            speed[0] = -XMAX
    if A[0] == False and LEFT[0] == False:
        if speed[0] < 0:
            if speed[0] > XDECELERATION:
                speed[0] = 0
            else:
                speed[0] += XDECELERATION
    return [speed, "playerSpeed"]

def eventRIGHT(speed, Key):
    D = Key[Key.index("D")+1]
    RIGHT = Key[Key.index("RIGHT")+1]
    if D[0] == True or RIGHT[0] == True:
        if speed[0] < XMAX:
            speed[0] += XACCELERATION
        if speed[0] > XMAX:
            speed[0] = XMAX
    if D[0] == False and RIGHT[0] == False:
        if speed[0] > 0:
            if speed[0] < XDECELERATION:
                speed[0] = 0
            else:
                speed[0] -= XDECELERATION
    return [speed, "playerSpeed"]
def eventMOVEWITHMOUSE(pos, Mouse):
    MouseRight = Mouse[Mouse.index("MOUSERIGHT")+1]
    Mouse = Mouse[Mouse.index("MOUSE")+1]
    if MouseRight[0] == True:
        Mouse[0] = pygame.mouse.get_pos()
        pos[0] = (Mouse[1][0] - Mouse[0][0] + pos[0])
        pos[1] = (Mouse[1][1] - Mouse[0][1] + pos[1])
        Mouse[1] = Mouse[0]
def eventSPAWNCUBE(Key, Mouse, Cubes: list, mousePos, scroll, n, LH):
    O = Key[Key.index("O")+1]
    MouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    n = 0
    for cube in Cubes:
        if cube.extra_info == ["holding"]:
            n += 1
            cube.pos[0] = round(mousePos[0] + scroll[0] - (cube.size[0] /2))
            cube.pos[1] = round(mousePos[1] + scroll[1] - (cube.size[1] /2))
            if MouseLeft[0] == True:
                cube.extra_info = []
    if n <= 0:
        if O[0] == True:
            Cubes.append(objects.cube(mousePos[0] + scroll[0], mousePos[1] + scroll[1], 50, 50, extra_info=["holding"]))
            LH.objectWriter(Cubes)
    n = 0
    return Cubes


def eventDELETECUBE(Cubes: list, utils, LH):
    mouse = utils.getInfo("Mouse", "MOUSE")
    Del = utils.getInfo("Key", "DEL")
    i = 0
    for cube in Cubes:
        
        if collision.mouseCollision(mouse[0][0], mouse[0][1], cube.pos[0], cube.pos[1], cube.size[0], cube.size[1]) and Del[0] == True:
            del Cubes[i]
            LH.objectWriter(Cubes)
        i += 1 
def eventDRAGXSIZEONCUBE(Cubes: list, utils, LH, scroll):
    mouse = utils.getInfo("Mouse", "MOUSE")
    mouseLeft = utils.getInfo("Mouse", "MOUSELEFT")
    tolerance = 5
    
    for cube in Cubes:
        print(cube.extra_info)
        
        if collision.mouseCollision(mouse[0][0] + scroll[0], mouse[0][1] +  scroll[1], cube.pos[0] + cube.size[0] - tolerance, cube.pos[1], tolerance, cube.size[1]) == True and mouseLeft[0] == True:
            cube.extra_info = ["dragingRight"]   
        print(cube.extra_info)
        if mouseLeft[0] == False:
                cube.extra_info = [""]
        print(cube.extra_info)
        if cube.extra_info == "dragingRight":
            cube.size[0] = mouse[0][0] + scroll[0] - cube.pos[0]
            if cube.size[0] < tolerance:
                cube.size[0] = tolerance
            LH.objectWriter(Cubes)
        print(cube.extra_info)

def inputSaver(event, Key, Mouse):
    
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

    #mouse saver
    MouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    MouseRight = Mouse[Mouse.index("MOUSERIGHT")+1]
    MouseVar = Mouse[Mouse.index("MOUSE")+1]
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            MouseLeft[0] = True
            MouseVar[1] = pygame.mouse.get_pos()
        if event.button == 3:
            MouseRight[0] = True
            MouseVar[1] = pygame.mouse.get_pos()

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            MouseLeft[0] = False
        if event.button == 3:
            MouseRight[0] = False
 


def inputHandler(app):
    eventDOWN(app.user.speed, app.u.Key)
    eventUP(app.user.speed, app.u.Key) 
    eventLEFT(app.user.speed, app.u.Key)
    eventRIGHT(app.user.speed, app.u.Key)
    eventMOVEWITHMOUSE(app.user.pos, app.u.Mouse) 
    eventSPAWNCUBE(app.u.Key, app.u.Mouse, app.cubes, app.mousePos, app.scroll, app.n, app.lh)
    eventDELETECUBE(app.cubes, app.u, app.lh)
    eventDRAGXSIZEONCUBE(app.cubes, app.u, app.lh, app.scroll)
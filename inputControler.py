import pygame, objects
from pygame.locals import *

YACCELERATION = .1
YDECELERATION = .1
YMAX = 3
XACCELERATION = .1
XDECELERATION = .1
XMAX = 3


def eventDOWN(speed, Key):
    if Key[11][1] == True or Key[28][1] == True:
        if speed[1] < YMAX:
            speed[1] += YACCELERATION
        if speed[1] > YMAX:
            speed[1] = YMAX
    if Key[11][1] == False and Key[28][1] == False: 
        if speed[1] > 0:
            if speed[1] < YDECELERATION:
                speed[1] = 0
            else:
                speed[1] -= YDECELERATION
    return [speed, "playerSpeed"]

def eventUP(speed, Key):
    if Key[1][1] == True or Key[26][1] == True:
        if speed[1] > -YMAX:
            speed[1] -= YACCELERATION
        if speed[1] < -YMAX:
            speed[1] = -YMAX
    if Key[1][1] == False and Key[26][1] == False:
        if speed[1] < 0:
            if speed[1] > YDECELERATION:
                speed[1] = 0
            else:
                speed[1] += YDECELERATION
    return [speed, "playerSpeed"]

def eventLEFT(speed, Key):
    if Key[10][1] == True or Key[27][1] == True:
        if speed[0] > -XMAX:
            speed[0] -= XACCELERATION
        if speed[0] < -XMAX:
            speed[0] = -XMAX
    if Key[10][1] == False and Key[27][1] == False:
        if speed[0] < 0:
            if speed[0] > XDECELERATION:
                speed[0] = 0
            else:
                speed[0] += XDECELERATION
    return [speed, "playerSpeed"]

def eventRIGHT(speed, Key):
    if Key[12][1] == True or Key[29][1] == True:
        if speed[0] < XMAX:
            speed[0] += XACCELERATION
        if speed[0] > XMAX:
            speed[0] = XMAX
    if Key[12][1] == False and Key[29][1] == False:
        if speed[0] > 0:
            if speed[0] < XDECELERATION:
                speed[0] = 0
            else:
                speed[0] -= XDECELERATION
    return [speed, "playerSpeed"]
def eventMOVEWITHMOUSE(pos, Key):
    for i in Key:
        if i[0] == "MOUSERIGHT" and i[1] == True:
            for key in Key:
                if key[0] == "MOUSE":
                    key[1] = pygame.mouse.get_pos()
                    pos[0] = (key[2][0] - key[1][0] + pos[0])
                    pos[1] = (key[2][1] - key[1][1] + pos[1])
                    key[2] = key[1]
def eventSPAWNCUBE(Key, Cubes: list, mousePos, scroll, n):
    n = 0
    for cube in Cubes:
        if cube.extra_info == ["holding"]:
            n += 1
            cube.pos[0] = mousePos[0] + scroll[0] - (cube.size[0] /2)
            cube.pos[1] = mousePos[1] + scroll[1] - (cube.size[1] /2)
            for key in Key:
                if key[0] == "MOUSELEFT" and key[1] == True:
                    cube.extra_info = []
    if n <= 0:
        for i in Key:
            if i[0] == "O" and i[1] == True:
                Cubes.append(objects.cube(mousePos[0] + scroll[0], mousePos[1] + scroll[1], 50, 50, extra_info=["holding"]))
    return Cubes
    




def inputSaver(event, Key):
    
    #Keyboard saver
    if event.type == pygame.KEYDOWN: 
        for i in Key:
            if i[2] != "MOUSELEFT" or i[2] != "MOUSERIGHT":
                if event.key == i[2]:
                    i[1] = True

    if event.type == pygame.KEYUP:     
        for i in Key:
            if i[2] != "MOUSELEFT" or i[2] != "MOUSERIGHT":
                if event.key == i[2]:
                    i[1] = False

    #mouse saver
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            Key[30][1] = True
            Key[32][2] = pygame.mouse.get_pos()
        if event.button == 3:
            Key[31][1] = True

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            Key[30][1] = False
        if event.button == 3:
            Key[31][1] = False
 


def inputHandler(app):
    eventDOWN(app.user.speed, app.u.Key)
    eventUP(app.user.speed, app.u.Key) 
    eventLEFT(app.user.speed, app.u.Key)
    eventRIGHT(app.user.speed, app.u.Key)
    eventMOVEWITHMOUSE(app.user.pos, app.u.Key) 
    eventSPAWNCUBE(app.u.Key, app.cubes, app.mousePos, app.scroll, app.n)
import pygame
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
def eventMOVEWITHMOUSE(pos, mousepos, Key):
    for i in Key:
        if i[0] == "MOUSELEFT" and i[1] == True:
            




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
        if event.button == 2:
            Key[31][1] = True

    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:
            Key[30][1] = True
        if event.button == 2:
            Key[31][1] = True
 



def inputHandler(user, Key):
    eventDOWN(user.speed, Key)
    eventUP(user.speed, Key) 
    eventLEFT(user.speed, Key)
    eventRIGHT(user.speed, Key)
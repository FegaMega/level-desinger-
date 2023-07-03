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

def inputSaver(event, Key):
    if event.type == pygame.KEYDOWN: 
        
 #       if event.key == K_q:
 #           Key[0][1] == True
 #       if event.key == K_w:
 #           Key[1][1] == True
 #       if event.key == K_e:
 #           Key[2][1] == True
 #       if event.key == K_r:
 #           Key[3][1] == True
 #       if event.key == K_t:
 #           Key[4][1] == True
 #       if event.key == K_y:
 #           Key[5][1] == True
 #       if event.key == K_u:
 #           Key[6][1] == True
 #       if event.key == K_i:
 #           Key[7][1] == True
 #       if event.key == K_o:
 #           Key[8][1] == True
 #       if event.key == K_p:
 #           Key[9][1] == True
 #       if event.key == K_a:
 #           Key[10][1] == True
 #       if event.key == K_s:
 #           Key[11][1] == True
 #       if event.key == K_d:
 #           Key[12][1] == True
 #       if event.key == K_f:
 #           Key[13][1] == True
 #       if event.key == K_g:
 #           Key[14][1] == True
 #       if event.key == K_h:
 #           Key[15][1] == True
 #       if event.key == K_j:
 #           Key[16][1] == True
 #       if event.key == K_k:
 #           Key[17][1] == True
 #       if event.key == K_l:
 #           Key[18][1] == True
 #       if event.key == K_z:
 #           Key[19][1] == True
 #       if event.key == K_x:
 #           Key[20][1] == True
 #       if event.key == K_c:
 #           Key[21][1] == True
 #       if event.key == K_v:
 #           Key[22][1] == True
 #       if event.key == K_b:
 #           Key[23][1] == True
 #       if event.key == K_n:
 #           Key[24][1] == True
 #       if event.key == K_m:
 #           Key[25][1] == True
        for i in Key:
            if event.key == vars(("K_", str(i[0].lower()))):
                i[1] = True
        
 #      if event.key == K_s:
 #          Key[11][1] = True
 #      if event.key == K_w:
 #          Key[1][1] = True
 #      if event.key == K_a:
 #          Key[10][1] = True
 #      if event.key == K_d:
 #          Key[12][1] = True
 #      if event.key == K_DOWN:
 #          Key[28][1] = True
 #      if event.key == K_UP:
 #          Key[26][1] = True
 #      if event.key == K_LEFT:
 #          Key[27][1] = True
 #      if event.key == K_RIGHT:
 #          Key[29][1] = True
 #  if event.type == pygame.MOUSEBUTTONDOWN:
 #      if event.button == 1:
 #          Key[30][1] = True
 #      if event.button == 1:
 #          Key[31][1] = True

    if event.type == pygame.KEYUP:
        for i in Key:
            if event.key == vars(("K_", str(i[0].lower()))):
                i[1] = False
 
 
 #       if event.key == K_s:
 #          Key[11][1] = False
 #      if event.key == K_w:
 #          Key[1][1] = False
 #      if event.key == K_a:
 #          Key[10][1] = False
 #      if event.key == K_d:
 #          Key[12][1] = False
 #      if event.key == K_DOWN:
 #          Key[28][1] = False
 #      if event.key == K_UP:
 #          Key[26][1] = False
 #      if event.key == K_LEFT:
 #          Key[27][1] = False
 #      if event.key == K_RIGHT:
 #          Key[29][1] = False
def inputHandler(user, Key):
    eventDOWN(user.speed, Key)
    eventUP(user.speed, Key) 
    eventLEFT(user.speed, Key)
    eventRIGHT(user.speed, Key)
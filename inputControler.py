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
            Cubes.append(objects.cube(mousePos[0] + scroll[0], mousePos[1] + scroll[1], 50, 50))
            Cubes[len(Cubes)-1].extra_info = ["holding"]
            LH.objectWriter(Cubes)
    n = 0
    return Cubes


def eventDELETECUBE(Cubes: list, utils, LH):
    mouse = utils.getInfo("Mouse", "MOUSE", 1)
    Del = utils.getInfo("Key", "DEL", 1)
    i = 0
    for cube in Cubes:
        
        if collision.mouseCollision(mouse[0][0], mouse[0][1], cube.pos[0], cube.pos[1], cube.size[0], cube.size[1]) and Del[0] == True:
            del Cubes[i]
            LH.objectWriter(Cubes)
        i += 1 


def eventDRAGXSIZEONCUBE(Cubes: list, utils, scroll, Draging):
    mouse = utils.getInfo("Mouse", "MOUSE", 1)
    mouseLeft = utils.getInfo("Mouse", "MOUSELEFT", 1)
    outputDR = 0
    outputDRG = 0
    for cube in Cubes:
        if True == collision.mouseCollision(mouse[0][0] + scroll[0], mouse[0][1] + scroll[1], (cube.pos[0] + cube.size[0] - utils.tolerance), cube.pos[1], utils.tolerance, cube.size[1]):
            outputDRG = utils.getInfo(cube.extra_info, "drawRightGreen", 1)
            if outputDRG.__class__ != bool:
                cube.extra_info.append("drawRightGreen")
                cube.extra_info.append(True)
            else:
                cube.extra_info[cube.extra_info.index("drawRightGreen")+1] = True
            if mouseLeft[0] == True and Draging[0] == False and Draging[3] == cube or mouseLeft == True and Draging[0] == False and Draging[3] == 0:
                outputDR = utils.getInfo(cube.extra_info, "dragRight", 1)
                if outputDR.__class__ != bool:
                    cube.extra_info.append("dragRight")
                    cube.extra_info.append(True)
                
                else:
                    cube.extra_info[cube.extra_info.index("dragRight")+1] = True
                Draging[0] = True
                Draging[1] = cube    
        try:
            outputDRG = utils.getInfo(cube.extra_info, "drawRightGreen", 1)
        except:
            TypeError
            ValueError
            break
        try:
            outputDR = utils.getInfo(cube.extra_info, "dragRight", 1)
        except:
            TypeError
            ValueError
            break
        if mouseLeft[0] == False:
            try:
                cube.extra_info[cube.extra_info.index("dragRight")+1] = False
                Draging[0] = False
                Draging[1] = 0
            except:
                TypeError
                NameError
            if False == collision.mouseCollision(mouse[0][0] + scroll[0], mouse[0][1] + scroll[1], (cube.pos[0] + cube.size[0] - utils.tolerance), cube.pos[1], utils.tolerance, cube.size[1]):
                try:
                    cube.extra_info[cube.extra_info.index("drawRightGreen")+1] = False
                except:
                    TypeError
                    NameError
        try: 
            if outputDR.__class__ == bool and outputDR == True:
                cube.size[0] = mouse[0][0] + scroll[0] - cube.pos[0]
                if cube.size[0] < utils.tolerance:
                    cube.size[0] = utils.tolerance
        except:
            NameError
            ValueError
            TypeError

def eventDRAGYSIZEONCUBE(Cubes: list, utils, scroll, Draging):
    mouse = utils.getInfo("Mouse", "MOUSE", 1)
    mouseLeft = utils.getInfo("Mouse", "MOUSELEFT", 1)
    outputDD = 0
    outputDDG = 0
    for cube in Cubes:
        if True == collision.mouseCollision(mouse[0][0] + scroll[0], mouse[0][1] + scroll[1], cube.pos[0], cube.pos[1] + cube.size[1] - utils.tolerance, cube.size[0], utils.tolerance):
            outputDDG = utils.getInfo(cube.extra_info, "drawDownGreen", 1)
            if outputDDG.__class__ != bool:
                cube.extra_info.append("drawDownGreen")
                cube.extra_info.append(True)
            else:
                cube.extra_info[cube.extra_info.index("drawDownGreen")+1] = True
            if mouseLeft[0] == True and Draging[2] == False and Draging[1] == cube or mouseLeft == True and Draging[2] == False and Draging[1] == 0:
                outputDD = utils.getInfo(cube.extra_info, "dragDown", 1)
                if outputDD.__class__ != bool:
                    cube.extra_info.append("dragDown")
                    cube.extra_info.append(True)
                else:
                    cube.extra_info[cube.extra_info.index("dragDown")+1] = True
                Draging[2] = True
                Draging[3] = cube
        try:
            outputDDG = utils.getInfo(cube.extra_info, "drawDownGreen", 1)
        except:
            TypeError
            ValueError
            break
        try:
            outputDD= utils.getInfo(cube.extra_info, "dragDown", 1)
        except:
            TypeError
            ValueError
            break
        if mouseLeft[0] == False:
            try:
                cube.extra_info[cube.extra_info.index("dragDown")+1] = False
                Draging[2] = False
                Draging[3] = 0
            except:
                TypeError
                NameError
            if False == collision.mouseCollision(mouse[0][0] + scroll[0], mouse[0][1] + scroll[1], cube.pos[0], cube.pos[1] + cube.size[1] - utils.tolerance, cube.size[0], utils.tolerance):
                try:
                    cube.extra_info[cube.extra_info.index("drawDownGreen")+1] = False
                except:
                    TypeError
                    NameError
        try: 
            if outputDD.__class__ == bool and outputDD == True:
                cube.size[1] = mouse[0][1] + scroll[1] - cube.pos[1]
                if cube.size[1] < utils.tolerance:
                    cube.size[1] = utils.tolerance
        except:
            NameError
            ValueError
            TypeError
        



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
    eventDRAGXSIZEONCUBE(app.cubes, app.u, app.scroll, app.draging)
    eventDRAGYSIZEONCUBE(app.cubes, app.u, app.scroll, app.draging)
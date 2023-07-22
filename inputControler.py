import pygame, objects, collision
from pygame.locals import *

YACCELERATION = .1
YDECELERATION = .1
YMAX = 3
XACCELERATION = .1
XDECELERATION = .1
XMAX = 3

def eventDOWN(rANDwKey, rANDwSpeed):
    speed = rANDwSpeed(0, "r")
    Key = rANDwKey(0, "r")   
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

def eventUP(rANDwKey, rANDwSpeed):
    speed = rANDwSpeed(0, "r")
    Key = rANDwKey(0, "r")   
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

def eventLEFT(rANDwKey, rANDwSpeed):
    speed = rANDwSpeed(0, "r")
    Key = rANDwKey(0, "r")   
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

def eventRIGHT(rANDwKey, rANDwSpeed):
    speed = rANDwSpeed(0, "r")
    Key = rANDwKey(0, "r")   
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
def eventMOVEWITHMOUSE(rANDwPos, rANDwMouse):
    mouse = rANDwMouse(0, "r")
    MouseRight = mouse[mouse.index("MOUSERIGHT")+1]
    Mouse = mouse[mouse.index("MOUSE")+1]
    pos = rANDwPos(0, "r")
    if MouseRight[0] == True:
        Mouse[0] = pygame.mouse.get_pos()
        pos[0] = (Mouse[1][0] - Mouse[0][0] + pos[0])
        pos[1] = (Mouse[1][1] - Mouse[0][1] + pos[1])
        Mouse[1] = Mouse[0]
def eventSPAWNCUBE(rANDwCubes, rANDwMouse, rANDwKey, rANDwscroll, LH):
    Cubes = rANDwCubes(0, "r")
    scroll = rANDwscroll(0, "r")
    Mouse = rANDwMouse(0, "r")
    MouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    mouse = Mouse[Mouse.index("MOUSE")+1][0]
    Key = rANDwKey(0, "r")
    O = Key[Key.index("O")+1]
    n = 0
    for cube in Cubes:
        if cube.extra_info == ["holding"]:
            n += 1
            cube.pos[0] = round(mouse[0] + scroll[0] - (cube.size[0] /2))
            cube.pos[1] = round(mouse[1] + scroll[1] - (cube.size[1] /2))
            if MouseLeft[0] == True:
                cube.extra_info = []
    if n <= 0:
        if O[0] == True:
            Cubes.append(objects.cube(mouse[0] + scroll[0], mouse[1] + scroll[1], 50, 50))
            Cubes[len(Cubes)-1].extra_info = ["holding"]
            LH.objectWriter(Cubes)
    n = 0
    return Cubes


def eventDELETECUBE(rANDwCubes, rANDwscroll, utils, LH):
    Cubes = rANDwCubes(0, "r")
    Mouse = utils.rANDwMouse(0, "r")
    mouse = Mouse[Mouse.index("MOUSE")+1][0]
    scroll = rANDwscroll(0, "r")
    Key = utils.rANDwKey(0, "r")
    Del = Key[Key.index("DEL")+1]
    i = 0
    for cube in Cubes:
        
        if collision.mouseCollision(mouse[0] + scroll[0], mouse[1] + scroll[1], cube.pos[0], cube.pos[1], cube.size[0], cube.size[1]) and Del[0] == True:
            del Cubes[i]
            LH.objectWriter(Cubes)
        i += 1 


def eventDRAGXSIZEONCUBE(rANDwCubes, utils, rANDwscroll, rANDwMoving, rANDwDraging, rANDwVisualMisc):
    Cubes = rANDwCubes(0, "r")
    scroll = rANDwscroll(0, "r")
    moving = rANDwMoving(0, "r")
    draging = rANDwDraging(0, "r")
    Mouse = utils.rANDwMouse(0, "r")
    mouse = Mouse[Mouse.index("MOUSE")+1][0]
    mouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    VisMisc = rANDwVisualMisc(0, "r")
    outputDR = 0
    outputDRG = 0
    for cube in Cubes:
        extra_info = cube.rANDwExtra_info(0, "r")

        try:
            outputDRG = extra_info.index("drawRightGreen")+1
        except:
            ValueError
            TypeError
            extra_info.append("drawRightGreen")
            extra_info.append(False)
            outputDRG = extra_info.index("drawRightGreen")+1
        try:            
            outputDR = extra_info.index("dragRight")+1
        except:
            ValueError
            TypeError
            extra_info.append("dragRight")
            extra_info.append(False)
            outputDR = extra_info.index("dragRight")+1
            
        if True == collision.mouseCollision(mouse[0] + scroll[0], mouse[1] + scroll[1], (cube.pos[0] + cube.size[0] - utils.tolerance), cube.pos[1], utils.tolerance, cube.size[1]) and moving == False:
            if draging[0] == False or draging[0] == True and draging[1] == cube:
                extra_info[outputDRG] = True
                if mouseLeft[0] == True:
                    extra_info[outputDR] = True
                    draging[0] = True 
                    draging[1] = cube

        if mouseLeft[0] == False:
            extra_info[outputDR] = False
            draging[0] = False
            draging[1] = 0
            if False == collision.mouseCollision(mouse[0] + scroll[0], mouse[1] + scroll[1], (cube.pos[0] + cube.size[0] - utils.tolerance), cube.pos[1], utils.tolerance, cube.size[1]):
                extra_info[outputDRG] = False


        if extra_info[outputDR] == True:
            cube.size[0] = mouse[0] + scroll[0] - cube.pos[0]
            if cube.size[0] < utils.tolerance:
                cube.size[0] = utils.tolerance
        if extra_info[outputDRG] == True:
            VisMisc.append(objects.cube(cube.pos[0] + cube.size[0] - utils.tolerance, cube.pos[1], utils.tolerance, cube.size[1]))
        cube.rANDwExtra_info(extra_info, "w")
        rANDwVisualMisc(VisMisc, "w")
        print(cube.extra_info)
    rANDwDraging(draging, "w")
    rANDwMoving(moving, "w")

def eventDRAGYSIZEONCUBE(rANDwCubes, utils, rANDwscroll, rANDwMoving, rANDwDraging):
    Cubes = rANDwCubes(0, "r")
    scroll = rANDwscroll(0, "r")
    Mouse = utils.rANDwMouse(0, "r")
    mouse = Mouse[Mouse.index("MOUSE")+1][0]
    mouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    moving = rANDwMoving(0, "r")
    draging = rANDwDraging(0, "r")
    outputDD = 0
    outputDDG = 0
    for cube in Cubes:
        if True == collision.mouseCollision(mouse[0] + scroll[0], mouse[1] + scroll[1], cube.pos[0], cube.pos[1] + cube.size[1] - utils.tolerance, cube.size[0], utils.tolerance) and moving == False:
            if draging[0] == False or draging[0] == True and draging[1] == cube:
                outputDDG = utils.getInfo(cube.extra_info, "drawDownGreen", 1)
                if outputDDG.__class__ != bool:
                    cube.extra_info.append("drawDownGreen")
                    cube.extra_info.append(True)
                else:
                    cube.extra_info[cube.extra_info.index("drawDownGreen")+1] = True
                if mouseLeft[0] == True:
                    outputDD = utils.getInfo(cube.extra_info, "dragDown", 1)
                    if outputDD.__class__ != bool:
                        cube.extra_info.append("dragDown")
                        cube.extra_info.append(True)
                    else:
                        cube.extra_info[cube.extra_info.index("dragDown")+1] = True
                    draging[0] = True
                    draging[1] = cube
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
                draging[0] = False
                draging[1] = 0
            except:
                TypeError
                NameError
            if False == collision.mouseCollision(mouse[0] + scroll[0], mouse[1] + scroll[1], cube.pos[0], cube.pos[1] + cube.size[1] - utils.tolerance, cube.size[0], utils.tolerance):
                try:
                    cube.extra_info[cube.extra_info.index("drawDownGreen")+1] = False
                except:
                    TypeError
                    NameError
        try: 
            if outputDD.__class__ == bool and outputDD == True:
                cube.size[1] = mouse[1] + scroll[1] - cube.pos[1]
                if cube.size[1] < utils.tolerance:
                    cube.size[1] = utils.tolerance
        except:
            NameError
            ValueError
            TypeError
    rANDwDraging(draging, "w")
    rANDwMoving(moving, "w")
        
def eventMOVECUBE(rANDwCubes, utils, rANDwscroll, rANDwMoving, rANDwDraging):
    Cubes = rANDwCubes(0, "r")
    scroll = rANDwscroll(0, "r")
    moving = rANDwMoving(0, "r")
    draging = rANDwDraging(0, "r")
    Mouse = utils.rANDwMouse(0, "r")
    mouse = Mouse[Mouse.index("MOUSE")+1][0]
    mouseLeft = Mouse[Mouse.index("MOUSELEFT")+1]
    for cube in Cubes:
        if mouseLeft[0] == True and draging[0] == False and moving == False and True == collision.mouseCollision(mouse[0]+scroll[0], mouse[1]+scroll[1], cube.pos[0], cube.pos[1], cube.size[0], cube.size[1]):
            moving = True
            cube.extra_info.append("holding")
        for info in cube.extra_info:
            if info == "holding":
                cube.pos[0] = round(mouse[0] + scroll[0] - (cube.size[0] /2))
                cube.pos[1] = round(mouse[1] + scroll[1] - (cube.size[1] /2))
                if mouseLeft[0] == False:
                    moving = False
                    del cube.extra_info[cube.extra_info.index("holding")]
    rANDwDraging(draging, "w")
    rANDwMoving(moving, "w")

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
    rANDwMouse(Mouse, "w") 


def inputHandler(app):
    eventDOWN(app.u.rANDwKey, app.user.rANDwSpeed)
    eventUP(app.u.rANDwKey, app.user.rANDwSpeed) 
    eventLEFT(app.u.rANDwKey, app.user.rANDwSpeed)
    eventRIGHT(app.u.rANDwKey, app.user.rANDwSpeed)
    eventMOVEWITHMOUSE(app.user.rANDwPos, app.u.rANDwMouse) 
    eventSPAWNCUBE(app.rANDwCubes, app.u.rANDwMouse, app.u.rANDwKey, app.rANDwScroll, app.lh)
    eventDELETECUBE(app.rANDwCubes, app.rANDwScroll, app.u, app.lh, )
    eventDRAGXSIZEONCUBE(app.rANDwCubes, app.u, app.rANDwScroll, app.rANDwMoving, app.rANDwDraging, app.rANDwVisualMisc)
    eventDRAGYSIZEONCUBE(app.rANDwCubes, app.u, app.rANDwScroll, app.rANDwMoving, app.rANDwDraging)
    eventMOVECUBE(app.rANDwCubes, app.u, app.rANDwScroll, app.rANDwMoving, app.rANDwDraging)
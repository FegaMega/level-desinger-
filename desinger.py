import pygame, sys
import json, utils, collision, objects, camera
from pygame.locals import *
from JH import JsonHandler
import settingsfolder
import inputControler
import levelhandler
from buttonControler import button





def ArrayOfStrToInt(str):
        newstr = []
        for i in str:
            newstr.append(int(i))
        return newstr




class Designer:
    def __init__(self):
        self.u = utils.utils()
        self.user = camera.camera(self.u)
        self.jh = JsonHandler()
        self.sh = settingsfolder.settingshandeler(self.u)
        self.iC = inputControler
        self.lh = levelhandler.levelhandeler("data/json/level.json")
        self.Clock = pygame.time.Clock()
        self.deltaTime = [0, 0]
        self.r = True
        self.scroll = [0, 0]
        self.cubes = []
        self.buttons = [button([self.u.screenSize[0]-20, 20], [184, 44], "data/img/object2.png", "object", 0), button([self.u.screenSize[0]-20, 20], [184, 44], "data/img/speed.png", "speed", 1)]
        self.lh.objectReader(self.cubes)
        self.mousePos = [0, 0]
        self.draging = [False, 0]
        self.moving = False
        self.VisualMisc = []
        self.holding_newCube = False

    def deltaTimeUppdate(self):
        self.deltaTime[0] = pygame.time.get_ticks() - self.deltaTime[1]
        self.deltaTime[1] = pygame.time.get_ticks()
    def rANDwMoving(self, moving, rORw:str):
        if rORw == "w":
            self.moving = moving
        elif rORw == "r":
            return self.moving
    def rANDwHolding_newCube(self, holding_newCube, rORw:str):
        if rORw == "w":
            self.holding_newCube = holding_newCube
        elif rORw == "r":
            return self.holding_newCube
    def rANDwMousePos(self, mousePos, rORw:str):
        if rORw == "w":
            self.mousePos = mousePos
        elif rORw == "r":
            return self.mousePos
    def rANDwDraging(self, draging, rORw:str):
        if rORw == "w":
            self.draging = draging
        elif rORw == "r":
            return self.draging
    def rANDwScroll(self, scroll, rORw:str):
        if rORw == "w":
            self.scroll = scroll
        elif rORw == "r":
            return self.scroll
    def rANDwCubes(self, cubes, rORw:str):
        if rORw == "w":
            self.cubes = cubes
        elif rORw == "r":
            return self.cubes
    def rANDwButtons(self, button, rORw:str):
        if rORw == "w":
            self.buttons = button
        elif rORw == "r":
            return self.buttons
    def rANDwVisualMisc(self, VisualMisc, rORw:str):
        if rORw == "w":
            self.VisualMisc = VisualMisc
        elif rORw == "r":
            return self.VisualMisc
    def drawCubes(self):
        for i in self.cubes:
            i.draw(self.rANDwScroll)
    def drawButtons(self):
        for button in self.buttons:
            button.draw(self.u.rANDwScreen, self.u.rANDwScreenSize)
    def drawMisc(self):
        for i in self.VisualMisc:
            i.draw(self.rANDwScroll)
    def mousePosUpdate(self):
        mouse = self.u.rANDwMouse(0, "r")
        mouse[mouse.index("MOUSE")+1][0] = pygame.mouse.get_pos()
        self.u.rANDwMouse(mouse, "w")
        return pygame.mouse.get_pos()
    def scrollFunc(self):
        self.scroll[0] += (self.user.pos[0] + self.user.size[0]/2 - self.scroll[0] - self.u.screenSize[0] / 2) / 10
        self.scroll[1] += (self.user.pos[1] + self.user.size[0]/2 - self.scroll[1] - self.u.screenSize[1] / 2) / 10

    

def Designermain(MIXER) -> int:
    pygame.init()
    app = Designer()

    # spel loopen

    while app.r == True:
        app.deltaTimeUppdate()
        app.u.screen.fill((146, 244, 255)) # Dubbelbuffer (ej visad bild)
        #Updaterar mus positionen
        app.mousePos = app.mousePosUpdate()
        # Töm (hantera) eventkön
        for event in pygame.event.get():
            # Avsluta kod
            if event.type == QUIT:
                app.r = False
            else:
                app.iC.inputSaver(event, app.u.rANDwKey, app.u.rANDwMouse)
        app.iC.inputHandler(app)
            
        # Ritar object
        app.drawCubes()
        app.user.move(app.deltaTime[0])
        app.scrollFunc()
        app.drawButtons()
        # uppdaterar skärmen
        pygame.display.update()
        #spelar musik
        MIXER.RunMusic()
        # 60 Fps limit
        pygame.time.Clock().tick(60)
    app.lh.objectWriter(app.cubes)
    return 1



if __name__ == '__main__':
    sys.exit(Designermain())
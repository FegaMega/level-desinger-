import pygame, json, sys, utils, collision, objects, camera
from pygame.locals import *
from JH import JsonHandler
import settingsfolder
import inputControler
import levelhandler






def ArrayOfStrToInt(str):
        newstr = []
        for i in str:
            newstr.append(int(i))
        return newstr




class designer:
    def __init__(self):
        self.user = camera.camera()
        self.jh = JsonHandler()
        self.u = utils.utils()
        self.sh = settingsfolder.settingshandeler()
        self.iC = inputControler
        self.lh = levelhandler.levelhandeler("level.json")
        self.r = True
        self.scroll = [0, 0]
        self.cubes = []
        self.lh.objectReader(self.cubes)
        self.mousePos = [0, 0]
        self.n: int = 0
        self.draging = [False, 0]
        self.moving = [False, 0]
    def drawCubes(self):
        for i in self.cubes:
            i.draw(self.scroll)
    def mousePosUpdate(self):
        self.u.changeInfo("Mouse", "MOUSE", 0, 1, pygame.mouse.get_pos())
        return pygame.mouse.get_pos()
    def scrollFunc(self):
        self.scroll[0] += (self.user.pos[0] + self.user.size[0]/2 - self.scroll[0] - self.u.screenSize[0] / 2) / 10
        self.scroll[1] += (self.user.pos[1] + self.user.size[0]/2 - self.scroll[1] - self.u.screenSize[1] / 2) / 10
    

def main() -> int:
    pygame.init()
    app = designer()

    # spel loopen

    while app.r == True:
        app.mousePos = app.mousePosUpdate()
        app.u.screen.fill((146, 244, 255)) # Dubbelbuffer (ej visad bild)
        #Updaterar mus positionen
        app.mousePos = app.mousePosUpdate()
        # Töm (hantera) eventkön
        for event in pygame.event.get():
            # Avsluta kod
            if event.type == QUIT:
                app.r = False
            else:
                app.iC.inputSaver(event, app.u.Key, app.u.Mouse)
        app.iC.inputHandler(app)
            
        # Ritar object
        app.drawCubes()
        app.user.move()
        app.scrollFunc()
        # uppdaterar skärmen
        
        pygame.display.update()
        # 60 Fps limit
        pygame.time.Clock().tick(60)
    app.lh.objectWriter(app.cubes)
    return 0



if __name__ == '__main__':
    sys.exit(main())
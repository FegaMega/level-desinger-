import pygame, json, sys, utils, collision, objects, camera
from utils import main
from pygame.locals import *
from JH import JsonHandler
import settingsfolder
import inputControler






def ArrayOfStrToInt(str):
        newstr = []
        for i in str:
            newstr.append(int(i))
        return newstr




class designer:
    def __init__(self):
        self.user = camera.camera()
        self.jh = JsonHandler()
        self.u = utils.main()
        self.sh = settingsfolder.settingshandeler()
        self.iC = inputControler
        self.r = True
        self.scroll = [0, 0]
        self.cubes = [objects.cube(self.u.screenSize[0]/2, self.u.screenSize[1]/2, 50, 50)]
        self.mousePos = [0, 0]
    def drawCubes(self):
        for i in self.cubes:
            i.draw(self.scroll)
    def mousePosUpdate(self):
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
        app.u.screen.fill((146, 244, 255))
        # Töm event kön
        for event in pygame.event.get():
            # Quit kod
            if event.type == QUIT:
                app.r = False
            app.iC.inputSaver(event, app.u.Key)
        app.iC.inputHandler(app.user, app.u.Key)
            
        #Ritar object
        app.drawCubes()
        app.user.move()
        app.scrollFunc()
        # uppdaterar skärmen
        pygame.display.update()
        #Updaterar mus positionen
        print(app.user.speed)
        # 60 Fps limmit
        pygame.time.Clock().tick(60)
    return 0



if __name__ == '__main__':
    sys.exit(main())
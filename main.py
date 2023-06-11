import pygame, json, sys, utils, collision, objects, camera
from utils import main
from pygame.locals import *
from JH import JsonHandler
import settingsfolder
import inputControler


USER = camera.camera()
JH = JsonHandler()
U = utils.main()
SH = settingsfolder.settingshandeler()



def ArrayOfStrToInt(str):
        newstr = []
        for i in str:
            newstr.append(int(i))
        return newstr


class designer:
    def __init__(self):
        self.r = True
        self.scroll = [0, 0]
        self.cubes = [objects.cube(U.screenSize[0]/2, U.screenSize[1]/2, 50, 50)]
        self.mousePos = [0, 0]
    def drawCubes(self):
        for i in self.cubes:
            i.draw(self.scroll)
    def mousePosUpdate(self):
        return pygame.mouse.get_pos()
    def scrollFunc(self):
        self.scroll[0] += (USER.x - self.scroll[0] - U.screenSize[0] / 2) / 10
        self.scroll[1] += (USER.y - self.scroll[1] - U.screenSize[1] / 2) / 10
        

def main() -> int:
    pygame.init()
    app = designer()

    # spel loopen

    while app.r == True:
        app.mousePos = app.mousePosUpdate()
        U.screen.fill((146, 244, 255))
        # Töm event kön
        for event in pygame.event.get():
            # Quit kod
            if event.type == QUIT:
                app.r = False
            inputControler.inputHandler(USER, event)
        #Ritar object
        app.drawCubes()
        USER.move()
        USER.draw(app.scroll)
        # uppdaterar skärmen
        pygame.display.update()
        #Updaterar mus positionen
        
        
        # 60 Fps limmit
        pygame.time.Clock().tick(60)
    return 0



if __name__ == '__main__':
    sys.exit(main())
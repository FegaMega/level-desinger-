import pygame
from desinger import Designermain
from game import gamemain
from buttonControler import button
from pygame.locals import *
import utils 
from JH import JsonHandler
import settingsfolder
import collision
import sys
from music import mixer
class Start:
    def __init__(self):
        self.u = utils.utils()
        self.jh = JsonHandler()
        self.sh = settingsfolder.settingshandeler(self.u)
        self.buttons = [button([self.u.screenSize[0]/4 + 75, (self.u.screenSize[1]/4)*3], [100, 50], "data/img/sprite-0001.png", "game", 0), button([self.u.screenSize[0]/4*3 + 75, (self.u.screenSize[1]/4)*3], [100, 50], "data/img/sprite-0002.png", "desinger", False)]
        self.r = True
        self.mousePos = [0, 0]
        self.MouseLeft = False
        
        self.FPS = self.sh.readSetting("FPS")[0]
        
    def drawButtons(self):
        for i in self.buttons:
            i.draw(self.u.rANDwScreen, self.u.rANDwScreenSize)


def main() -> int:
    pygame.init()
    app = Start()

    # spel loopen

    while app.r == True:
        app.u.screen.fill((146, 244, 255)) # Dubbelbuffer (ej visad bild)
        #Updaterar mus positionen
        app.mousePos = pygame.mouse.get_pos()
        # Töm (hantera) eventkön
        for event in pygame.event.get():
            # Avsluta kod
            if event.type == QUIT:
                app.r = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        app.MouseLeft = True
        for button in app.buttons:
            if collision.mouseCollision(app.mousePos[0], app.mousePos[1], button.pos[0], button.pos[1], button.size[0], button.size[1]) == True and app.MouseLeft == True:
                return str(button.type)
        # Ritar object
        app.drawButtons()
        #spelar musik

        # uppdaterar skärmen
        pygame.display.update()

        # 60 Fps limit
        pygame.time.Clock().tick(app.FPS)
        app.MouseLeft = False
    return 0

if __name__ == "__main__":
    i = True
    music_lib = ["data/music/Cipher_BGM.flac", "data/music/Aloft_BGM.flac", "data/music/lemmino-nocturnal.flac"]
    Mixer = mixer(music_lib)
    while i == True:
        r = main()
        if r == "game":
            gamemain(Mixer)
        if r == "desinger":
            Designermain(Mixer)
        if r == 0:
            sys.exit() 
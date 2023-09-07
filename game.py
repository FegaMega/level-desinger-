import pygame, sys
import json, utils, collision, objects, camera
from pygame.locals import *
from JH import JsonHandler
import settingsfolder
import inputControler2
import levelhandler
from music import mixer
from buttonControler import button
import pistol

class Game:
    def __init__(self):
        self.r = True
        self.u = utils.utils()
        self.music_lib = ["data/music/Cipher_BGM.flac", "data/music/Aloft_BGM.flac", "data/music/lemmino-nocturnal.flac"]
        self.m = mixer(self.music_lib)
        self.user = camera.camera(self.u)
        self.jh = JsonHandler()
        self.sh = settingsfolder.settingshandeler(self.u)
        self.iC = inputControler2
        self.lh = levelhandler.levelhandeler("data/json/level.json")
        self.bullets = []
        self.gun
def main():
    pygame.init()
    game = Game()

    # spel loopen

    while game.r == True:
        game.u.screen.fill((146, 244, 255)) # Dubbelbuffer (ej visad bild)
        #Updaterar mus positionen
        # Töm (hantera) eventkön
        for event in pygame.event.get():
            # Avsluta kod
            if event.type == QUIT:
                game.r = False
            else:
                game.iC.inputSaver(event, game.u.rANDwKey, game.u.rANDwMouse)
        game.iC.inputHandler(game)
            
        # Ritar object
        game.drawCubes()
        game.user.move()
        game.scrollFunc()
        game.drawButtons()
        #spelar musik
        game.m.RunMusic()
        # uppdaterar skärmen
        pygame.display.update()

        # 60 Fps limit
        pygame.time.Clock().tick(60)
    game.lh.objectWriter(game.cubes)
    return 0
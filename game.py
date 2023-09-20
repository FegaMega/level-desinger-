import pygame, sys
import json, utils, collision, objects, camera
from pygame.locals import *
from JH import JsonHandler
import settingsfolder
import inputControlerGame
import levelhandler
from music import mixer
from buttonControler import button
import player
import pistol
from portals import portal
from speed import speed
from tunnels import tunnel
from Extra_jump import extra_jump
from Finish import finish
from bullet import bullet
import math

class Game:
    def __init__(self):
        self.r = True
        self.player = player.Player()
        self.u = utils.utils()
        self.gun = pistol.Pistol(self.player.pos[0], self.player.pos[1], 90)
        self.music_lib = ["data/music/Cipher_BGM.flac", "data/music/Aloft_BGM.flac", "data/music/lemmino-nocturnal.flac"]
        self.m = mixer(self.music_lib)
        self.user = camera.camera(self.u)
        self.jh = JsonHandler()
        self.sh = settingsfolder.settingshandeler(self.u)
        self.iC = inputControlerGame
        self.lh = levelhandler.levelhandeler("data/json/level.json")
        self.c = collision
        self.bullets = []
        self.gun = pistol.Pistol(0, 0, 90)
        self.scroll = [0, 0]
        self.Level = []
        self.lh.objectReader(self.Level)
        self.FONT = pygame.font.SysFont("Helvetica-bold", 50)
    def scrollFunc(self):
        self.scroll[0] += (self.player.pos[0] - self.scroll[0] - self.u.screenSize[0] / 2) / 10
        self.scroll[1] += (self.player.pos[1] - self.scroll[1] - self.u.screenSize[1] / 2) / 10
#        if self.scroll[1] > 0:
#           self.scroll[1] = 0

    def rANDwScroll(self, scroll, rORw:str):
        if rORw == "w":
            self.scroll = scroll
        elif rORw == "r":
            return self.scroll
        
    def drawCubes(self):
        # Ritar objekten i game.Level
        for Object in self.Level:
            Object.draw(self.rANDwScroll)
    
    def rANDwBullets(self, bullets, rORw:str):
        if rORw == "w":
            self.bullets = bullets
        elif rORw == "r":
            return self.bullets

    def golvCheck(self):
        # kollar om spelaren är under kamerans botten
        if self.player.pos[1] >= self.u.screenSize[1] - self.player.size[1]:
            self.player.pos[1] = self.u.screenSize[1] - self.player.size[1]
            self.player.on_floor = True
        else:
            # Gravitation
            # säger att spelaren inte är på golvet
            self.player.speed[1] += 0.4 / 60
            self.player.on_floor = False

            
    def portalKollision(self,object):
        if self.c.rectCollision(object.posR[0], object.posR[1], object.sizeR[0], object.sizeR[1], self.player.pos[0], self.player.pos[1], self.player.size[0], self.player.size[1]):
            if self.TPallow == True:
                self.player.pos[0] = object.posB[0]
                self.player.pos[1] = object.posB[1]
                self.TPallow = False
        elif self.c.rectCollision(object.posB[0], object.posB[1], object.sizeB[0], object.sizeB[1], self.player.pos[0], self.player.pos[1], self.player.size[0], self.player.size[1]):
            if self.TPallow == True:
                self.player.pos[0] = object.posR[0]
                self.player.pos[1] = object.posR[1]
                self.TPallow = False
        else:
            self.TPallow = True



    def collektebleCollekted(self, object):
        # Kollar om det är en extra_jump
        if object.__class__ == extra_jump:
            self.player.max_jumps += 1
            # tar bort extra_jump saken
            self.Level.remove(object)
        # Kollar om det är en extra_jump
        if object.__class__ == speed:
            self.player.max_speed += .1
            # tar bort extra_jump saken
            self.Level.remove(object)
    


    def finished(self, object):
        if object.__class__ == finish:
            self.r = False



    def TunnelKollision(self, line, object):
        # Kollar ifall spelaren är på/under tunneln eller om den är i
        if line[4] == "right" or line[4] == "left":
            self.player.in_tunnel = True
        if self.player.in_tunnel == False:
            if line[4] == "down":
                self.player.pos[1] = object.pos[1] - self.player.size[1]
                self.player.yspeed = 0
                self.player.on_floor = True
            elif line[4] == "up":
                self.player.pos[1] = object.pos[1] + object.size[1]
                self.player.yspeed = 0



    def vanligaObjektsKollision(self, line, object):
        self.player.in_tunnel = False
        if line[4] == "right":
            self.player.pos[0] = object.pos[0] - self.player.size[0]
            self.player.xspeed = 0
        elif line[4] == "left":
            self.player.pos[0] = object.pos[0] + object.size[0]
            self.player.xspeed = 0
        elif line[4] == "down":
            self.player.pos[1] = object.pos[1] - self.player.size[1]
            self.player.yspeed = 0
            self.player.on_floor = True
        elif line[4] == "up":
            self.player.pos[1] = object.pos[1] + object.size[1]
            self.player.yspeed = 0



    def linjeKollisiomMedObjekt(self, object):
        for line in self.player.collision_lines:
            if self.c.rectCollision(line[0], line[1], line[2], line[3], object.pos[0], object.pos[1], object.size[0], object.size[1]):
                # vanliga objekt
                if object.__class__ != tunnel:
                    self.vanligaObjektsKollision(line, object)
                else:
                    self.TunnelKollision(line, object)
                if line[4] == "down":
                    if self.player.speed[1] > 0:
                        self.player.speed[1] = 0
                    self.player.on_floor = True
                if line[4] == "up":
                    if self.player.speed[1] < 0:
                        self.player.speed[1] = 0



    def kollision(self):
        # sätter player.in_tunnel av för collision loopen
        self.player.in_tunnel = False
        for i in range(9):
            # Rör spelaren
            self.player.movement()
            # kollar om spelaren är under kamerans botten
            self.golvCheck()
            # objekt collision loopen
            for object in self.Level:
                # kollar om det är en portal (de är speciella)
                if object.__class__ == portal:
                    self.portalKollision(object)
                # vanliga objekts kod
                else:
                    # Kollar om spelaren är inuti objektet
                    if self.c.rectCollision(object.pos[0], object.pos[1], object.size[0], object.size[1], self.player.pos[0], self.player.pos[1], self.player.size[0], self.player.size[1]):
                        if object.__class__ == extra_jump or object.__class__ == speed:
                            self.collektebleCollekted(object)
                        elif object.__class__ == finish:
                            self.finished(object)
                        else:
                            # Kollar vilken sida som nuddade objektet med linjer på spelaren
                            self.linjeKollisiomMedObjekt(object)
                # lägger till ett så att jag vet att jag är i nästa objekt i listan game.Level
        # resetar mina hopp ifall jag är på marken
        if self.player.on_floor == True:
            self.player.jumps = self.player.max_jumps



    def roteraPistol(self):   
        if self.gun.rotateleft == True:
            self.gun.angle -= 2
        if self.gun.rotateright == True:
            self.gun.angle += 2
        self.gun.rot() 



    def centreraPistol(self):
        # flyttar vapnet till spelaren
        self.gun.pos[0] = self.player.pos[0] + 10
        self.gun.pos[1] = self.player.pos[1] + 20
        


    def ritaSpelare(self):
        # ritar spelaren
        self.player.draw(self.scroll[0], self.scroll[1], self.u.screen)



    def bulletPortalKollision(self, Object, Bullet):
        if self.c.rectCollision(Object.xB, Object.yB, Object.xsizeB, Object.ysizeB, Bullet.pos[0], Bullet.pos[1], Bullet.size[0], Bullet.size[1]) == True:
            if Bullet.TPallow == True:
                Bullet.pos[0] = Object.xR + (Object.xB - Bullet.pos[0])
                Bullet.pos[1] = Object.yR + (Object.yB - Bullet.pos[1])
                Bullet.TPallow = False
        elif self.c.rectCollision(Object.xR, Object.yR, Object.xsizeR, Object.ysizeR, Bullet.pos[0], Bullet.pos[1], Bullet.size[0], Bullet.size[1]) == True:
            if Bullet.TPallow == True:
                Bullet.pos[0] = Object.xB + (Object.xR - Bullet.pos[0])
                Bullet.pos[1] = Object.yB + (Object.yR - Bullet.pos[1])

                Bullet.TPallow = False
        else:
            Bullet.TPallow = True



    def bulletNormalKollision(self, Object, Bullet):
        if self.c.rectCollision(Object.pos[0], Object.pos[1], Object.size[0], Object.size[1], Bullet.pos[0], Bullet.pos[1], Bullet.size[0], Bullet.size[1]) == True:
            self.bullets.remove(Bullet)



    def bulletCollectebleKollision(self, Object, Bullet):
        if self.c.rectCollision(Object.pos[0], Object.pos[1], Object.size[0], Object.size[1], Bullet.pos[0], Bullet.pos[1], Bullet.size[0], Bullet.size[1]) == True:
            self.collektebleCollekted(Object)
            self.Level.remove(Object)



    def bulletKollision(self, Object, Bullet):
        if Object.__class__ == portal:
            self.bulletPortalKollision(Object, Bullet)
        elif Object.__class__ == extra_jump:
            self.bulletCollectebleKollision(Object, Bullet)
        else:
            self.bulletNormalKollision(Object, Bullet)
    
    
    
    def bulletÅlderCheck(self, Bullet):
        if Bullet.frames_drawn > 500:
                self.bullets.remove(Bullet)
        Bullet.frames_drawn += 1
    


    def bulletKollisionLoop(self):
        for Bullet in self.bullets:
            Bullet.move()
            for Object in self.Level:
                self.bulletKollision(Object, Bullet)
            Bullet.draw(self.u.screen, self.rANDwScroll)
            # kollar om skotten är gamla
            self.bulletÅlderCheck(Bullet)



    def ritaObject(self):
        # Ritar objekten i game.Level
        for Object in self.Level:
            Object.draw(self.rANDwScroll)


            
    def ritaKollisiolinjer(self):
        for i in self.player.collision_lines:
            pygame.draw.rect(self.u.screen, (255, 0, 0), pygame.Rect(i[0] - self.scroll[0], i[1] - self.scroll[1], i[2], i[3]))
def main() -> int:
    pygame.init()
    game = Game()

    # spel loopen

    while game.r == True:
        game.u.screen.fill((146, 244, 255))
        # Töm event kön
        for event in pygame.event.get():
            # Quit kod
            if event.type == QUIT:
                game.r = False
        # inputs
            else:
                game.iC.inputSaver(event, game.u.rANDwKey, game.u.rANDwMouse)
        game.iC.inputHandler(game)

        # Scroll effekt
        game.scrollFunc()

        # collision loopen
        game.kollision()

        # Roterar vapnbet
        game.roteraPistol()

        # flyttar vapnet till spelaren
        game.centreraPistol()

        # ritar spelaren och flyttar den
        game.ritaSpelare()

        # Kollar om skotten rör vid ett objekt och flyttar de fram
        game.bulletKollisionLoop()
        
        # Ritar vapnet
        game.gun.draw(game.scroll[0], game.scroll[1], game.u.screen)
        
        # Ritar objekten i game.Level
        game.ritaObject()
        
        # ritat kollision linjerna på spelar(tillfällig)
        game.ritaKollisiolinjer()
        
        # Skriver hur många hopp spelaren har kvar på skärmen
        jumps_left = game.FONT.render(("jumps: " + str(game.player.jumps) + "/" + str(game.player.max_jumps)), True, (0, 0, 0))
        game.u.screen.blit(jumps_left, (10, 10))
    
        jumps_left = game.FONT.render(("jumps: " + str(game.u.Key[3][2])), True, (0, 0, 0))
        game.u.screen.blit(jumps_left, (10, 100))

        # Skriver hur snabb spelaren är på skärmen
        jumps_left = game.FONT.render(("speed: " + str(round(game.player.speed[0]*10, 1)/10) + "/" + str(round(game.player.max_speed*10, 1)/10)), True, (0, 0, 0))
        game.u.screen.blit(jumps_left, (10, 50))

        #Spelar musik
        game.m.RunMusic()
        
        # uppdaterar skärmen
        pygame.display.update()
        
        # 60 Fps limmit
        pygame.time.Clock().tick(60)
        
        # spelaren rör sig inte upp
        #         game.player.mu = False
    return 0
sys.exit(main())
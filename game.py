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
from start import startBlock
class Game:
    def find_start(self):
        for obj in self.Level:
            if isinstance(obj, startBlock):
                return obj
    def __init__(self):
        self.r = True
        self.u = utils.utils()
        self.Clock = pygame.time.Clock()
        self.deltaTime = [0, 0]
#        self.player.gun = pistol.Pistol(self.player.pos[0], self.player.pos[1], 90)
        self.music_lib = ["data/music/Cipher_BGM.flac", "data/music/Aloft_BGM.flac", "data/music/lemmino-nocturnal.flac"]
        self.jh = JsonHandler()
        self.sh = settingsfolder.settingshandeler(self.u)
        self.iC = inputControlerGame
        self.lh = levelhandler.levelhandeler("data/json/level.json")
        self.Level = []
        self.lh.objectReader(self.Level)
        self.start = self.find_start()
        self.player = player.Player(self.start.pos[0], self.start.pos[1])
        self.user = camera.camera(self.u, self.player.pos)
        self.c = collision
        self.scroll = [0, 0]
        self.FONT = pygame.font.SysFont("Helvetica-bold", 50)
        self.mousePos = [0, 0]
        self.FPS = self.sh.readSetting("FPS")[0]
    def scrollFunc(self):
        self.scroll[1] += ((self.player.pos[1] - self.scroll[1] - self.u.screenSize[1] / 2) / 10)/16 * self.deltaTime[0]
        self.scroll[0] += ((self.player.pos[0] - self.scroll[0] - self.u.screenSize[0] / 2) / 10)/16 * self.deltaTime[0]
#        if self.scroll[1] > 0:
#           self.scroll[1] = 0
    def deltaTimeUppdate(self):
        self.deltaTime[0] = pygame.time.get_ticks() - self.deltaTime[1]
        self.deltaTime[1] = pygame.time.get_ticks()
    
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
            self.player.gun.bullets = bullets
        elif rORw == "r":
            return self.player.gun.bullets

    def golvCheck(self):
        # kollar om spelaren är under kamerans botten
        if self.player.pos[1] >= self.u.screenSize[1] - self.player.size[1]:
            self.player.pos[1] = self.u.screenSize[1] - self.player.size[1]
            self.player.on_floor = True
        else:
            # Gravitation
            self.player.speed[1] += 20 / 60
            # säger att spelaren inte är på golvet
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
            self.player.max_speed += .0005
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
                self.player.speed[1] = 0
                self.player.on_floor = True
            elif line[4] == "up":
                self.player.pos[1] = object.pos[1] + object.size[1]
                self.player.speed[1] = 0



    def vanligaObjektsKollision(self, line, object):
        self.player.in_tunnel = False
        if line[4] == "up":
            self.player.pos[1] = object.pos[1] + object.size[1]
            if self.player.speed[1] < 0:
                self.player.speed[1] = 0
        elif line[4] == "down":
            self.player.pos[1] = object.pos[1] - self.player.size[1]
            self.player.speed[1] = 0
            if self.player.speed[1] > 0:
                self.player.speed[1] = 0
            self.player.on_floor = True
        elif line[4] == "right":
            self.player.pos[0] = object.pos[0] - self.player.size[0]
            if self.player.speed[0] > 0:
                self.player.speed[0] = 0
            if self.player.on_wall_object_left != object:
                self.player.on_wall = True
                self.player.on_wall_object = object
                self.player.on_wall_right = True
        elif line[4] == "left":
            self.player.pos[0] = object.pos[0] + object.size[0]
            if self.player.speed[0] < 0:
                self.player.speed[0] = 0
            if self.player.on_wall_object_left != object:
                self.player.on_wall = True
                self.player.on_wall_left = True
                self.player.on_wall_object = object

        return self.player


    def linjeKollisiomMedObjekt(self, object):
        for line in self.player.collision_lines:
            if self.c.rectCollision(line[0], line[1], line[2], line[3], object.pos[0], object.pos[1], object.size[0], object.size[1]):
                # vanliga objekt
                #if object.__class__ != tunnel:
                    #self.player = self.vanligaObjektsKollision(line, object)
                if object.__class__ == tunnel:
                    self.TunnelKollision(line, object)
                else:
                    if line[4] == "down":
                        if self.player.speed[1] > 0:
                            self.player.pos[1] = object.pos[1] - self.player.size[1]
                            self.player.speed[1] = 0
                        self.player.on_floor = True
                    elif line[4] == "up":
                        if self.player.speed[1] < 0:
                            self.player.pos[1] = object.pos[1] + object.size[1]
                            self.player.speed[1] = 0
                    elif line[4] == "right":
                        if self.player.speed[0] > 0:
                            self.player.pos[0] = object.pos[0] - self.player.size[0]
                            self.player.speed[0] = 0
                        if self.player.on_wall_object_left != object:
                            self.player.on_wall = True
                            self.player.on_wall_object = object
                            self.player.on_wall_right = True
                    elif line[4] == "left":
                        if self.player.speed[0] < 0:
                            self.player.pos[0] = object.pos[0] + object.size[0] 
                            self.player.speed[0] = 0
                        if self.player.on_wall_object_left != object:
                            self.player.on_wall = True
                            self.player.on_wall_left = True
                            self.player.on_wall_object = object
        return self.player



    def kollision(self):
        # sätter player.in_tunnel av för collision loopen
        self.player.in_tunnel = False
        self.player.on_floor = False
        self.player.on_wall = False
        self.player.on_wall_left = False
        self.player.on_wall_right = False
        for i in range(9):
            # Rör spelaren
            self.player.movement(self.deltaTime[0])
            # kollar om spelaren är under kamerans botten
#            self.golvCheck()
            self.player.speed[1] += 0.000025 * self.deltaTime[0]
            # objekt collision loopen
            for object in self.Level:
                # kollar om det är en portal (de är speciella)
                if object.__class__ == portal:
                    self.portalKollision(object)
                if object.__class__ == startBlock:
                    continue
                # vanliga objekts kod
                else:
                    # Kollar om spelaren är inuti objektet
                    if self.c.rectCollision(object.pos[0], object.pos[1], object.size[0], object.size[1], self.player.pos[0] - 1, self.player.pos[1] - 1, self.player.size[0] + 2, self.player.size[1] + 2):
                        if object.__class__ == extra_jump or object.__class__ == speed:
                            self.collektebleCollekted(object)
                        elif object.__class__ == finish:
                            self.finished(object)
                        elif object.__class__ == objects.cube:
                            # Kollar vilken sida som nuddade objektet med linjer på spelaren
                            self.linjeKollisiomMedObjekt(object)
                # lägger till ett så att jag vet att jag är i nästa objekt i listan game.Level
        # återställer mina hopp ifall jag är på marken
        if self.player.on_wall == True:
            self.player.jumps = 1
        if self.player.on_wall == False and self.player.on_wall_object != 0:
            self.player.on_wall_object_left = self.player.on_wall_object
        if self.player.on_floor == True:
            self.player.jumps = self.player.max_jumps
            self.player.on_wall_object_left = 0
            self.player.on_wall_object = 0
        if self.player.on_floor == False and self.player.on_wall == False:
            self.player.jumps = 0



    def roteraPistol(self):   
        self.player.gun.rot(self.mousePos, self.rANDwScroll) 
        


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
            self.player.gun.bullets.remove(Bullet)
            return 1
        return 0



    def bulletCollectebleKollision(self, Object, Bullet):
        if self.c.rectCollision(Object.pos[0], Object.pos[1], Object.size[0], Object.size[1], Bullet.pos[0], Bullet.pos[1], Bullet.size[0], Bullet.size[1]) == True:
            self.collektebleCollekted(Object)



    def bulletKollision(self, Object, Bullet):
        if Object.__class__ == portal:
            self.bulletPortalKollision(Object, Bullet)
        elif Object.__class__ == extra_jump or Object.__class__ == speed:
            self.bulletCollectebleKollision(Object, Bullet)
        elif Object.__class__ != startBlock:
            self.bulletNormalKollision(Object, Bullet)
    
    
    
    def bulletÅlderCheck(self, Bullet):
        if Bullet.Time_drawn > 5000:
            self.player.gun.bullets.remove(Bullet)
            return 1
        Bullet.Time_drawn = pygame.time.get_ticks() - Bullet.Time_created
        return 0


    def bulletKollisionLoop(self):
        for Bullet in self.player.gun.bullets:
            Bullet.move(self.deltaTime[0])
            for Object in self.Level:
                if 1 == self.bulletKollision(Object, Bullet):
                    continue
            Bullet.draw(self.u.screen, self.rANDwScroll)
            # kollar om skotten är gamla
            if 1 == self.bulletÅlderCheck(Bullet):
                continue



    def ritaObject(self):
        # Ritar objekten i game.Level
        for Object in self.Level:
            if Object.__class__ == startBlock:
                continue
            Object.draw(self.rANDwScroll)


            
    def ritaKollisiolinjer(self):
        for i in self.player.collision_lines:
            pygame.draw.rect(self.u.screen, (255, 0, 0), pygame.Rect(i[0] - self.scroll[0], i[1] - self.scroll[1], i[2], i[3]))

    def updateMouse(self):
        self.mousePos = pygame.mouse.get_pos()
def gamemain(MIXER = 0) -> int:
    pygame.init()
    game = Game()
    if MIXER != 0:
        print("Mixer Recived")
    # spel loopen

    while game.r == True:
        game.u.screen.fill((146, 244, 255))
        game.updateMouse()
        game.deltaTimeUppdate()
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

        # ritar spelaren och flyttar den
        game.ritaSpelare()

        # Kollar om skotten rör vid ett objekt och flyttar de fram
        game.bulletKollisionLoop()
        
        # Ritar objekten i game.Level
        game.ritaObject()
        
        # ritat kollision linjerna på spelar(tillfällig)
        game.ritaKollisiolinjer()
        
        #spelar musik
        if MIXER != 0:
            MIXER.RunMusic()
        
        # uppdaterar skärmen
        pygame.display.update()

        #spelar musik
        if MIXER != 0:
            MIXER.RunMusic()
        
        #Fps limmit
        game.Clock.tick(game.FPS)
    return 1
if __name__ == "__main__":
    sys.exit(gamemain(0))
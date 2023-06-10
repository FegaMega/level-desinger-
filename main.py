import pygame, json, sys, utils
from utils import main
from pygame.locals import *
from JH import JsonHandler


JH = JsonHandler()
utils = utils.main()
screen = utils.screen
screenSize = utils.screenSize
user_primary_display_size = utils.user_primary_display_size
def ArrayOfStrToInt(str):
        newstr = []
        for i in str:
            newstr.append(int(i))
        return newstr


class desinger:
    def __init__(self):
        self.r = True
        self.settingsfolder = "setting.json"
        currentSettingsInfo = JH.JsonReader(self.settingsfolder)
        currentSettingsInfo["userPrimaryDisplaySize"] = utils.user_primary_display_size
        print(currentSettingsInfo["userPrimaryDisplaySize"])
        JH.JsonWriter(self.settingsfolder, currentSettingsInfo)
        utils.screenSize = currentSettingsInfo["screenSize"]
        utils.newScreen()
    
#    def input(self, event):
#        
#        
#    def Movecamera(self, event, up):
        

def main() -> int:
    pygame.init()
    app = desinger()

    # spel loopen

    while app.r == True:
        screen.fill((146, 244, 255))
        # Töm event kön
        for event in pygame.event.get():
            # Quit kod
            if event.type == QUIT:
                app.r = False
        # uppdaterar skärmen
        pygame.display.update()
        
        # 60 Fps limmit
        pygame.time.Clock().tick(60)
    return 0



if __name__ == '__main__':
    sys.exit(main())
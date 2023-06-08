import pygame, json, sys, utils
from utils import main
from pygame.locals import *

utils = utils.main()
screen = utils.screen
screenSize = utils.screenSize

class desinger:
    def __init__(self):
        self.settingsfolder = "setting.json"
        self.r = True
        self.filecontent = self.JsonReader(self.settingsfolder)
        self.n = []
        for i in self.filecontent["screenSize"]:
            self.n.append(int(i))
        self.filecontent["screenSize"] = self.n
        print((self.filecontent["screenSize"]), self.n)
        utils.screenSize = self.filecontent["screenSize"]
        print(utils.screenSize)
        utils.newScreen()
        
    def JsonReader(self, folder):
        with open(folder, 'r') as f:
            filecontent = json.load(f)
            return filecontent
    def JsonWriter(self, folder, info, Add=True):
        if Add == True: 
            with open(folder, 'w') as f:
                json.dumps(info, f)
        else:
            with open(folder, 'w') as f:
                json.dumps(info, f)
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
    print(app.filecontent)
    return 0



if __name__ == '__main__':
    sys.exit(main())
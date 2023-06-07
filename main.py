import pygame, json, sys, utils
from pygame.locals import *


class desinger:
    def __init__(self):
        self.settingsfolder = "setting.json"
        self.filecontent = ""
        self.filecontent = self.JsonReader(self.settingsfolder)
        if self.filecontent == "":
            self.JsonWriter(self.settingsfolder, "[[screenSize, [700, 700]]]", False)
            utils.screenSize = [700, 700]
        else:
            self.filecontent = self.JsonReader(self.settingsfolder)
            print(self.filecontent)
            utils.screenSize = self.filecontent[0][1]
        utils.newScreen()
        
    def JsonReader(self, folder):
        with open(folder, 'r') as f:
            filecontent = json.load(f)
            return filecontent
    def JsonWriter(self, folder, info, Add=True):
        if Add == True: 
            with open(folder, 'w') as f:
                json.dump(info, f)
        else:
            with open(folder, 'w') as f:
                json.dumps((info), f)
#    def input(self, event):
#        
#        
#    def Movecamera(self, event, up):
        
app = desinger()
print(app.filecontent)

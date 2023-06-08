import  json, utils, pygame
from utils import main


class settingshandeler:
    def __init__(self, Screensize, Screen):
        self.settingsfolder = "setting.json"
        self.r = True
        self.filecontent = self.JsonReader(self.settingsfolder)
        self.n = []
        for i in self.filecontent["screenSize"]:
            self.n.append(int(i))
        self.filecontent["screenSize"] = self.n
        ScreenSize = self.filecontent["screenSize"]
        Screen = pygame.display.set_mode(ScreenSize)
        self.info ={"notscreenSize":["700", "800"]}
        
        
    def JsonReader(self, folder):
        with open(folder, 'r') as f:
            filecontent = json.load(f)
            return filecontent
    def JsonWriter(self, folder, info):
        newFile = json.dumps(info)
        with open(folder, 'w') as outfile:
            outfile.write(newFile, outfile)
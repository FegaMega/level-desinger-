import  JH, utils, pygame
from utils import main
JH = JH.JsonHandler()
utils = main()

class settingshandeler:
    def __init__(self):
        self.settingsfolder = "setting.json"
        self.currentSettingsInfo = JH.JsonReader(self.settingsfolder)
        self.currentSettingsInfo["userPrimaryDisplaySize"] = utils.user_primary_display_size
        print(self.currentSettingsInfo["userPrimaryDisplaySize"])
        JH.JsonWriter(self.settingsfolder, self.currentSettingsInfo)
        self.currentSettingsInfo = JH.JsonReader(self.settingsfolder)
        print(self.currentSettingsInfo["screenSize"])
        utils.screenSize = self.currentSettingsInfo["screenSize"]
        print(utils.screenSize)
        utils.newScreen()
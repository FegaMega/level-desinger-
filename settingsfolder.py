import  JH, utils, pygame, json
from utils import main
JH = JH.JsonHandler()
utils = main()

class settingshandeler:
    def __init__(self):
        self.settingsfolder = "setting.json"
        self.currentSettingsInfo = JH.JsonReader(self.settingsfolder)
        self.currentSettingsInfo["userPrimaryDisplaySize"] = utils.user_primary_display_size
        JH.JsonWriter(self.settingsfolder, self.currentSettingsInfo)
        utils.screenSize = self.currentSettingsInfo["screenSize"]
        utils.newScreen()

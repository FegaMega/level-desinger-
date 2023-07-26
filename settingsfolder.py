import  JH, utils, pygame, json
from utils import utils
JH = JH.JsonHandler()
utils = utils()

class settingshandeler:
    def __init__(self):
        self.settingsfolder = "data/json/setting.json"
        self.currentSettingsInfo = JH.JsonReader(self.settingsfolder)
        self.currentSettingsInfo["userPrimaryDisplaySize"] = utils.user_primary_display_size
        JH.JsonWriter(self.settingsfolder, self.currentSettingsInfo)
        utils.screenSize = self.currentSettingsInfo["screenSize"]
        utils.newScreen()
        
        

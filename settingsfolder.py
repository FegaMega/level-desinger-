import  JH, utils, pygame
from utils import main
JH = JH.JsonHandler()
utils = main()

class settingshandeler:
    def __init__(self):
        self.settingsfolder = "setting.json"
        currentSettingsInfo = JH.JsonReader(self.settingsfolder)
        currentSettingsInfo["userPrimaryDisplaySize"] = utils.user_primary_display_size
        JH.JsonWriter(self.settingsfolder, currentSettingsInfo)
        utils.screenSize = currentSettingsInfo["screenSize"]
        utils.newScreen()
        
        
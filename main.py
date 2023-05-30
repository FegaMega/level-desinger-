import pygame, json, sys
what_to_write = "fuck"

class desinger:
    def __init__(self):
        self.settingsfolder = "setting.json"
        self.filecontent = ""
    def JsonReader(self, folder):
        with open(folder, 'r') as f:
            self.filecontent = json.load(f)
    def JsonWriter(self, folder, info, Add=True):
        if Add == True: 
            with open(folder, 'w') as f:
                json.dump(info, f)
        else:
            with open(folder, 'w') as f:
                json.dumps((info), f)
app = desinger()
app.JsonReader(app.settingsfolder)
app.JsonWriter(app.settingsfolder, what_to_write, True)
print(app.filecontent)

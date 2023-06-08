import json


class settingshandeler:
    def __init__(self):
        self.settingsfolder = "setting.json"

        self.info = {

    "screenSize" : [
        "700", "700"
    ]
}
        self.JsonWriter("json crap2.json", self.info)
        self.JsonWriter("json crap2.json", self.info)
    def JsonReader(self, folder):
        with open(folder, 'r') as f:
            filecontent = json.load(f)
            return filecontent
    def JsonWriter(self, folder, info):
        newInfo = json.dumps(info)
        currentfile = open(folder, 'r')
        currentInfo = currentfile.read()
        newInfo = str(info) + str(currentInfo)
        newFile2 = json.dumps(newInfo)
        currentfile.close()
        currentfile = open(folder, 'w')
        currentfile.write(newInfo)
        currentfile.close
app = settingshandeler()
app.__init__()
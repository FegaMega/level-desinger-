import  JH, utils, objects
from utils import utils
JH = JH.JsonHandler()
utils = utils()

class levelhandeler:
    def __init__(self, levelfolder):
        self.levelfolder = levelfolder
        self.info = JH.JsonReader(self.levelfolder)
        self.objects:list = self.info["Level one"]["objects"]
    def objectReader(self, Cubes):
        self.info = JH.JsonReader(self.levelfolder)
        self.objects = self.info["Level one"]["objects"]
        for Object in self.objects:
            
            Cubes.append(objects.cube(Object[0], Object[1], Object[2], Object[3], (Object[4][0], Object[4][1], Object[4][2])))
        return Cubes
    def objectWriter(self, Cubes=[]):
        self.info = JH.JsonReader(self.levelfolder)
        self.objects = []
        for cube in Cubes:
            self.objects.append([int(cube.pos[0]), int(cube.pos[1]), int(cube.size[0]), int(cube.size[1]), [cube.color[0], cube.color[1], cube.color[2]]])
        self.info["Level one"]["objects"] = self.objects
        JH.JsonWriter(self.levelfolder, self.info)
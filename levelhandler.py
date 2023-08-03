import  JH, utils, objects, speed
from utils import utils
JH = JH.JsonHandler()
utils = utils()

class levelhandeler:
    def __init__(self, levelfolder):
        self.levelfolder = (levelfolder)
        self.info = JH.JsonReader(self.levelfolder)
        self.objects:list = self.info["Level one"]["objects"]
        self.speed:list = self.info["Level one"]["speed"]
    def objectReader(self, Cubes):
        self.info = JH.JsonReader(self.levelfolder)
        self.objects = self.info["Level one"]["objects"]
        for Object in self.objects:
            Cubes.append(objects.cube(Object[0], Object[1], Object[2], Object[3], (Object[4][0], Object[4][1], Object[4][2])))
        self.speed = self.info["Level one"]["speed"]
        for Object in self.speed:
            Cubes.append(speed.speed(Object[0], Object[1], Object[2], Object[3], (Object[4][0], Object[4][1], Object[4][2])))
        return Cubes
    def objectWriter(self, Cubes=[]):
        self.info = JH.JsonReader(self.levelfolder)
        self.objects = []
        self.speed = []
        for cube in Cubes:
            if cube.__class__ == objects.cube:
                self.objects.append([int(cube.pos[0]), int(cube.pos[1]), int(cube.size[0]), int(cube.size[1]), [cube.color[0], cube.color[1], cube.color[2]]])
            elif cube.__class__ == speed.speed:
                self.speed.append([int(cube.pos[0]), int(cube.pos[1]), int(cube.size[0]), int(cube.size[1]), [cube.color[0], cube.color[1], cube.color[2]]])
        self.info["Level one"]["objects"] = self.objects
        self.info["Level one"]["speed"] = self.speed
        JH.JsonWriter(self.levelfolder, self.info)
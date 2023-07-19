import pygame
from screeninfo import get_monitors
for m in get_monitors():
    if m.is_primary == True:
        Primary_screen = m
class utils:
    def __init__(self):
        self.user_primary_display_size = [Primary_screen.width, Primary_screen.height]
        self.screenSize = [700, 700]
        self.screen = pygame.display.set_mode(self.screenSize, vsync=1)
        self.tolerance = 5
        self.Key = [
            # How to read

            # Find index of letter
            # Then add one to get the index of the letter variables
            # Example:
            # S = Key[Key.index("S")+1]
            "Q", [False, pygame.K_q],          
            "W", [False, pygame.K_w],          
            "E", [False, pygame.K_e],          
            "R", [False, pygame.K_r],          
            "T", [False, pygame.K_t],          
            "Y", [False, pygame.K_y],          
            "U", [False, pygame.K_u],          
            "I", [False, pygame.K_i],          
            "O", [False, pygame.K_o],          
            "P", [False, pygame.K_p],          
            "A", [False, pygame.K_a],           
            "S", [False, pygame.K_s],           
            "D", [False, pygame.K_d],           
            "F", [False, pygame.K_f],           
            "G", [False, pygame.K_g],           
            "H", [False, pygame.K_h],           
            "J", [False, pygame.K_j],           
            "K", [False, pygame.K_k],           
            "L", [False, pygame.K_l],           
            "Z", [False, pygame.K_z],           
            "X", [False, pygame.K_x],           
            "C", [False, pygame.K_c],           
            "V", [False, pygame.K_v],           
            "B", [False, pygame.K_b],           
            "N", [False, pygame.K_n],           
            "M", [False, pygame.K_m],           
            "UP", [False, pygame.K_UP],         
            "LEFT", [False, pygame.K_LEFT],     
            "DOWN", [False, pygame.K_DOWN],     
            "RIGHT", [False, pygame.K_RIGHT],
            "DEL", [False, pygame.K_DELETE]   
        ]
        self.Mouse = [
            "MOUSELEFT", [False, 1],            
            "MOUSERIGHT", [False, 3],           
            "MOUSE", [[0, 0], [0, 0]] #[str, pos, oldpos]

        ]
    def getInfo(self, List, item, offset = 0):
        if List == "Mouse":
            try:
                return self.Mouse[(self.Mouse.index(item)+offset)]
            except TypeError:
                return TypeError
        elif List == "Key":
            try:
                return self.Key[(self.Key.index(item)+offset)]
            except TypeError:
                return TypeError
        else:
            try:
                return List[(List.index(item)+offset)]
            except:
                NameError
                
                TypeError
                
                ValueError
                
                return 1
            
    def changeInfo(self, List:list, item, changeIndex:int = 0, offset=0, Input=0):
        if List == "Mouse":
            self.Mouse[(self.Mouse.index(item)+offset)][changeIndex] = Input
        elif List == "Key":
            self.Key[(self.Key.index(item)+offset)][changeIndex] = Input
        else:
            try:
                List[(List.index(item)+offset)] = Input
            except List.__class__ != list or NameError:
                if List.__class__ != list:
                    print("List is not type: list and if you are trying to access Mouse or Key list it is not spelt correctly")
                else:
                    print("List does not exist")
    def addInfo(self, List:list, item, append:bool, insert:bool, insertpoint:int = 1):
        if append == insert:
            print("addInfo error")
            return 1
        if append == True:
            List.append(item)
        if insert == True:
            List.insert(item, insertpoint)
    def newScreen(self):
        self.screen = pygame.display.set_mode(self.screenSize, vsync=1)

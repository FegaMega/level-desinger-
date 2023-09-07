import pygame
from screeninfo import get_monitors
import os
x=100
y=100
os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)
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
            "DEL", [False, pygame.K_DELETE],   
            "SPACE", [False, pygame.K_SPACE, False]
        ]
        self.Mouse = [
            "MOUSELEFT", [False, 1],           
            "MOUSERIGHT", [False, 3],
            "MOUSE", [[0, 0], [0, 0]], #[str, pos, oldpos]
            "MOUSESCROLLUP", [False, 4],
            "MOUSESCROLLDOWN", [False, 5]
            ] 
    def rANDwMouse(self, Mouse, rORw:str):
        if rORw == "w":
            self.Mouse = Mouse
        elif rORw == "r":
            return self.Mouse
    def rANDwKey(self, Key, rORw:str):
        if rORw == "w":
            self.Key = Key
        elif rORw == "r":
            return self.Key
    def rANDwScreen(self, screen, rORw:str):
        if rORw == "w":
            self.screen = screen
        elif rORw == "r":
            return self.screen
    def rANDwScreenSize(self, screenSize, rORw:str):
        if rORw == "w":
            self.screenSize = screenSize
        elif rORw == "r":
            return self.screenSize
    def newScreen(self):
        x=100
        y=100
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)
        self.screen = pygame.display.set_mode(self.screenSize, vsync=1)
    def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
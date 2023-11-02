import pygame
from screeninfo import get_monitors
import os
x=0
y=30
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
            "Q", [False, pygame.K_q, 0],          
            "W", [False, pygame.K_w, 0],          
            "E", [False, pygame.K_e, 0],          
            "R", [False, pygame.K_r, 0],          
            "T", [False, pygame.K_t, 0],          
            "Y", [False, pygame.K_y, 0],          
            "U", [False, pygame.K_u, 0],          
            "I", [False, pygame.K_i, 0],          
            "O", [False, pygame.K_o, 0],          
            "P", [False, pygame.K_p, 0],          
            "A", [False, pygame.K_a, 0],           
            "S", [False, pygame.K_s, 0],           
            "D", [False, pygame.K_d, 0],           
            "F", [False, pygame.K_f, 0],           
            "G", [False, pygame.K_g, 0],           
            "H", [False, pygame.K_h, 0],           
            "J", [False, pygame.K_j, 0],           
            "K", [False, pygame.K_k, 0],           
            "L", [False, pygame.K_l, 0],           
            "Z", [False, pygame.K_z, 0],           
            "X", [False, pygame.K_x, 0],           
            "C", [False, pygame.K_c, 0],           
            "V", [False, pygame.K_v, 0],           
            "B", [False, pygame.K_b, 0],           
            "N", [False, pygame.K_n, 0],           
            "M", [False, pygame.K_m, 0],           
            "UP", [False, pygame.K_UP, 0],         
            "LEFT", [False, pygame.K_LEFT, 0],     
            "DOWN", [False, pygame.K_DOWN, 0],     
            "RIGHT", [False, pygame.K_RIGHT, 0],
            "DEL", [False, pygame.K_DELETE, 0],   
            "SPACE", [False, pygame.K_SPACE, 0]
        ]
        self.Mouse = [
            "MOUSELEFT", [False, 1, 0, [0, 0]],           
            "MOUSERIGHT", [False, 3, 0, ],
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
        x=0
        y=30
        os.environ['SDL_VIDEO_WINDOW_POS'] = '%d,%d' % (x,y)
        self.screen = pygame.display.set_mode(self.screenSize, vsync=1)
    def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image,rot_rect
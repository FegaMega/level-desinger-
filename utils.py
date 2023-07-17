import pygame
from screeninfo import get_monitors
for m in get_monitors():
    if m.is_primary == True:
        Primary_screen = m
class main:
    def __init__(self):
        self.user_primary_display_size = [Primary_screen.width, Primary_screen.height]
        self.screenSize = [700, 700]
        self.screen = pygame.display.set_mode(self.screenSize)
        self.Key = [
            ["Q", False, pygame.K_q],           #0
            ["W", False, pygame.K_w],           #1
            ["E", False, pygame.K_e],           #2
            ["R", False, pygame.K_r],           #3
            ["T", False, pygame.K_t],           #4
            ["Y", False, pygame.K_y],           #5
            ["U", False, pygame.K_u],           #6
            ["I", False, pygame.K_i],           #7
            ["O", False, pygame.K_o],           #8
            ["P", False, pygame.K_p],           #9
            ["A", False, pygame.K_a],           #10
            ["S", False, pygame.K_s],           #11
            ["D", False, pygame.K_d],           #12
            ["F", False, pygame.K_f],           #13
            ["G", False, pygame.K_g],           #14
            ["H", False, pygame.K_h],           #15
            ["J", False, pygame.K_j],           #16
            ["K", False, pygame.K_k],           #17
            ["L", False, pygame.K_l],           #18
            ["Z", False, pygame.K_z],           #19
            ["X", False, pygame.K_x],           #20
            ["C", False, pygame.K_c],           #21
            ["V", False, pygame.K_v],           #22
            ["B", False, pygame.K_b],           #23
            ["N", False, pygame.K_n],           #24
            ["M", False, pygame.K_m],           #25
            ["UP", False, pygame.K_UP],         #26
            ["LEFT", False, pygame.K_LEFT],     #27
            ["DOWN", False, pygame.K_DOWN],     #28
            ["RIGHT", False, pygame.K_RIGHT],   #29
            ["MOUSELEFT", False, 1],            #30
            ["MOUSERIGHT", False, 3],           #31
            ["MOUSE", [0, 0], [0, 0]]           #32 [str, pos, oldpos]
        ]
    def newScreen(self):
        self.screen = pygame.display.set_mode(self.screenSize)

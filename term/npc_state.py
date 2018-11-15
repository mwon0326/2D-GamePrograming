from pico2d import *
import game_framework
import random
from image_state import Font

class NPC:
    def __init__(self):
        self.image = None
        self.cartoon = None
        self.present = None
        self.cartoon2 = None
        self.time = 0
        self.npc_time = 12
        self.x, self.y = 180, 350
        self.cx, self.cy = 300, 450
        self.px, self.py = 302, 475
        self.cx2, self.cy2 = 330, 350
        self.ft = Font()
        self.font = self.ft.f
        self.stage_in = False
        self.is_collide = True
        self.is_draw = False
        self.left_a, self.bottom_a, self.right_a, self.top_a = 0, 0, 0, 0
        self.left_b, self.bottom_b, self.right_b, self.top_b = 0, 0, 0, 0

    def draw(self):
        if self.is_draw:
            self.image.draw(self.x, self.y)
            self.cartoon.draw(self.cx, self.cy)
            self.present.draw(self.px, self.py)
            self.cartoon2.draw(self.cx2 + 3, self.cy2 + 10)
            self.font.draw(self.cx2, self.cy2, '%d' % self.npc_time, (0, 0, 0))

    def change_level(self, level):
        if level % 2 == 1:
            self.x, self.y = 180, 350
            self.cx, self.cy = 300, 450
            self.px, self.py = 302, 475
            self.cx2, self.cy2 = 330, 350
        elif level % 2 == 0:
            self.x, self.y = 620, 350
            self.cx, self.cy = 500, 450
            self.px, self.py = 498, 475
            self.cx2, self.cy2 = 470, 350
        self.time = 0
        self.is_collide = True

    def timer(self):
        self.npc_time = 8 - self.time
        if self.time >= 3 and self.is_collide:
            self.is_draw = True
        else:
            self.is_draw = False

    def stop(self):
        self.is_collide = False

    def get_bb(self):
        return self.x - 60, self.y - 100, self.x + 50, self.y - 10

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


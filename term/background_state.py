from pico2d import *
import game_framework

class Castle:
    def __init__(self):
        self.image = None
        self.x = 800
        self.dir = 1

    def draw(self):
        self.image.clip_draw(self.x, 0, 800, 600, 400, 300)

    def move(self):
        if self.dir == 1:
            self.x -= 25
        else:
            self.x += 25
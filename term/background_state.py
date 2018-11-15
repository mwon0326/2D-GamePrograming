from pico2d import *
import game_framework
from image_state import Font

class BackGround:
    def __init__(self):
        self.image = None
        self.x = 800
        self.dir = 1
        self.speed = 5

    def draw(self):
        self.image.clip_draw(self.x, 0, 800, 500, 400, 350)

    def move(self):
        if self.dir == 1:
            self.x -= self.speed
        else:
            self.x += self.speed

class ItemBox:
    def __init__(self):
        self.ft = Font()
        self.image = load_image('resource/menu.png')
        self.font = self.ft.f
        self.time = 0
        self.x = 130
        self.y = 50

    def draw(self):
        self.image.draw(400, 50);
        self.font.draw(self.x, self.y, '%d' % self.time, (0, 0, 0))
from pico2d import *
import game_framework

class Princess:
    def __init__(self):
        self.image = load_image('resource/animation.png')
        self.x, self.y = 200, 200
        self.frame = 0
        self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 200, self.dir * 300, 200, 300, self.x, self.y)

    def move(self):
        if self.dir == 1:
            self.x -= 25
        else:
            self.x += 25
        self.frame = (self.frame + 1) % 4

    def motion(self):
        self.frame = (self.frame + 1) % 4
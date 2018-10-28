from pico2d import *
import game_framework
import random

class Fire:
    image = None
    def __init__(self):
        if Fire.image == None:
            Fire.image = load_image('resource/fire.png')
        self.x = random.randint(110, 690)
        self.y = 550
        self.speed = random.randint(10, 15)

    def draw(self):
        Fire.image.draw(self.x, self.y)

    def update(self):
        self.y = self.y + (self.speed * -1)
        if self.y <= 0:
            self.x = random.randint(110, 690)
            self.y = 550
            self.speed = random.randint(10, 15)
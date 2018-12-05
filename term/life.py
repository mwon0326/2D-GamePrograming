from pico2d import *
import game_framework
import logo_state

class Life:
    def __init__(self):
        self.image = logo_state.red
        self.x, self.y = 450, 40

    def draw(self, count):
        self.x = 450
        for i in range(count):
            self.image.draw(self.x, self.y)
            self.x += 70

    def image_change(self, level):
        if level == 2:
            self.image = logo_state.pink
        elif level == 3:
            self.image = logo_state.black
        elif level == 4:
            self.image = logo_state.yellow
        elif level == 5:
            self.image = logo_state.blue

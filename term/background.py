from pico2d import *
import game_framework
import logo_state
import game_framework
import title_state

class BackGround:
    def __init__(self):
        self.image = logo_state.stage1

    def draw(self):
        self.image.draw(400, 300)

    def changeLevel(self, level):
        if level == 2:
            self.image = logo_state.stage2
        elif level == 3:
            self.image = logo_state.stage3
        elif level == 4:
            self.image = logo_state.stage4
        elif level == 5:
            self.image = logo_state.stage5

    def update(self):
        pass

class StateBox:
    def __init__(self):
        self.image = logo_state.menu_image
        self.time = 0
        self.x = 130
        self.y = 50

    def draw(self):
        self.image.draw(400, 50)

    def update(self):
        pass

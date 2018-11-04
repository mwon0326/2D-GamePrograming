from pico2d import *
import game_framework

class Princess:
    def __init__(self):
        self.image = load_image('resource/animation.png')
        self.x, self.y = 200, 250
        self.frame = 0
        self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 150, self.dir * 250, 150, 250, self.x, self.y)

    def move(self):
        if self.dir == 1:
            self.x -= 25
        else:
            self.x += 25
        self.frame = (self.frame + 1) % 4

    def motion(self):
        self.frame = (self.frame + 1) % 4

    def get_bb(self, state, num):
        if state == 1:
            if num == 1:
                return self.x - 33, self.y + 96, self.x - 6, self.y + 114
            elif num == 2:
                return self.x - 58, self.y + 17, self.x + 33, self.y + 96
            else:
                return self.x - 68, self.y - 100, self.x + 40, self.y - 82
        else:
            if num == 1:
                return self.x - 15, self.y + 96, self.x + 11, self.y + 114
            elif num == 2:
                return self.x - 58, self.y + 17, self.x + 33, self.y + 96
            else:
                return self.x - 67, self.y - 100, self.x + 41, self.y - 82

    def draw_face_left_bb(self):
        draw_rectangle(*self.get_bb(1, 2))

    def draw_crown_left_bb(self):
        draw_rectangle(*self.get_bb(1, 1))

    def draw_dress_left_bb(self):
        draw_rectangle(*self.get_bb(1, 3))

    def draw_face_right_bb(self):
        draw_rectangle(*self.get_bb(2, 2))

    def draw_crown_right_bb(self):
        draw_rectangle(*self.get_bb(2, 1))

    def draw_dress_right_bb(self):
        draw_rectangle(*self.get_bb(2, 3))
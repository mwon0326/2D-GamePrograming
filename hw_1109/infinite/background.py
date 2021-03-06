from pico2d import *

class Infinite:
    def __init__(self):
        self.image = load_image('back.jpg')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h
        self.x, self.y = 0, 0
        self.target = None


    def draw(self):
        self.image.clip_draw_to_origin(self.x3, self.y3, self.w3, self.h3, 0, 0)
        self.image.clip_draw_to_origin(self.x2, self.y2, self.w2, self.h2, 0, self.h3)
        self.image.clip_draw_to_origin(self.x4, self.y4, self.w4, self.h4, self.w3, 0)
        self.image.clip_draw_to_origin(self.x1, self.y1, self.w1, self.h1, self.w3, self.h3)

    def update(self):
        self.x = int(self.target.x - self.cw / 2)
        self.y = int(self.target.y - self.ch / 2)
        
        self.x3, self.y3 = self.x % self.width, self.y % self.height
        self.w3, self.h3 = self.width - self.x3, self.height - self.y3

        self.x2, self.y2 = self.x3, 0
        self.w2, self.h2 = self.w3, self.ch - self.h3

        self.x4, self.y4 = 0, self.y3
        self.w4, self.h4 = self.cw - self.w3, self.h3

        self.x1, self.y1 = 0, 0
        self.w1, self.h1 = self.w4, self.h2

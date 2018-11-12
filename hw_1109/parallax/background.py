from pico2d import *

class ParallaxLayer:
    def __init__(self, image_name, speed):
        self.image = load_image(image_name)
        self.w, self.h = self.image.w, self.image.h
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.speed = speed
        self.w1, self.w2 = 0, 0
        self.x1, self.x2 = 0, 0
        
    def draw(self):
        self.image.clip_draw_to_origin(self.x1, 0, self.w1, self.h, 0, 0)
        self.image.clip_draw_to_origin(self.x2, 0, self.w2, self.h, self.w1, 0)

    def update(self, x):
        self.x1 = int(x * self.speed) % self.image.w
        self.w1 = self.image.w - self.x1
        
        self.x2 = 0
        self.w2 = self.cw - self.w1

class ParallaxBackground:
    def __init__(self):
        self.layers = [ParallaxLayer('back0.png', 0.3), ParallaxLayer('back1.png', 0.7), ParallaxLayer('back2.png', 1.0), ParallaxLayer('back3.png', 1.2)]
        self.min_x, self.min_y = 0, 100
        self.max_x, self.max_y = 20000, 100
        self.x, self.y = 0, 0
        self.target = None

    def clamp(self, o):
        o.x = clamp(self.min_x, o.x, self.max_x)
        o.y = clamp(self.min_y, o.y, self.max_y)

    def draw(self):
        for i in self.layers:
            i.draw()

    def update(self):
        self.x = int(self.target.x - 100)
        for i in self.layers:
            i.update(self.x)

class Background:
    def __init__(self):
        self.image = load_image('../../image/futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h
        self.x, self.y = 0,0
        self.target = None

    def draw(self):
        self.image.clip_draw_to_origin(self.x, self.y, self.cw, self.ch, 0, 0)

    def update(self):
        if self.target == None:
            return
        self.x = clamp(0, int(self.target.x - self.cw // 2), self.width - self.cw)
        self.y = clamp(0, int(self.target.y - self.ch // 2), self.height - self.ch)
        

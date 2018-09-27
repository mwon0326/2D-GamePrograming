from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    global x, y
    def __init__(self):
        self.x, self.y = random.randint(0, 200), random.randint(90, 550)
        self.frame = random.randint(0, 7)
        self.image = load_image('../image/run_animation.png')
        self.speed = random.uniform(1.0, 3.0)

    def update(self):
        if x > self.x:
            self.x += self.speed
            if x <= self.x:
                self.x = x
        elif x < self.x:
            self.x -= self.speed
            if x >= self.x:
                self.x = x
        if y > self.y:
            self.y += self.speed
            if y <= self.y:
                self.y = y
        elif y < self.y:
            self.y -= self.speed
            if y >= self.y:
                self.y = y
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def hanble_events():
    global running
    global x, y
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
                x = e.x
                y = 600 - e.y

open_canvas()
g = Grass()
boys = []
for i in range(20):
    boys += [Boy()]
x,y = 0, 0
#boys = [Boys() for i in range(20)]
    
running = True
while running:
    hanble_events()
        
    clear_canvas()
    g.draw()
    for b in boys:
        b.draw()

    for b in boys:
        b.update()
        
    update_canvas()
    delay(0.025)

from pico2d import *
import game_framework
import title_state
import random
import math

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    global waypoints
    def __init__(self):
        self.x, self.y = random.randint(0, 200), random.randint(90, 550)
        self.frame = random.randint(0, 7)
        self.image = load_image('../image/run_animation.png')
        self.speed = random.uniform(1.0, 3.0)
        self.i = 0
        
    def update(self):
        if len(waypoints) > 0:
            (x, y) = waypoints[self.i]
            dx, dy = x - self.x, y - self.y
            dist = math.sqrt(dx ** 2 + dy ** 2)
            if dist > 0:
                self.x += self.speed * dx / dist
                self.y += self.speed * dy / dist

                if dx < 0 and self.x < x: self.x = x
                if dx > 0 and self.x > x: self.x = x
                if dy < 0 and self.y < y: self.y = y
                if dy > 0 and self.y > y: self.y = y
            if self.x == x and self.y == y and self.i < len(waypoints) - 1:
                self.i += 1
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    global boys
    global waypoints
    
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
        elif e.type == SDL_MOUSEBUTTONDOWN:
            x, y = e.x, 600 - e.y
            waypoints += [(x, y)]

def enter():
    global boys, g, waypoints, wp
    open_canvas()

    g = Grass()
    boys = []
    for i in range(20):
        boys += [Boy()]
    
    waypoints = []
    wp = load_image('../image/wp.png')
    
#boys = [Boys() for i in range(20)]
    
def draw():
    global boys, g, waypoints, wp
    clear_canvas()
    g.draw()
    
    for loc in waypoints:
        wp.draw(loc[0], loc[1])        
    for b in boys:
        b.draw()
    update_canvas()
    
def update():
    global boys
    for b in boys:
        b.update()
    delay(0.025)

def exit():
    global boys, g, wp
    del(wp)
    del(boys)
    del(g)

if __name__ == '__main__':
    main()

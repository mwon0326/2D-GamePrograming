from pico2d import *
import game_framework
import title_state
import random
import math
import json

class Grass:
    def __init__(self):
        self.image = load_image('../image/grass.png')

    def draw(self):
        self.image.draw(400,30)

IDLE, RUN, SLEEP = range(3)
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, TIME_OUT = range(5)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT) : LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT) : RIGHT_UP,
    (SDL_KEYUP, SDLK_RIGHT) : LEFT_UP
}
    
next_state_table = {
    IDLE : {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN: RUN, LEFT_DOWN: RUN, TIME_OUT: SLEEP},
    RUN : {RIGHT_UP: IDLE, LEFT_UP: IDLE, RIGHT_DOWN: IDLE, LEFT_DOWN: IDLE},
    SLEEP : {LEFT_DOWN: RUN, RIGHT_DOWN: RUN}
}
    
class Boy:
    image = None;
    
    def __init__(self):
        if Boy.image == None:
            Boy.image = load_image('../image/animation_sheet.png')
        self.x, self.y = 800 // 2, 90
        self.velocity = 0
        self.dir = 1
        self.cur_state = IDLE
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.enter_state[IDLE](self)

    def exit_IDLE(self):
        pass

    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0

    def do_IDLE(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(SLEEP_TIMER)

    def draw_IDLE(self):
        if self.dir == 1:
            Boy.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            Boy.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

    def enter_RUN(self):
        self.frame = 0
        self.dir = self.velocity

    def exit_RUN(self):
        pass

    def do_RUN(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.velocity
        self.x = clamp(25, self.x, 800 - 25)

    def draw_RUN(self):
        if self.velocity == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def enter_SLEEP(self):
        self.frame = 0

    def exit_SLEEP(self):
        pass

    def do_SLEEP(self):
        self.frame = (self.frame + 1) % 8

    def draw_SLEEP(self):
        if self.dir == 1:
            Boy.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, ''. self.x - 25, self.y - 25, 100, 100)
        else:
            Boy.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, ''. self.x + 25, self.y - 25, 100, 100)

    def change_state(self, state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state
    
    def update(self):
        self.do_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):
        self.draw_state[self.cur_state](self)
    
    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.velocity += 1
            elif key_event == LEFT_DOWN:
                self.velocity -= 1
            elif key_event == RIGHT_UP:
                self.velocity -= 1
            elif key_event == LEFT_UP:
                self.velocity += 1
            self.add_event(key_event)

    def add_event(self, event):
        self.event_que.insert(0, event)
            
        
    enter_state = {IDLE : enter_IDLE, RUN: enter_RUN, SLEEP: enter_SLEEP}
    exit_state = {IDLE : exit_IDLE, RUN: exit_RUN, SLEEP: exit_SLEEP}
    do_state = {IDLE : do_IDLE, RUN: do_RUN, SLEEP: do_SLEEP}
    draw_state = {IDLE : draw_IDLE, RUN: draw_RUN, SLEEP: draw_SLEEP}

def enter():
    global grass, boy
    open_canvas()
    grass = Grass()
    boy = Boy()

def draw():
    global grass, boy
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

def update():
    global boy
    boy.update()
    delay(0.025)

def exit():
    global boy, grass
    del grass
    del boy

def handle_events():
    global boy

    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.pop_state()
            else:
                boy.handle_event(e)
    
if __name__ == '__main__':
    main()

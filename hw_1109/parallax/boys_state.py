from pico2d import *
import random
import time
import game_world

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE_DOWN, ENTER_DOWN = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT) : LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT) : RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT) : LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE) : SPACE_DOWN,
    (SDL_KEYDOWN, SDLK_RETURN) : ENTER_DOWN
}

class IdleState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 1) % 8
        t = time.time() - boy.time
        if t > 10.0:
            boy.set_state(SleepState)

    @staticmethod
    def draw(boy):
        if boy.dir == 0:
            Boy.image.clip_draw(boy.frame * 100, 200, 100, 100, *boy.pos())
        else:
            Boy.image.clip_draw(boy.frame * 100, 300, 100, 100, *boy.pos())

class RunState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def update(boy):
        t = time.time() - boy.time
        if t > 2.0:
            m = 2
        else:
            m = 1
        boy.frame = (boy.frame + 1) % 8
        boy.x = boy.x + m * boy.m * boy.dx
        #boy.x = clamp(25, boy.x, 775)
        if hasattr(boy.bg, 'clamp'):
            boy.bg.clamp(boy)
            
    @staticmethod
    def draw(boy):
        if boy.dir == 0:
            Boy.image.clip_draw(boy.frame * 100, 0, 100, 100, *boy.pos())
        else:
            Boy.image.clip_draw(boy.frame * 100, 100, 100, 100, *boy.pos())


class SleepState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def update(boy):
        boy.frame = (boy.frame + 1) % 8

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            Boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            Boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

class Boy:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0, 200), 90
        self.speed = random.uniform(5.0, 8.0)
        self.frame = random.randint(0, 7)
        self.state = None
        self.set_state(IdleState)
        self.dir = 1
        self.dx, self.dy = 0, 0
        self.m = 1
        self.bg = None
        if Boy.image == None:
            Boy.image = load_image('../../image/animation_sheet.png')

    def draw(self):
        self.state.draw(self)

    def pos(self):
        return self.x - self.bg.x, self.y - self.bg.y
    
    def update(self):
        self.state.update(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == RIGHT_DOWN:
                self.dx += self.speed
                if self.dx > 0:
                    self.dir = 1
            elif key_event == LEFT_DOWN:
                self.dx -= self.speed
                if self.dx < 0:
                    self.dir = 0
            elif key_event == RIGHT_UP:
                self.dx -= self.speed
                if self.dx < 0:
                    self.dir = 0
            elif key_event == LEFT_UP:
                self.dx += self.speed
                if self.dx > 0:
                    self.dir = 1
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LSHIFT):
                self.m = 2.0
            elif (event.type, event.key) == (SDL_KEYUP, SDLK_LSHIFT):
                self.m = 1.0
        self.set_state(IdleState if self.dx == 0 and self.dy == 0 else RunState)

    def set_state(self, state):
        if self.state == state:
            return
        if self.state and self.state.exit:
            self.state.exit(self)
        self.state = state
        if self.state.enter:
            self.state.enter(self)

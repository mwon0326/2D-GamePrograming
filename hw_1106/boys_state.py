from pico2d import *
import game_framework
import game_world
import title_state
import time
import ball_state
import game_world
import random
import math

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
        elapsed = time.time() - boy.time
        if elapsed > 10.0:
            boy.set_state(SleepState)

    @staticmethod
    def draw(boy):
        y = 200 if boy.dir == 0 else 300
        diffx = boy.mx - boy.x
        diffy = boy.my - boy.y
        boy.rad = math.atan2(diffy, diffx)
        Boy.image.clip_composite_draw(boy.frame * 100, y, 100, 100, boy.rad, '', boy.x, boy.y, 100, 100)
        #boy.image.clip_draw(boy.frame * 100, y, 100, 100, boy.x, boy.y)

class RunState:
    @staticmethod
    def enter(boy):
        boy.time = time.time()

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def update(boy):
        elapsed = time.time() - boy.time
        mag = 2 if elapsed > 2.0 else 1
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x = max(25, min(boy.x + mag * boy.dx, 775))

    @staticmethod
    def draw(boy):
        y = 0 if boy.dir == 0 else 100
        boy.image.clip_draw(boy.frame * 100, y, 100, 100, boy.x, boy.y)

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
            y, mx, angle = 300, -25, 3.141592 / 2
        else:
            y, mx, angle = 200, +25, -3.141592 / 2
        Boy.image.clip_composite_draw(boy.frame * 100, y, 100, 100, angle, '', boy.x + mx, boy.y - 25, 100, 100)

next_state_table = {
    IdleState : {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE_DOWN: IdleState},
    RunState : {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: IdleState, LEFT_DOWN: IdleState, SPACE_DOWN: RunState},
    SleepState : {LEFT_DOWN: RunState, RIGHT_DOWN: RunState}
}

class Boy:
    image = None
    def __init__(self):
        if Boy.image == None:
            Boy.image = load_image('../image/animation_sheet.png')
        self.x = 100
        self.y = 90
        self.speed = 0
        self.dx,self.dy = 0, 0
        self.dir = 1
        self.state = IdleState
        self.set_state(IdleState)
        self.frame = 0
        self.time = 0
        self.mx, self.my = 400, 90
        self.rad = 0
    def update(self):
        self.state.update(self)

    def fire_ball(self):
        diffx = self.mx - self.x
        diffy = self.my - self.y
        self.speed = math.sqrt((diffx ** 2) + (diffy ** 2)) / 100

        mag = 1.5 if self.dir == 1 else -1.5
        mag *= random.uniform(0.5, 1.0)
        ballSpeed = mag * self.speed + math.cos(self.rad)
        ySpeed = 2 * self.speed * math.sin(self.rad)
        ball = ball_state.Ball(self.x, self.y + 70, ballSpeed, ySpeed)
        game_world.add_object(ball, game_world.layer_obstacle)

    def draw(self):
        self.state.draw(self)
    
    def handle_event(self, event):
        if event.type == SDL_MOUSEMOTION:
            self.mx, self.my = event.x, 600 - event.y
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if key_event == SPACE_DOWN or key_event == ENTER_DOWN:
                self.fire_ball()
                if self.state == SleepState:
                    self.set_state(IdleState)
                return
            if key_event == RIGHT_DOWN:
                self.dx += self.speed
                if self.dx > 0: self.dir = 1
            elif key_event == LEFT_DOWN:
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            elif key_event == RIGHT_UP:
                self.dx -= self.speed
                if self.dx < 0: self.dir = 0
            elif key_event == LEFT_UP:
                self.dx += self.speed
                if self.dx > 0: self.dir = 1

            self.set_state(IdleState if self.dx == 0 else RunState)

    def set_state(self, state):
        if self.state == state: return
        if self.state and self.state.exit:
            self.state.exit(self)
        self.state == state
        if self.state.enter:
            self.state.enter(self)
    
if __name__ == '__main__':
    main()

from pico2d import *
import  game_framework

class Castle:
    global backgroundX
    image = None

    def __init__(self):
        Castle.backgroundX = 800
        self.stage1 = load_image('resource/노을.png')
        self.stage2 = load_image('resource/저녁.png')
        self.stage3 = load_image('resource/밤.png')
        self.stage4 = load_image('resource/새벽.png')
        self.stage5 = load_image('resource/아침.png')
        self.count = 0
        Castle.image = self.stage1

    def draw(self):
        self.image.clip_draw(Castle.backgroundX, 0, 800, 600, 400, 300)

    def change(self):
        self.count += 1
        if self.count == 1:
            Castle.image = self.stage2
        elif self.count == 2:
            Castle.image = self.stage3
        elif self.count == 3:
            Castle.image = self.stage4
        elif self.count == 4:
            Castle.image = self.stage5

class Princess:
    image = None
    global state, backgroundX
    def __init__(self):
        self.rightP = load_image('resource/princess_right.png')
        self.leftP = load_image('resource/princess_left.png')
        self.frame = 0
        Princess.state = 0
        self.x, self.y = 700, 200
        Princess.image = self.leftP

    def draw(self):
       self.image.clip_draw(self.frame * 200, 0, 200, 300, self.x, self.y)

    def update(self):
        if state == 0:
            Princess.image = self.leftP
            self.x -= 50
        elif state == 1:
            Princess.image = self.rightP
            self.x += 50

        if self.x <= 400 and Castle.backgroundX >= 400:
            self.x = 400
            if state == 0:
                Castle.backgroundX -= 50
            elif state == 1:
                Castle.backgroundX += 50

        self.frame = (self.frame + 1) % 4

def enter():
    global  c, p
    open_canvas()
    c = Castle()
    p = Princess()

def draw():
    global  c, p
    c.draw()
    p.draw()
    update_canvas()

def update():
    pass

def exit():
    global c
    del c

def pause():
    pass

def resume():
    pass

def handle_events():
    global p
    global state
    events = get_events()

    for e in events:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                state = 0
                p.update()
            elif e.key == SDLK_RIGHT:
                state = 1
                p.update()

if __name__ == '__main__':
    main()

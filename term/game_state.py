from pico2d import *
import  game_framework

class Castle:
    global backgroundX, princessX, state, count
    image = None

    def __init__(self):
        Castle.backgroundX = 800
        self.stage1 = load_image('resource/노을.png')
        self.stage2 = load_image('resource/저녁.png')
        self.stage3 = load_image('resource/밤.png')
        self.stage4 = load_image('resource/새벽.png')
        self.stage5 = load_image('resource/아침.png')
        Castle.count = 0
        Castle.image = self.stage1

    def draw(self):
        self.image.clip_draw(Castle.backgroundX, 0, 800, 600, 400, 300)

    def update(self):
        if Princess.princessX <= 400 and Castle.backgroundX > 0 and Princess.state == 0:
            Princess.princessX = 400
            Castle.backgroundX -= 50
        elif Princess.princessX >= 400 and Castle.backgroundX < 800 and Princess.state == 1:
            Princess.princessX = 400
            Castle.backgroundX += 50

    def change(self):
        if Castle.count == 1:
            Castle.image = self.stage2
        elif Castle.count == 2:
            Castle.image = self.stage3
        elif Castle.count == 3:
            Castle.image = self.stage4
        elif Castle.count == 4:
            Castle.image = self.stage5

class Princess:
    image = None
    global state, backgroundX, princessX
    def __init__(self):
        self.rightP = load_image('resource/princess_right.png')
        self.leftP = load_image('resource/princess_left.png')
        self.frame = 0
        Princess.state = 0
        Princess.princessX, self.y = 700, 200
        Princess.image = self.leftP

    def draw(self):
       self.image.clip_draw(self.frame * 200, 0, 200, 300, Princess.princessX, self.y)

    def update(self):
        if Princess.state == 0 and Princess.princessX >= 100:
            if Princess.image != self.leftP:
                Princess.image = self.leftP
            Princess.princessX -= 50
        elif Princess.state == 1 and Princess.princessX <= 700:
            if Princess.image != self.rightP:
                Princess.image = self.rightP
            Princess.princessX += 50

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
    global state, princessX, backgroundX, count
    events = get_events()

    for e in events:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_LEFT:
                Princess.state = 0
                p.update()
                c.update()
            elif e.key == SDLK_RIGHT:
                Princess.state = 1
                p.update()
                c.update()

    if Castle.count % 2 == 0 and Princess.princessX <= 50:
        Princess.princessX = 50
        Princess.state = 1
        Castle.backgroundX = 0
        Castle.count += 1
        c.change()
        p.update()
    elif Castle.count % 2 == 1 and Princess.princessX >= 750:
        Princess.princessX = 750
        Princess.state = 0
        Castle.backgroundX = 800
        Castle.count += 1
        c.change()
        p.update()

if __name__ == '__main__':
    main()

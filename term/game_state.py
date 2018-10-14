from pico2d import *
import  game_framework

class Castle:
    image = None
    def __init__(self):
        self.stage1 = load_image('resource/노을.png')
        self.stage2 = load_image('resource/저녁.png')
        self.stage3 = load_image('resource/밤.png')
        self.stage4 = load_image('resource/새벽.png')
        self.stage5 = load_image('resource/아침.png')
        self.count = 0
        Castle.image = self.stage1

    def draw(self):
        self.image.draw(400, 300)

    def update(self):
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
    global rightP, leftP
    global frame, state
    global x, y
    image = None

    def __init__(self):
        self.rightP = load_image('resource/princess_right.png')
        self.leftP = load_image('resource/princess_left.png')
        self.frame = 0
        self.state = 0
        self.x, self.y = 750, 100
        Princess.image = self.leftP

    def draw(self):
       self.image.clip_draw(self.frame * 100, 0, 100, 149, self.x, self.y)

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
    pass


if __name__ == '__main__':
    main()

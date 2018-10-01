from pico2d import *
import game_framework
import title_state

time = 0.0
image = None
name = "logo_state"

def enter():
    global image
    open_canvas()
    image = load_image('../image/kpu_credit.png')

def update():
    global time
    if (time > 1.0):
        time = 0.0
        game_framework.change_state(title_state)
    delay(0.1)
    time += 0.1

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    pass
    
def exit():
    global image
    del(image)
    
if __name__ == '__main__':
    main()

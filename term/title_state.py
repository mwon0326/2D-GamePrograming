from pico2d import *
import game_framework
import game

image = None

def enter():
    global  image
    open_canvas()
    image = load_image('../image/title.png')

def update():
    pass

def draw():
    global  image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()

    for e in events:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE:
                game_framework.change_state(game)
        elif e.type == SDL_QUIT:
                game_framework.quit()

def pause():
    pass

def resume():
    pass

def exit():
    global image
    del(image)

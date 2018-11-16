from pico2d import *
import game_framework
import game_state
import logo_state
Image = None

def enter():
    global Image
    Image = logo_state.title_image

def update():
    pass

def draw():
    global Image
    clear_canvas()
    Image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()

    for e in events:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE:
                game_framework.change_state(game_state)
        elif e.type == SDL_QUIT:
                game_framework.quit()

def pause():
    pass

def resume():
    pass

def exit():
    global Image
    del(Image)

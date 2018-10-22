from pico2d import *
import game_framework
from player_state import Princess

player = None

def enter():
    global  player
    open_canvas()
    player = Princess()

def exit():
    global  player
    del player

def update():
    pass

def resume():
    pass

def pause():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            player.handle_event(event)

def draw():
    clear_canvas()
    player.draw()
    update_canvas()
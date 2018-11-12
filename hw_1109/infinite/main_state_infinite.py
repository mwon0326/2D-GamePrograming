from pico2d import *
import game_world
import game_framework
from boys_state import Boy
from background import Infinite
import title_state

boy = None
bg = None

def enter():
    global boy
    boy = Boy()
    bg = Infinite()

    boy.bg = bg
    bg.target = boy
    
    game_world.add_object(bg, game_world.layer_bg)
    game_world.add_object(boy, game_world.layer_player)

def exit():
    game_world.clear()

def update():
    game_world.update()
    delay(0.03)

def draw():
    clear_canvas()
    game_world.draw()
    update_canvas()

def handle_events():
    global boy
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        else:
            boy.handle_event(e)

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()

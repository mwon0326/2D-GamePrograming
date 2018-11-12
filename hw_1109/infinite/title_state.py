from pico2d import *
import game_framework
import main_state_infinite

name = "title_state"
image = None

def enter():
    global image
    image = load_image('../../image/title.png')

def update():
    pass

def draw():
    global image
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                game_framework.quit()
            elif e.key == SDLK_SPACE:
                game_framework.push_state(main_state_infinite)
            
def pause():
    pass

def resume():
    global image
    image = load_image('../../image/title.png')
    
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def exit():
    global image    
    del(image)

if __name__ == '__main__':
    main()

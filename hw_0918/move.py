from pico2d import *
import math

x = 400
y = 90
x2, y2 = x, y
speed = 10

def hanble_events():
    global running
    global x, y
    events = get_events()

    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            x = e.x
            y = 600 - e.y

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

running = True
frame = 0
while running:
    clear_canvas()
    grass.draw(400,30)
    if x2 < x:
        x2 += speed
        if x2 > x:
            x2 = x
    if x2 > x:
        x2 -= speed
        if x2 < x:
            x2 = x
    if y2 < y:
        y2 += speed
        if y2 > y:
            y2 = y
    if y2 > y:
        y2 -= speed
        if y2 < y:
            y2 = y
    character.clip_draw(frame * 100, 0, 100, 100, x2, y2)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.025)
    hanble_events()

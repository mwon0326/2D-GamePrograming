from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

cycle = 0
x = 0
y = 90
frame = 0
r = 210
pi = math.pi / 180
angle = 270

while True:
    if cycle == 0 :  
        while (x < 750):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 5
            delay(0.025)
        while (x >= 750 & y < 550):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y += 5
            delay(0.025)
        while (x > 50):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x -= 5
            delay(0.025)
        while (y >= 90):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            y -= 5
            delay(0.025)
        cycle = 1
        while (x <= 400):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
            update_canvas()
            frame = (frame + 1) % 8
            x += 5
            delay(0.025)
    if cycle == 1 :
        while (angle <= 360):
            clear_canvas()
            grass.draw(400,30)
            cx = math.cos(angle * pi) * r
            cy = math.sin(angle * pi) * r
            character.clip_draw(frame * 100, 0, 100, 100, 400 + cx, 300 + cy)
            update_canvas()
            frame = (frame + 1) % 8
            angle += 5
            delay(0.025)
        angle = 0
        while (angle <= 270):
            clear_canvas()
            grass.draw(400,30)
            cx = math.cos(angle * pi) * r
            cy = math.sin(angle * pi) * r
            character.clip_draw(frame * 100, 0, 100, 100, 400 + cx, 300 + cy)
            update_canvas()
            frame = (frame + 1) % 8
            angle += 5
            delay(0.025)
        cycle = 0

        

        

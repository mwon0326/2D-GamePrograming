from pico2d import *
import game_framework
from player_state import Princess
from background_state import Castle
from image_state import BackGround
from fire_state import  Fire
import json

player = None
fire = None
background = None
cur_event = None
level = 1
data = None

CHARACTER_MOVE, BACKGROUND_MOVE = range(2)
RIGHT_MOVE, LEFT_MOVE, LEFT_STOP, RIGHT_STOP = range(4)

dir_table = {
    RIGHT_MOVE : 0,
    LEFT_MOVE: 1,
    RIGHT_STOP : 2,
    LEFT_STOP : 3
}

def enter():
    global  player, background, image, fire
    global  cur_event
    global level
    global  data

    open_canvas()
    player = Princess()
    background = Castle()
    image = BackGround()
    level = 1
    fire = [Fire() for i in range(level * 7)]

    fh = open('start_state.json')
    data = json.load(fh)

    player.x = data['LEFT']['x']
    player.frame = data['LEFT']['frame']
    player.dir = data['LEFT']['dir']

    background.image = image.stage1
    background.dir = data['LEFT']['dir']
    background.x = data['LEFT']['backX']

    cur_event = data['LEFT']['StartState']

def exit():
    global  player, background
    del player
    del background

def update():
    global fire
    for f in fire:
        f.update()
    delay(0.025)

def resume():
    pass

def pause():
    pass

def change_event():
    global  player, background
    global  cur_event
    if player.dir == dir_table[LEFT_MOVE] and player.x <= 400 and cur_event == 'CHARACTER_MOVE' and background.x >= 800:
        player.x = 400
        cur_event = 'BACKGROUND_MOVE'
    elif player.dir == dir_table[RIGHT_MOVE] and player.x >= 400 and cur_event == 'CHARACTER_MOVE' and background.x <= 0:
        player.x = 400
        cur_event = 'BACKGROUND_MOVE'
    elif player.dir == dir_table[LEFT_MOVE] and background.x <= 0 and cur_event == 'BACKGROUND_MOVE':
        background.x = 0
        cur_event = 'CHARACTER_MOVE'
    elif player.dir == dir_table[RIGHT_MOVE] and background.x >= 800 and cur_event == 'BACKGROUND_MOVE':
        background.x = 800
        cur_event = 'CHARACTER_MOVE'

def move():
    global player, background
    global cur_event
    global level

    if cur_event == 'CHARACTER_MOVE':
        player.move()
    elif cur_event == 'BACKGROUND_MOVE':
        background.move()
        player.motion()

    if player.x <= 100 and player.dir == dir_table[LEFT_MOVE]:
        player.x = 100
        player.motion()
    elif player.x >= 700 and player.dir == dir_table[RIGHT_MOVE]:
        player.x = 700
        player.motion()

    if player.x <= 100 and level % 2 == 1:
        level = level + 1
        change_level()
    elif player.x >= 700 and level % 2 == 0:
        level = level + 1
        change_level()

    change_event()

def change_level():
    global player, background, image
    global cur_event
    global level
    if level % 2 == 1:
        player.x = data['LEFT']['x']
        player.frame = data['LEFT']['frame']
        player.dir = data['LEFT']['dir']
        background.dir = data['LEFT']['dir']
        background.x = data['LEFT']['backX']
        cur_event = data['LEFT']['StartState']
    elif level % 2 == 0:
        player.x = data['RIGHT']['x']
        player.frame = data['RIGHT']['frame']
        player.dir = data['RIGHT']['dir']
        background.dir = data['RIGHT']['dir']
        background.x = data['RIGHT']['backX']
        cur_event = data['RIGHT']['StartState']

    if level == 2:
        background.image = image.stage2
    elif level == 3:
        background.image = image.stage3
    elif level == 4:
        background.image = image.stage4
    elif level == 5:
        background.image = image.stage5

def handle_events():
    global player, background
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                player.dir = dir_table[RIGHT_MOVE]
                background.dir = dir_table[RIGHT_MOVE]
                move()
            elif event.key == SDLK_LEFT:
                player.dir = dir_table[LEFT_MOVE]
                background.dir = dir_table[LEFT_MOVE]
                move()
            elif event.key == SDLK_DOWN:
                if player.dir == dir_table[LEFT_MOVE]:
                    player.dir = dir_table[LEFT_STOP]
                elif player.dir == dir_table[RIGHT_MOVE]:
                    player.dir = dir_table[RIGHT_STOP]
                elif player.dir == dir_table[LEFT_STOP]:
                    player.dir = dir_table[LEFT_STOP]
                else:
                    player.dir = dir_table[RIGHT_STOP]

def draw():
    global player, background, fire
    clear_canvas()
    background.draw()
    player.draw()
    for f in fire:
        f.draw()
    update_canvas()
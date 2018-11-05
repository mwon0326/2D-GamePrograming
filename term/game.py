from pico2d import *
import game_framework
from player_state import Princess
from background_state import Castle
from image_state import BackGround
from fire_state import Fire
from background_state import Menu
from image_state import NPCImage
from npc_state import NPC
from npc_state import Item

import json
import time

player = None
fire = None
background = None
npc = None
menu = None
cur_event = None
npc_image = None
item = None
level = 1
data = None
time = 0
cur_time = 0

CHARACTER_MOVE, BACKGROUND_MOVE = range(2)
RIGHT_MOVE, LEFT_MOVE, LEFT_STOP, RIGHT_STOP = range(4)

dir_table = {
    RIGHT_MOVE : 0,
    LEFT_MOVE: 1,
    RIGHT_STOP : 2,
    LEFT_STOP : 3
}

def enter():
    global player, background, image, fire, menu, npc, npc_image, item
    global cur_event
    global level, time, cur_time
    global data

    open_canvas()
    player = Princess()
    background = Castle()
    image = BackGround()
    menu = Menu()
    npc = NPC()
    npc_image = NPCImage()
    item = Item()

    level = 1
    fire = [Fire() for i in range(level * 4)]

    fh = open('start_state.json')
    data = json.load(fh)

    player.x = data['LEFT']['x']
    player.frame = data['LEFT']['frame']
    player.dir = data['LEFT']['dir']

    background.image = image.stage1
    background.dir = data['LEFT']['dir']
    background.x = data['LEFT']['backX']

    cur_event = data['LEFT']['StartState']
    time = 0
    cur_time = pico2d.get_time()

    npc.image = npc_image.npc_image
    npc.cartoon = npc_image.npc_bubble
    npc.present = npc_image.item1

def exit():
    global  player, background, image, fire, menu
    del player
    del background
    del image
    del fire
    del menu

def update():
    global fire, player, menu, npc
    global cur_time, time
    for f in fire:
        f.update()
        if collide(player, f, player.dir, 1):
            print("충돌")
        elif collide(player, f, player.dir, 2):
            print("충돌")
        elif collide(player, f, player.dir, 3):
            print("충돌")

    t = get_time()
    if t - cur_time >= 1:
        cur_time = t
        time = time + 1
        menu.time = time
        npc.time = time

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
    global player, background, image, fire, menu, npc_image, npc
    global cur_event,cur_time, time
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
        npc.present = npc_image.item2
    elif level == 3:
        background.image = image.stage3
        npc.present = npc_image.item3
    elif level == 4:
        background.image = image.stage4
        npc.present = npc_image.item4
    elif level == 5:
        background.image = image.stage5
        npc.present = npc_image.item5

    for f in fire:
        f.change_stage()

    time = 0
    menu.time = time
    cur_time = get_time()

def handle_events():
    global player, background, item
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
        item.event_hanble(event)

def draw():
    global player, background, fire, npc, item
    clear_canvas()
    background.draw()
    player.draw()
    for f in fire:
        f.draw()
        f.draw_bb()
    menu.draw()
    if player.dir == dir_table[LEFT_MOVE] or player.dir == dir_table[LEFT_STOP]:
        player.draw_face_left_bb()
        player.draw_crown_left_bb()
        player.draw_dress_left_bb()
    else:
        player.draw_face_right_bb()
        player.draw_crown_right_bb()
        player.draw_dress_right_bb()
    npc.draw()
    item.draw()
    update_canvas()

def collide(a, b, state, num):
    left_a, bottom_a, right_a, top_a = a.get_bb(state, num)
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if state == 2 or state == 3 : return False
    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return  False
    if bottom_a > top_b : return  False
    return True
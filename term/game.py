from pico2d import *
import game_framework
from player_state import Player
from background_state import BackGround
from image_state import BackGroundImage
from fire_state import Fire
from background_state import ItemBox
from image_state import NPCImage
from image_state import ItemImage
from npc_state import NPC
from item_state import Item
from image_state import StageImage

import json
import time

player = None
fire = None
background = None
npc = None
menu = None
stage = None
cur_event = None
npc_image = None
back_image = None
item_image = None
item = None
level = 1
data = None
time = 0
cur_time = 0
move_key = False

CHARACTER_MOVE, BACKGROUND_MOVE = range(2)
RIGHT_MOVE, LEFT_MOVE, LEFT_STOP, RIGHT_STOP = range(4)

dir_table = {
    RIGHT_MOVE : 0,
    LEFT_MOVE: 1,
    RIGHT_STOP : 2,
    LEFT_STOP : 3
}

def enter():
    global player, background, back_image, fire, menu, npc, npc_image, item, item_image
    global cur_event
    global level, time, cur_time
    global data
    global move_key

    open_canvas()
    player = Player()
    background = BackGround()
    back_image = BackGroundImage()
    menu = ItemBox()
    npc = NPC()
    npc_image = NPCImage()
    item = Item()
    item_image = ItemImage()

    level = 1
    fire = [Fire() for i in range(level * 4)]

    fh = open('start_state.json')
    data = json.load(fh)

    player.x = data['LEFT']['x']
    player.frame = data['LEFT']['frame']
    player.dir = data['LEFT']['dir']

    background.image = back_image.stage1
    background.dir = data['LEFT']['dir']
    background.x = data['LEFT']['backX']

    cur_event = data['LEFT']['StartState']
    time = 0
    cur_time = get_time()

    npc.image = npc_image.npc_image
    npc.cartoon = npc_image.npc_bubble
    npc.cartoon2 = npc_image.npc_bubble2
    npc.present = item_image.item1

    move_key = False

def exit():
    global player, background, back_image, fire, menu
    del player
    del background
    del back_image
    del fire
    del menu

def update():
    global fire, player, menu, npc, item, npc_image
    global cur_time, time
    global move_key

    for f in fire:
        f.update()
        if f.player_collide(player, f, player.dir, 1):
            print("충돌")
        elif f.player_collide(player, f, player.dir, 2):
            print("충돌")
        elif f.player_collide(player, f, player.dir, 3):
            print("충돌")

    t = get_time()
    if t - cur_time >= 1:
        cur_time = t
        time = time + 1
        menu.time = time
        npc.time = time
        npc.timer()

    if item.npc_collide(npc, item, level) and npc.is_draw:
        npc.image = npc_image.npc_image2
        npc.stop()
        item.stop()

    if npc.npc_time == 0 and item.npc_collide(npc, item, level) == False:
        npc.stop()

    if move_key:
        move()
    delay(0.025)

def resume():
    pass

def pause():
    pass

def change_event():
    global player, background
    global cur_event
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
    global player, background, back_image, fire, menu, item_image, npc, npc_image
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
        background.image = back_image.stage2
        npc.present = item_image.item2
    elif level == 3:
        background.image = back_image.stage3
        npc.present = item_image.item3
    elif level == 4:
        background.image = back_image.stage4
        npc.present = item_image.item4
    elif level == 5:
        background.image = back_image.stage5
        npc.present = item_image.item5

    for f in fire:
        f.change_stage()

    time = 0
    npc.change_level(level)
    npc.image = npc_image.npc_image

    menu.time = time
    cur_time = get_time()

def handle_events():
    global player, background, item
    global move_key

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
                move_key = True
            elif event.key == SDLK_LEFT:
                player.dir = dir_table[LEFT_MOVE]
                background.dir = dir_table[LEFT_MOVE]
                move_key = True
            elif event.key == SDLK_DOWN:
                if player.dir == dir_table[LEFT_MOVE]:
                    player.dir = dir_table[LEFT_STOP]
                elif player.dir == dir_table[RIGHT_MOVE]:
                    player.dir = dir_table[RIGHT_STOP]
                elif player.dir == dir_table[LEFT_STOP]:
                    player.dir = dir_table[LEFT_STOP]
                else:
                    player.dir = dir_table[RIGHT_STOP]
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                move_key = False
            elif event.key == SDLK_LEFT:
                move_key = False
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
    npc.draw_bb()
    item.draw()
    update_canvas()

from pico2d import *
import game_framework
from player import Player
from fire import Fire
from background import *
from npc import NPC
from item import Item
import title_state
import json
import time
import logo_state

player = None
fire = None
background = None
npc = None
menu = None
stage = None
cur_event = None
fail_stage = None
item = None
level = 1
data = None
time = 0
cur_time = 0
move_key = False
control = False
fail = False

CHARACTER_MOVE, BACKGROUND_MOVE = range(2)
RIGHT_MOVE, LEFT_MOVE, LEFT_STOP, RIGHT_STOP = range(4)

dir_table = {
    RIGHT_MOVE : 0,
    LEFT_MOVE: 1,
    RIGHT_STOP : 2,
    LEFT_STOP : 3
}

def enter():
    global player, background, fire, menu, npc, item, stage, fail_stage
    global cur_event
    global level, time, cur_time, timer
    global data
    global move_key, fail, control

    player = Player()
    background = BackGround()
    menu = ItemBox()
    npc = NPC()
    item = Item()
    stage = Stage()
    fail_stage = Fail()
    level = 1
    fire = [Fire() for i in range(level * 4)]

    fh = open('start_state.json')
    data = json.load(fh)

    player.x = data['LEFT']['x']
    player.frame = data['LEFT']['frame']
    player.dir = data['LEFT']['dir']

    background.image = logo_state.stage1
    background.dir = data['LEFT']['dir']
    background.x = data['LEFT']['backX']

    cur_event = data['LEFT']['StartState']
    time = 0
    cur_time = get_time()
    timer = 0

    npc.image = logo_state.npc_image1
    npc.cartoon = logo_state.npc_bubble
    npc.cartoon2 = logo_state.npc_bubble2
    npc.present = logo_state.item1

    stage.stage_image = logo_state.stage1_mb
    stage.clear_image = logo_state.stage_clear_normal

    move_key = False
    control = False
    fail = False

def exit():
    pass

def update():
    global fire, player, menu, npc, item, stage
    global cur_time, time, timer, level
    global move_key, control, fail

    for f in fire:
        if control:
            f.update()
        if f.player_collide(player, f, player.dir, 1):
            control = False
            fail = True
            move_key = False
        elif f.player_collide(player, f, player.dir, 2):
            control = False
            fail = True
            move_key = False
        elif f.player_collide(player, f, player.dir, 3):
            control = False
            fail = True
            move_key = False

    t = get_time()
    if t - cur_time >= 1:
        cur_time = t
        time = time + 1
        if control:
            timer = timer + 1
        menu.time = timer
        npc.time = timer
        npc.timer()

    if time > 1 and stage.is_clear == False and fail == False:
        control = True
        stage.is_stage_draw = False

    if item.npc_collide(npc, item, level) and npc.is_draw:
        npc.is_item_collide = True
        for f in fire:
            f.speed = f.success_speed
        npc.image = logo_state.npc_image2
        npc.stop()
        item.stop()

    if npc.npc_time == 0 and npc.is_item_collide == False:
        for f in fire:
            f.speed = f.fail_speed
        npc.stop()

    if move_key:
        move()

    if stage.is_change_level:
        if level == 6:
            game_framework.quit()
        else:
            change_level()
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

def stage_clear():
    global stage, npc
    global control, move_key
    global level
    if level == 6:
        stage.clear_image = logo_state.stage_success_normal

    npc.is_item_collide = False
    stage.is_clear = True
    control = False
    move_key = False

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
        stage_clear()
    elif player.x >= 700 and level % 2 == 0:
        level = level + 1
        stage_clear()

    change_event()

def change_level():
    global player, background, fire, menu, npc,  stage
    global cur_event,cur_time, time, timer
    global level
    global control, move_key

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
        background.image = logo_state.stage2
        npc.present = logo_state.item2
        stage.stage_image = logo_state.stage2_mb
    elif level == 3:
        background.image = logo_state.stage3
        npc.present = logo_state.item3
        stage.stage_image = logo_state.stage3_mb
    elif level == 4:
        background.image = logo_state.stage4
        npc.present = logo_state.item4
        stage.stage_image = logo_state.stage4_mb
    elif level == 5:
        background.image = logo_state.stage5
        npc.present = logo_state.item5
        stage.stage_image = logo_state.stage5_mb

    for f in fire:
        f.change_stage()

    time = 0
    timer = 0
    npc.change_level(level)
    npc.image = logo_state.npc_image1

    control = False
    stage.is_stage_draw = True
    stage.is_change_level = False
    stage.is_clear = False
    stage.press = False
    stage.mouse = False

    move_key = False
    menu.time = time
    cur_time = get_time()

def handle_events():
    global player, background, item, stage, fail_stage
    global move_key, fail, control
    global timer

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        if event.type == SDL_KEYDOWN and control:
            if event.key == SDLK_RIGHT:
                player.dir = dir_table[RIGHT_MOVE]
                background.dir = dir_table[RIGHT_MOVE]
                move_key = True
            elif event.key == SDLK_LEFT:
                player.dir = dir_table[LEFT_MOVE]
                background.dir = dir_table[LEFT_MOVE]
                move_key = True
            elif event.key == SDLK_DOWN:
                move_key = False
                if player.dir == dir_table[LEFT_MOVE]:
                    player.dir = dir_table[LEFT_STOP]
                elif player.dir == dir_table[RIGHT_MOVE]:
                    player.dir = dir_table[RIGHT_STOP]
                elif player.dir == dir_table[LEFT_STOP]:
                    player.dir = dir_table[LEFT_STOP]
                else:
                    player.dir = dir_table[RIGHT_STOP]
        if event.type == SDL_KEYUP and control:
            if event.key == SDLK_RIGHT:
                move_key = False
            elif event.key == SDLK_LEFT:
                move_key = False
        if fail:
            fail_stage.event_handle(event)
        if control:
            item.event_handle(event)
        if stage.is_clear:
            stage.event_handle(event, level)


def draw():
    global player, background, fire, npc, item, stage, fail_stage
    global fail
    clear_canvas()
    background.draw()
    player.draw()
    for f in fire:
        f.draw()
        #f.draw_bb()
    menu.draw()
    '''
    if player.dir == dir_table[LEFT_MOVE] or player.dir == dir_table[LEFT_STOP]:
        player.draw_face_left_bb()
        player.draw_crown_left_bb()
        player.draw_dress_left_bb()
    else:
        player.draw_face_right_bb()
        player.draw_crown_right_bb()
        player.draw_dress_right_bb()
    '''
    npc.draw()
    #npc.draw_bb()
    item.draw()
    stage.draw()
    #stage.draw_bb()
    if fail:
        fail_stage.draw()
    update_canvas()

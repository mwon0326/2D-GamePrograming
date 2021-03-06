from pico2d import *
import game_framework
import game_world
from player import Player
from background import BackGround
from background import StateBox
import logo_state
import title_state
from fire import Fire
from life import Life
from item import Item
import json
import random
from gate import Gate
import ui
from ui import UI

GAME_READY, IN_PLAY, GAME_END, GAME_SUCCESS, GAME_OVER, GAME_START = range(6)

player = None
background = None
state_box = None
position_data = None
level = 1
life = None
life_count = 0
time = 0.0
game_state = None
open_gate = False
key_check = False

def enter():
    global player, background, state_box, life
    global position_data
    global life_count, level
    global time
    global game_state
    global is_item, key_check, protect

    player = Player()
    game_world.add_object(player, game_world.layer_player)

    background = BackGround()
    game_world.add_object(background, game_world.layer_bg)

    state_box = StateBox()
    game_world.add_object(state_box, game_world.layer_bg)

    level = 1
    life = Life()
    life_count = 5
    fd = open('start_state.json')
    position_data = json.load(fd)

    player.x = position_data['LEFT']['x']
    player.image_index = position_data['LEFT']['dir']
    player.frame = 0

    time = 0.0
    is_item = True
    key_check = False
    protect = True
    GameEnter()

def GameEnter():
    global game_state
    global level
    if game_state == GAME_END:
        game_world.remove_objects_at_layer(game_world.layer_message)

    e = UI(level, 1)
    game_state = GAME_START
    game_world.add_object(e, game_world.layer_message)
    logo_state.intro_sound.set_volume(32)
    logo_state.intro_sound.play()

def GamePlay():
    global game_state
    game_state = IN_PLAY
    game_world.remove_objects_at_layer(game_world.layer_message)
    logo_state.back_sound.set_volume(64)
    logo_state.back_sound.repeat_play()

def GameEnd():
    global game_state
    game_state = GAME_END
    e = UI(level, 2)
    game_world.add_object(e, game_world.layer_message)
    logo_state.back_sound.stop()
    logo_state.clear_sound.set_volume(32)
    logo_state.clear_sound.play()

def GameSuccess():
    global game_state
    game_state = GAME_SUCCESS
    e = UI(level, 3)
    game_world.add_object(e, game_world.layer_message)
    logo_state.back_sound.stop()
    logo_state.ending_success.set_volume(32)
    logo_state.ending_success.play()

def GameReady():
    global game_state
    game_state = GAME_READY
    e = UI(level, 5)
    game_world.add_object(e, game_world.layer_message)
    logo_state.back_sound.stop()

def GameOver():
    global game_state
    game_state = GAME_OVER
    e = UI(level, 4)
    game_world.add_object(e, game_world.layer_message)
    logo_state.back_sound.stop()
    logo_state.fail.set_volume(32)
    logo_state.fail.play()

def CreateFire():
    global level
    fire = Fire(level)
    game_world.add_object(fire, game_world.layer_obstacle)

def CreateItemBox():
    global level
    item_box = Item(level)
    if item_box.item_kind == 0:
        logo_state.key_check = 2
    elif item_box.item_kind == 3 and logo_state.is_not_protect != 2:
        logo_state.is_not_protect = 3
    item_box.x = random.randint(2, 10) * 75
    game_world.add_object(item_box, game_world.layer_item)

def CreateGate():
    global open_gate
    g = Gate()
    game_world.add_object(g, game_world.layer_gate)
    open_gate = True

def draw():
    global life, player
    global life_count
    clear_canvas()
    game_world.draw()
    life.draw(life_count)
    update_canvas()

def changeLevel():
    global player, background, life
    global level
    global time
    global game_state
    global is_item
    level += 1
    background.changeLevel(level)
    life.image_change(level)

    game_world.remove_objects_at_layer(game_world.layer_gate)
    game_world.remove_objects_at_layer(game_world.layer_item)
    game_world.remove_objects_at_layer(game_world.layer_obstacle)

    if level % 2 == 0:
        player.x = position_data['RIGHT']['x']
        player.image_index = position_data['RIGHT']['dir']
    else:
        player.x = position_data['LEFT']['x']
        player.image_index = position_data['LEFT']['dir']

    player.frame = 0
    player.dx = 0
    player.time = 0
    player.is_move = 0

    time = 0.0
    is_item = True
    logo_state.key_check = 1
    logo_state.is_not_protect = 1
    GameEnter()

t = 0
is_item = True

def update():
    global player
    global life_count, level
    global time, t
    global game_state
    global open_gate
    global is_item

    if game_state == IN_PLAY:
        time += game_framework.frame_time
        game_world.update()

        for i in game_world.objects_at_layer(game_world.layer_item):
            if i.life_get:
                life_count += 1
                if life_count >= 5:
                    life_count = 5
                game_world.remove_object(i)
            elif i.key_get:
                CreateGate()
                i.key_get = False

        for f in game_world.objects_at_layer(game_world.layer_obstacle):
            for p in range(1, 4):
                if f.collide(player, f, player.image_index, p) and logo_state.is_not_protect == 1:
                    logo_state.collide_sound.set_volume(32)
                    logo_state.collide_sound.play()
                    life_count -= 1
                    game_world.remove_object(f)
                    if life_count == 0:
                        GameOver()

        fire_count = game_world.count_at_layer(game_world.layer_obstacle)
        if fire_count < level + 2:
            CreateFire()

        item_count = game_world.count_at_layer(game_world.layer_item)
        if item_count < 5 and is_item :
            CreateItemBox()
            t = time
            is_item = False

        if time - t > level + 3:
            is_item = True

    delay(0.03)

def handle_events():
    global player
    global game_state
    global open_gate
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT: game_framework.quit()
        if game_state == IN_PLAY:
            if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                GameReady()
            else :
                player.handle_events(e)
                if open_gate:
                    for g in game_world.objects_at_layer(game_world.layer_gate):
                        is_next = g.handle_events(e, player, player.image_index, 3)
                        if is_next:
                            if level < 5:
                                GameEnd()
                            else:
                                GameSuccess()
                            open_gate = False

            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_SPACE:
                    for i in game_world.objects_at_layer(game_world.layer_item):
                        if i.collide(player, i, player.image_index, 3):
                            i.is_press = True
            elif e.type == SDL_KEYUP:
                if e.key == SDLK_SPACE:
                    for i in game_world.objects_at_layer(game_world.layer_item):
                        i.is_press = False
        elif game_state == GAME_START:
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_SPACE:
                    GamePlay()
        elif game_state == GAME_END:
            for u in game_world.objects_at_layer(game_world.layer_message):
                is_change = u.handle_events(e)
                if is_change: changeLevel()
        elif game_state == GAME_SUCCESS:
            for u in game_world.objects_at_layer(game_world.layer_message):
                is_success = u.handle_events(e)
                if is_success : game_framework.change_state(title_state)
        elif game_state == GAME_OVER:
            for u in game_world.objects_at_layer(game_world.layer_message):
                is_fail = u.handle_events(e)
                if is_fail : game_framework.change_state(title_state)
        elif game_state == GAME_READY:
            for u in game_world.objects_at_layer(game_world.layer_message):
                is_pause = u.handle_events(e)
                if is_pause: GamePlay()

def exit():
    global player, background, state_box, life
    global level
    global life_count
    global game_state
    global position_data
    global time

    del player
    del background
    del state_box
    del life

    game_world.remove_objects_at_layer(game_world.layer_player)
    game_world.remove_objects_at_layer(game_world.layer_bg)
    game_world.remove_objects_at_layer(game_world.layer_message)
    game_world.remove_objects_at_layer(game_world.layer_item)
    game_world.remove_objects_at_layer(game_world.layer_obstacle)
    game_world.remove_objects_at_layer(game_world.layer_gate)
    position_data = None





from pico2d import *
import game_framework
import game_world
from player import Player
from background import BackGround
from background import StateBox
import title_state
from fire import Fire
from life import Life
from item import Item
import json
import random
from gate import Gate
import ui

GAME_READY, IN_PLAY, GAME_END, GAME_SUCCESS, GAME_OVER = range(5)

player = None
background = None
state_box = None
position_data = None
level = 1
life = None
life_count = 0
time = 0.0
random_list = []
game_state = None

def enter():
    global player, background, state_box, life
    global position_data
    global life_count
    global time
    global game_state

    player = Player()
    game_world.add_object(player, game_world.layer_player)

    background = BackGround()
    game_world.add_object(background, game_world.layer_bg)

    state_box = StateBox()
    game_world.add_object(state_box, game_world.layer_bg)

    life = Life()
    life_count = 5
    fd = open('start_state.json')
    position_data = json.load(fd)

    player.x = position_data['LEFT']['x']
    player.image_index = position_data['LEFT']['dir']
    player.frame = 0

    time = 0.0
    GameEnter()

def GameEnter():
    global game_state
    global level
    if game_state == GAME_END:
        game_world.remove_objects_at_layer(game_world.layer_message)

    e = ui.GameStart(level)
    game_state = GAME_READY
    game_world.add_object(e, game_world.layer_message)

def GamePlay():
    global game_state
    game_state = IN_PLAY
    game_world.remove_objects_at_layer(game_world.layer_message)

def GameEnd():
    global game_state
    game_state = GAME_END
    e = ui.GameEnd()
    game_world.add_object(e, game_world.layer_message)

def GameSuccess():
    global game_state
    game_state = GAME_SUCCESS
    e = ui.GameSuccess()
    game_world.add_object(e, game_world.layer_message)

def GameOver():
    global game_state
    game_state = GAME_OVER
    e = ui.GameOver()
    game_world.add_object(e, game_world.layer_message)

def CreateFire():
    global level
    fire = Fire(level)
    game_world.add_object(fire, game_world.layer_obstacle)

def CreateItemBox():
    global level
    item_box = Item(level)
    item_box.x = random.randint(2, 10) * 75
    game_world.add_object(item_box, game_world.layer_item)

def CreateGate():
    g = Gate()
    game_world.add_object(g, game_world.layer_gate)

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
    GameEnter()

def update():
    global player
    global life_count, level
    global time
    global game_state
    global random_list

    if game_state == IN_PLAY:
        time += game_framework.frame_time
        game_world.update()
        for f in game_world.objects_at_layer(game_world.layer_obstacle):
            for p in range(1, 4):
                if f.collide(player, f, player.image_index, p):
                    life_count -= 1
                    game_world.remove_object(f)
                    if life_count == 0:
                        GameOver()

        fire_count = game_world.count_at_layer(game_world.layer_obstacle)
        if fire_count < level + 2:
            CreateFire()

        for i in game_world.objects_at_layer(game_world.layer_item):
            if i.life_get:
                life_count += 1
                if life_count >= 5:
                    life_count = 5
                game_world.remove_object(i)
            if i.key_get:
                CreateGate()
                i.key_get = False

        item_count = game_world.count_at_layer(game_world.layer_item)
        if level * 5 < time and item_count < 1:
            CreateItemBox()

        for g in game_world.objects_at_layer(game_world.layer_gate):
            for p in range(1, 4):
                if g.collide(player, g, player.image_index, p):
                    if level < 5: GameEnd()
                    else : GameSuccess()
    delay(0.03)

def handle_events():
    global player
    global game_state
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT: game_framework.quit()
        if game_state == IN_PLAY:
            player.handle_events(e)
            if e.type == SDL_KEYDOWN:
                if e.key == SDLK_SPACE:
                    for i in game_world.objects_at_layer(game_world.layer_item):
                        if i.collide(player, i, player.image_index, 3):
                            i.press_time += game_framework.frame_time
        elif game_state == GAME_READY:
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

def exit():
    pass






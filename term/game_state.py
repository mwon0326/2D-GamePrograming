from pico2d import *
import game_framework
import game_world
from player import Player
from background import BackGround
from background import StateBox
from fire import Fire
from life import Life
from item import Item
import json
import random
from gate import Gate

READY, IN_PLAY = range(2)

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
    game_state = READY

def CreateFire():
    global level
    fire = Fire(level)
    game_world.add_object(fire, game_world.layer_obstacle)

def CreateItemBox():
    global level
    item_box = Item(level)
    item_box.x = random.randint(2, 10) * 75
    while item_box.x in random_list:
        item_box.x = random.randint(2, 10) * 75
    random_list.append(item_box.x)
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
    for i in game_world.objects_at_layer(game_world.layer_item):
        i.draw_bb()

    for g in game_world.objects_at_layer(game_world.layer_gate):
        g.draw_bb()
    update_canvas()

def changeLevel():
    global player, background
    global level
    global time
    global game_state
    level += 1
    background.changeLevel(level)

    for f in game_world.objects_at_layer(game_world.layer_obstacle):
        game_world.remove_object(f)

    for i in game_world.objects_at_layer(game_world.layer_item):
        game_world.remove_object(i)

    for g in game_world.objects_at_layer(game_world.layer_gate):
        game_world.remove_object(g)

    if level % 2 == 0:
        player.x = position_data['RIGHT']['x']
        player.image_index = position_data['RIGHT']['dir']
    else:
        player.x = position_data['LEFT']['x']
        player.image_index = position_data['LEFT']['dir']

    player.frame = 0

    time = 0.0
    game_state = READY

def update():
    global player
    global life_count, level
    global time
    global game_state

    if game_state == IN_PLAY:
        time += game_framework.frame_time
        game_world.update()
        for f in game_world.objects_at_layer(game_world.layer_obstacle):
            for p in range(1, 4):
                if f.collide(player, f, player.image_index, p):
                    life_count -= 1
                    game_world.remove_object(f)

        fire_count = game_world.count_at_layer(game_world.layer_obstacle)
        if fire_count < level + 3:
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
                    if level < 5: changeLevel()
    delay(0.03)

def handle_events():
    global player
    events = get_events()
    for e in events:
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE:
                for i in game_world.objects_at_layer(game_world.layer_item):
                    if i.collide(player, i, player.image_index, 3):
                        i.press_time += game_framework.frame_time
        player.handle_events(e)




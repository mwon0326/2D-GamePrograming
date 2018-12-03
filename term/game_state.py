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

player = None
background = None
state_box = None
position_data = None
level = 1
life = None
life_count = 0
time = 0.0
random_list = []

def enter():
    global player, background, state_box, life
    global position_data
    global life_count
    global time
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

def CreateFire():
    global level
    fire = Fire(level)
    game_world.add_object(fire, game_world.layer_obstacle)

def CreateItemBox():
    item_box = Item()
    item_box.x = random.randint(2, 10) * 75
    while item_box.x in random_list:
        item_box.x = random.randint(2, 10) * 75
    random_list.append(item_box.x)
    game_world.add_object(item_box, game_world.layer_item)

def draw():
    global life, player
    global life_count
    clear_canvas()
    game_world.draw()
    life.draw(life_count)
    for i in game_world.objects_at_layer(game_world.layer_item):
        i.draw_bb()

    update_canvas()

def update():
    global player
    global life_count, level
    global time

    time += game_framework.frame_time
    game_world.update()
    for f in game_world.objects_at_layer(game_world.layer_obstacle):
        for p in range(3):
            if f.collide(player, f, player.image_index, p):
                life_count -= 1
                break
    fire_count = game_world.count_at_layer(game_world.layer_obstacle)
    if fire_count < level + 3:
        CreateFire()

    item_count = game_world.count_at_layer(game_world.layer_item)
    if level * 5 < time and item_count < 5:
        CreateItemBox()
    delay(0.03)

def handle_events():
    global player
    events = get_events()
    for e in events:
        player.handle_events(e)




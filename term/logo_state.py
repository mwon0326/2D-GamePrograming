import game_framework
from pico2d import *
import title_state

stage1, stage2, stage3, stage4, stage5 = None, None, None, None, None
npc_image1 = None
black, red, pink, yellow, blue = None, None, None, None, None
f = None
stage1_mb, stage2_mb, stage3_mb, stage4_mb, stage5_mb = None, None, None, None, None
stage_clear_press, stage_clear_normal, stage_clear_enter = None, None, None
stage_fail_normal, stage_fail_enter, stage_fail_press = None, None, None
stage_success_normal, stage_success_enter, stage_success_press = None, None, None
fire_image = None
item_box = None
menu_image = None
title_image = None
player_image = None
progress_bar = None
key_image, power_up = None, None
gate_image = None
start_ui_normal, start_ui_enter, start_ui_press = None, None, None
back_sound, effect_sound, intro_sound, clear_sound, ending_success, fail = None, None, None, None, None, None
pause_normal, pause_enter, pause_press = None, None, None
collide_sound, power_sound = None, None
time = 0.0
image = None
name = "logo_state"

is_not_protect, key_check = None, None
def enter():
    global stage1, stage2, stage3, stage4, stage5
    global npc_image1
    global black, pink, yellow, red, blue
    global f
    global stage1_mb, stage2_mb, stage3_mb, stage4_mb, stage5_mb
    global stage_clear_press, stage_clear_normal, stage_clear_enter
    global stage_fail_normal, stage_fail_enter, stage_fail_press
    global stage_success_normal, stage_success_enter, stage_success_press
    global image, fire_image, menu_image, title_image
    global player_image, item_box, progress_bar, key_image, gate_image, power_up
    global start_ui_enter, start_ui_normal, start_ui_press
    global back_sound, effect_sound, intro_sound, clear_sound,ending_success, fail, collide_sound, power_sound
    global is_not_protect, key_check
    global pause_normal, pause_enter, pause_press

    pause_normal = load_image('resource/pause_normal.png')
    pause_enter = load_image('resource/pause_enter.png')
    pause_press = load_image('resource/pause_press.png')

    image = load_image('resource/kpu_credit.png')
    player_image = load_image('resource/animation.png')
    gate_image = load_image('resource/gate.png')

    stage1 = load_image('resource/노을.png')
    stage2 = load_image('resource/저녁.png')
    stage3 = load_image('resource/밤.png')
    stage4 = load_image('resource/새벽.png')
    stage5 = load_image('resource/아침.png')

    npc_image1 = load_image('resource/npc.png')

    black = load_image('resource/item_black.png')
    pink= load_image('resource/item_pink.png')
    yellow = load_image('resource/item_yellow.png')
    red = load_image('resource/item_red.png')
    blue = load_image('resource/item_blue.png')

    f = load_font('resource/DIEHLDA.ttf', 25)

    stage1_mb = load_image('resource/stage1.png')
    stage2_mb = load_image('resource/stage2.png')
    stage3_mb = load_image('resource/stage3.png')
    stage4_mb = load_image('resource/stage4.png')
    stage5_mb = load_image('resource/stage5.png')
    stage_clear_normal = load_image('resource/stageC.png')
    stage_clear_enter = load_image('resource/stageCS.png')
    stage_clear_press = load_image('resource/stageP.png')
    stage_success_normal = load_image('resource/stage_success_normal.png')
    stage_success_enter = load_image('resource/stage_success_enter.png')
    stage_success_press = load_image('resource/stage_success_press.png')
    stage_fail_normal = load_image('resource/fail_normal.png')
    stage_fail_enter = load_image('resource/fail_enter.png')
    stage_fail_press = load_image('resource/fail_press.png')

    menu_image = load_image('resource/menu.png')
    fire_image = load_image('resource/fire.png')
    title_image = load_image('resource/title.png')
    item_box = load_image('resource/item_box.png')

    progress_bar = load_image('resource/progress_bar.png')
    key_image = load_image('resource/key.png')

    start_ui_normal = load_image('resource/start_ui_normal.png')
    start_ui_enter = load_image('resource/start_ui_enter.png')
    start_ui_press = load_image('resource/start_ui_press.png')

    effect_sound = load_wav('resource/item.wav')
    back_sound = load_music('resource/back.mp3')
    intro_sound = load_wav('resource/success.wav')
    clear_sound = load_wav('resource/clear.wav')
    ending_success = load_wav('resource/victory.wav')
    fail = load_wav('resource/fail.wav')
    collide_sound = load_wav('resource/collide.wav')

    power_up = load_image('resource/item_power1.png')
    power_sound = load_wav('resource/jump.wav')

    is_not_protect = 1
    key_check = 1

def exit():
    pass

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    global time
    if (time > 1.0):
        time = 0.0
        game_framework.change_state(title_state)
    delay(0.1)
    time += 0.1

def resume():
    pass

def pause():
    pass

def handle_events():
    events = get_events()
    pass

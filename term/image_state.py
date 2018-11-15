from pico2d import *
import game_framework

class BackGroundImage:
    def __init__(self):
        self.stage1 = load_image('resource/노을.png')
        self.stage2 = load_image('resource/저녁.png')
        self.stage3 = load_image('resource/밤.png')
        self.stage4 = load_image('resource/새벽.png')
        self.stage5 = load_image('resource/아침.png')

class NPCImage:
    def __init__(self):
        self.npc_image = load_image('resource/npc.png')
        self.npc_image2 = load_image('resource/npc_clear.png')
        self.npc_bubble = load_image('resource/말풍선.png')
        self.npc_bubble2 = load_image('resource/말풍선2.png')

class ItemImage:
    def __init__(self):
        self.item1 = load_image('resource/item_black.png')
        self.item2 = load_image('resource/item_pink.png')
        self.item3 = load_image('resource/item_yellow.png')
        self.item4 = load_image('resource/item_red.png')
        self.item5 = load_image('resource/item_blue.png')

class Font:
    def __init__(self):
        self.f = load_font('resource/DIEHLDA.ttf', 25)

class StageImage:
    def __init__(self):
        self.stage1 = load_image('resource/stage1.png')
        self.stage2 = load_image('resource/stage2.png')
        self.stage3 = load_image('resource/stage3.png')
        self.stage4 = load_image('resource/stage4.png')
        self.stage5 = load_image('resource/stage5.png')
        self.stage_clear_normal = load_image('resource/stageC.png')
        self.stage_clear_enter = load_image('resource/stageCS.png')
        self.stage_clear_press = load_image('resource/stageP.png')
        self.stage_success_normal = load_image('resource/stage_success_normal.png')
        self.stage_success_enter = load_image('resource/stage_success_enter.png')
        self.stage_success_press = load_image('resource/stage_success_press.png')
        self.stage_fail_normal = load_image('resource/fail_normal.png')
        self.stage_fail_enter = load_image('resource/fail_enter.png')
        self.stage_fail_press = load_image('resource/fail_press.png')


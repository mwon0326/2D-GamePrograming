from pico2d import *
import game_framework

class BackGround:
    def __init__(self):
        self.stage1 = load_image('resource/노을.png')
        self.stage2 = load_image('resource/저녁.png')
        self.stage3 = load_image('resource/밤.png')
        self.stage4 = load_image('resource/새벽.png')
        self.stage5 = load_image('resource/아침.png')

class NPCImage:
    def __init__(self):
        self.item1 = load_image('resource/item_black.png')
        self.item2 = load_image('resource/item_pink.png')
        self.item3 = load_image('resource/item_yellow.png')
        self.item4 = load_image('resource/item_red.png')
        self.item5 = load_image('resource/item_blue.png')
        self.npc_image = load_image('resource/npc.png')
        self.npc_image2 = load_image('resource/npc_clear.png')
        self.npc_bubble = load_image('resource/말풍선.png')

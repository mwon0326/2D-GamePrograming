from pico2d import *
import game_framework

class BackGround:
    def __init__(self):
        self.stage1 = load_image('resource/노을.png')
        self.stage2 = load_image('resource/저녁.png')
        self.stage3 = load_image('resource/밤.png')
        self.stage4 = load_image('resource/새벽.png')
        self.stage5 = load_image('resource/아침.png')
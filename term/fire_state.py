from pico2d import *
import game_framework
import random

STAGE1, STAGE2, STAGE3, STAGE4, STAGE5 = range(5)
MIN, MAX = range(2)
speed_table = {
                STAGE1 : {MIN : 5, MAX : 8},
                STAGE2 : {MIN : 7, MAX : 9},
                STAGE3 : {MIN : 9, MAX : 11},
                STAGE4 : {MIN : 11, MAX : 13},
                STAGE5 : {MIN : 13, MAX : 15}}

next_stage_table = {STAGE1 : STAGE2, STAGE2 : STAGE3, STAGE3 : STAGE4, STAGE4 : STAGE5}

class Fire:
    image = None

    def __init__(self):
        if Fire.image == None:
            Fire.image = load_image('resource/fire.png')
        self.x = random.randint(150, 650)
        self.y = 575
        self.minSpeed = speed_table[STAGE1][MIN]
        self.maxSpeed = speed_table[STAGE1][MAX]
        self.cur_stage = STAGE1
        self.speed = random.randint(self.minSpeed, self.maxSpeed)
        self.next_stage = None

    def draw(self):
        Fire.image.draw(self.x, self.y)

    def change_stage(self):
        self.next_stage = next_stage_table[self.cur_stage]
        self.minSpeed = speed_table[self.next_stage][MIN]
        self.maxSpeed = speed_table[self.next_stage][MAX]
        self.cur_stage = self.next_stage
        self.y = 575

    def update(self):
        self.y = self.y + (self.speed * -1)
        if self.y <= 0:
            self.x = random.randint(150, 650)
            self.y = 575
            self.speed = random.randint(self.minSpeed, self.maxSpeed)

    def get_bb(self):
        return self.x - 10, self.y - 25, self.x + 10, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def player_collide(self, a, b, state, num):
        left_a, bottom_a, right_a, top_a = a.get_bb(state, num)
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if state == 2 or state == 3: return False
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True
from pico2d import *
import logo_state
import random
import game_framework

class Item:
    SPEED = 200
    BOTTOM = 150
    def __init__(self):
        self.image = logo_state.item_box
        self.x, self.y = 0, 575
        self.speed = 1 + random.random()
        self.setting = False

    def update(self):
        if self.y > Item.BOTTOM:
            self.y += -1 * game_framework.frame_time * self.speed * Item.SPEED
        if self.y < Item.BOTTOM:
            self.y = Item.BOTTOM
            self.setting = True

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 25, self.x + 50, self.y + 25

    def npc_collide(self, a, b, level):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        if level == self.click:
            return True
        else:
            return False
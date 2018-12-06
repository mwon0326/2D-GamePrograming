from pico2d import *
import logo_state
import random
import game_framework
import game_world

class Item:
    SPEED = 200
    BOTTOM = 150
    ANIMATION_TOP = 200
    def __init__(self, level):
        self.image = logo_state.item_box
        self.x, self.y = 0, 575
        self.speed = 1 + random.random()
        self.setting = False
        self.item_kind = random.randint(0, level + 1)
        self.progress_image = logo_state.progress_bar
        self.progress_index = 9
        self.press_time = 0.0
        self.level = level
        self.animation_index = 0
        self.life_get = False
        self.key_get = False
        self.is_press = False
        print(self.item_kind)

    def item_down_animation(self):
        if self.y > Item.BOTTOM:
            self.y += -1 * game_framework.frame_time * self.speed * Item.SPEED
            if self.y <= Item.BOTTOM:
                self.y = Item.BOTTOM
                self.setting = True

    def item_get_animation(self):
        if self.y < Item.ANIMATION_TOP:
            self.y += game_framework.frame_time * self.speed * Item.SPEED
            if self.y >= Item.ANIMATION_TOP:
                if self.item_kind == 0:
                    self.x, self.y = 150, 40
                    self.key_get = True
                elif self.item_kind == 1:
                    self.life_get = True
                self.animation_index += 1

    def item_goto_sky(self):
        if self.y < 575:
            self.y += game_framework.frame_time * self.speed * Item.SPEED
            if self.y >= 575:
                game_world.remove_object(self)

    def update(self):
        if self.animation_index == 0: Item.item_down_animation(self)
        elif self.animation_index == 1: Item.item_get_animation(self)
        elif self.animation_index == 2 and (self.item_kind != 0 and self.item_kind != 1): Item.item_goto_sky(self)

        if self.setting:
            self.progress_index = round(self.press_time * 20)
            if self.progress_index > 9:
                logo_state.effect_sound.set_volume(32)
                logo_state.effect_sound.play()
                if self.item_kind == 0: self.image = logo_state.key_image
                elif self.item_kind == 1:
                    if self.level == 1: self.image = logo_state.red
                    elif self.level == 2: self.image = logo_state.pink
                    elif self.level == 3: self.image = logo_state.black
                    elif self.level == 4: self.image = logo_state.yellow
                    elif self.level == 5: self.image = logo_state.blue
                else:
                    self.image = logo_state.npc_image1

                self.animation_index += 1
                self.setting = False

        if self.is_press:
            self.press_time += game_framework.frame_time

    def draw(self):
        self.image.draw(self.x, self.y)
        if self.setting:
            self.progress_image.clip_draw(0, self.progress_index * 50, 100, 50, self.x, self.y + 50)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 35, self.y - 35, self.x + 35, self.y + 35

    def collide(self, a, b, state, num):
        left_a, bottom_a, right_a, top_a = a.get_bb(state, num)
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if state == 2 or state == 3: return False
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True
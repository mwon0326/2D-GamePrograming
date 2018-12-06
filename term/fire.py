from pico2d import *
import game_framework
import random
import logo_state
import game_world
import game_framework

class Fire:
    image = None
    SPEED = 200
    BOTTOM = 120
    def __init__(self, level):
        Fire.image = logo_state.fire_image
        self.x = random.randint(150, 650)
        self.y = 575
        self.speed = 0.5 + random.random()

    def draw(self):
        Fire.image.draw(self.x, self.y)

    def update(self):
        self.y += -1 * game_framework.frame_time * self.speed * Fire.SPEED
        if self.y < Fire.BOTTOM:
            game_world.remove_object(self)

    def get_bb(self):
        return self.x - 10, self.y - 25, self.x + 10, self.y + 25

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def collide(self, a, b, state, num):
        left_a, bottom_a, right_a, top_a = a.get_bb(state, num)
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if state == 2 or state == 3: return False
        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        logo_state.collide_sound.set_volume(32)
        logo_state.collide_sound.play()
        return True
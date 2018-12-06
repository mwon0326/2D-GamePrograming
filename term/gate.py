from pico2d import *
import logo_state
import game_framework
import game_world
import random

class Gate:
    def __init__(self):
        self.x = random.randint(150, 650)
        self.y = 250
        self.is_next = False
        self.image = logo_state.gate_image

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 150, self.x + 50, self.y + 150

    def update(self):
        pass

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
        return True

    def handle_events(self, event, a, state, num):
        self.is_next = False
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE and self.collide(a, self, state, num):
                self.is_next = True
        return self.is_next



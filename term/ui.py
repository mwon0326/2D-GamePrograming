from pico2d import *
import logo_state
import game_framework
import game_world

class UI:
    image = None
    def __init__(self, level, state):
        self.state = state
        if state == 1:
            if level == 1:
                UI.image = logo_state.stage1_mb
            elif level == 2:
                UI.image = logo_state.stage2_mb
            elif level == 3:
                UI.image = logo_state.stage3_mb
            elif level == 4:
                UI.image = logo_state.stage4_mb
            elif level == 5:
                UI.image = logo_state.stage5_mb
        elif state == 2:
            UI.image = logo_state.stage_clear_normal
        elif state == 3:
            UI.image = logo_state.stage_success_normal
        elif state == 4:
            UI.image = logo_state.stage_fail_normal
        self.is_press = False
        self.is_mouse = False
        self.is_return = False
        self.x, self.y = 400, 400

    def draw(self):
        UI.image.draw(self.x, self.y)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 30, self.y - 80, self.x + 40, self.y - 45

    def collide(self, a, mouseX, mouseY):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        if left_a <= mouseX <= right_a and bottom_a <= mouseY <= top_a:
            return True

    def image_select(self, mode):
        if self.state == 2:
            if mode == 1:
                return logo_state.stage_clear_normal
            elif mode == 2:
                return logo_state.stage_clear_enter
            elif mode == 3:
                return logo_state.stage_clear_press
        elif self.state == 3:
            if mode == 1:
                return logo_state.stage_success_normal
            elif mode == 2:
                return logo_state.stage_success_enter
            elif mode == 3:
                return logo_state.stage_success_press
        elif self.state == 4:
            if mode == 1:
                return logo_state.stage_fail_normal
            elif mode == 2:
                return logo_state.stage_fail_enter
            elif mode == 3:
                return logo_state.stage_fail_press

    def handle_events(self, event):
        self.is_return = False
        if event.type == SDL_MOUSEMOTION:
            if self.collide(self, event.x, 600 - event.y) and self.is_press == False:
                self.is_mouse = True
                UI.image = self.image_select(2)
            else:
                self.is_mouse = False
                UI.image = self.image_select(1)
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.collide(self, event.x, 600 - event.y):
                self.is_press = True
                UI.image = self.image_select(3)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.is_press = False
            self.is_return = True
            UI.image = self.image_select(2)
        return self.is_return


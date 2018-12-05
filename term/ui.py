from pico2d import *
import logo_state
import game_framework
import game_world

class GameStart:
    image = None
    def __init__(self, level):
        if level == 1:
            GameStart.image = logo_state.stage1_mb
        elif level == 2:
            GameStart.image = logo_state.stage2_mb
        elif level == 3:
            GameStart.image = logo_state.stage3_mb
        elif level == 4:
            GameStart.image = logo_state.stage4_mb
        elif level == 5:
            GameStart.image = logo_state.stage5_mb

    def draw(self):
        GameStart.image.draw(400, 400)

    def update(self):
        pass

class GameEnd:
    image = None
    def __init__(self):
        GameEnd.image = logo_state.stage_clear_normal
        self.is_press = False
        self.is_mouse = False
        self.change_level = False
        self.x, self.y = 400, 400

    def get_bb(self):
        return self.x - 30, self.y - 80, self.x + 40, self.y - 45

    def collide(self, a, mouseX, mouseY):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        if left_a <= mouseX <= right_a and bottom_a <= mouseY <= top_a:
            return True

    def handle_events(self, event):
        self.change_level = False
        if event.type == SDL_MOUSEMOTION:
            if self.collide(self, event.x, 600 - event.y) and self.is_press == False:
                self.is_mouse = True
                GameEnd.image = logo_state.stage_clear_enter
            else:
                self.is_mouse = False
                GameEnd.image = logo_state.stage_clear_normal
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.collide(self, event.x, 600 - event.y):
                self.is_press = True
                GameEnd.image = logo_state.stage_clear_press
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.is_press = False
            self.change_level = True
            GameEnd.image = logo_state.stage_clear_enter
        return self.change_level

    def draw(self):
        GameEnd.image.draw(self.x, self.y)

    def update(self):
        pass

class GameSuccess:
    image = None
    def __init__(self):
        GameSuccess.image = logo_state.stage_success_normal
        self.is_press = False
        self.is_mouse = False
        self.change_stage = False
        self.x, self.y = 400, 400

    def get_bb(self):
        return self.x - 30, self.y - 80, self.x + 40, self.y - 45

    def collide(self, a, mouseX, mouseY):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        if left_a <= mouseX <= right_a and bottom_a <= mouseY <= top_a:
            return True

    def handle_events(self, event):
        self.change_stage = False
        if event.type == SDL_MOUSEMOTION:
            if self.collide(self, event.x, 600 - event.y) and self.is_press == False:
                self.is_mouse = True
                GameSuccess.image = logo_state.stage_success_enter
            else:
                self.is_mouse = False
                GameSuccess.image = logo_state.stage_success_normal
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.collide(self, event.x, 600 - event.y):
                self.is_press = True
                GameSuccess.image = logo_state.stage_success_press
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.is_press = False
            GameEnd.image = logo_state.stage_success_enter
            self.change_stage = True
        return self.change_stage

    def draw(self):
        GameSuccess.image.draw(self.x, self.y)

    def update(self):
        pass

class GameOver:
    image = None
    def __init__(self):
        GameOver.image = logo_state.stage_fail_normal
        self.is_press = False
        self.is_mouse = False
        self.change_stage = False
        self.x, self.y = 400, 400

    def get_bb(self):
        return self.x - 30, self.y - 80, self.x + 40, self.y - 45

    def collide(self, a, mouseX, mouseY):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        if left_a <= mouseX <= right_a and bottom_a <= mouseY <= top_a:
            return True

    def handle_events(self, event):
        self.change_stage = False
        if event.type == SDL_MOUSEMOTION:
            if self.collide(self, event.x, 600 - event.y) and self.is_press == False:
                self.is_mouse = True
                GameOver.image = logo_state.stage_fail_enter
            else:
                self.is_mouse = False
                GameOver.image = logo_state.stage_fail_normal
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.collide(self, event.x, 600 - event.y):
                self.is_press = True
                GameOver.image = logo_state.stage_fail_press
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.is_press = False
            GameOver.image = logo_state.stage_fail_enter
            self.change_stage = True
        return self.change_stage

    def draw(self):
        GameOver.image.draw(self.x, self.y)

    def update(self):
        pass


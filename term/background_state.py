from pico2d import *
import game_framework
from image_state import Font
from image_state import StageImage
import game_framework
import title_state

class BackGround:
    def __init__(self):
        self.image = None
        self.x = 800
        self.dir = 1
        self.speed = 5

    def draw(self):
        self.image.clip_draw(self.x, 0, 800, 500, 400, 350)

    def move(self):
        if self.dir == 1:
            self.x -= self.speed
        else:
            self.x += self.speed

class ItemBox:
    def __init__(self):
        self.ft = Font()
        self.image = load_image('resource/menu.png')
        self.font = self.ft.f
        self.time = 0
        self.x = 130
        self.y = 50

    def draw(self):
        self.image.draw(400, 50)
        self.font.draw(self.x, self.y, '%d' % self.time, (0, 0, 0))

class Stage:
    def __init__(self):
        self.stage_image = None
        self.x = 400
        self.y = 400
        self.is_stage_draw = True
        self.clear_image = None
        self.is_clear = False
        self.image = StageImage()
        self.press = False
        self.mouse = False
        self.is_change_level = False

    def draw(self):
        if self.is_stage_draw:
            self.stage_image.draw(self.x, self.y)
        elif self.is_clear:
            self.clear_image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 80, self.x + 40, self.y - 45

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def popup_collide(self, a, mouseX, mouseY):
        left_a, bottom_a, right_a, top_a = a.get_bb()

        if left_a <= mouseX <= right_a and bottom_a <= mouseY <= top_a:
            return True

    def image_change(self, level):
        if self.press:
            if level == 6:
                self.clear_image = self.image.stage_success_press
            else:
                self.clear_image = self.image.stage_clear_press
        elif self.mouse:
            if level == 6:
                self.clear_image = self.image.stage_success_enter
            else:
                self.clear_image = self.image.stage_clear_enter
        else:
            if level == 6:
                self.clear_image = self.image.stage_success_normal
            else:
                self.clear_image = self.image.stage_clear_normal

    def event_handle(self, event, level):
        if event.type == SDL_MOUSEMOTION:
            if self.popup_collide(self, event.x, 600 - event.y) and self.is_clear and self.press == False:
                self.mouse = True
            else:
                self.mouse = False
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.popup_collide(self, event.x, 600 - event.y) and self.is_clear:
                self.press = True
                self.is_change_level = True
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.press = False
        self.image_change(level)

class Fail:
    def __init__(self):
        self.x, self.y = 400, 400
        self.is_stage_draw = True
        self.fail_image = StageImage()
        self.image = self.fail_image.stage_fail_normal
        self.press = False
        self.mouse = False
        self.is_draw = False

    def draw(self):
        self.image.draw(self.x, self.y)

    def image_change(self):
        if self.press:
            self.image = self.fail_image.stage_fail_press
        elif self.mouse:
            self.image = self.fail_image.stage_fail_enter
        else:
            self.image = self.fail_image.stage_fail_normal

    def get_bb(self):
        return self.x - 30, self.y - 80, self.x + 40, self.y - 45

    def popup_collide(self, a, mouseX, mouseY):
        left_a, bottom_a, right_a, top_a = a.get_bb()

        if left_a <= mouseX <= right_a and bottom_a <= mouseY <= top_a:
            return True

    def event_handle(self, event):
        if event.type == SDL_MOUSEMOTION:
            if self.popup_collide(self, event.x, 600 - event.y) and self.press == False:
                self.mouse = True
            else:
                self.mouse = False
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.popup_collide(self, event.x, 600 - event.y):
                self.press = True
                game_framework.push_state(title_state)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.press = False
        self.image_change()
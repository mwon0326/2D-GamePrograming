from pico2d import *
import game_framework
import logo_state
import time

class Player:
    SPEED = 300
    POSY = 210
    def __init__(self):
        self.image = logo_state.player_image
        self.x, self.y = 0, Player.POSY
        self.dx= 0
        self.frame = 0
        self.image_index = 1
        self.speed = 5
        self.stage_width = get_canvas_width()
        self.time = 0
        self.fps = 5
        self.is_move = 0

    def draw(self):
        if self.dx < 0 : self.image_index = 1
        elif self.dx > 0 : self.image_index = 0
        elif self.dx == 0 and self.is_move == 0:
            if self.image_index in [1, 3]: self.image_index = 5
            elif self.image_index in [0, 2] : self.image_index = 4
        elif self.dx == 0 and self.is_move == 1:
            if self.image_index in [1, 3, 5]: self.image_index = 3
            elif self.image_index in [0, 2, 4]: self.image_index = 2

        self.image.clip_draw(self.frame * 100, self.image_index * 200, 100, 200, self.x, self.y)

    def update(self):
        distance = Player.SPEED * game_framework.frame_time
        self.x += (self.dx * distance)
        self.x = clamp(50, self.x, self.stage_width - 50)
        self.time += game_framework.frame_time
        self.frame = round(self.time * self.fps) % 4

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                self.dx -= 1
            elif event.key == SDLK_d:
                self.dx += 1
            elif event.key == SDLK_s:
                self.is_move = 1
        if event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                self.dx += 1
            elif event.key == SDLK_d:
                self.dx -= 1
            elif event.key == SDLK_s:
                self.is_move = 0

    def get_bb(self, state, num):
        if state == 1:
            if num == 1:
                return self.x - 25, self.y + 75, self.x - 6, self.y + 90
            elif num == 2:
                return self.x - 40, self.y + 10, self.x + 21, self.y + 75
            else:
                return self.x - 43, self.y - 80, self.x + 30, self.y - 68
        else:
            if num == 1:
                return self.x - 10, self.y + 77, self.x + 6, self.y + 92
            elif num == 2:
                return self.x - 40, self.y + 12, self.x + 21, self.y + 77
            else:
                return self.x - 43, self.y - 78, self.x + 30, self.y - 66

    def draw_face_left_bb(self):
        draw_rectangle(*self.get_bb(1, 2))

    def draw_crown_left_bb(self):
        draw_rectangle(*self.get_bb(1, 1))

    def draw_dress_left_bb(self):
        draw_rectangle(*self.get_bb(1, 3))

    def draw_face_right_bb(self):
        draw_rectangle(*self.get_bb(2, 2))

    def draw_crown_right_bb(self):
        draw_rectangle(*self.get_bb(2, 1))

    def draw_dress_right_bb(self):
        draw_rectangle(*self.get_bb(2, 3))
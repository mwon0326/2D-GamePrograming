from pico2d import *
import game_framework

CHARACTER_MOVE, BACKGROUND_MOVE = range(2)

class Princess:
    def __init__(self):
        self.image = load_image('resource/animation.png')
        self.x, self.y = 200, 100
        self.frame = 0
        self.state = CHARACTER_MOVE
        self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 200, self.dir * 300, 200, 300, self.x, self.y)

    def handle_event(self, event):
        if self.state == CHARACTER_MOVE:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir = 0
                    self.x += 25
                    self.frame = (self.frame + 1) % 4
                elif event.key == SDLK_LEFT:
                    self.dir = 1
                    self.x -= 25
                    self.frame = (self.frame + 1) % 4


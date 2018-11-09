from pico2d import *
import game_world
import game_framework
import math
import time

DEL_MARGIN = 25
WIND_RESISTANCE = 0.99
BOUNCE_RESISTANCE = 0.7
GRAVITY = 10 / 33
BOUNCING_GROUND = 40

MIN_MOVE = 2

class Ball:
    image = None
    canvas_width = 0
    canvas_height = 0
    def __init__(self, x = 800, y = 300, dx = 1, dy = 0):
        if Ball.image == None:
            Ball.image = load_image('../image/ball21x21.png')
        if Ball.canvas_width == 0:
            Ball.canvas_width = get_canvas_width()
            Ball.canvas_height = get_canvas_height()            
        self.x, self.y = x, y
        self.dx, self.dy = dx, dy
        self.stopTimer = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        if self.stopTimer > 0:
            elapsed = get_time() - self.stopTimer
            if elapsed > 3.0:
                game_world.remove_object(self)
            return
        self.x += self.dx
        self.y += self.dy

        self.dx *= WIND_RESISTANCE
        self.dy -= GRAVITY

        height = self.y - BOUNCING_GROUND
        if height < 0:
            self. y -= height
            self.dy *= -BOUNCE_RESISTANCE

        if math.fabs(height) < MIN_MOVE and math.fabs(self.dx) < MIN_MOVE and math.fabs(self.dy) < MIN_MOVE:
            self.dx = self.dy = 0
            self.y = BOUNCING_GROUND
            self.stopTimer = get_time()

        if self.x < -DEL_MARGIN or self.x > self.canvas_width + DEL_MARGIN or self.y < -DEL_MARGIN or self.y > self.canvas_height + DEL_MARGIN:
            game_world.remove_object(self)

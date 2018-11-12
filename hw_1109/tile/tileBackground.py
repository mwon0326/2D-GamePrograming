from pico2d import *
import json

class TiledBackground:
    def __init__(self):
        file = open('map.json', 'r')
        dict = json.load(file)
        file.close()
        layer = dict["layers"][0]
        self.data = layer["data"]
        self.map_width = layer["width"]
        self.map_height = layer["height"]
        self.tile_width = dict["tilewidth"]
        self.tile_height = dict["tileheight"]
        self.image = load_image('../../image/terrain_atlas.png')
        self.tile_count_x, self.tile_count_y = 32, 32
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = self.map_width * self.tile_width, self.map_height * self.tile_height
        self.x, self.y = 0, 0
        self.target = None
        self.xx = 0

    def clamp(self, o):
        o.x = int(clamp(self.min_x + 25, o.x, self.max_x - 25))
        o.y = int(clamp(self.min_y + 25, o.y, self.max_y - 25))
        
    def draw(self):
        tile_x = self.x // self.tile_width
        tile_y = self.y // self.tile_width
        beg_x = - int(self.x % self.tile_width)
        beg_y = - int(self.y % self.tile_height)

        y = beg_y
        ty = tile_y
        while y < self.ch:
            x = beg_x
            tx = tile_x
            ti = (self.map_height - ty - 1) * self.map_width + tx
            while x < self.cw:
                tile = self.data[ti]
                rect = self.rectForTile(tile)
                self.image.clip_draw_to_origin(*rect, x, y)
                x += self.tile_width
                ti += 1
            y += self.tile_height
            ty += 1
        self.xx = 1

    def rectForTile(self, tile):
        x = (tile - 1) % self.tile_count_x
        y = self.tile_count_y - 1 - (tile - 1) // self.tile_count_x
        sx = x * (self.tile_width)
        sy = y * (self.tile_height)
        return sx, sy, self.tile_width, self.tile_height
    
    def update(self):
        if self.target == None:
            return
        self.x = clamp(0, int(self.target.x - self.cw // 2), self.max_x - self.cw)
        self.y = clamp(0, int(self.target.y - self.ch // 2), self.max_y - self.ch)

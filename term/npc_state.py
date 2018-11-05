from pico2d import *
import game_framework
import random
from image_state import NPCImage

class NPC:
    def __init__(self):
        self.image = None
        self.cartoon = None
        self.present = None
        self.time = 0
        self.x, self.y = 200, 350
        self.cx, self.cy = 300, 450
        self.px, self.py = 302, 475

    def draw(self):
        if self.time > 5:
            self.image.draw(self.x, self.y)
            self.cartoon.draw(self.cx, self.cy)
            self.present.draw(self.px, self.py)

ITEM1, ITEM2, ITEM3, ITEM4, ITEM5 = range(5)
x, y = range(2)
item_table = {
        ITEM1 : {x : 450, y : 40},
        ITEM2 : {x : 520, y : 40},
        ITEM3 : {x : 590, y : 40},
        ITEM4 : {x : 660, y : 40},
        ITEM5 : {x : 730, y : 40}
    }

class Item:
    item = None
    mouse = None
    def __init__(self):
        Item.item = NPCImage()
        self.item1 = Item.item.item1
        self.item2 = Item.item.item2
        self.item3 = Item.item.item3
        self.item4 = Item.item.item4
        self.item5 = Item.item.item5

        self.x1, self.y1 = item_table[ITEM1][x], item_table[ITEM1][y]
        self.x2, self.y2 = item_table[ITEM2][x], item_table[ITEM2][y]
        self.x3, self.y3 = item_table[ITEM3][x], item_table[ITEM3][y]
        self.x4, self.y4 = item_table[ITEM4][x], item_table[ITEM4][y]
        self.x5, self.y5, = item_table[ITEM5][x], item_table[ITEM5][y]

        mouse = False
        self.click = 0
        self.drag = False

    def draw(self):
        self.item1.draw(self.x1, self.y1)
        self.item2.draw(self.x2, self.y2)
        self.item3.draw(self.x3, self.y3)
        self.item4.draw(self.x4, self.y4)
        self.item5.draw(self.x5, self.y5)

    def event_hanble(self, event):
        global mouse
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if self.collide(event.x, 600 - event.y):
                Item.mouse = True
        elif event.type == SDL_MOUSEBUTTONUP and event.button == SDL_BUTTON_LEFT:
            if self.click == 1:
                self.x1, self.y1 = item_table[ITEM1][x], item_table[ITEM1][y]
            elif self.click == 2:
                self.x2, self.y2 = item_table[ITEM2][x], item_table[ITEM2][y]
            elif self.click == 3:
                self.x3, self.y3 = item_table[ITEM3][x], item_table[ITEM3][y]
            elif self.click == 4:
                self.x4, self.y4 = item_table[ITEM4][x], item_table[ITEM4][y]
            elif self.click == 5:
                self.x5, self.y5 = item_table[ITEM5][x], item_table[ITEM5][y]
            self.click = 0
            Item.mouse = False

        if event.type == SDL_MOUSEMOTION and Item.mouse:
            if self.click == 1:
                self.x1, self.y1 = event.x, 600 - event.y
            elif self.click == 2:
                self.x2, self.y2 = event.x, 600 - event.y
            elif self.click == 3:
                self.x3, self.y3 = event.x, 600 - event.y
            elif self.click == 4:
                self.x4, self.y4 = event.x, 600 - event.y
            elif self.click == 5:
                self.x5, self.y5 = event.x, 600 - event.y

    def collide(self, mouseX, mouseY):
        if self.x1 - 25 <= mouseX <= self.x1 + 25 and self.y1 - 25 <= mouseY <= self.y1 + 25:
            self.click = 1
            return True
        elif self.x2 - 25 <= mouseX <= self.x2 + 25 and self.y2 - 25 <= mouseY <= self.y2 + 25:
            self.click = 2
            return True
        elif self.x3 - 25 <= mouseX <= self.x3 + 25 and self.y3 - 25 <= mouseY <= self.y3 + 25:
            self.click = 3
            return True
        elif self.x4 - 25 <= mouseX <= self.x4 + 25 and self.y4 - 25 <= mouseY <= self.y4 + 25:
            self.click = 4
            return True
        elif self.x5 - 25 <= mouseX <= self.x5 + 25 and self.y5 - 25 <= mouseY <= self.y5 + 25:
            self.click = 5
            return True
        return False

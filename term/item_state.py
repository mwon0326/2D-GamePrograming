from pico2d import *
from image_state import ItemImage
from npc_state import NPC

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
        Item.item = ItemImage()
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

        Item.mouse = False
        self.click = 0
        self.drag = False

        self.draw1 = True
        self.draw2 = True
        self.draw3 = True
        self.draw4 = True
        self.draw5 = True

    def draw(self):
        if self.draw1:
            self.item1.draw(self.x1, self.y1)
        if self.draw2:
            self.item2.draw(self.x2, self.y2)
        if self.draw3:
            self.item3.draw(self.x3, self.y3)
        if self.draw4:
            self.item4.draw(self.x4, self.y4)
        if self.draw5:
            self.item5.draw(self.x5, self.y5)

    def event_handle(self, event):
        global mouse
        if event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if self.mouse_collide(event.x, 600 - event.y):
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

    def stop(self):
        if self.click == 1:
            self.draw1 = False
        elif self.click == 2:
            self.draw2 = False
        elif self.click == 3:
            self.draw3 = False
        elif self.click == 4:
            self.draw4 = False
        elif self.click == 5:
            self.draw5 = False

    def get_bb(self):
        if self.click == 1:
            return self.x1 - 25, self.y1 - 25, self.x1 + 25, self.y1 + 25
        elif self.click == 2:
            return self.x2 - 25, self.y2 - 25, self.x2 + 25, self.y2 + 25
        elif self.click == 3:
            return self.x3 - 25, self.y3 - 25, self.x3 + 25, self.y3 + 25
        elif self.click == 4:
            return self.x4 - 25, self.y4 - 25, self.x4 + 25, self.y4 + 25
        elif self.click == 5:
            return self.x5 - 25, self.y5 - 25, self.x5 + 25, self.y5 + 25
        else:
            return 0, 0, 0, 0

    def mouse_collide(self, mouseX, mouseY):
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

    def npc_collide(self, a, b, level):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False

        if level == self.click:
            return True
        else:
            return False
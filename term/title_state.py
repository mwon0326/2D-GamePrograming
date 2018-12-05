from pico2d import *
import game_framework
import game_state
import logo_state
Image = None

class UI:
    def __init__(self):
        self.start_image = logo_state.start_ui_normal
        self.start_x, self.start_y = 400, 250
        self.is_press = False
        self.is_mouse = False
        self.next_stage = False

    def draw(self):
        self.start_image.draw(self.start_x, self.start_y)

    def get_bb(self):
        return self.start_x - 52, self.start_y - 25, self.start_x + 52, self.start_y + 25

    def collide(self, a, mouseX, mouseY):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        if left_a <= mouseX <= right_a and bottom_a <= mouseY <= top_a:
            return True

    def handle_events(self, event):
        self.next_stage = False
        if event.type == SDL_MOUSEMOTION:
            if self.collide(self, event.x, 600 - event.y) and self.is_press == False:
                self.is_mouse = True
                self.start_image = logo_state.start_ui_enter
            else:
                self.is_mouse = False
                self.start_image = logo_state.start_ui_normal
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if self.collide(self, event.x, 600 - event.y):
                self.is_press = True
                self.start_image = logo_state.start_ui_press
        elif (event.type, event.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
            self.is_press = False
            self.next_stage = True
            self.start_image = logo_state.start_ui_enter
        return self.next_stage

def enter():
    global Image
    global ui
    Image = logo_state.title_image
    ui = UI()

def update():
    pass

def draw():
    global Image
    global ui
    clear_canvas()
    Image.draw(400, 300)
    ui.draw()
    update_canvas()

def handle_events():
    global ui
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT: game_framework.quit()
        stage = ui.handle_events(e)
        if stage:
            game_framework.change_state(game_state)

def pause():
    pass

def resume():
    pass

def exit():
    global Image
    del(Image)

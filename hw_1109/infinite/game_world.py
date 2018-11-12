objects = [[], [], []]
layer_bg = 0
layer_player = 1
layer_obstacle = 2

def add_object(o, layer):
    objects[layer].append(o)

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o

def clear():
    for o in all_objects():
        del o
    objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o
            
def update():
    for o in all_objects():
        o.update()

def draw():
    for o in all_objects():
        o.draw()

objects = [[],[],[],[],[],[]]
layer_bg = 0
layer_player = 2
layer_obstacle = 3
layer_item = 4
layer_gate = 1
layer_message = 5

def add_object(o, layer):
	objects[layer].append(o)

def remove_object(o):
	for i in range(len(objects)):
		if o in objects[i]:
			# print('deleting', o)
			objects[i].remove(o)
			del o
			break

def remove_objects_at_layer(layer):
	for o in objects[layer]:
		# print('deleting', o)
		del o
	objects[layer] = []

def clear():
	for o in all_objects():
		del o
	objects.clear()

def all_objects():
	for i in range(len(objects)):
		for o in objects[i]:
			yield o

def objects_at_layer(layer):
	for o in objects[layer]:
		yield o

def count_at_layer(layer):
	return len(objects[layer])

def update():
	for o in all_objects():
		o.update()

def draw():
	for o in all_objects():
		o.draw()


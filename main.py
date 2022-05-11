from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
ground = Entity(model = 'plane',texture = 'grass',collider = 'mesh',scale = (100,1,100))
player = FirstPersonController()
Sky()
blocks = []
for i in range(8):
    block = Entity(model='cube',
                   color=color.azure,
                   collider='box',
                   position=(5, 1, 3+i*5),
                   texture = 'white_cube',
                   scale = (3,0.5,3))
    blocks.append(block)

direction = 1
def update():
    global direction
    for block in blocks:
        block.x -= direction*time.dt
        if abs(block.x) > 5:
            direction *= -1
def input(key):
    if key == 'q':
        quit()
app.run()

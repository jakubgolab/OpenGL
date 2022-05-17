import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from pygame import mixer
from camera import Camera
from Sound import Sound
from load_obj import Load_object


cam = Camera()
WIDTH, HEIGHT = 1280, 720
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True
left, right, forward, backward = False, False, False, False
velocity = 0.15 # prędkość poruszania się po mapie
sound_enabled = False


loader = Load_object()


# the keyboard input callback
def key_input_clb(window, key, scancode, action, mode):
    global left, right, forward, backward
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, True)

    if key == glfw.KEY_W and action == glfw.PRESS:
        forward = True
    elif key == glfw.KEY_W and action == glfw.RELEASE:
        forward = False
    if key == glfw.KEY_S and action == glfw.PRESS:
        backward = True
    elif key == glfw.KEY_S and action == glfw.RELEASE:
        backward = False
    if key == glfw.KEY_A and action == glfw.PRESS:
        left = True
    elif key == glfw.KEY_A and action == glfw.RELEASE:
        left = False
    if key == glfw.KEY_D and action == glfw.PRESS:
        right = True
    elif key == glfw.KEY_D and action == glfw.RELEASE:
        right = False
    # if key in [glfw.KEY_W, glfw.KEY_S, glfw.KEY_D, glfw.KEY_A] and action == glfw.RELEASE:
    #     left, right, forward, backward = False, False, False, False
    if key == glfw.KEY_L and action == glfw.PRESS: # ustalenie aktualnej pozycji
        print_location(cam.get_position())

# do the movement, call this function in the main loop
def do_movement():
    if left:
        cam.process_keyboard("LEFT", velocity)
    if right:
        cam.process_keyboard("RIGHT", velocity)
    if forward:
        cam.process_keyboard("FORWARD", velocity)
    if backward:
        cam.process_keyboard("BACKWARD", velocity)


# the mouse position callback function
def mouse_look_clb(window, xpos, ypos):
    global first_mouse, lastX, lastY

    if first_mouse:
        lastX = xpos
        lastY = ypos
        first_mouse = False

    xoffset = xpos - lastX
    yoffset = lastY - ypos

    lastX = xpos
    lastY = ypos

    cam.process_mouse_movement(xoffset, yoffset)


# shaders
vertex_src = """
# version 330

layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
layout(location = 2) in vec3 a_normal;

uniform mat4 model;
uniform mat4 projection;
uniform mat4 view;

out vec2 v_texture;

void main()
{
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

fragment_src = """
# version 330

in vec2 v_texture;

out vec4 out_color;

uniform sampler2D s_texture;

void main()
{
    out_color = texture(s_texture, v_texture);
}
"""


# the window resize callback function
def window_resize_clb(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

def print_location(position):
    print(position)


# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
window = glfw.create_window(WIDTH, HEIGHT, "My OpenGL window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 100, 100)

# set the callback function for window resize
glfw.set_window_size_callback(window, window_resize_clb)
# set the mouse position callback
glfw.set_cursor_pos_callback(window, mouse_look_clb)
# set the keyboard input callback
glfw.set_key_callback(window, key_input_clb)
# capture the mouse cursor
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)

# make the context current
glfw.make_context_current(window)

# Tutaj dodajemy obiekty
loader.add_object("cube1", "texture/lana.png", "objects/cube.obj", [26, 4, 1])
loader.add_object("cube2", "texture/lana_del_rey.jpg", "objects/cube.obj", [36, 4, 10])
loader.add_object("floor", "texture/floor3.png", "objects/floor2.obj", [0, 0, 0])
loader.add_object("wall", "texture/wall.jpg", "objects/wall.obj", [0, 0, 0])
loader.add_object("ceiling", "texture/ceiling.png", "objects/ceiling.obj", [0, 0, 0])
loader.add_object("meta_kula", "texture/meta_kula.png", "objects/meta_kula.obj", [46, 4, 10])
loader.add_object("grass", "texture/grass2.png", "objects/grass.obj", [0, -0.01, 0])
loader.add_object("Bench", "texture/floor3.png", "objects/outdoor_bench.obj", [23, 0, 7])

loader.send_to_GPU()

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

glUseProgram(shader)
glClearColor(1.0, 1.0, 1.0, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, WIDTH / HEIGHT, 0.1, 100)

model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

if sound_enabled == True:
    mixer.init()
    music = mixer.Sound('music/young_and_beautiful.mp3')
    music.play()
    sound = Sound(music, pyrr.Vector3([36, 4, 10]), cam.get_position())


# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    do_movement()

    if sound_enabled == True:
        sound.update_pos(cam.get_position())
        sound.change_volume()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    view = cam.get_view_matrix()
    glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    rot_y = pyrr.Matrix44.from_y_rotation(0.8 * glfw.get_time())
    model = pyrr.matrix44.multiply(rot_y, pyrr.matrix44.create_from_translation(pyrr.Vector3([26, 4, 1])))
    model2 = pyrr.matrix44.multiply(rot_y, pyrr.matrix44.create_from_translation(pyrr.Vector3([36, 4, 10])))

    # draw the cube
    loader.draw("cube1", model_loc, model)

    # draw the floor
    loader.draw("floor", model_loc)

    # draw the cube 2
    loader.draw("cube2", model_loc, model2)

    # draw the wall
    loader.draw("wall", model_loc)

    # draw the ceiling
    loader.draw("ceiling", model_loc)

    # draw the meta_kula
    loader.draw("meta_kula", model_loc)

    #draw the grass
    loader.draw("grass", model_loc)

    #draw the bench
    loader.draw("Bench", model_loc, loader.change_orientation("Bench", 'Y', 90))

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()

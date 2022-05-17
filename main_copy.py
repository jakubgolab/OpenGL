import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr
from ObjLoader import ObjLoader
import TextureLoader
from pygame import mixer
from camera import Camera
from Sound import Sound
from load_obj import Load_object



cam = Camera()
WIDTH, HEIGHT = 1280, 720
lastX, lastY = WIDTH / 2, HEIGHT / 2
first_mouse = True
left, right, forward, backward = False, False, False, False


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


# do the movement, call this function in the main loop
def do_movement():
    if left:
        cam.process_keyboard("LEFT", 0.15)
    if right:
        cam.process_keyboard("RIGHT", 0.15)
    if forward:
        cam.process_keyboard("FORWARD", 0.15)
    if backward:
        cam.process_keyboard("BACKWARD", 0.15)


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

loader.add_object("cube1", "texture/lana.png", "objects/cube.obj", [26, 4, 1])
loader.add_object("cube2", "texture/lana_del_rey.jpg", "objects/cube.obj", [36, 4, 10])
loader.add_object("floor", "texture/floor3.png", "objects/floor2.obj", [0, 0, 0])
loader.add_object("wall", "texture/wall.jpg", "objects/wall.obj", [0, 0, 0])
loader.add_object("ceiling", "texture/ceiling.png", "objects/ceiling.obj", [0, 0, 0])
loader.add_object("meta_kula", "texture/meta_kula.png", "objects/meta_kula.obj", [46, 4, 10])

# cube_indices, cube_buffer = ObjLoader.load_model("objects/cube.obj")
# cube_indices_2, cube_buffer_2 = ObjLoader.load_model("objects/cube.obj")
# floor_indices, floor_buffer = ObjLoader.load_model("objects/floor2.obj")
# wall_indices, wall_buffer = ObjLoader.load_model("objects/wall.obj")
# ceiling_indices, ceiling_buffer = ObjLoader.load_model("objects/ceiling.obj")
# meta_kula_indices, meta_kula_buffer = ObjLoader.load_model("objects/meta_kula.obj")
#
# VAO = glGenVertexArrays(6) # ilość obiektów
# VBO = glGenBuffers(6) # ilość obiektów

# # cube VAO
# glBindVertexArray(VAO[0])

loader.send_to_GPU()

shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))


# # cube Vertex Buffer Object
# glBindBuffer(GL_ARRAY_BUFFER, VBO[0])
# glBufferData(GL_ARRAY_BUFFER, cube_buffer.nbytes, cube_buffer, GL_STATIC_DRAW)
#
# # cube vertices
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, cube_buffer.itemsize * 8, ctypes.c_void_p(0))
# # cube textures
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, cube_buffer.itemsize * 8, ctypes.c_void_p(12))
# # cube normals
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, cube_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
#
#
# # floor VAO
# glBindVertexArray(VAO[1])
# # floor Vertex Buffer Object
# glBindBuffer(GL_ARRAY_BUFFER, VBO[1])
# glBufferData(GL_ARRAY_BUFFER, floor_buffer.nbytes, floor_buffer, GL_STATIC_DRAW)
#
# # floor vertices
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, floor_buffer.itemsize * 8, ctypes.c_void_p(0))
# # floor textures
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, floor_buffer.itemsize * 8, ctypes.c_void_p(12))
# # floor normals
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, floor_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # cube VAO
# glBindVertexArray(VAO[2])
#
# # cube2 Vertex Buffer Object
# glBindBuffer(GL_ARRAY_BUFFER, VBO[2])
# glBufferData(GL_ARRAY_BUFFER, cube_buffer_2.nbytes, cube_buffer_2, GL_STATIC_DRAW)
#
# # cube2 vertices
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, cube_buffer_2.itemsize * 8, ctypes.c_void_p(0))
# # cube2 textures
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, cube_buffer_2.itemsize * 8, ctypes.c_void_p(12))
# # cube2 normals
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, cube_buffer_2.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # wall VAO
# glBindVertexArray(VAO[3])
# # wall Vertex Buffer Object
# glBindBuffer(GL_ARRAY_BUFFER, VBO[3])
# glBufferData(GL_ARRAY_BUFFER, wall_buffer.nbytes, wall_buffer, GL_STATIC_DRAW)
#
# # wall vertices
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, wall_buffer.itemsize * 8, ctypes.c_void_p(0))
# # wall textures
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, wall_buffer.itemsize * 8, ctypes.c_void_p(12))
# # wall normals
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, wall_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # ceiling VAO
# glBindVertexArray(VAO[4])
# # ceiling Vertex Buffer Object
# glBindBuffer(GL_ARRAY_BUFFER, VBO[4])
# glBufferData(GL_ARRAY_BUFFER, ceiling_buffer.nbytes, ceiling_buffer, GL_STATIC_DRAW)
#
# # ceiling vertices
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, ceiling_buffer.itemsize * 8, ctypes.c_void_p(0))
# # ceiling textures
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, ceiling_buffer.itemsize * 8, ctypes.c_void_p(12))
# # ceiling normals
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, ceiling_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# # meta_kula VAO
# glBindVertexArray(VAO[5])
# # meta_kula Vertex Buffer Object
# glBindBuffer(GL_ARRAY_BUFFER, VBO[5])
# glBufferData(GL_ARRAY_BUFFER, meta_kula_buffer.nbytes, meta_kula_buffer, GL_STATIC_DRAW)
#
# # meta_kula vertices
# glEnableVertexAttribArray(0)
# glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, meta_kula_buffer.itemsize * 8, ctypes.c_void_p(0))
# # meta_kula textures
# glEnableVertexAttribArray(1)
# glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, meta_kula_buffer.itemsize * 8, ctypes.c_void_p(12))
# # meta_kula normals
# glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, meta_kula_buffer.itemsize * 8, ctypes.c_void_p(20))
# glEnableVertexAttribArray(2)
#
# textures = glGenTextures(6)
# TextureLoader.load_texture("texture/lana.png", textures[0])
# TextureLoader.load_texture("texture/floor3.png", textures[1])
# TextureLoader.load_texture("texture/lana_del_rey.jpg", textures[2])
# TextureLoader.load_texture("texture/wall.jpg", textures[3])
# TextureLoader.load_texture("texture/ceiling.png", textures[4])
# TextureLoader.load_texture("texture/meta_kula.png", textures[5])

glUseProgram(shader)
glClearColor(1.0, 1.0, 1.0, 1)
glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

projection = pyrr.matrix44.create_perspective_projection_matrix(45, WIDTH / HEIGHT, 0.1, 100)
# cube_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([26, 4, 1]))
# cube2pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([36, 4, 10]))
# floor_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
# wall_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
# ceiling_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([0, 0, 0]))
# meta_kula_pos = pyrr.matrix44.create_from_translation(pyrr.Vector3([46, 4, 10]))

model_loc = glGetUniformLocation(shader, "model")
proj_loc = glGetUniformLocation(shader, "projection")
view_loc = glGetUniformLocation(shader, "view")

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

mixer.init()
music = mixer.Sound('music/young_and_beautiful.mp3')
music.play()
sound = Sound(music, pyrr.Vector3([36, 4, 10]), cam.get_position())

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    do_movement()
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

    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
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
sound_enabled = True


loader = Load_object()


# Odczytywanie sygnałów z klawiatury
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
    if key == glfw.KEY_L and action == glfw.PRESS: # ustalenie aktualnej pozycji
        print_location(cam.get_position())

# Wykonywanie ruchu po przestrzeni
def do_movement():
    if left:
        cam.process_keyboard("LEFT", velocity)
    if right:
        cam.process_keyboard("RIGHT", velocity)
    if forward:
        cam.process_keyboard("FORWARD", velocity)
    if backward:
        cam.process_keyboard("BACKWARD", velocity)


# Obsługa sygnału z myszy
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
out vec3 Normal;
out vec3 crntPos;

void main()
{
    crntPos = vec3(model * vec4(a_position, 1.0f));
    gl_Position = projection * view * model * vec4(a_position, 1.0);
    v_texture = a_texture;
    Normal = a_normal;
}
"""

fragment_src = """
# version 330

in vec2 v_texture;
in vec3 Normal;
in vec3 crntPos;

out vec4 out_color;

uniform sampler2D s_texture;

uniform vec4 lightColor;
uniform vec3 lightPos;
uniform vec3 camPos;

void main()
{
    vec3 normal = normalize(Normal);
    vec3 lightDirection = normalize(lightPos - crntPos);
    
    float ambient = 0.95f;

    out_color = texture(s_texture, v_texture) * lightColor * ambient;
}
"""


# Skalowanie ekranu
def window_resize_clb(window, width, height):
    glViewport(0, 0, width, height)
    projection = pyrr.matrix44.create_perspective_projection_matrix(45, width / height, 0.1, 100)
    glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

def print_location(position):
    print(position)


# Inicjalizacja biblioteki glfw
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# Utworzenie okna
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
window = glfw.create_window(WIDTH, HEIGHT, "My OpenGL window", None, None)

# Sprawdzenie czy okno zostało utworzone
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# Ustawienie pozycji okna
glfw.set_window_pos(window, 100, 100)



# Obsługa kamery
glfw.set_window_size_callback(window, window_resize_clb)
glfw.set_cursor_pos_callback(window, mouse_look_clb)
glfw.set_key_callback(window, key_input_clb)
glfw.set_input_mode(window, glfw.CURSOR, glfw.CURSOR_DISABLED)


glfw.make_context_current(window)

# Dodawanie obiektów
loader.add_object("cube2", "texture/lana_del_rey.jpg", "objects/cube2.obj", [65.5, 7, 75])
loader.add_object("floor", "texture/floor3.png", "objects/floor2.obj", [0, 0, 0])
loader.add_object("wall", "texture/wall.jpg", "objects/wall.obj", [0, 0, 0])
loader.add_object("ceiling", "texture/sufit6.jpg", "objects/ceiling.obj", [0, 0, 0])
loader.add_object("grass", "texture/grass2.png", "objects/grass.obj", [0, -0.01, 0])
loader.add_object("LawkaSciana", "texture/Marmur3.jpg", "objects/lawkaScianaSmall.obj", [26.75, 0, 42])
loader.add_object("duze_skrzypce", "texture/pictures/5.jpg", "objects/frame1.obj", [0, 0, 0])
loader.add_object("maly_pan", "texture/pictures/4.jpg", "objects/frame2.obj", [0, 0, 0])
loader.add_object("instrumenty", "texture/pictures/2.jpg", "objects/frame3.obj", [0, 0, 0])
loader.add_object("muzycy", "texture/pictures/3.jpg", "objects/frame4.obj", [0, 0, 0])
loader.add_object("gitarzysta", "texture/pictures/1.jpg", "objects/frame5.obj", [0, 0, 0])
loader.add_object("jan_matejko", "texture/pictures/6.png", "objects/frame6.obj", [0, 0, 0])
loader.add_object("van_gogh", "texture/pictures/7.jpg", "objects/frame7.obj", [0, 0, 0])
loader.add_object("miasto", "texture/pictures/8.jpg", "objects/frame8.obj", [0, 0, 0])
loader.add_object("most", "texture/pictures/9.jpg", "objects/frame9.obj", [0, 0, 0])
loader.add_object("domki", "texture/pictures/10.jpg", "objects/frame10.obj", [0, 0, 0])
loader.add_object("alejka", "texture/pictures/11.jpg", "objects/frame11.obj", [0, 0, 0])
loader.add_object("mostek", "texture/pictures/12.jpg", "objects/frame12.obj", [0, 0, 0])
loader.add_object("las", "texture/pictures/13.jpg", "objects/frame13.obj", [0, 0, 0])
loader.add_object("drzwi", "texture/drzwi.jpg", "objects/drzwi.obj", [0, 0, 0])
loader.add_object("drzwiz", "texture/drzwi.jpg", "objects/drzwiz.obj", [0, 0, 0])
loader.add_object("lawka_srodek", "texture/Marmur3.jpg", "objects/lawka_srodek.obj", [24, 0, 75])
loader.add_object("plant1", "texture/plant.png", "objects/plant.obj", [2.75, 0, 52.75])
loader.add_object("plant2", "texture/plant.png", "objects/plant.obj", [2.75, 0, 97.25])
loader.add_object("plant3", "texture/plant.png", "objects/plant.obj", [72.25, 0, 52.75])
loader.add_object("plant4", "texture/plant.png", "objects/plant.obj", [72.25, 0, 97.25])
loader.add_object("plant5", "texture/plant.png", "objects/plant.obj", [28.25, 0, 2.75])
loader.add_object("plant6", "texture/plant.png", "objects/plant.obj", [46.75, 0, 2.75])
loader.add_object("bench_outside", "texture/hipster.jpg", "objects/bench.obj", [23, 0, 25])
loader.add_object("bench_outside2", "texture/hipster.jpg", "objects/bench.obj", [53, 0, 25])
loader.add_object("statue", "texture/statue.jpg", "objects/statue.obj", [37.5, 0, 97])

# Przesłanie przetworzonych obiektów do GPU
loader.send_to_GPU()

# Kompilacja shadera
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


# Ustawienie światła
lightColor = pyrr.Vector4([1.0, 1.0, 1.0, 1.0])
lightPosition = pyrr.Vector3([0.0, 0.0, 0.0])
glUniform4f(glGetUniformLocation(shader, "lightColor"), lightColor[0], lightColor[1], lightColor[2], lightColor[3])

glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

# Obsługa dźwięku
if sound_enabled == True:
    mixer.init()
    music = mixer.Sound('music/young_and_beautiful.mp3')
    music.play()
    sound = Sound(music, pyrr.Vector3([65.5, 7, 75]), cam.get_position())


# Pętla główna
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
    model2 = pyrr.matrix44.multiply(rot_y, pyrr.matrix44.create_from_translation(pyrr.Vector3([65.5, 7, 75])))

    glUniform3f(glGetUniformLocation(shader, "camPos"), cam.camera_pos[0], cam.camera_pos[1], cam.camera_pos[2])


    # Rysowanie obiektów
    loader.draw("floor", model_loc)
    loader.draw("cube2", model_loc, model2)
    loader.draw("wall", model_loc)
    loader.draw("ceiling", model_loc)
    loader.draw("grass", model_loc)
    loader.draw("LawkaSciana", model_loc, loader.change_orientation("LawkaSciana", "XY", 90, 90))
    loader.draw("duze_skrzypce", model_loc)
    loader.draw("maly_pan", model_loc)
    loader.draw("instrumenty", model_loc)
    loader.draw("muzycy", model_loc)
    loader.draw("gitarzysta", model_loc)
    loader.draw("jan_matejko", model_loc)
    loader.draw("van_gogh", model_loc)
    loader.draw("miasto", model_loc)
    loader.draw("most", model_loc)
    loader.draw("domki", model_loc)
    loader.draw("alejka", model_loc)
    loader.draw("mostek", model_loc)
    loader.draw("las", model_loc)
    loader.draw("drzwi", model_loc)
    loader.draw("drzwiz", model_loc)
    loader.draw("lawka_srodek", model_loc, loader.change_orientation("lawka_srodek", 'X', 90))
    loader.draw("plant1", model_loc)
    loader.draw("plant2", model_loc)
    loader.draw("plant3", model_loc)
    loader.draw("plant4", model_loc)
    loader.draw("plant5", model_loc)
    loader.draw("plant6", model_loc)
    loader.draw("bench_outside", model_loc, loader.change_orientation("bench_outside", 'Y', 90))
    loader.draw("bench_outside2", model_loc, loader.change_orientation("bench_outside2", 'Y', 90))
    loader.draw("statue", model_loc, loader.change_orientation("statue", "XY", 90, 180))

    glfw.swap_buffers(window)

# Zamykanie aplikacji i zwalnianie zasobów
glfw.terminate()

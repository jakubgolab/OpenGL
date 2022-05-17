import math

import TextureLoader
from ObjLoader import ObjLoader
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import pyrr

class Object:
    def __init__(self, name, indices, buffer, texturePath, coordinates):
        self.name = name
        self.indices = indices
        self.buffer = buffer
        self.texturePath = texturePath
        self.coordinates = pyrr.matrix44.create_from_translation(pyrr.Vector3(coordinates))


class Load_object:
    def __init__(self):
        self.objects = []
        self.objects_names = []
        self.VAO = None
        self.VBO = None
        self.textures = None

    def add_object(self, name, texture_path, obj_path, coordinates):
        if name in self.objects_names:
            print("Wybrany obiekt już istnieje!")
        else:
            indices, buffer = ObjLoader.load_model(obj_path)
            self.objects.append(Object(name, indices, buffer, texture_path, coordinates))
            self.objects_names.append(name)
            print("Dodano obiekt " + name)

    def send_to_GPU(self):
        index = 0
        self.VAO = glGenVertexArrays(len(self.objects))
        self.VBO = glGenBuffers(len(self.objects))
        self.textures = glGenTextures(len(self.objects))
        for object in self.objects:
            # VAO
            glBindVertexArray(self.VAO[index])

            # Vertex Buffer Object
            glBindBuffer(GL_ARRAY_BUFFER, self.VBO[index])
            glBufferData(GL_ARRAY_BUFFER, object.buffer.nbytes, object.buffer, GL_STATIC_DRAW)

            # vertices
            glEnableVertexAttribArray(0)
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, object.buffer.itemsize * 8, ctypes.c_void_p(0))
            # textures
            glEnableVertexAttribArray(1)
            glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, object.buffer.itemsize * 8, ctypes.c_void_p(12))
            # normals
            glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, object.buffer.itemsize * 8, ctypes.c_void_p(20))
            glEnableVertexAttribArray(2)

            # texture
            TextureLoader.load_texture(object.texturePath, self.textures[index])

            index += 1

    def draw(self, name, model_loc, model_pos = None):
        if model_pos is None:
            position = self.objects_names.index(name)
            glBindVertexArray(self.VAO[position])
            glBindTexture(GL_TEXTURE_2D, self.textures[position])
            glUniformMatrix4fv(model_loc, 1, GL_FALSE, self.objects[position].coordinates)
            glDrawArrays(GL_TRIANGLES, 0, len(self.objects[position].indices))
        else:
            position = self.objects_names.index(name)
            glBindVertexArray(self.VAO[position])
            glBindTexture(GL_TEXTURE_2D, self.textures[position])
            glUniformMatrix4fv(model_loc, 1, GL_FALSE, model_pos)
            glDrawArrays(GL_TRIANGLES, 0, len(self.objects[position].indices))

    def change_orientation(self, name, how, degrees, degrees2=None):
        position = self.objects_names.index(name)
        radians = math.radians(degrees)
        radians2 = math.radians(degrees2)
        if how == 'X':
            rot = pyrr.Matrix44.from_x_rotation(radians)
            model = pyrr.matrix44.multiply(rot, self.objects[position].coordinates)
            return model
        elif how == 'Y':
            rot = pyrr.Matrix44.from_y_rotation(radians)
            model = pyrr.matrix44.multiply(rot, self.objects[position].coordinates)
            return model
        elif how == 'XY':
            rot_x = pyrr.Matrix44.from_x_rotation(radians)
            rot_y = pyrr.Matrix44.from_y_rotation(radians2)
            rot = pyrr.matrix44.multiply(rot_x, rot_y)
            model = pyrr.matrix44.multiply(rot, self.objects[position].coordinates)
            return model
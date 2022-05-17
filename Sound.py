import pyrr
from pyrr import *
from pygame import mixer
from scipy.spatial import distance

class Sound():
    def __init__(self, music, obj_pos, curr_pos):
        self.music = music
        self.obj_pos = obj_pos
        self.curr_pos = curr_pos

    def calculate_distance(self):
        x, y, z = self.obj_pos.xyz
        a = [x, y, z]
        x, y, z = self.curr_pos.xyz
        b = [x, y, z]
        dist = distance.euclidean(a, b)
        return dist

    def update_pos(self, curr_pos):
        self.curr_pos = curr_pos

    def change_volume(self):
        dist = self.calculate_distance()
        self.music.set_volume(1.0/dist)
import numpy as np
from openGL_toObj import convert

floor_vertices = [25, 0, 0, 0, 0,
                  50, 0, 0, 8, 0,
                  25, 0, 50, 0, 16,
                  50, 0, 50, 8, 16,
                  0, 0, 50, 0, 0,
                  0, 0, 100, 0, 16,
                  75, 0, 100, 24, 16,
                  75, 0, 50, 24, 0]

floor_indices = [0, 1, 2,
                 1, 2, 3,
                 4, 5, 7,
                 5, 6, 7]

floor_vertices = np.array(floor_vertices, dtype=np.float32)
floor_indices = np.array(floor_indices, dtype=np.uint32)

# convert(floor_vertices, floor_indices, 'floor2')

wall_vertices = [
#Daszek T ściana 1
    25, 0, 50, 0, 0,    #0
    0, 0, 50, 8, 0,     #1
    25, 25, 50, 0, 8,   #2
    0, 25, 50, 8, 8,    #3
#Daszek T ściana 2
    0, 0, 50, 0, 0,     #4
    0, 0, 100, 16, 0,   #5
    0, 25, 50, 0, 8,    #6
    0, 25, 100, 16, 8,  #7
#Daszek T ściana 3
    0, 0, 100, 0, 0,    #8
    75, 0, 100, 24, 0,  #9
    0, 25, 100, 0, 8,   #10
    75, 25, 100, 24, 8, #11
#Daszek T ściana 4 (na przeciwko 2)
    75, 0, 100, 0, 0,   #12
    75, 0, 50, 16, 0,   #13
    75, 25, 100, 0, 8,  #14
    75, 25, 50, 16, 8,  #15
#Daszek T ściana 5 (odbicie 1)
    75, 0, 50, 0, 0,    #16
    50, 0, 50, 8, 0,
    75, 25, 50, 0, 8,
    50, 25, 50, 8, 8,   #19
#Noga T ściana 1
    50, 0, 50, 0, 0,    #20
    50, 0, 0, 16, 0,
    50, 25, 50, 0, 8,
    50, 25, 0, 16, 8,   #23
#Noga T ściana 2 (odbicie 1)
    25, 0, 0, 0, 0,     #24
    25, 0, 50, 16, 0,
    25, 25, 0, 0, 8,
    25, 25, 50, 16, 8,  #27
#Noga T ściana 3
    50, 0, 0, 0, 0,     #28
    25, 0, 0, 8, 0,
    50, 25, 0, 0, 8,
    25, 25, 0, 8, 8]

wall_indices = [0, 1, 2, 1, 2, 3,
                4, 5, 6, 5, 6, 7,
                8, 9, 10, 9, 10, 11,
                12, 13, 14, 13, 14, 15,
                16, 17, 18, 17, 18, 19,
                20, 21, 22, 21, 22, 23,
                24, 25, 26, 25, 26, 27,
                28, 29, 30, 29, 30, 31]

wall_vertices = np.array(wall_vertices, dtype=np.float32)
wall_indices = np.array(wall_indices, dtype=np.uint32)

# convert(wall_vertices, wall_indices, 'wall')

ceiling_vertices = [25, 25, 0, 0, 0,
                  50, 25, 0, 8, 0,
                  25, 25, 50, 0, 16,
                  50, 25, 50, 8, 16,
                  0, 25, 50, 0, 0,
                  0, 25, 100, 0, 16,
                  75, 25, 100, 24, 16,
                  75, 25, 50, 24, 0]

ceiling_indices = [0, 1, 2,
                   1, 2, 3,
                   4, 5, 7,
                   5, 6, 7]

ceiling_vertices = np.array(ceiling_vertices, dtype=np.float32)
ceiling_indices = np.array(ceiling_indices, dtype=np.uint32)

# convert(ceiling_vertices, ceiling_indices, 'ceiling')

grass_vertices = [-100, 0, -100, 0, 0,
                  100, 0, -100, 50, 0,
                  -100, 0, 100, 0, 50,
                  100, 0, 100, 50, 50]

grass_indices = [0, 1, 2, 1, 2, 3]

grass_vertices = np.array(grass_vertices, dtype=np.float32)
grass_indices = np.array(grass_indices, dtype=np.uint32)

convert(grass_vertices, grass_indices, 'grass')

frame1_vertices = [-100, 0, -100, 0, 0,
                  100, 0, -100, 50, 0,
                  -100, 0, 100, 0, 50,
                  100, 0, 100, 50, 50]

frame1_indices = [0, 1, 2, 1, 2, 3]

frame1_vertices = np.array(frame1_vertices, dtype=np.float32)
frame1_indices = np.array(frame1_indices, dtype=np.uint32)

convert(frame1_vertices, frame1_indices, 'frame1')
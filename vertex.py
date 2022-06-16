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

# convert(grass_vertices, grass_indices, 'grass')

frame1_vertices = [74.50, 7, 90, 1, 0, #A
                  74.50, 15, 90, 1, 1, #B
                  74.50, 7, 60, 0, 0,  #C
                  74.50, 15, 60, 0, 1] #D

frame1_indices = [0, 1, 2, 1, 2, 3]

frame1_vertices = np.array(frame1_vertices, dtype=np.float32)
frame1_indices = np.array(frame1_indices, dtype=np.uint32)

# convert(frame1_vertices, frame1_indices, 'frame1')

frame2_vertices = [70, 7, 50.5, 1, 0, #A
                  70, 15, 50.5, 1, 1, #B
                  65, 15, 50.50, 0, 1,  #C
                  65, 7, 50.50, 0, 0] #D

frame2_indices = [0, 1, 2, 3, 2, 0]

frame2_vertices = np.array(frame2_vertices, dtype=np.float32)
frame2_indices = np.array(frame2_indices, dtype=np.uint32)

# convert(frame2_vertices, frame2_indices, 'frame2')

frame3_vertices = [60, 7, 50.5, 1, 0, #A
                  60, 15, 50.5, 1, 1, #B
                  55, 15, 50.50, 0, 1,  #C
                  55, 7, 50.50, 0, 0] #D

frame3_indices = [0, 1, 2, 3, 2, 0]

frame3_vertices = np.array(frame3_vertices, dtype=np.float32)
frame3_indices = np.array(frame3_indices, dtype=np.uint32)

# convert(frame3_vertices, frame3_indices, 'frame3')

frame4_vertices = [55, 7, 99.5, 1, 0, #A
                  55, 15, 99.5, 1, 1, #B
                  60, 15, 99.5, 0, 1,  #C
                  60, 7, 99.5, 0, 0] #D

frame4_indices = [0, 1, 2, 3, 2, 0]

frame4_vertices = np.array(frame4_vertices, dtype=np.float32)
frame4_indices = np.array(frame4_indices, dtype=np.uint32)

# convert(frame4_vertices, frame4_indices, 'frame4')

frame5_vertices = [65, 7, 99.5, 1, 0, #A
                  65, 15, 99.5, 1, 1, #B
                  70, 15, 99.5, 0, 1,  #C
                  70, 7, 99.5, 0, 0] #D

frame5_indices = [0, 1, 2, 3, 2, 0]

frame5_vertices = np.array(frame5_vertices, dtype=np.float32)
frame5_indices = np.array(frame5_indices, dtype=np.uint32)

# convert(frame5_vertices, frame5_indices, 'frame5')

frame6_vertices =[49.5, 7, 40, 1, 0,
                  49.5, 18, 40, 1, 1,
                  49.5, 18, 10 , 0, 1,
                  49.5, 7, 10, 0, 0]

frame6_indices = [0, 1, 2, 3, 2, 0]

frame6_vertices = np.array(frame6_vertices, dtype=np.float32)
frame6_indices = np.array(frame6_indices, dtype=np.uint32)

# convert(frame6_vertices, frame6_indices, 'frame6')

frame7_vertices = [25.5, 7, 10, 1, 0,
                   25.5, 15, 10, 1, 1,
                   25.5, 15, 30, 0, 1,
                   25.5, 7, 30, 0, 0]

frame7_indices = [0, 1, 2, 3, 2, 0]

frame7_vertices = np.array(frame7_vertices, dtype=np.float32)
frame7_indices = np.array(frame7_indices, dtype=np.uint32)

# convert(frame7_vertices, frame7_indices, 'frame7')

frame8_vertices = [0.5, 7, 60, 1, 0,
                  0.5, 15, 60, 1, 1,
                  0.5, 15, 70, 0, 1,
                  0.5, 7, 70, 0, 0]

frame8_indices = [0, 1, 2, 3, 2, 0]

frame8_vertices = np.array(frame8_vertices, dtype=np.float32)
frame8_indices = np.array(frame8_indices, dtype=np.uint32)

# convert(frame8_vertices, frame8_indices, 'frame8')

frame9_vertices = [0.5, 7, 80, 1, 0,
                  0.5, 15, 80, 1, 1,
                  0.5, 15, 90, 0, 1,
                  0.5, 7, 90, 0, 0]

frame9_indices = [0, 1, 2, 3, 2, 0]

frame9_vertices = np.array(frame9_vertices, dtype=np.float32)
frame9_indices = np.array(frame9_indices, dtype=np.uint32)

# convert(frame9_vertices, frame9_indices, 'frame9')

frame10_vertices = [20, 7, 50.5, 1, 0,
                  20, 15, 50.5, 1, 1,
                  15, 15, 50.5, 0, 1,
                  15, 7, 50.5, 0, 0]

frame10_indices = [0, 1, 2, 3, 2, 0]

frame10_vertices = np.array(frame10_vertices, dtype=np.float32)
frame10_indices = np.array(frame10_indices, dtype=np.uint32)

# convert(frame10_vertices, frame10_indices, 'frame10')

frame11_vertices = [10, 7, 50.5, 1, 0,
                  10, 15, 50.5, 1, 1,
                  5, 15, 50.5, 0, 1,
                  5, 7, 50.5, 0, 0]

frame11_indices = [0, 1, 2, 3, 2, 0]

frame11_vertices = np.array(frame11_vertices, dtype=np.float32)
frame11_indices = np.array(frame11_indices, dtype=np.uint32)

# convert(frame11_vertices, frame11_indices, 'frame11')

frame12_vertices = [5, 7, 99.5, 1, 0,
                  5, 15, 99.5, 1, 1,
                  10, 15, 99.5, 0, 1,
                  10, 7, 99.5, 0, 0]

frame12_indices = [0, 1, 2, 3, 2, 0]

frame12_vertices = np.array(frame12_vertices, dtype=np.float32)
frame12_indices = np.array(frame12_indices, dtype=np.uint32)

# convert(frame12_vertices, frame12_indices, 'frame12')

frame13_vertices = [15, 7, 99.5, 1, 0,
                  15, 15, 99.5, 1, 1,
                  20, 15, 99.5, 0, 1,
                  20, 7, 99.5, 0, 0]

frame13_indices = [0, 1, 2, 3, 2, 0]

frame13_vertices = np.array(frame13_vertices, dtype=np.float32)
frame13_indices = np.array(frame13_indices, dtype=np.uint32)

# convert(frame13_vertices, frame13_indices, 'frame13')

drzwi_vertices = [32.5, 0, 0.5, 1, 0,
                  32.5, 12, 0.5, 1, 1,
                  42.5, 12, 0.5, 0, 1,
                  42.5, 0, 0.5, 0, 0]

drzwi_indices = [0, 1, 2, 3, 2, 0]

drzwi_vertices = np.array(drzwi_vertices, dtype=np.float32)
drzwi_indices = np.array(drzwi_indices, dtype=np.uint32)

# convert(drzwi_vertices, drzwi_indices, 'drzwi')

drzwiz_vertices = [32.5, 0, -0.5, 1, 0,
                  32.5, 12, -0.5, 1, 1,
                  42.5, 12, -0.5, 0, 1,
                  42.5, 0, -0.5, 0, 0]

drzwiz_indices = [0, 1, 2, 3, 2, 0]

drzwiz_vertices = np.array(drzwiz_vertices, dtype=np.float32)
drzwiz_indices = np.array(drzwiz_indices, dtype=np.uint32)

# convert(drzwiz_vertices, drzwiz_indices, 'drzwiz')
import numpy as np

# współrzędne wierzchołków      # współrzędne textur
vertices = [-0.5, -0.5,  0.5, 0.0, 0.0,
             0.5, -0.5,  0.5, 1.0, 0.0,
             0.5,  0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5,  0.5, 0.0, 1.0,

            -0.5, -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, -0.5, 1.0, 0.0,
             0.5,  0.5, -0.5, 1.0, 1.0,
            -0.5,  0.5, -0.5, 0.0, 1.0,

             0.5, -0.5, -0.5, 0.0, 0.0,
             0.5,  0.5, -0.5, 1.0, 0.0,
             0.5,  0.5,  0.5, 1.0, 1.0,
             0.5, -0.5,  0.5, 0.0, 1.0,

            -0.5,  0.5, -0.5, 0.0, 0.0,
            -0.5, -0.5, -0.5, 1.0, 0.0,
            -0.5, -0.5,  0.5, 1.0, 1.0,
            -0.5,  0.5,  0.5, 0.0, 1.0,

            -0.5, -0.5, -0.5, 0.0, 0.0,
             0.5, -0.5, -0.5, 1.0, 0.0,
             0.5, -0.5,  0.5, 1.0, 1.0,
            -0.5, -0.5,  0.5, 0.0, 1.0,

             0.5, 0.5, -0.5, 0.0, 0.0,
            -0.5, 0.5, -0.5, 1.0, 0.0,
            -0.5, 0.5,  0.5, 1.0, 1.0,
             0.5, 0.5,  0.5, 0.0, 1.0]

# Ponowne wykorzystanie wierzchołków
indices = [ 0,  1,  2,  2,  3,  0,
            4,  5,  6,  6,  7,  4,
            8,  9, 10, 10, 11,  8,
           12, 13, 14, 14, 15, 12,
           16, 17, 18, 18, 19, 16,
           20, 21, 22, 22, 23, 20]

vertices = np.array(vertices, dtype=np.float32) # konwertowanie macierzy na macierz nunmpy
indices = np.array(indices, dtype=np.uint32) # konwertowanie macierzy na macierz numpy


def convert(vertices, indices, nazwa, normals = None):
    flag = False
    vertex = []
    texture = []
    if (len(indices) % 3 == 0) and (len(vertices) % 5 == 0):
        flag = True

    if not(flag):
        print("Niepoprawny format danych wejściowych.")
        return 0
    else:
        nazwa = nazwa + ".obj"
        file = open(nazwa, 'w')
        file.write("o " + nazwa.split(".")[0] + "\n") # nagłówek pliku obj
        iterator = 0
        for element in vertices:
            if iterator in [0, 1, 2]:
                vertex.append(element)
                iterator += 1
            elif iterator == 3:
                texture.append(element)
                iterator += 1
            elif iterator == 4:
                texture.append(element)
                iterator = 0
        iterator = 0
        for v in vertex:
            if iterator == 0:
                file.write("v ")
                file.write(str(float(v)))
                file.write(" ")
                iterator += 1
            elif iterator == 1:
                file.write(str(float(v)))
                file.write(" ")
                iterator += 1
            elif iterator == 2:
                file.write(str(float(v)))
                file.write("\n")
                iterator = 0
        iterator = 0
        for vt in texture:
            if iterator == 0:
                file.write("vt ")
                file.write(str(float(vt)))
                file.write(" ")
                iterator += 1
            elif iterator == 1:
                file.write(str(float(vt)))
                file.write("\n")
                iterator = 0
        if (normals == None):
            file.write("vn 0.0 0.0 0.0\n")
            file.write("s off\n")
        iterator = 0
        for f in indices:
            if iterator == 0:
                file.write("f " + str(f+1) + "/" + str(f+1) + "/1")
                iterator += 1
            elif iterator == 1:
                file.write(" " + str(f+1) + "/" + str(f+1) + "/1")
                iterator += 1
            elif iterator == 2:
                file.write(" " + str(f+1) + "/" + str(f+1) + "/1\n")
                iterator = 0
        file.close()

# convert(vertices, indices, "cube")
import numpy as np
import random as rd
import math
import os
from stl import mesh


FACES = np.array([
    [0, 3, 1],
    [1, 3, 2],
    [0, 4, 7],
    [0, 7, 3],
    [4, 5, 6],
    [4, 6, 7],
    [5, 1, 2],
    [5, 2, 6],
    [2, 3, 6],
    [3, 7, 6],
    [0, 1, 5],
    [0, 5, 4]])


class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def toVector(self):
        return [self.x, self.y, self.z]

    def updateFromVector(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]
        return self


class cuboid:
    def __init__(self, x):
        self.vertices = [Vertex(0, 0, 0), Vertex(x, 0, 0), Vertex(x, x, 0), Vertex(0, x, 0),
                         Vertex(0, 0, x), Vertex(x, 0, x), Vertex(x, x, x), Vertex(0, x, x)]

    def randomSize(self, roomSize):
        xAxis = rd.uniform(-1, roomSize/2)
        yAxis = rd.uniform(-1, roomSize/2)
        zAxis = roomSize/4
        for i in range(0, 2):
            self.vertices[i+1].x += xAxis
            self.vertices[i+5].x += xAxis
            self.vertices[i].y += yAxis
            self.vertices[i+4].y += yAxis
        for i in range(4, 8):
            self.vertices[i].z += zAxis
        return self

    def stayInRoom(self, roomSize):
        smallValue = rd.uniform(0, 1)
        for vertex in self.vertices:
            if (vertex.x > roomSize):
                diff = vertex.x - roomSize + smallValue
                for v in self.vertices:
                    v.x = v.x - diff
            if (vertex.y > roomSize):
                diff = vertex.y - roomSize + smallValue
                for v in self.vertices:
                    v.y = v.y - diff
        return self

    def randomRotate(self):
        angle = rd.uniform(0.0, 9.0)
        cosAngle = math.cos(angle)
        sinAngle = math.sin(angle)
        rotateM = np.array([[cosAngle, -sinAngle, 0],
                            [sinAngle, cosAngle, 0],
                            [0,  0, 1]])
        for v in self.vertices:
            v = v.updateFromVector(np.matmul(rotateM, v.toVector()))
        return self

    def randomMove(self, roomSize):
        Movex = rd.uniform(0, 2*roomSize)
        Movey = rd.uniform(0, 2*roomSize)
        for v in self.vertices:
            v.x += Movex
            v.y += Movey
        return self

    def getNpArray(self):
        a = np.empty(shape=(8, 3))
        for i in range(8):
            a[i, 0] = self.vertices[i].x
            a[i, 1] = self.vertices[i].y
            a[i, 2] = self.vertices[i].z
        return a


class room:
    def __init__(self, objNum, roomSize):
        if(roomSize):
            self.roomSize = roomSize
        else:
            self.roomSize = rd.uniform(5, 15)

        self.mesh = mesh.Mesh(
            np.zeros(FACES.shape[0] * objNum, dtype=mesh.Mesh.dtype))
        objNumWritten = 0

        for _ in range(objNum):
            c = cuboid(1)

            # transforming the object
            c = c.randomSize(self.roomSize).randomRotate().randomMove(
                self.roomSize).stayInRoom(self.roomSize)

            vertices = c.getNpArray()

            for i, fi in enumerate(FACES):
                for j in range(3):
                    i_ = i + (objNumWritten * FACES.shape[0])
                    self.mesh.vectors[i_][j] = vertices[fi[j], :]
            objNumWritten += 1

    def writeToStl(self, path, name):
        name += "RS_" + str(self.roomSize)+"_"
        if not os.path.exists(path):
            os.makedirs(path)
        self.mesh.save(path + '/'+name+'.stl')

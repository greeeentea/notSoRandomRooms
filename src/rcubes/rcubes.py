import numpy as np
import random as rd
import math
from stl import mesh
import os


#	 g +--------+ f
#	  /        /|
#	 /        / |
#	+--------+e |
#	| h      |  |
#	|c +--------+ b
#	| /      | /
#	|/       |/
#d	+--------+ a
#


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

    def backTo1(self):
        self.x = self.x/abs(self.x)
        self.y = self.y/abs(self.y)
        self.z = self.z/abs(self.z)

    def toVector(self):
        return [self.x, self.y, self.z]

    def updateFromVector(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]
        return self


class cuboid:
    def __init__(self, x):
        self.vertices = [Vertex(-x, -x, -x), Vertex(x, -x, -x), Vertex(x, x, -x), Vertex(-x, x, -x),
                         Vertex(-x, -x, x), Vertex(x, -x, x), Vertex(x, x, x), Vertex(-x, x, x)]

    def backTo1(self):
        for v in self.vertices:
            v.backTo1()

    def randomSize(self):
        xAxis = rd.uniform(-1.9, 1.9)
        yAxis = rd.uniform(-1.9, 1.9)
        for i in range(0, 2):
            self.vertices[i+1].x += xAxis
            self.vertices[i+5].x += xAxis
            self.vertices[i].y += yAxis
            self.vertices[i+4].y += yAxis
        zAxis = rd.uniform(-1.9, 1.9)
        for i in range(4, 8):
            self.vertices[i].z += zAxis

    def randomRotate(self):
        angle = rd.uniform(0.0, 360.0)
        cosAngle = math.cos(angle)
        sinAngle = math.sin(angle)
        rotateM = np.array([[cosAngle, -sinAngle, 0],
                            [sinAngle, cosAngle, 0],
                            [0,  0, 1]])
        for v in self.vertices:
            v = v.updateFromVector(np.matmul(v.toVector(), rotateM))

    def randomMove(self):

        Movex = rd.uniform(-10, 10)
        Movey = rd.uniform(-10, 10)
        for v in self.vertices:
            v.x += Movex
            v.y += Movey

    def getNpArray(self):
        a = np.empty(shape=(8, 3))
        for i in range(8):
            a[i, 0] = self.vertices[i].x
            a[i, 1] = self.vertices[i].y
            a[i, 2] = self.vertices[i].z
        return a


class cube:
    def __init__(self, objNum):
        self.mesh = mesh.Mesh(
            np.zeros(FACES.shape[0] * objNum, dtype=mesh.Mesh.dtype))
        objNumWritten = 0
        c = cuboid(1)

        for _ in range(objNum):
            c.backTo1()
            c.randomMove()
            c.randomRotate()
            c.randomSize()

            vertices = c.getNpArray()

            for i, fi in enumerate(FACES):
                for j in range(3):
                    i_ = i + (objNumWritten * FACES.shape[0])
                    self.mesh.vectors[i_][j] = vertices[fi[j], :]
            objNumWritten += 1

    def writeToStl(self, name):
        if not os.path.exists('../stl'):
            os.makedirs('../stl')
        self.mesh.save('../stl/'+name+'.stl')

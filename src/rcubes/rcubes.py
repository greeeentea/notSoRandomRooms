import numpy as np
import random as rd
import math
from stl import mesh


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

    def toVector(self):
        return [self.x, self.y, self.z]

    def updateFromVector(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]
        return self


class cube:
    def __init__(self):
        self.a = Vertex(-1.0, -1.0, -1.0)
        self.b = Vertex(1.0, -1.0, -1.0)
        self.c = Vertex(1.0, 1.0, -1.0)
        self.d = Vertex(-1.0, 1.0, -1.0)
        self.e = Vertex(-1.0, -1.0, 1.0)
        self.f = Vertex(1.0, -1.0, 1.0)
        self.g = Vertex(1.0, 1.0, 1.0)
        self.h = Vertex(-1.0, 1.0, 1.0)

    def randomScale(self):
        xAxis = rd.uniform(-1.9, 1.9)
        self.b.x += xAxis
        self.c.x += xAxis
        self.f.x += xAxis
        self.g.x += xAxis
        yAxis = rd.uniform(-1.9, 1.9)
        self.a.y += yAxis
        self.b.y += yAxis
        self.e.y += yAxis
        self.f.y += yAxis
        zAxis = rd.uniform(-1.9, 1.9)
        self.e.z += zAxis
        self.f.z += zAxis
        self.g.z += zAxis
        self.h.z += zAxis

    def randomRotate(self):
        angle = rd.uniform(0.0, 360.0)
        cosAngle = math.cos(angle)
        sinAngle = math.sin(angle)
        rotateM = np.array([[cosAngle, -sinAngle, 0],
                            [sinAngle, cosAngle, 0],
                            [0,  0, 1]])
        self.a = self.a.updateFromVector(np.matmul(self.a.toVector(), rotateM))
        self.b = self.b.updateFromVector(np.matmul(self.b.toVector(), rotateM))
        self.c = self.c.updateFromVector(np.matmul(self.c.toVector(), rotateM))
        self.d = self.d.updateFromVector(np.matmul(self.d.toVector(), rotateM))
        self.e = self.e.updateFromVector(np.matmul(self.e.toVector(), rotateM))
        self.f = self.f.updateFromVector(np.matmul(self.f.toVector(), rotateM))
        self.g = self.g.updateFromVector(np.matmul(self.g.toVector(), rotateM))
        self.h = self.h.updateFromVector(np.matmul(self.h.toVector(), rotateM))

    def randomMove(self):
        Movex = rd.uniform(0, 10)
        Movey = rd.uniform(0, 10)
        self.a.y += Movey
        self.b.y += Movey
        self.c.y += Movey
        self.d.y += Movey
        self.e.y += Movey
        self.f.y += Movey
        self.g.y += Movey
        self.h.y += Movey
        self.a.x += Movex
        self.b.x += Movex
        self.c.x += Movex
        self.d.x += Movex
        self.e.x += Movex
        self.f.x += Movex
        self.g.x += Movex
        self.h.x += Movex

    def writeToStl(self, name):
        vertices = np.array([
            [self.a.x, self.a.y, self.a.z],
            [self.b.x, self.b.y, self.b.z],
            [self.c.x, self.c.y, self.c.z],
            [self.d.x, self.d.y, self.d.z],
            [self.e.x, self.e.y, self.e.z],
            [self.f.x, self.f.y, self.f.z],
            [self.g.x, self.g.y, self.g.z],
            [self.h.x, self.h.y, self.h.z], ])

        cube = mesh.Mesh(np.zeros(FACES.shape[0], dtype=mesh.Mesh.dtype))
        for i, f in enumerate(FACES):
            for j in range(3):
                cube.vectors[i][j] = vertices[f[j], :]

        cube.save('../stl_files/'+name+'.stl')

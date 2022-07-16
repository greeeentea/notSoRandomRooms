class Vertex:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def backTo1(self):
        self.x = abs(self.x) and self.x / abs(self.x) or 0  # a / b
        self.y = abs(self.y) and self.y / abs(self.y) or 0  # a / b
        self.z = abs(self.z) and self.z / abs(self.z) or 0  # a / b

    def toVector(self):
        return [self.x, self.y, self.z]

    def updateFromVector(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]
        return self
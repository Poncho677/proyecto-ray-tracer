class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __eq__(self, otro):
        if isinstance(otro, Vector):
            return self.x == otro.x and self.y == otro.y and self.z == otro.z
        return False

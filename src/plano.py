from vector import Vector
from figuras import Figuras

<<<<<<< HEAD
class plano(Figuras):
=======
class Plano(Figuras):
>>>>>>> 970907b3a0723c65b242d6dcda03895489f5b49a

    def __init__(self, punto, normal, color):
        super().__init__(color, punto)
        self.normal = Vector(normal[0], normal[1], normal[2])

<<<<<<< HEAD
=======
    def __iter__(self):
        return super().__iter__()

>>>>>>> 970907b3a0723c65b242d6dcda03895489f5b49a
    def getColor(self):
        return self.color

    def getPunto(self):
        return self.punto

    def getNormal():
        return self.normal


        

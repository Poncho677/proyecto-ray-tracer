from vector import Vector
from figuras import Figuras

class plano(Figuras):

    def __init__(self, punto, normal, color):
        super().__init__(color, punto)
        self.normal = Vector(normal[0], normal[1], normal[2])

    def getColor(self):
        return self.color

    def getPunto(self):
        return self.punto

    def getNormal():
        return self.normal


        

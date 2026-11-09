from vector import Vector

class plano:

    def __init__(self, punto, normal, color):
        self.color = color
        self.punto = punto
        self.normal = Vector(normal[0], normal[1], normal[2])

    def getColor(self):
        return self.color

    def getPunto(self):
        return self.punto

    def getNormal():
        return self.normal


        

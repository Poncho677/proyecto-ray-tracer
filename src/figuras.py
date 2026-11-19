class Esfera:
    def __init__(self, centro, radio, color):
        self.centro = centro
        self.radio = radio
        self.color = color

    def interseccion(self, rayo):
        oc = rayo.origen - self.centro

    def normal_en(self, punto):
        return (punto - self.centro).normalizar()


class Plano:
    
    def __init__(self, punto, normal, color):
        self.punto = punto
        self.normal = normal
        self.color = color

    def interseccion(self, rayo):
        denom = self.normal.punto(rayo.direccion)

    def normal_en(self, punto):
            return self.normal

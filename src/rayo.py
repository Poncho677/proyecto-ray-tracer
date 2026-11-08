class Rayo:
    def __init__(self, origen, direccion):
        self.origen = origen
        self.direccion = direccion

    def punto_en(self, t):
        return self.origen + self.direccion * t

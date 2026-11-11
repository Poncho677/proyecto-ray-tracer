from vector import Vector

ARRIBA_MUNDO = Vector(0, 1, 0)


class Camara:

    def __init__(self, posicion, mira_a, fov, ancho, alto):
        if ancho <= 0 or alto <= 0:
            raise ValueError("Las dimensiones deben ser positivas")
        if fov <= 0 or fov >= 180:
            raise ValueError("El FOV debe estar entre 0 y 180 grados")
        self.posicion = posicion
        self.mira_a = mira_a
        self.fov = fov
        self.ancho = ancho
        self.alto = alto
        self.adelante = (mira_a - posicion).normalizar()
        self.derecha = self.adelante.producto_cruz(ARRIBA_MUNDO).normalizar()

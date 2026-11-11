import math

from rayo import Rayo
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
        self.arriba = self.derecha.producto_cruz(self.adelante)
        self.mitad_ancho = math.tan(math.radians(fov) / 2)
        self.mitad_alto = self.mitad_ancho * alto / ancho

    def generar_rayo(self, columna, fila):
        desplazamiento_horizontal = (2 * (columna + 0.5) / self.ancho - 1) * self.mitad_ancho
        direccion = self.adelante + self.derecha * desplazamiento_horizontal
        return Rayo(self.posicion, direccion)

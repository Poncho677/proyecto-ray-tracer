import math

e = 10**-6


class Esfera:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def interseccion(self, rayo):
        oc = rayo.origen - self.centro
        a = rayo.direccion.punto(rayo.direccion)
        b = 2 * (oc.punto(rayo.direccion))
        c = oc.punto(oc) - (self.radio**2)
        delta = (b**2) - (4 * a * c)

        # No hay intersección si el discriminante es negativo
        if delta < 0:
            return None

        raiz_delta = math.sqrt(delta)
        t1 = (-b - raiz_delta) / (2 * a)
        t2 = (-b + raiz_delta) / (2 * a)
        if t1 > e:
            return t1
        elif t2 > e:
            return t2
        else:
            return None


class Plano:
    def __init__(self, punto, normal):
        self.punto = punto
        self.normal = normal

    def interseccion(self, rayo):
        denom = self.normal.punto(rayo.direccion)

        # El rayo es paralelo al plano, no intersecta
        if abs(denom) < e:
            return None

        t = (self.punto - rayo.origen).punto(self.normal) / denom
        if t > e:
            return t
        else:
            return None

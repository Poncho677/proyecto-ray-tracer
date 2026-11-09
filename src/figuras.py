class Figuras:

e = 10**-6


class Esfera:
    def __init__(self, centro, radio, color):
        self.centro = centro
        self.radio = radio
        self.color = color

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

    def normal_en(self, punto):
        return (punto - self.centro).normalizar()


class Plano:
    def __init__(self, punto, normal, color):
        self.punto = punto
        self.normal = normal
        self.color = color

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

    def normal_en(self, punto):
            return self.normal

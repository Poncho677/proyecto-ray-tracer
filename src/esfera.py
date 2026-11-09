class Esfera:

    def __init__(self, centro, radio, color):
        self.color = color
        self.radio = radio
        self.centro = centro

    def getCentro(self):
        return self.centro

    def getRadio(self):
        return self.radio

    def getColor():
        return self.color

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
        if t1 > 0:
            return t1
        elif t2 > 0:
            return t2
        else:
            return None

                    
                
        

    

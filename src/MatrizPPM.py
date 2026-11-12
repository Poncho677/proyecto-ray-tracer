class MatrizPPM:
    def __init__(self, ancho, alto, relleno=(0.0, 0.0, 0.0)):
        self.ancho = ancho #ancho de la matriz
        self.alto =alto #alto de la matriz
        self.datos = [] #lista que va a contener los colores de las casillas

        for j in range(alto):
            fila = []
            for i in range(ancho):
                fila.append(relleno)
            self.datos.append(fila)

#Guarda el color 
    def set(self, i, j, color):
        self.datos[j][i] = color

#Regresa el color
    def get(self, i, j):
        return self.datos[j][i]

#de rgb a bytes
    def a_bytes(self):
        matriz = []
        for fila in self.datos:
            fila_ent = []
            for (r, g, b) in fila:
                fila_ent.append((
                    self._clamp(r),
                    self._clamp(g),
                    self._clamp(b),
                ))
            matriz.append(fila_ent)
        return matriz

    @staticmethod
    def _clamp(x):
        if x < 0.0:
            x = 0.0
        elif x > 1.0:
            x = 1.0
        return round(x * 255) #es como la función techo 
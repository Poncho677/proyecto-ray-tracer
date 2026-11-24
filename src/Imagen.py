from MatrizPPM import MatrizPPM  

class Imagen:
    def __init__(self, ancho, alto, camara, fondo, luz_ambiental, luces, objetos):
        self.ancho = ancho
        self.alto = alto
        self.camara = camara
        self.fondo = fondo
        self.luz_ambiental = luz_ambiental
        self.luces = luces
        self.objetos = objetos

    def calcular_pixel(self, i, j, raytracer):
     

    def render(self, raytracer):
        matriz = MatrizPPM(self.ancho, self.alto)
        for j in range(self.alto):
            for i in range(self.ancho):
                color = self.calcular_pixel(i, j, raytracer)
                matriz.set(i, j, color)
        return matriz
	
from MatrizPPM import MatrizPPM
from iluminacion import color_rayo

class Imagen:

    def __init__(self, ancho, alto, camara, escena):
        self.ancho = ancho
        self.alto = alto
        self.camara = camara
        self.escena = escena

    def calcular_pixel(self, i, j):
	    rayo = self.camara.generar_rayo(i, j)       
	    color = color_rayo(self.escena, rayo)     
	    return color

    def render(self):
	    matriz = MatrizPPM(self.ancho, self.alto)
	    for j in range(self.alto):
	        for i in range(self.ancho):
	            color = self.calcular_pixel(i, j)
	            matriz.set(i, j, color)
	    return matriz
	
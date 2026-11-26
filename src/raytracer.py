import sys
from escena import Escena
from iluminacion import color_rayo
from MatrizPPM import MatrizPPM
from EntradaError import EntradaError
from APPM import APPM

escena = Escena().leer()

if len(sys.argv) > 1:
    args = sys.argv
else:
    raise EntradaError("No se recibió texto alguno")
ruta = None
encontrado = False
for k in args:
    if ".ppm" in k:
        ruta = k
        encontrado = True

if encontrado == False:
    ruta = "salida.ppm"

ancho = escena.camara.ancho
altura = escena.camara.alto

matriz = MatrizPPM(ancho, altura)

for i in range(altura):
    for j in range(ancho):
        rayo = escena.camara.generar_rayo(j, i)
        color = color_rayo(escena, rayo)
        matriz.set(j, i, color)

escritor = APPM(ruta)
escritor.escribir(matriz)

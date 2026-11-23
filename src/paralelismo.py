import multiprocessing as mp
import time

from iluminacion import color_rayo
from MatrizPPM import MatrizPPM
from trabajadoresError import trabajadoresError

def renderizar_fila(fila: int, escena, camara) -> list:
    """Calcula los colores RGB de una fila completa de píxeles."""
    fila_colores = []
    for columna in range(camara.ancho):
        rayo = camara.generar_rayo(columna, fila)
        color = color_rayo(escena, rayo)
        fila_colores.append(color)
    return fila_colores

class RenderizadorParalelo:
    def __init__(self, trabajadores: int):
        if trabajadores < 1:
            raise TrabajadoresError("El número de trabajadores debe ser mayor o igual a 1.")
        self.trabajadores = trabajadores

    def renderizar(self, escena, camara) -> MatrizPPM:
        filas = [renderizar_fila(y, escena, camara) for y in range(camara.alto)]
        matriz = MatrizPPM(camara.ancho, camara.alto)
        matriz.datos = filas
        return matriz

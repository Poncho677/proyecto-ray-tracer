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

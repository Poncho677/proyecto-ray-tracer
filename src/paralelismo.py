import multiprocessing as mp

from Imagen import Imagen
from MatrizPPM import MatrizPPM
from trabajadoresError import TrabajadoresError

_imagen = None

def _inicializar(imagen):
    global _imagen
    _imagen = imagen

def renderizar_fila(fila: int) -> list:
    """Calcula los colores RGB de una fila completa de píxeles."""
    return [_imagen.calcular_pixel(columna, fila) for columna in range (_imagen.ancho)]


class RenderizadorParalelo:
    def __init__(self, trabajadores: int):
        if trabajadores < 1:
            raise TrabajadoresError("El número de trabajadores debe ser mayor o igual a 1.")
        self.trabajadores = trabajadores

    def renderizar(self, escena, camara) -> MatrizPPM:
        imagen = Imagen(camara.ancho, camara.alto, camara, escena)
        if self.trabajadores == 1:
            _inicializar(imagen)
            filas = [renderizar_fila(y) for y in range(imagen.alto)]
        else:
            with mp.Pool(processes=self.trabajadores, initializer=_inicializar, initargs=[imagen]) as pool:
                filas = pool.map(renderizar_fila, range(imagen.alto))

        matriz = MatrizPPM(imagen.ancho, imagen.alto)
        matriz.datos = filas
        return matriz

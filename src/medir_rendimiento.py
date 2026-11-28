import time
from camara import Camara
from escena import Escena, Luz
from figuras import Esfera, Plano
from paralelismo import RenderizadorParalelo
from vector import Vector

def crear_escena():
    objetos = [
        Plano(Vector(0, -1, 0), Vector(0, 1, 0), (0.8, 0.8, 0.8)),
        Esfera(Vector(0, 0, -3), 1, (0.9, 0.3, 0.2)),
        Esfera(Vector(2, 0, -4), 1, (0.2, 0.9, 0.3)),
        Esfera(Vector(-2, 0, -1), 1, (0.2, 0.3, 0.9)),
        Esfera(Vector(0.8, -0.6, -1.8), 0.4, (0.9, 0.9, 0.2)),
        Esfera(Vector(-1, -0.6, -2), 0.4, (0.9, 0.2, 0.9)),
        Esfera(Vector(1.5, -0.7, -2.5), 0.3, (0.3, 0.9, 0.9)),
        Esfera(Vector(-1.5, -0.7, -3), 0.3, (0.9, 0.6, 0.2)),
    ]
    luces = [
        Luz(Vector(5, 5, 0), 1.0),
        Luz(Vector(-5, 5, 2), 0.5),
        Luz(Vector(0, 6, -2), 0.4)
    ]
    escena = Escena(objetos, luces, (0.6, 0.8, 1.0), 0.1)
    camara = Camara(Vector(0, 1, 3), Vector(0, 0, -3), 60, 400, 225)
    return escena, camara

def medir(trabajadores, escena, camara):
    inicio = time.perf_counter()
    RenderizadorParalelo(trabajadores).renderizar(escena, camara)
    return time.perf_counter() - inicio

if __name__ == "__main__":
    escena, camara = crear_escena()
    segundos = medir(1, escena, camara)
    print(f"1 trabajador: {segundos:.2f} s")
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

#función para medir el rendimiento del render y sacar el promedio medido en segundos
def medir_promedio(trabajadores, escena, camara, repeticiones = 3):
    tiempos = []
    for repeticion in range(repeticiones):
        tiempos.append(medir(trabajadores, escena, camara))
    return sum(tiempos) / len(tiempos)

if __name__ == "__main__":
    escena, camara = crear_escena()
    tiempos = {}
    for trabajadores in (1, 2, 4, 8):
        tiempos[trabajadores] = medir_promedio(trabajadores, escena, camara)

    base = tiempos[1]
    print("Trabajadores   Tiempo (s)   Speedup")
    for trabajadores in tiempos:
        speedup = base / tiempos[trabajadores]
        print(f"{trabajadores:>12} {tiempos[trabajadores]:>10.2f} {speedup:>7.2f}")
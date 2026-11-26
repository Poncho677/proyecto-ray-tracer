from camara import Camara
from escena import Escena, Luz
from figuras import Esfera, Plano
from Imagen import Imagen
from paralelismo import RenderizadorParalelo
from vector import Vector

def escena_de_prueba():
    objetos = [
        Plano(Vector(0, -1, 0), Vector(0, 1, 0), (0.8,0.8,0.8)),
        Esfera(Vector(0, 0, -3), 1, (0.9, 0.3, 0.2)),
        Esfera(Vector(2, 0 ,-4), 1, (0.2, 0.9, 0.3)),
        Esfera(Vector(-2, 0, -4), 1, (0.2, 0.3, 0.9)),
        Esfera(Vector(0.8, -0.6, -1.8), 0.4, (0.9, 0.9, 0.2)),
    ]
    luces = [Luz(Vector(5, 5, 0), 1.0)]
    escena = Escena(objetos, luces, (0.6, 0.8, 1.0), 0.1)
    camara = Camara(Vector(0, 1, 3), Vector(0, 0, -3), 60, 80, 45)
    return escena, camara

def test_dimensiones_de_la_matriz():
    escena, camara = escena_de_prueba()
    matriz = RenderizadorParalelo(1).renderizar(escena, camara)
    assert len(matriz.datos) == camara.alto
    assert all(len(fila) == camara.ancho for fila in matriz.datos)
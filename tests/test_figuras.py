import pytest
from rayo import Rayo
from vector import Vector
from figuras import Esfera


@pytest.mark.parametrize(
    "centro, radio, origen, direccion, esperado",
    [
        (Vector(0, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, -1), 2),
        (Vector(0, 0, -5), 5, Vector(3, 0, 0), Vector(0, 0, -1), 1),
        (Vector(1, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, -1), 3),
        (Vector(0, 0, 0), 1, Vector(0, 0, 1), Vector(0, 0, -1), 2),
    ],
)
def test_rayo_al_centro(centro, radio, origen, direccion, esperado):
    esfera = Esfera(centro, radio)
    rayo = Rayo(origen, direccion)
    assert esfera.interseccion(rayo) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "centro, radio, origen, direccion",
    [
        (Vector(0, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, 1)),
        (Vector(1.5, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, 1)),
    ],
)
def test_esfera_sin_choque(centro, radio, origen, direccion):
    esfera = Esfera(centro, radio)
    rayo = Rayo(origen, direccion)
    assert esfera.interseccion(rayo) is None

import pytest
from rayo import Rayo
from vector import Vector
from figuras import Esfera
from figuras import Plano


# Tests con esferas
@pytest.mark.parametrize(
    "centro, radio, origen, direccion, esperado",
    [
        (Vector(0, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, -1), 2),
        (Vector(0, 0, -5), 5, Vector(3, 0, 0), Vector(0, 0, -1), 1),
        (Vector(1, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, -1), 3),
        (Vector(0, 0, 0), 1, Vector(0, 0, 1), Vector(0, 0, -1), 2),
    ],
)
def test_esfera_con_choque(centro, radio, origen, direccion, esperado):
    esfera = Esfera(centro, radio)
    rayo = Rayo(origen, direccion)
    assert esfera.interseccion(rayo) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "centro, radio, origen, direccion",
    [
        (Vector(0, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, 1)),
        (Vector(1.5, 0, -3), 1, Vector(0, 0, 0), Vector(0, 0, 1)),
        (Vector(0, 0, 0.5), 0.5, Vector(0, 0, 0), Vector(0, 0, -1)),
        (Vector(0, 0, 1.5), 0.5, Vector(0, 0, 0), Vector(0, 0, -1)),
        (Vector(0.625, 0, -3), 0.375, Vector(0, 0, 0), Vector(0, 0, -1)),
    ],
)
def test_esfera_sin_choque(centro, radio, origen, direccion):
    esfera = Esfera(centro, radio)
    rayo = Rayo(origen, direccion)
    assert esfera.interseccion(rayo) is None


# Tests con planos
@pytest.mark.parametrize(
    "punto, normal, origen, direccion, esperado",
    [
        (Vector(0, -1, 0), Vector(0, 1, 0), Vector(0, 0, 0), Vector(0, -1, 0), 1),
        (Vector(0, -1, 0), Vector(0, 1, 0), Vector(0, 2, 0), Vector(0, -1, 0), 3),
        (Vector(0, -1, 0), Vector(0, 1, 0), Vector(0, -3, 0), Vector(0, 1, 0), 2),
        (Vector(0, -1, 0), Vector(0, 2, 0), Vector(0, 0, 0), Vector(0, -1, 0), 1),
        (Vector(0, 1, 0), Vector(0, 1, 0), Vector(0, 0, 0), Vector(0, 1, 0), 1),
    ],
)
def test_plano_con_choque(punto, normal, origen, direccion, esperado):
    plano = Plano(punto, normal)
    rayo = Rayo(origen, direccion)
    assert plano.interseccion(rayo) == pytest.approx(esperado)


@pytest.mark.parametrize(
    "punto, normal, origen, direccion",
    [
        (Vector(0, -1, 0), Vector(0, 1, 0), Vector(0, 0, 0), Vector(1, 0, 0)),
        (Vector(0, -1, 0), Vector(0, 1, 0), Vector(0, 0, 0), Vector(0, 1, 0)),
        (Vector(0, -1, 0), Vector(0, 1, 0), Vector(0, -1, 0), Vector(0, -1, 0)),
        (Vector(0, 1, 0), Vector(0, 1, 0), Vector(0, 0, 0), Vector(0, -1, 0)),
    ],
)
def test_plano_sin_choque(punto, normal, origen, direccion):
    plano = Plano(punto, normal)
    rayo = Rayo(origen, direccion)
    assert plano.interseccion(rayo) is None

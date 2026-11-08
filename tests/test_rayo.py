import pytest
from rayo import Rayo
from vector import Vector


@pytest.mark.parametrize(
    "origen, direccion, t, esperado",
    [
        (Vector(0, 0, 0), Vector(0, 0, 0), 0, Vector(0, 0, 0)),
        (Vector(1, 3, 5), Vector(2, 4, 6), 3, Vector(7, 15, 23)),
        (Vector(0, 0, 0), Vector(1, 2, 3), -1, Vector(-1, -2, -3)),
        (Vector(0, 0, 0), Vector(0, 0, 1), 2, Vector(0, 0, 2)),
        (Vector(1, 3, 5), Vector(7, 9, 11), 0.5, Vector(4.5, 7.5, 10.5)),
    ],
)
def test_punto_en(origen, direccion, t, esperado):
    rayo = Rayo(origen, direccion)
    assert rayo.punto_en(t) == esperado

import pytest

from vector import Vector


@pytest.mark.parametrize(
    "vector_1, vector_2, esperado",
    [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(5, 7, 9)),
    (Vector(-1, -2, -3), Vector(-4, -5, -6), Vector(-5, -7, -9)),
    (Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)),
    ],
)
def test_suma(vector_1, vector_2, esperado):
    assert vector_1 + vector_2 == esperado

@pytest.mark.parametrize(
    "vector_1, vector_2, esperado",
    [
        (Vector(4, 5, 6), Vector(1, 2, 3), Vector(3, 3, 3)),
        (Vector(-1, -2, 3), Vector(-4, 5, -6), Vector(3, -7, 9)),
        (Vector(1, 1, 1), Vector(1, 1, 1), Vector(0, 0, 0)),
    ],
)
def test_resta(vector_1, vector_2, esperado):
    assert vector_1 - vector_2 == esperado

@pytest.mark.parametrize(
    "vector, escalar, esperado",
    [
        (Vector(1, 2, 3), 2, Vector(2, 4, 6)),
        (Vector(4, -2, 0), -3, Vector(-12, 6, 0)),
        (Vector(10, 5, 2), 0.5, Vector(5.0, 2.5, 1.0)),
        (Vector(1, 2, 3), 0, Vector(0, 0, 0)),
    ],
)
def test_producto_por_escalar(vector, escalar, esperado):
    assert vector * escalar == esperado
    assert escalar * vector == esperado

def test_producto_punto():
    assert Vector(1, 2, 3).punto(Vector(4, 5, 6)) == 32

def test_norma():
    assert Vector(3, 4, 0).norma() == pytest.approx(5.0)

def test_repr():
    v = Vector(1, -2, 3)
    assert repr(v) == "Vector(1, -2, 3)"

def test_igualdad_con_otros_tipos():
    v = Vector(1, 2, 3)
    assert v != [1, 2, 3]
    assert v != "Vector(1, 2, 3)"
    assert v != 42

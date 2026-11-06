import math
import pytest

from vector import Vector


@pytest.mark.parametrize(
    "vector_1, vector_2, esperado",
    [
    (Vector(1, 2, 3), Vector(4, 5, 6), Vector(5, 7, 9)),
    (Vector(-1, -2, -3), Vector(-4, -5, -6), Vector(-5, -7, -9)),
    (Vector(0, 0, 0), Vector(0, 0, 0), Vector(0, 0, 0)),
    ],
    ids=[
        "Vector(1, 2, 3) + Vector(4, 5, 6) = Vector(5, 7, 9)",
        "Vector(-1, -2, -3) + Vector(-4, -5, -6) = Vector(-5, -7, -9)",
        "Vector(0, 0, 0) + Vector(0, 0, 0) = Vector(0, 0, 0)"
    ]
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
    ids=[
        "Vector(4, 5, 6) - Vector(1, 2, 3) = Vector(3, 3, 3)",
        "Vector(-1, -2, 3) - Vector(-4, 5, -6) = Vector(3, -7, 9)",
        "Vector(1, 1, 1) - Vector(1, 1, 1) = Vector(0, 0, 0)"
    ]
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
    ids=[
        "Vector(1, 2, 3) * 2 = Vector(2, 4, 6)",
        "Vector(4, -2, 0) * -3 = Vector(-12, 6, 0)",
        "Vector(10, 5, 2) * 0.5 = Vector(5.0, 2.5, 1.0)",
        "Vector(1, 2, 3) * 0 = Vector(0, 0, 0)"
    ]
)
def test_producto_por_escalar(vector, escalar, esperado):
    assert vector * escalar == esperado
    assert escalar * vector == esperado

@pytest.mark.parametrize(
    "vector_1, vector_2, esperado",
    [
        (Vector(1, 2, 3), Vector(4, 5, 6), 32),
        (Vector(5, 0, 0), Vector(0, 3, 0), 0),
        (Vector(1, 2, 3), Vector(0, 0, 0), 0),
    ],
    ids=[
        "Vector(1, 2, 3).punto(Vector(4, 5, 6)) = 32",
        "Vector(5, 0, 0).punto(Vector(0, 3, 0)) = 0",
        "Vector(1, 2, 3).punto(Vector(0, 0, 0)) = 0"
    ]
)
def test_producto_punto(vector_1, vector_2, esperado):
    assert vector_1.punto(vector_2) == pytest.approx(esperado)

def test_propiedad_autoproducto_punto():
    v = Vector(2, 4, 5)
    assert v.punto(v) == pytest.approx(v.norma() ** 2)

@pytest.mark.parametrize(
    "vector, esperado",
    [
        (Vector(3, 4, 0), 5.0),
        (Vector(0, 0, 0), 0.0),
        (Vector(1, 1, 1), math.sqrt(3)),
        (Vector(-1, -2, -3), math.sqrt(14)),
    ],
    ids=[
        "||Vector(3, 4, 0)|| = 5.0",
        "||Vector(0, 0, 0)|| = 0.0",
        "||Vector(1, 1, 1)|| = 1.73205...",
        "||Vector(-1, -2, -3)|| = 3.74165..."
    ]
)
def test_norma(vector, esperado):
    assert vector.norma() == pytest.approx(esperado)

def test_repr():
    v = Vector(1, -2, 3)
    assert repr(v) == "Vector(1, -2, 3)"

def test_igualdad_con_otros_tipos():
    v = Vector(1, 2, 3)
    assert v != [1, 2, 3]
    assert v != "Vector(1, 2, 3)"
    assert v != 42

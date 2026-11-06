import pytest

from vector import Vector


def test_suma():
    assert Vector(1, 2, 3) + Vector(3, 4, 5) == Vector(4, 6, 8)

def test_resta():
    assert Vector(4, 5, 6) - Vector(1, 2, 3) == Vector(3, 3, 3)

def test_producto_por_escalar():
    assert Vector(1, 2, 3) * 2 == Vector(2, 4, 6)
    assert 2 * Vector(1, 2, 3) == Vector(2, 4, 6)

def test_producto_punto():
    assert Vector(1, 2, 3).punto(Vector(4, 5, 6)) == Vector(4, 10, 18)

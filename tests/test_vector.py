import pytest

from vector import Vector


def test_suma():
    assert Vector(1, 2, 3) + Vector(3, 4, 5) == Vector(4, 6, 8)

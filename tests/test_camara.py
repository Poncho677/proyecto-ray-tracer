import math

import pytest

from camara import Camara
from vector import Vector


def componentes(v):
    return (v.x, v.y, v.z)


@pytest.fixture
def camara_base():
    return Camara(
        Vector(0, 0, 0),
        Vector(0, 0, -1),
        60,
        401,
        225
    )


@pytest.fixture
def camara_inclinada():
    return Camara(
        Vector(0, 1, 3),
        Vector(0, 0, -3),
        60,
        401,
        225
    )


def test_crear_camara(camara_base):
    assert camara_base.posicion == Vector(0, 0, 0)
    assert camara_base.mira_a == Vector(0, 0, -1)
    assert camara_base.fov == 60
    assert camara_base.ancho == 401
    assert camara_base.alto == 225


def test_adelante(camara_base):
    assert camara_base.adelante == Vector(0,0,-1)


def test_derecha(camara_base):
    assert camara_base.derecha == Vector(1, 0, 0)

    
def test_arriba(camara_base):
    assert camara_base.arriba == Vector(0, 1, 0)


def test_camara_inclinada_adelante(camara_inclinada):
    raiz = math.sqrt(37)
    assert componentes(camara_inclinada.adelante) == pytest.approx((0, -1 / raiz, -6 / raiz))


def test_camara_inclinada_derecha(camara_inclinada):
    assert componentes(camara_inclinada.derecha) == pytest.approx((1, 0, 0))


def test_camara_inclinada_arriba(camara_inclinada):
    raiz = math.sqrt(37)
    assert componentes(camara_inclinada.arriba) == pytest.approx((0, 6 / raiz, -1 / raiz))


@pytest.mark.parametrize(
    "ancho, alto, fov",
    [
        (0, 225, 60),
        (400, -5, 60),
        (400, 225, 180)
    ]
)
def test_parametros_invalidos(ancho, alto, fov):
    with pytest.raises(ValueError):
        Camara(Vector(0, 0, 0), Vector(0, 0, -1), fov, ancho, alto)

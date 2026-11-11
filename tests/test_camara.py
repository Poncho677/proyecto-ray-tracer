import pytest

from camara import Camara
from vector import Vector


@pytest.fixture
def camara_base():
    return Camara(
        Vector(0, 0, 0),
        Vector(0, 0, -1),
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

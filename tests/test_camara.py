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


def test_ventana_fov_90_imagen_4x2():
    c = Camara(Vector(0, 0, 0), Vector(0, 0, -1), 90, 4, 2)
    assert c.mitad_ancho == pytest.approx(1.0)
    assert c.mitad_alto == pytest.approx(0.5)


def test_ventana_fov_60(camara_base):
    assert camara_base.mitad_ancho == pytest.approx(1 / math.sqrt(3))
    assert camara_base.mitad_alto == pytest.approx(1 / math.sqrt(3) * 225 / 401)


def test_rayo_sale_de_la_posicion_de_la_camara(camara_inclinada):
    rayo = camara_inclinada.generar_rayo(10, 20)
    assert rayo.origen == Vector(0, 1, 3)


def test_rayo_central_apunta_adelante(camara_base):
    rayo = camara_base.generar_rayo(200, 112)
    assert componentes(rayo.direccion) == pytest.approx((0, 0, -1))


def test_rayo_columnas_laterales(camara_base):
    assert camara_base.generar_rayo(400, 112).direccion.x > 0
    assert camara_base.generar_rayo(0, 112).direccion.x < 0


def test_rayo_filas_extremas(camara_base):
    assert camara_base.generar_rayo(200, 0).direccion.y > 0
    assert camara_base.generar_rayo(200, 224).direccion.y < 0


def test_rayos_esquinas_fov_90():
    c = Camara(Vector(0, 0, 0), Vector(0, 0, -1), 90, 2, 2)
    r = math.sqrt(0.5**2 + 0.5**2 + 1)
    esperado = {
        (0, 0): (-0.5, 0.5, -1),
        (1, 0): (0.5, 0.5, -1),
        (0, 1): (-0.5, -0.5, -1),
        (1, 1): (0.5, -0.5, -1),
        }
    for (columna, fila), (x, y, z) in esperado.items():
        d = c.generar_rayo(columna, fila).direccion
        assert componentes(d) == pytest.approx((x / r, y / r, z / r))


def test_rayo_direccion_unitaria(camara_inclinada):
    for columna, fila in [(0, 0), (400, 224), (123, 45), (200, 112)]:
        assert camara_inclinada.generar_rayo(columna, fila).direccion.norma() == pytest.approx(1)

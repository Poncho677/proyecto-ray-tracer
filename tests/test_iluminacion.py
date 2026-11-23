import pytest

from vector import Vector
from rayo import Rayo
from figuras import Esfera, Plano
from iluminacion import limitar, choque_ilum, esta_sombra, color_rayo
from escena import Escena, Luz

BLANCO = (1.0, 1.0, 1.0)
FONDO = (0.6, 0.8, 1.0)
RAYO_SUELO = Rayo(Vector(0, 1, 0), Vector(0, -1, 0))

def escena(objetos, luces, ambiental=0.1):
    return Escena(objetos, luces, FONDO, ambiental)

def luz(x, y, z, intensidad=1.0):
    return Luz(Vector(x, y, z), intensidad)

def suelo(color=BLANCO):
    return Plano(Vector(0, 0, 0), Vector(0, 1, 0), color)

@pytest.mark.parametrize(
     "valor, esperado",
     [(-0.5, 0.0), (0.0, 0.0), (0.3, 0.3), (1.0, 1.0), (2.5, 1.0)],
     ids=[
         "limitar(-0.5) = 0.0",
         "limitar(0.0) = 0.0",
         "limitar(0.3) = 0.3",
         "limitar(1.0) = 1.0",
         "limitar(2.5) = 1.0",
     ],
)
def test_limitar(valor, esperado):
    assert limitar(valor) == pytest.approx(esperado)

def test_choque_sin_objetos():
    assert choque_ilum(escena([], []), RAYO_SUELO) is None

def test_choque_plano():
    plano = suelo()
    t, obj = choque_ilum(escena([plano], []), RAYO_SUELO)
    assert t == pytest.approx(1.0)
    assert obj is plano

def test_choque_deuelve_mas_cercano():
    cerca = Esfera(Vector(0, 0, -3), 1 , BLANCO)
    lejos = Esfera(Vector(0, 0, -6), 1, BLANCO)
    rayo = Rayo(Vector(0, 0, 0), Vector (0, 0, -1))
    t, obj = choque_ilum(escena([lejos, cerca], []), rayo)
    assert t == pytest.approx(2.0)
    assert obj is cerca

def test_choque_t_max():
    esfera = Esfera(Vector(0, 0, -3), 1, BLANCO)
    rayo = Rayo(Vector(0, 0, 0), Vector(0, 0, -1))
    assert choque_ilum(escena([esfera], []), rayo, t_max=1.5) is None

@pytest.mark.parametrize(
     "centro, esperado",
     [(Vector(0, 2, 0, ), True), (Vector(0, 8, 0,), False), (Vector(5, 2, 0,), False)],
     ids=[
         "esfera entre el punto y la luz, hay sombra",
         "esfera detras de la luz, no hay sombra",
         "esfera a un lado, no hay sombra",
     ],
)
def test_esta_sombra(centro, esperado):
    esc = escena([Esfera(centro, 0.5, BLANCO)], [])
    assert esta_sombra(esc, Vector(0, 0, 0), Vector(0, 1, 0), luz(0, 5, 0)) is esperado

def test_color_sin_choque_devuelve_fondo():
    esc = escena([], [luz(0, 5, 0)])
    rayo = Rayo(Vector(0, 0, 0), Vector(0, 0, -1))
    assert color_rayo(esc, rayo) == FONDO

def test_sin_sombra_sin_objetos():
    esc = escena ([], [])
    assert esta_sombra(esc, Vector(0, 0, 0), Vector(0, 1, 0), luz(0, 5, 0)) is False

@pytest.mark.parametrize(
     "luces, ambiental, esperado",
     [([luz(0, 5, 0, 0.5)], 0.1, (0.6, 0.6, 0.6)), 
      ([luz(5, 0, 0)], 0.1, (0.1, 0.1, 0.1)),
      ([luz(0, -5, 0)], 0.1, (0.1, 0.1, 0.1)),
      ([luz(5, 5, 0)], 0.0, (2 **0.5/ 2,) * 3),
      ([luz(0, 5, 0, 0.2), luz(0, 7, 0, 0.3)], 0.1, (0.6, 0.6, 0.6)),
      ([luz(0, 5, 0, 3.0)], 0.1, (1.0, 1.0, 1.0)),
      ],
     ids=[
         "luz de frente: 0.1 + 0.5 * 1 = 0.6",
         "luz de lado: solo es ambiental",
         "luz por debajo del suelo: solo es ambiental",
         "luz a 45 grados: N.L = 0.7071",
         "si dos luces se suman y la ambiental cuenta una vez",
         "brillo mayor a 1 se limita a 1.0",         
     ],
)
def test_lambert_sobre_plano(luces, ambiental, esperado):
    esc = escena([suelo()], luces, ambiental)
    assert color_rayo(esc, RAYO_SUELO) == pytest.approx(esperado)

def test_color_base_multiplica_brillo():
    esc = escena([suelo((0.8, 0.4, 0.0))], [luz(0, 5, 0, 0.5)])
    assert color_rayo(esc, RAYO_SUELO) == pytest.approx((0.48,0.24, 0.0))

def test_punto_en_sombra_solo_recibe_ambiental():
    esfera = Esfera(Vector(0, 2, 0), 0.5, BLANCO)
    esc = escena([suelo(), esfera], [luz(0, 5, 0)])
    assert color_rayo(esc, RAYO_SUELO) == pytest.approx((0.1, 0.1, 0.1))

def test_plano_visto_por_debajo_voltea_norma():
    esc = escena([suelo()], [luz(0, -5, 0, 0.5)])
    rayo = Rayo(Vector(0, -1, 0), Vector(0, 1, 0))
    assert color_rayo(esc, rayo) == pytest.approx((0.6, 0.6, 0.6))

def test_esfera_frente_la_luz():
    esfera = Esfera(Vector(0, 0, -3), 1, (0.9, 0.3, 0.2))
    esc = escena([esfera], [luz(0, 0, 5, 0.5)])
    rayo = Rayo(Vector(0, 0, 0), Vector(0, 0, -1))
    assert color_rayo(esc, rayo) == pytest.approx((0.54, 0.18, 0.12))
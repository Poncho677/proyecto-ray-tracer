import pytest

from vector import Vector
from rayo import Rayo
from iluminacion import limitar, choque_ilum, esta_sombra, color_rayo

BLANCO = (1.0, 1.0, 1.0)
FONDO = (0.6, 0.8, 1.0)
RAYO_SUELO = Rayo(Vector(0, 1, 0), Vector(0, -1, 0))

class EscenaF:
    def __init__(self, objetos, luces, luz_ambiental):
        self.objetos = objetos
        self.luces = luces
        self.luz_ambiental = luz_ambiental
        self.fondo = FONDO

class LuzF:
    def __init__(self, posicion, intensidad):
        self.posicion = posicion
        self.intensidad = intensidad

class FiguraF:
    def __init__(self, t, normal, color=BLANCO, cuando=lambda rayo: True):
        self.t = t
        self.normal = normal 
        self.color = color
        self.cuando = cuando

    def interseccion(self, rayo):
        return self.t if self.cuando(rayo) else None

    def normal_en(self, punto):
        return self.normal

def escena(objetos, luces, ambiental=0.1):
    return EscenaF(objetos, luces, ambiental)

def luz(x, y, z, intensidad=1.0):
    return LuzF(Vector(x, y, z), intensidad)

def suelo(color=BLANCO):
    return FiguraF(1.0, Vector(0, 1, 0), color, cuando=lambda r: r.direccion.y < 0)

def bloqueo(t):
    return FiguraF(t, Vector(0, -1, 0), cuando=lambda r:r.direccion.y > 0)

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
    cerca = FiguraF(2.0, Vector(0, 0, 1))
    lejos = FiguraF(5.0, Vector(0, 0, 1))
    rayo = Rayo(Vector(0, 0, 0), Vector (0, 0, -1))
    t, obj = choque_ilum(escena([lejos, cerca], []), rayo)
    assert t == pytest.approx(2.0)
    assert obj is cerca

def test_choque_t_max():
    esfera = FiguraF(2.0, Vector(0, 0, 1))
    rayo = Rayo(Vector(0, 0, 0), Vector(0, 0, -1))
    assert choque_ilum(escena([esfera], []), rayo, t_max=1.5) is None

@pytest.mark.parametrize(
     "t, esperado",
     [(2.0, True), (8.0, False), (None, False)],
     ids=[
         "objeto entre el punto y la luz, hay sombra",
         "objeto detras de la luz, no hay sombra",
         "objeto a un lado, no hay sombra",
     ],
)
def test_esta_sombra(t, esperado):
    esc = escena([bloqueo(t)], [])
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
    esc = escena([suelo(), bloqueo(2.0)], [luz(0, 5, 0)])
    assert color_rayo(esc, RAYO_SUELO) == pytest.approx((0.1, 0.1, 0.1))

def test_plano_visto_por_debajo_voltea_norma():
    figura = FiguraF(1.0, Vector(0, 1, 0), cuando=lambda r: r.direccion.y > 0)
    esc = escena([figura], [luz(0, -5, 0, 0.5)])
    rayo = Rayo(Vector(0, -1, 0), Vector(0, 1, 0))
    assert color_rayo(esc, rayo) == pytest.approx((0.6, 0.6, 0.6))

def test_esfera_frente_la_luz():
    figura = FiguraF(
        2.0, Vector(0, 0, 1), (0.9, 0.3, 0.2), cuando=lambda r: r.direccion.z < 0
    )
    esc = escena([figura], [luz(0, 0, 5, 0.5)])
    rayo = Rayo(Vector(0, 0, 0), Vector(0, 0, -1))
    assert color_rayo(esc, rayo) == pytest.approx((0.54, 0.18, 0.12))
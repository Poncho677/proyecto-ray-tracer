from rayo import Rayo

e = 1e-4

def limitar(x):
    return max(0.0, min(1.0, x))

def choque_ilum(escena, rayo, t_max=float("inf")):
    mej = None
    for o in escena.objetos:
        t = o.interseccion(rayo)
        if t is not None and e < t < t_max and (mej is None or t < mej[0]):
            mej = (t, o)
    return mej

def esta_sombra(escena, punto, normal, luz):
    hacia_luz = luz.posicion - punto
    distancia = hacia_luz.norma()
    direccion = hacia_luz * (1.0 / distancia)
    origen = punto + normal * e
    return choque_ilum(escena, Rayo(origen, direccion), t_max=distancia) is not None

def color_rayo(escena, rayo):
    choque = choque_ilum(escena, rayo)
    if choque is None:
        return tuple(escena.fondo)

    t, obj = choque
    punto = rayo.punto_en(t)
    normal = obj.normal_en(punto)
    if normal.punto(rayo.direccion) > 0:
        normal = normal * -1

    brillo = escena.luz_ambiental
    for luz in escena.luces:
        if esta_sombra(escena, punto, normal, luz):
            continue
        L = (luz.posicion - punto).normalizar()
        brillo += luz.intensidad * max(0.0, normal.punto(L))

    return tuple(limitar(c * brillo) for c in obj.color)
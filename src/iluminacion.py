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

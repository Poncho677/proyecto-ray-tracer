import sys
import json
from imageError import ImageError
from camara import Camara
from Imagen import Imagen
from vector import Vector
from camError import CamError
from lightError import LightError
from trabajadoresError import TrabajadoresError
from EntradaError import EntradaError
from figuras import Esfera
from figuras import Plano

args = None

class Luz:
    def __init__(self, posicion, intensidad):
        self.posicion = posicion
        self.intensidad = intensidad

class Escena:
    def __init__(self, objetos, luces, fondo, luz_ambiental):
        self.objetos = objetos
        self.luces = luces
        self.fondo = fondo 
        self.luz_ambiental = luz_ambiental

    @staticmethod
    def leer():
        if len(sys.argv) > 1:
            args = sys.argv
        else:
            raise EntradaError("No se recibió texto alguno")
        encontrado = False
        archivo = None
        for j in args:
            if ".json" in j:
                encontrado = True
                archivo = j
        if encontrado == False:
            raise EntradaError("No hay archivo json")
        try:
            dicc = json.load(open(archivo))
            numTrabajadores = 0
            t = args.index("--trabajadores")
            try:
                if t+1 >= len(args):
                    raise TrabajadoresError()
                numTrabajadores = int(args[t+1])
                if numTrabajadores < 1:
                    raise TrabajadoresError("Número invalido, porfavor ingresar números positivos mayores a 1 dentro de la capacidad de su dispositivo")
                            
            except ValueError:
                print(args[t+1])
                print("No es del tipo númerico")

            ancho = 0
            alto = 0
            if 'imagen' in dicc:
                img = dicc['imagen']
                ancho = img['ancho']
                alto = img['alto']
                if ancho < 0 or alto < 0:
                    raise ImageError("Tipo de dato invalido: ancho o altura menor a 0")

            camara = None
            if 'camara' in dicc:
                cam = dicc['camara']
                posicion = cam['posicion']
                mira = cam['mira_a']
                fov = cam['fov']
                if fov < 60 or fov > 120:
                    raise CamError("Tipo de dato invalido: fov negativo")
                posicion2 = Vector(posicion[0], posicion[1], posicion[2])
                mira_a = Vector(mira[0], mira[1], mira[2])
                camara = Camara(posicion2, mira_a, fov, ancho, alto)

            fondo2 = Vector(0, 0, 0)
            if 'fondo' in dicc:
                fondo = dicc['fondo']
                fondo2 = Vector(fondo[0], fondo[1], fondo[2])

            luz_ambiental = 0
            if 'luz_ambiental' in dicc:
                luz_ambiental = dicc['luz_ambiental']

            luces2 = []
            if 'luces' in dicc:
                luces = dicc['luces']
                for i in luces:
                    luces2.append(Luz(Vector(i['posicion'][0], i['posicion'][1], i['posicion'][2]), i['intensidad']))

            objetos = []
            if 'objetos' in dicc:
                obj = dicc['objetos']
                esf = []
                pln = []
                for i in range(len(obj)):
                    if obj[i]['tipo'] == "esfera":
                        esf.append(Esfera(obj[i]['centro'], obj[i]['radio'], obj[i]['color']))
                    if obj[i]['tipo'] == "plano":
                        pln.append(Plano(obj[i]['punto'], obj[i]['normal'], obj[i]['color']))
            objetos = esf + pln

        except FileNotFoundError:
            print("Archivo no encontrado, porfavor revisar el nombre del archivo")
            return None

        escena = Escena(objetos, luces2, fondo2, luz_ambiental)
        imagen = Imagen(ancho, alto, camara, escena)
        return escena
        

import sys
import json
from imageError import ImageError
from camError import CamError
from lightError import LightError
from trabajadoresError import TrabajadoresError
from EntradaError import EntradaError
from esfera import Esfera
from plano import Plano

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


def leer():
    if len(sys.argv) > 1:
        args = sys.argv
    else:
        raise EntradaError("No se recibió texto alguno")
    valor = False
    for j in args:
        if ".json" in j:
                valor = True
                try:
                        dicc = json.load(open(j))
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
                            
                        if 'imagen' in dicc:
                            img = dicc['imagen']
                            ancho = img['ancho']
                            alto = img['alto']
                            if ancho < 0 or alto < 0:
                                raise ImageError("Tipo de dato invalido: ancho o altura menor a 0")
                            else:
                                raise ImageError("No hay imágen")
                                                
                        if 'camara' in dicc:
                            cam = dicc['camara']
                            posicion = cam['posicion']
                            mira = cam['mira_a']
                            fov = cam['fov']
                            if fov < 0:
                                raise ValueError("Tipo de dato invalido: fov negativo")
                            else:
                                raise CamError("No hay cámara a usar")
                
                        if 'luz_ambiental' in dicc:
                            valor = dicc['luz_ambiental']
                                
                        if 'luces' in dicc:
                            luces = dicc['luces']
                        '''else:
                            raise LightError("No hay luces a usar")'''

                        if 'objetos' in dicc:
                            obj = dicc['objetos']
                            esf = []
                            pln = []
                            for i in range(len(obj)):
                                if obj[i]['tipo'] == "esfera":
                                    esf += Esfera(obj[i]['centro'], obj[i]['radio'], obj[i]['color'])
                                if obj[i]['tipo'] == "plano":
                                    pln += Plano(obj[i]['punto'], obj[i]['normal'], obj[i]['color'])
                except FileNotFoundError:
                        print("Archivo no encontrado, porfavor revisar el nombre del archivo")
    if valor == False:
        raise EntradaError("No hay archivo json")

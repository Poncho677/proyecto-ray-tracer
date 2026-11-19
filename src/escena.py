import json
from esfera import Esfera

with open("Prueba_Texto.json") as f:
    dicc = json.load(f)
    if 'imagen' in dicc:
        img = dicc['imagen']
        ancho = img['ancho']
        alto = img['alto']


    if 'camara' in dicc:
        cam = dicc['camara']
        posicion = cam['posicion']
        mira = cam['mira_a']
        fov = cam['fov']

    if 'luz_ambiental' in dicc:
        valor = dicc['luz_ambiental']

    if 'luces' in dicc:
        luces = dicc['luces']
        
    if 'objetos' in dicc:
        obj = dicc['objetos']
        esf = []
        pln = []
        for i in range(len(obj)):
            if obj[i]['tipo'] == "esfera":
                esf += Esfera(obj[i]['centro'], obj[i]['radio'], obj[i]['color'])
            if obj[i]['tipo'] == "plano":
                pln += Plano(obj[i]['punto'], obj[i]['normal'], obj[i]['color'])

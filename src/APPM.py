from MatrizPPM import MatrizPPM 

class APPM:
    def __init__(self, ruta):
        self.ruta = ruta

    def escribir(self, matriz_ppm):
        pixeles = matriz_ppm.a_bytes()
        alto = len(pixeles)

        if alto > 0:
            ancho = len(pixeles[0])
        else:
            ancho = 0

        #indicar la lectura del archivo en formato ppm
        cabecera = "P3\n" + str(ancho) + " " + str(alto) + "\n255\n"

        with open(self.ruta, "w", encoding="ascii") as f:
            f.write(cabecera)
            for fila in pixeles:
                for (r, g, b) in fila:
                    f.write(f"{r} {g} {b}\n")
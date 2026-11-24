from MatrizPPM import MatrizPPM
from APPM import APPM

m = MatrizPPM(3, 2)
m.set(0, 0, (1.0, 0.0, 0.0))
m.set(2, 0, (0.0, 0.0, 1.0))
m.set(1, 1, (0.0, 1.0, 0.0))

APPM("test.ppm").escribir(m)
print("Listo: test.ppm generado")
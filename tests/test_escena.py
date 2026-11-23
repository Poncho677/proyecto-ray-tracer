import pytest
import sys
from unittest.mock import patch
from escena import leer
from EntradaError import EntradaError
from trabajadoresError import TrabajadoresError

@pytest.mark.parametrize("datos", [[], ["Pruebas.texto", "--trabajadores", "3"]])
def test_leer_sin_datos(datos):
    with pytest.raises(EntradaError):
        with patch.object(sys, "argv", datos):
            escena = leer()

def test_archivo_no_encontrado():
    with patch.object(sys, "argv", ["Pruebas_Texto.json", "--trabajadores", "7"]):
        resultado = leer()
        assert resultado is None

'''Capsys, captura los datos que se imprimieron en la terminal
   tmp_path, crea un archivo temporal para que el test pueda verificar los errores'''
def test_trabajadores_invalidos_no_numericos(tmp_path, capsys):

    archivo_falso = tmp_path / "Prueba_Texto.json"
    archivo_falso.write_text("{}")
    
    with patch.object(sys, "argv", [str(archivo_falso), "--trabajadores", "Hola"]):
        escena = leer()

        salida = capsys.readouterr().out
        assert "No es del tipo númerico" in salida

def test_trabajadores_invalidos_negativos(tmp_path):

    archivo_falso = tmp_path / "Prueba_Texto.json"
    archivo_falso.write_text("{}")
    
    with pytest.raises(TrabajadoresError):
        with patch.object(sys, "argv", ["main.py", str(archivo_falso), "--trabajadores", "-5"]):
            escena = leer()
    

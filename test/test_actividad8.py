import pytest
from src.actividad8 import traducir_frase
@pytest.mark.parametrize(
    "diccionario,palabraenespañol,frasetraducida",
    [
        ({'hola':'hello'},"hola","hello"),
    ]
)

def test_traducir_frase_params(diccionario,palabraenespañol,frasetraducida):
    assert traducir_frase(diccionario,palabraenespañol)==frasetraducida

from src.actividad8 import traducir_frase
@pytest.mark.parametrize(
    "diccionario,palabraenespañol,frasetraducida",
    [
        ({'hola':'hello', 'perro':'dog'},"hola","hello"),
        ({'hola':'hello', 'perro':'dog'},"perro","dog")

    ]
)
def test_traducir_frase_params(diccionario,palabraenespañol,frasetraducida):
    assert traducir_frase(diccionario,palabraenespañol)==frasetraducida
import pytest
from src.actividad6 import crear_informacion
@pytest.mark.parametrize(
    "diccionario,,clave,valor,informacion",
    [
        ({'nombre': 'cesar'},"nombre","cesar","{'nombre': 'cesar'}"),
    ]
)
def test_crear_informacion_params(diccionario,clave,valor,informacion):
    assert crear_informacion(diccionario,clave,valor)==informacion
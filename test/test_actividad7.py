import pytest
from src.actividad7 import crear_tabla
@pytest.mark.parametrize(
    "total,articulos,articulo,tabla",
    [
        (1,{'manzana': 2.0},"manzana","manzana => 2.0€"),
        (2,{'pera': 3.0},"pera","pera => 3.0€")
    ]
)

def test_crear_tabla_params(total,articulos,articulo,tabla):
    assert crear_tabla(total,articulos,articulo)==tabla

from src.actividad7 import crear_precio
@pytest.mark.parametrize(
    "total,preciototal",
    [
        ("5.0","precio total: 5.0€"),
    ]
)
def test_crear_precio_params(total,preciototal):
    assert crear_precio(total)==preciototal
import pytest
from src.actividad3 import elegir_fruta
@pytest.mark.parametrize(
    "fruta, cantidad, mensaje",
    [
        ("platano",2,"2k de platano a 2.7€"),
        ("manzana",2,"2k de manzana a 1.6€"),
        ("pera",2,"2k de pera a 1.7€"),
        ("naranja",2,"2k de naranja a 1.4€")
    ]
)
def test_elegir_fruta_params(fruta,cantidad,mensaje):
    assert elegir_fruta(fruta,cantidad)==mensaje
import pytest
from src.actividad1 import elegir_divisa
@pytest.mark.parametrize(
    "moneda,divisa,eleccion",
    [
        ({'euro':'€', 'dolar':'$', 'yen':'¥'},"euro","€"),
        ({'euro':'€', 'dolar':'$', 'yen':'¥'},"dolar","$"),
        ({'euro':'€', 'dolar':'$', 'yen':'¥'},"yen","¥")
    ]
)
def test_elegir_divisa_params(moneda,divisa,eleccion):
    assert elegir_divisa(moneda,divisa)==eleccion

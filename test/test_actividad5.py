import pytest
from src.actividad5 import crear_mensaje
@pytest.mark.parametrize(
    "asignatura, mensaje",
    [
        ("matematicas","la asignatura matematicas tiene 6 creditos"),
        ("fisica","la asignatura fisica tiene 4 creditos"),
        ("quimica","la asignatura quimica tiene 5 creditos")

    ]
)
def test_crear_mensaje_params(asignatura,mensaje):
    assert crear_mensaje(asignatura)==mensaje
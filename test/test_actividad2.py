import pytest
from src.actividad2 import crear_mensaje
@pytest.mark.parametrize(
    "nombre,edad,direccion,telefono,mensaje",
    [
        ("cesar",21,"calle quencio","+34-627-19-80-83","cesar tiene 21 años, vive en la calle quencio y su numero de telefono es +34-627-19-80-83")
    ]
)
def test_crear_mensaje_params(nombre,edad,direccion,telefono,mensaje):
    assert crear_mensaje(nombre,edad,direccion,telefono)==mensaje

import pytest
from src.actividad4 import crear_fecha
@pytest.mark.parametrize(
    "introducirdia,introducirmes,introduciraño,fecha",
    [
        (2,"diciembre",1972,"02/12/1972"),
        (30,"diciembre",1979,"30/12/1979"),
        (18,"febrero",1993,"18/02/1993"),
        (11,"noviembre",2001,"11/11/2001"),
        (4,"octubre",2003,"04/10/2003"),
        (7,"mayo",2005,"07/05/2005")
    ]
)
def test_crear_fecha_params(introducirdia,introducirmes,introduciraño,fecha):
    assert crear_fecha(introducirdia,introducirmes,introduciraño)==fecha
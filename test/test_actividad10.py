import pytest
'''from src.actividad10 import añadir_cliente
@pytest.mark.parametrize(
    "clientes,nif,nombre,direccion,telefono,correo,preferente,añadircliente",
    [
        ({'76588815B': {'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'}},"76588815B","cesar","calle quencio","+34-627-19-80-83","cesar2001ricitos@gmail.com","si", "{'76588815B': {'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'}}"),
    ]
)
def test_añadir_cliente_params(clientes,nif,nombre,direccion,telefono,correo,preferente,añadircliente):
    assert añadir_cliente(clientes,nif,nombre,direccion,telefono,correo,preferente)==añadircliente
'''
from src.actividad10 import eliminar_cliente
@pytest.mark.parametrize(
    "nif,clientes,eliminarcliente",
    [
        ({'1': {'nombre': 'one', 'direccion': 'calle one', 'telefono': '+1', 'correo': 'one@gmail.com', 'preferencia': 'no'}},"1","usuario eliminado")
    ]
)

def test_eliminar_cliente_params(clientes,nif,eliminarcliente):
    assert eliminar_cliente(clientes,nif)==eliminarcliente

from src.actividad10 import mostrar_cliente
@pytest.mark.parametrize(
    "nif,clientes,mostrarcliente",
    [
        ({'76588815B': {'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'}},"76588815B",{'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'})
    ]
)

def test_mostrar_cliente_params(clientes,nif,mostrarcliente):
    assert mostrar_cliente(clientes,nif)==mostrarcliente

from src.actividad10 import lista_cliente
@pytest.mark.parametrize(
    "clientes,lista",
    [
        ({'76588815B': {'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'}, '1': {'nombre': 'one', 'direccion': 'calle one', 'telefono': '+1', 'correo': 'one@gmail.com', 'preferencia': 'no'}},"{'76588815B': {'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'}, '1': {'nombre': 'one', 'direccion': 'calle one', 'telefono': '+1', 'correo': 'one@gmail.com', 'preferencia': 'no'}}")
    ]
)

def test_lista_cliente_params(clientes,lista):
    assert lista_cliente(clientes)==lista

from src.actividad10 import lista_preferente
@pytest.mark.parametrize(
    "clientes,listapreferente",
    [
        ({'76588815B': {'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'}, '1': {'nombre': 'one', 'direccion': 'calle one', 'telefono': '+1', 'correo': 'one@gmail.com', 'preferencia': 'no'}},"{'76588815B': {'nombre': 'cesar', 'direccion': 'calle quencio', 'telefono': '+34-627-19-80-83', 'correo': 'cesar2001ricitos@gmail.com', 'preferencia': 'si'}}")
    ]
)
def test_lista_preferente_params(clientes,listapreferente):
    assert lista_preferente(clientes)==listapreferente

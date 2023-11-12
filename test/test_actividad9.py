import pytest
from src.actividad9 import añadir_factura
@pytest.mark.parametrize(
    "facturas,numerofacturas,cantidad,dineropendiente,dineropagado,mensaje",
    [
        ({2001: 1000.0},2001,1000,0.0,0,"dinero pendiente: 1000.0€\ndinero pagado: 0€"),
    ]
)
def test_añadir_factura_params(facturas,numerofacturas,cantidad,dineropendiente,dineropagado,mensaje):
    assert añadir_factura(facturas,numerofacturas,cantidad,dineropendiente,dineropagado)==mensaje

from src.actividad9 import pagar_factura
@pytest.mark.parametrize(
    "facturas,numerofactura,dineropendiente,dineropagado,mensaje",
    [
        ({2001: 1000.0},2023,1000.0,0,"la factura no existe\ndinero pendiente: 1000.0€\ndinero pagado: 0€"),
        ({2001: 1000.0},2001,0.0,0.0,"dinero pendiente: 0.0€\ndinero pagado: 1000.0€")
    ]
)
def test_pagar_factura_params(facturas,numerofactura,dineropendiente,dineropagado,mensaje):
    assert pagar_factura(facturas,numerofactura,dineropendiente,dineropagado)==mensaje

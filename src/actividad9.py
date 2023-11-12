'''Ejercicio 3.2.9: escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.'''
# funcion de la definicion
def añadir_factura(facturas,numerofactura,cantidad,dineropendiente,dineropagado):
    facturas[numerofactura]=cantidad
    dineropendiente+=cantidad
    mensaje="dinero pendiente: "+str(dineropendiente)+"€\ndinero pagado: "+str(dineropagado)+"€"
    return mensaje

def pagar_factura(facturas,numerofactura,dineropendiente,dineropagado):
    if numerofactura in facturas:
        dineropagado+=facturas[numerofactura]
        mensaje="dinero pendiente: "+str(dineropendiente)+"€\ndinero pagado: "+str(dineropagado)+"€"
        return mensaje
    else:
        mensaje="la factura no existe\ndinero pendiente: "+str(dineropendiente)+"€\ndinero pagado: "+str(dineropagado)+"€"
        return mensaje

if __name__=="__main__":
    # entrada
    facturas={}
    continuacion=True
    dineropendiente=0
    dineropagado=0
    # procesamiento
    while continuacion:
        opcion=int(input("menu principal\n1: agregar factura\n2: pagar factura\n3: terminar el programa\nelige una opcion: "))
        if opcion==1:
            numerofactura=int(input("introduce el numero de la factura: "))
            cantidad=float(input("cantidad de dinero: "))
            mensaje=añadir_factura(facturas,numerofactura,cantidad,dineropendiente,dineropagado)
            # salida 1
            print(mensaje)
        elif opcion==2:
            numerofactura=int(input("introduce el numero de la factura a pagar: "))
            mensaje=pagar_factura(facturas,numerofactura,dineropendiente,dineropagado)
            # salida 2
            print(mensaje)
        elif opcion==3:
            continuacion=False
            mensaje="hasta luego"
            # salida 3
            print(mensaje)
if __name__=="__main__":
    facturas={}
    continuacion=True
    dineropendiente=0
    dineropagado=0
    while continuacion:
        opcion=int(input("menu principal\n1: agregar factura\n2: pagar factura\n3: terminar el programa\nelige una opcion: "))
        if opcion==1:
            numerofactura=int(input("introduce el numero de la factura: "))
            cantidad=float(input("cantidad de dinero: "))
            facturas[numerofactura]=cantidad
            dineropendiente+=cantidad
            mensajedineropendiente="dinero pendiente: "+str(dineropendiente)+"€"
            mensajedinerocobrado="dinero pagado: "+str(dineropagado)+"€"
            print(dineropendiente)
            print(dineropagado)
        elif opcion==2:
            numerofactura=int(input("introduce el numero de la factura a pagar: "))
            if numerofactura in facturas:
                dineropendiente-=facturas[numerofactura]
                dineropagado+=facturas[numerofactura]
                mensajedineropendiente="dinero pendiente: "+str(dineropendiente)+"€"
                mensajedineropagado="dinero pagado: "+str(dineropagado)+"€"
                print(mensajedineropendiente)
                print(mensajedineropagado)
            else:
                mensajeerror="la factura no existe"
                mensajedineropendiente="dinero pendiente: "+str(dineropendiente)+"€"
                mensajedinerocobrado="dinero pagado: "+str(dineropagado)+"€"
                print(mensajeerror)
                print(dineropendiente)
                print(dineropagado)
        elif opcion==3:
            continuacion=False
            mensaje="hasta luego"
            print(mensaje)
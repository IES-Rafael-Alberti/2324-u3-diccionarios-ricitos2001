# definicion de la funcion
if __name__=="__main__":
    clientes={}
    menu=True
    while menu:
        menu=int(input("menu principal\n1: añadir clientes\n2: eliminar clientes\n3: mostrar clientes\n4: listar clientes\n5: listar clientes preferntes\n6: terminar el programa\n\nelige una opcion: "))
        if menu==1:
            nif=str(input("introduce un NIF: "))
            nombre=str(input("introduce tu nombre: "))
            direccion=str(input("introduce tu direccion: "))
            telefono=str(input("introduce tu numero de telefono: "))
            correo=str(input("introduce tu correo: "))
            preferencia=str(input("es preferente (si o no): "))
            preferancia=preferencia.lower()
            cliente={'nombre':nombre, 'direccion':direccion, 'telefono':telefono, 'correo':correo, 'preferencia':preferencia}
            clientes[nif]=cliente
            print(clientes)
        elif menu ==2:
            for nif in clientes:
                for clave, valor in clientes[nif].items():
                    mensaje=clave+" : "+valor
                    del(clientes[nif])
                    mensaje="usuario eliminado"
                    print (mensaje)
        elif menu==3:
            nif=str(input("introduce el NIF del usuario solicitado: "))
            mostrarusuario=clientes.get(nif)    
            print (mostrarusuario)
        elif menu ==4:
            for nif in clientes:
                for clave, valor in clientes[nif].items():
                    mensaje=clave+" : "+valor
                    print (mensaje)
        elif menu ==5:
            for j in clientes:
                for k in clientes[j].items():
                    if nif in k:
                        clave=k[0]
                        valor=k[1]
                        mensaje=j+" "+clave+":"+valor
                        print (mensaje)
        elif menu==6:
            menu=False
            mensaje="hasta luego"
            print(mensaje)
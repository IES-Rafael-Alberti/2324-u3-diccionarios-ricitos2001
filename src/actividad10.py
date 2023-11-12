'''Ejercicio 3.2.10: escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente: 1.) Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos, 2.) Preguntar por el NIF del cliente y eliminar sus datos de la base de datos, 3.) Preguntar por el NIF del cliente y mostrar sus datos, 4.) Mostrar lista de todos los clientes de la base datos con su NIF y nombre, 5.) Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre, 6.) Terminar el programa.'''
# definicion de la funcion
def añadir_cliente(clientes,nif,nombre,direccion,telefono,correo,preferente):
    cliente={'nombre':nombre, 'direccion':direccion, 'telefono':telefono, 'correo':correo, 'preferencia':preferente}
    clientes[nif]=cliente
    añadircliente=str(cliente)
    return añadircliente

def eliminar_cliente(nif,clientes):
    for nif in clientes:
        del(clientes[nif])
        eliminarcliente="usuario eliminado"
        return eliminarcliente

def mostrar_cliente(nif,clientes):
    mostrarcliente=clientes.get(nif)
    return mostrarcliente

def lista_cliente(clientes):
    lista=str(clientes)
    return lista

def lista_preferente(clientes,preferente):
    clientes.get(preferente)
    if preferente=='si':
        listapreferente=clientes[preferente['si']]
        return listapreferente
if __name__=="__main__": #76588815B
    # entrada
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
            preferente=preferencia.lower()
            añadircliente=añadir_cliente(clientes,nif,nombre,direccion,telefono,correo,preferente)
            print(añadircliente)
        elif menu ==2:
            nif=str(input("introduce el NIF del usuario solicitado: "))
            eliminarcliente=eliminar_cliente(nif,clientes)
            print (eliminarcliente)
        elif menu ==3:
            nif=str(input("introduce el NIF del usuario solicitado: "))
            mostrarcliente=mostrar_cliente(nif,clientes)
            print (mostrarcliente)
        elif menu ==4:
            lista=lista_cliente(clientes)
            print(lista)
        elif menu ==5:
            if preferencia[preferente]=='si':
                listapreferente=lista_preferente(clientes,preferente)
                print (listapreferente)
        elif menu==6:
            menu=False
            mensaje="hasta luego"
            print(mensaje)
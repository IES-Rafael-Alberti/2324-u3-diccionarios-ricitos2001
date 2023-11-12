'''Ejercicio 3.2.2: escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''
# definicion de la funcion
def crear_mensaje(nombre,edad,direccion,telefono):
    diccionario={'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono}
    mensaje=diccionario['nombre']+" tiene "+str(diccionario['edad'])+" años, vive en la "+diccionario['direccion']+" y su numero de telefono es "+diccionario['telefono']
    return mensaje
if __name__=="__main__":
    error="valor incorrecto"
    try:
        # entrada
        nombre=input("introduce tu nombre: ")
        edad=int(input("introduce tu edad: "))
        direccion=input("introduce tu direccion: ")
        telefono=input("introduce tu numero de telefono: ")
        # procesamiento
        mensaje=crear_mensaje(nombre,edad,direccion,telefono)
        # salida
        print(mensaje)
    except ValueError:
        # salida del error
        print(error)
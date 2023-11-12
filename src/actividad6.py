'''Ejercicio 3.2.6: escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''
# definicion de la funcion
def crear_informacion(diccionario,clave,valor):
    diccionario[clave]=valor
    informacion=str(diccionario)
    return informacion

if __name__=="__main__":
    # entrada
    diccionario={}
    continuacion=1
    while continuacion==1:
        clave = input("introduce algun tipo de dato, ejemplo: nombre, edad, sexo, teléfono, correo electrónico, etc...: ")
        valor = input(" introduce la informacion correspondiente: ")
        # procesamiento
        informacion=crear_informacion(diccionario,clave,valor)
        # salida 1
        print(informacion)
        continuacion = int(input("quieres añadir más informacion (1: si, 2: no) "))
    despedida="adios"
    # salida 2
    print(despedida)

def crear_informacion(clave,valor):
    diccionario={clave:valor}
    diccionario.update({clave:valor})
    return diccionario

if __name__=="__main__":
    continuacion=1
    while continuacion==1:
            clave = str(input("introduce algun tipo de dato, ejemplo: nombre, edad, sexo, teléfono, correo electrónico, etc...: "))
            valor = str(input(" introduce la informacion correspondiente: "))
            diccionario=crear_informacion(clave,valor)
            print(diccionario)
            continuacion = int(input("quieres añadir más informacion (1: si, 2: no) "))
    despedida="adios"
    print(despedida)

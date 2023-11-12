'''Ejercicio 3.2.8: escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.'''
# definicion de la funcion
def traducir_palabra(diccionario):
    palabratraducida=str(diccionario)
    return palabratraducida

def traducir_frase(diccionario,palabraenespañol):
    if palabraenespañol in diccionario:
        frasetraducida=diccionario[palabraenespañol]
        return frasetraducida
    else:
        frasetraducida=palabraenespañol
        return frasetraducida

if __name__=="__main__":
    # entrada
    diccionario={}
    palabras=str(input("introduce palabras en español y su traducion el ingles mediante el siguiente formato (hola:hello): "))
    # procesamiento
    for traduccion in palabras.split(","):
        palabraenespañol,palabraeningles=traduccion.split(":")
        diccionario[palabraenespañol]=palabraeningles
    palabratraducida=traducir_palabra(diccionario)
    # salida 1
    print (palabratraducida)
    frase=input("escribe una frase en español: ")
    for palabraenespañol in frase.split(" "):
        frasetraducida=traducir_frase(diccionario,palabraenespañol)
        # salida 2
        print(frasetraducida)


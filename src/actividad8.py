if __name__=="__main__":
    diccionario={}
    palabras=str(input("introduce palabras en español y su traducion el ingles mediante el siguiente formato (hola:hello): "))
    for traduccion in palabras.split(","):
        palabraenespañol,palabraeningles=traduccion.split(":")
        diccionario[palabraenespañol]=palabraeningles
        print (diccionario)
    frase=input("escribe una frase en español: ")
    for palabraenespañol in frase.split(" "):
        if palabraenespañol in diccionario:
            frasetraducida=diccionario[palabraenespañol]
            print(frasetraducida)
        else:
            frasetraducida=palabraenespañol
            print (frasetraducida)


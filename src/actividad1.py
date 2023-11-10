'''Ejercicio 3.2.1: escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.'''
# funcion de la definicion
def elegir_divisa(moneda,divisa):
    eleccion=moneda[divisa]
    return eleccion

if __name__=="__main__":
    error="la moneda no existe "
    try:
        # entrada
        moneda={'euro':'€', 'dolar':'$', 'yen':'¥'}
        divisa=input("introduce una divisa (euro, dolar o yen): ")
        # procesamiento
        eleccion=elegir_divisa(moneda,divisa)
        # salida
        print(eleccion)
    except ValueError:
        # salida error
        print (error)
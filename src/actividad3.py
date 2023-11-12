'''Ejercicio 3.2.3: escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.'''
# definicion de la funcion
def elegir_fruta(fruta,cantidad):
    frutas={'platano':1.35, 'manzana':0.80,'pera':0.85, 'naranja':0.70}
    eleccion=frutas.get(fruta)
    print(eleccion)
    resultado=eleccion*cantidad
    mensaje=str(cantidad)+"k de "+fruta+" a "+str(float(resultado))+"€"
    return mensaje

if __name__=="__main__":
    error="el nombre de la fruta no existe"
    try:
        # entrada
        fruta=input("introduce cualquier fruta: ")
        cantidad=int(input("introduce la cantidad en kilogramos: "))
        # procesamiento
        mensaje=elegir_fruta(fruta,cantidad)
        # salida
        print(mensaje)
    except ValueError:
        # salida del error
        print (error)
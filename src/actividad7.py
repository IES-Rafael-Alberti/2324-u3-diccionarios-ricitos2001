'''Ejercicio 3.2.7: escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, mostrando toda la informacion de manera que se parezca a una tabla'''

# definicion de la funcion
def crear_tabla(total,articulos,articulo):
    total+=articulos[articulo]
    tabla=articulo+" => "+str(articulos[articulo])+"€"
    return tabla

def crear_precio(total):
    preciototal="precio total: "+str(total)+"€"
    return preciototal

if __name__=="__main__":
    # entrada
    articulos={}
    total=0
    continuacion=1
    while continuacion==1:
        articulo = str(input("introduce el nombre de un articulo: "))
        precio = float(input("introduce el precio de articulo: "))
        articulos[articulo]=precio
        continuacion = int(input("quieres añadir otro porducto (1: si, 2: no) "))
    # procesamiento
    for articulo in articulos:
        tabla=crear_tabla(total,articulos,articulo)
        # salida 1
        print(tabla)
    preciototal=crear_precio(total)
    # salida 2
    print(preciototal)
if __name__=="__main__":
    articulos={}
    total=0
    continuacion=1
    while continuacion==1:
        articulo = str(input("introduce el nombre de un articulo: "))
        precio = float(input("introduce el precio de articulo: "))
        articulos[articulo]=precio
        print (articulos)
        continuacion = int(input("quieres añadir otro porducto (1: si, 2: no) "))
    for articulo in articulos:
        tabla=articulo+" => "+str(articulos[articulo])+"€"
        total+=articulos[articulo]
        print(tabla)
    mensaje="precio total: "+str(total)+"€"
    print(mensaje)
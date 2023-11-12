'''Ejercicio 3.2.4: escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.'''
# definicion de la funcion
def crear_fecha(introducirdia,introducirmes,introduciraño):
    meses={'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
    obtenermes=meses.get(introducirmes)
    dia=str(introducirdia).zfill(2)
    mes=str(obtenermes).zfill(2)
    año=str(introduciraño).zfill(4)
    fecha=dia+"/"+mes+"/"+año
    return fecha

if __name__=="__main__":
    error="no existe ese mes"
    try:
        # entrada
        introducirdia=int(input("introduce un dia: "))
        introducirmes=str(input("introduce un mes: "))
        introduciraño=int(input("introduce un año: "))
        # procesamiento
        fecha=crear_fecha(introducirdia,introducirmes,introduciraño)
        # salida
        print(fecha)
    except ValueError:
        # salida del error
        print (error)



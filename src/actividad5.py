'''Ejercicio 3.2.5: escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.'''
# definicion de la funcion
def crear_mensaje(asignatura):
    asignaturas={'matematicas': 6, 'fisica': 4, 'quimica': 5}
    creditos=asignaturas.get(asignatura)
    mensaje="la asignatura "+str(asignatura)+" tiene "+str(creditos)+" creditos"
    return mensaje

if __name__=="__main__":
    error="el nombre de la fruta no existe"
    try:
        # entrada
        asignatura=input("introduce el nombre de una asignatura: ")
        # procesamiento
        mensaje=crear_mensaje(asignatura)
        # salida
        print(mensaje)
    except ValueError:
        # salida del error
        print (error)

# definicion de la funcion
def crear_directorio(clientes,campos):
    directorio={}
    for i in clientes[1:]:
        diccionario={}
        cliente=i.split(";")
        for j in range(len(cliente)):
            if j==0:
                nif=cliente[j]
            else:
                diccionario[campos[j]]=cliente[j]
        directorio[nif]=diccionario
    return directorio

if __name__=="__main__":
    lista="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    clientes=lista.split("\n")
    print(clientes,"\n\n")
    campos=clientes[0].split(";")
    print(campos,"\n\n")
    directorio=crear_directorio(clientes,campos)
    print(directorio)




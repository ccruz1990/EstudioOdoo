#-----Curso python video 8 tuplas-----
miTupla = ("Juan",5,3,1995)
Lista = ["Juan",5,3,1995]
miLista2 = list(miTupla) #convertir tupla a lista
miTupla2 = tuple(Lista) #convertir lista a tupla
print(miTupla[2]) #imprimiendo un elemento por su indice
print(miLista2)
print(miTupla)
print(miTupla2)
print("Juan" in miTupla) #buscar si un elemento está en la tupla
print(miTupla.count(13)) #cuenta cuantas veces esta un elemento en la tupla
print(len(miTupla)) #imprime la longitud de la tupla
print(miTupla2)
#------------------------------
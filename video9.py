#-----Curso python video 9 diccionarios-----
miDiccionario = {"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "España":"Madrid"}
miDiccionario["Italia"]="Lisboa" #agregar un nuevo elemento
print(miDiccionario)

miDiccionario["Italia"]="Roma" #modificar un elemento
print(miDiccionario)
del miDiccionario["Reino Unido"] #eliminar un elemnto
print(miDiccionario)

miTupla = ("Alemania", "Francia", "Reino Unido", "España")
miDiccionario2 = {miTupla[0]:"Berlin", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Madrid"} #creando diccionario con valores de una tupla

print(miDiccionario2)

miDiccionario3 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993,1996,1997,1998]} #tupla dentro de un diccionario
print(miDiccionario3["Anillos"])
miDiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}} #diccionario dentro de un diccionario
print(miDiccionario4.keys()) #imprime claves del diccionario
print(miDiccionario4.values()) #imprime valores del diccionario


#------------------------------
#----------Curso python video 20 generadores II------------
def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento
ciudades_devueltas=devuelveCiudades("Madrid","Francia","Berlin","Londres")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
#----------------------------------------------------------
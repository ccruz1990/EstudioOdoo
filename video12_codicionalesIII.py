#-----Curso python video 12 condicionales III-----

salario_presidente = int(input("Ingrese salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director= int(input("Ingrese salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area = int(input("Ingrese salario jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo = int(input("Ingrese salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print("Todo funciona correctamente")
else:
    print("Algo anda mal")
#----------------------------------------------
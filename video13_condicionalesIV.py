#-----Curso python video 13 condicionales IV-----
#Programa 1
print("Programa de becas")
distancia_escuela = int(input("Introduce la distancia a la escuela en Km: "))
print(distancia_escuela)
numero_hermanos = int(input("Introduce el número de hermanos: "))
print(numero_hermanos)
salario_familiar = int(input("Introduce el salario familiar : "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar < 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

#Programa 2
print("Asignaturas optativas año 2022")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida: ")

asignatura=opcion.lower()               #transforma todas las letras a minúsculas

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("La asignatura escogida no está contemplada")

#------------------------------------------------
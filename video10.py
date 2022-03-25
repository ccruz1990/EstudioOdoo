#-----Curso python video 10 condicionales-----
print("Programa de evaluación de notas de alumnos")

nota_alumno = input("Introduzca la nota del alumno: ") #el usuario ingresa la variable a evaluar

def evaluacion(nota):                   #función
    valoracion="aprobado"
    if nota<5:                          #condicion
        valoracion="reprobado"          #si se cumple la condicion

    return valoracion

print(evaluacion(int(nota_alumno)))     #transforma la variable a entero, se la pasa a la función y se imprime el resultado
#---------------------------------------------
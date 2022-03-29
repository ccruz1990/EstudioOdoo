#-----------Curso python video 23 excepciones III------------
import math
#Programa 1
def evaluaEdad(edad):
    if edad<0:
        raise MiPropioError("No se permiten edades negativas")
    if edad<20:
        return  "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Cuídate..."

#print(evaluaEdad(-15))


#Programa 2
def calcuclaRaiz(num):
    if num<0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num)


op1=(int(input("Introduce un número: ")))

try:
    print(calcuclaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa terminado")

#-----------------------------------------------------------
#--------Curso python video 17 bucles IV---------
#Programa 1
import math
i=1
while i<=5:
    print(f"Ejecución {i}")
    i=i+1
print("Terminó la ejecución")

#Programa 2
edad=int(input("Introduce la edad: "))

while edad<5 or edad>100:
    print("Has introducido una edad incorrecta, vuelve a intentarlo")
    edad = int(input("Introduce la edad: "))

print("Gracias por colaborar, puedes pasar")
print(f"Edad del aspirante {edad}")

#Programa 3
print("Programa de cálculo de raíz cuadrada")
numero=int(input("Introduce un número : "))

intentos=0

while numero<0:
    print("No se puede encontrar la raíz de un numero negativo")

    if intentos==2:
        print("Has realizado demasiados intentos. El programa ha finalizado")
        break;

    numero = int(input("Introduce un número : "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {solucion}")
#------------------------------------------------
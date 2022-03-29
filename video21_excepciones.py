#-----------Curso python video 21 excepciones------------
def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplica(num1,num2):
    return num1*num2
def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:           #captura del error
        print("No se puede dividir entre 0")
        return "Operación errónea"      #lo que retorna en caso de que capture el error

while True:
    try:
        op1=int(input("Ingrese el número 1: "))
        op2=int(input("Ingrese el número 2: "))
        break
    except ValueError:
        print("Los valores introducidos no son correctos.Intentalo de nuevo")

operacion = input("Introduce la operación a realizar (suma,resta,multiplica, divide): ")

if operacion=="suma":
    print(suma(op1,op2))
elif operacion=="resta":
    print(resta(op1,op2))
elif operacion=="multiplica":
    print(multiplica(op1,op2))
elif operacion=="divide":
    print(divide(op1,op2))
else:
    print("Operación no contemplada")

print("Operación ejecutada, continuación de ejecución del programa")
#--------------------------------------------------------
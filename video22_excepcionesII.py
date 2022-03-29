#-----------Curso python video 22 excepciones II------------
def divide():
    try:
        op1 = float(input("Introduzca el primer número: "))
        op2 = float(input("Introduzca el segundo número: "))

        print("El resultado de la división es: " + str(op1/op2))
    except:             #Capturará cualquier tipo de error
        print("Ha ocurrido un error")
    finally:            #Hará que el código se ejecute si o si
        print("Cálculo finalizado")

divide()
#------------------------------------------------------------
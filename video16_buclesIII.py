#--------Curso python video 16 bucles III---------
#Programa 1
for i in range(5,50,3):
    print(f"valor de las variables {i}")

#Programa 2
valido=False

email=input("Introduce tu email: ")
for i in range(len(email)):
    if email[i]=="@":
        valido=True
if valido:
    print("El email es correcto")
else:
    print("El email es incorrecto")
#-------------------------------------------------
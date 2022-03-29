#--------Curso python video 15 bucles II---------
#Programa 1
contador=0
email=False
miEmail=input("Introduce tu direccion de email: ")

for i in miEmail:
    if (i=="@" or i=="."):
        contador=contador+1
if contador==2:
    print("El email es correcto")
else:
    print("El email es incorrecto")

#Programa 2
for i in range(5):
    print(I)
#-----------------------------------------------
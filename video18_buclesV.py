#--------Curso python video 18 bucles V---------
#Programa 1
for letra in "python":
    if letra=="h":
        continue
    print(f"viendo la letra {letra}")

#Programa 2
nombre= "Grupo visión"

contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1

print(contador)

#Programa 3
class MiClase:
    pass  #para implementar mas tarde

email=input("Por favor, introduce tu email: ")

for i in email:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)
#------------------------------------------------
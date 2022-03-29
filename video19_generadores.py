#----------Curso python video 19 generadores I-------------
#función normal
def generaPares(limite):

    num=1

    miLista=[]

    while num<limite:
        miLista.append(num*2)

        num+=1
    return miLista

print(generaPares(10))

#generador
def generaParesGen(limite):

    num=1

    while num<limite:
        yield num*2
        num+=1


devuelve_pares=generaParesGen(10)

print(next(devuelve_pares))

print("Aquí podria ir mas codigo")
print(next(devuelve_pares))
print(next(devuelve_pares))
#----------------------------------------------------------
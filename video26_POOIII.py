#--------Curso python video 26 POO III--------------
class Coche():
    largoChasis=250                 #Atributos de la clase
    anchoChasis=120
    ruedas=4
    enMarcha=False

    def arrancar(self):             #Métodos de la clase
        self.enMarcha=True

    def estado(self):
        if (self.enMarcha):

            return "El coche está en marcha"
        else:
            return  "El coche está parado"

miChoche = Coche()          #instancia de la clase

print("El largo del chasis es: ", miChoche.largoChasis)     #acceso a los atributos de la clase
print("El coche tiene ", miChoche.ruedas, " ruedas")

#miChoche.arrancar()

print(miChoche.estado())                #acceso a los métodos de la clase


#-----------------------------------------------------------
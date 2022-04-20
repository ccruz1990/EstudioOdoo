#--------Curso python video 26, 27 y 28 POO III, IV y V--------------
class Coche():

    def __init__(self):

        self.__largoChasis=250                 #Atributos de la clase
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

    def arrancar(self, arrancamos):             #Métodos de la clase
        self.__enMarcha=arrancamos
        if (self.__enMarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enMarcha and chequeo):
            return "El coche está en marcha"
        elif (self.__enMarcha and chequeo==False):
            return "Algo anda mal, el coche no puede arrancar"
        else:
            return "El coche está parado"

        self.enMarcha=True

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):

        print("realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="mal"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False


miChoche = Coche()                  #instancia de la clase

print(miChoche.arrancar(True))
miChoche.estado()        #acceso a los métodos de la clase

print("------------A continuación creamos el 2do objeto---------------------")

miChoche2 = Coche()
print(miChoche.arrancar(False))
miChoche2.estado()

#-----------------------------------------------------------
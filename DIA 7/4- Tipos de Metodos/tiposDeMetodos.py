class Pajaro:
#Atributos
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
#Metodos
    def piar(self):
        print('pio')
        print('pio, mi color es {}'.format(self.color))
        #se pone self.color si fuera solo color no llamaria a la instancia
    def volar(self, metros):
        print(f"El pajaro a volado {metros} metros.")
        #mensionando aca tambien puedo hacer que pie
        self.piar()



#metodos de instancia que afectan a mi pajaro
#creo un nuevo metodo
    def pintar_negro(self):
    #este metodo pintara a cualquier pajaron de negro
        self.color = 'negro'
        print(f"Ahora el pajaro es {self.color}")
        
piolin = Pajaro('amarillo','canario')
piolin.pintar_negro()
piolin.volar(50)
#modificar estado de clase
piolin.alas= False
print(piolin.alas)
#puedo modificar algo de arriba de True a False

# Metodos de Clase
#se declara condecorado classmethod
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        print(f"Es de color {self.color}")
        cls.alas= False
        print(Pajaro.alas)
Pajaro.poner_huevos(3)
Pajaro.piar()
#si puedo modificar los atributos de la clase
#pajaro no puede piar no tiene self diferencia con metodos de clase no necesitan tener una instancia no accede a color y especie

#metodos estaticos
    @staticmethod
#no se carga ni self ni cls
    def mirar():
        self.alas = 2
        #los metodos de clase no pueden acceder si quiero que no se modifiquen es la manera de hacerlo
        print("El pajaro mira")
Pajaro.mirar()
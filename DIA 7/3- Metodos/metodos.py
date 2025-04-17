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

piolin = Pajaro('amarillo','canario')
piolin.piar()
piolin.volar(50)
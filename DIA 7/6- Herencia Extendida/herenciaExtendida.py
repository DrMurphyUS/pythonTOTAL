#no eres igual
#clase hija puede tener 3 tipos de metodos
# 1 metodos heredados
# 2 metodos modificados
# 3 metodos nuevos
# pasa igual con los atributos
# Herencia multiple puede heredar de padre y madre muchas clases no solo 1 y y puede transmitrlo a un hijo
# Animal es un metodo Pajaro lo modifica canario que metodo hereda
class Animal:
        def __init__(self,edad,color):
            self.edad = edad
            self.color = color

        def nacer(self):
              print("Este animal ha nacido")
        def hablar(self):
              print("Este animal emite un sonido")

class Pajaro(Animal):
    #atributos
    def __init__(self, edad, color,altura_vuelo):
         #si le pongo el super no es necesario describir otras cosas como lo hago en el ejemplo de abajo con self
         super().__init__(edad, color)
         self.altura_vuelo=altura_vuelo
    #def __init__(self, edad, color,altura_vuelo):
    #    self.edad=edad
    #    self.color=color
    #    self.altura_vuelo=altura_vuelo
    #metodos
    def hablar(self):
        print("pio")
    #el siguiente es un nuevo metodo
    def volar(self,metros):
         print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(3,"amarillo",60)
# metodo modificado
piolin.hablar()
piolin.volar(100)
mi_animal= Animal(5,"negro")

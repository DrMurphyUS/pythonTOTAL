#Herencia Multiple
class Padre:
    def hablar(self):
        print("HOLA")
class Madre:
    def reir(self):
        print("ja ja")
    def hablar(self):
        print("QUE TAL")
class Hijo(Padre, Madre):
    pass
class Nieto(Hijo):
    pass
mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
#Hereda lo que primero toma es decir del primera clase es orden de busqueda
print(Nieto.__mro__)
#mro imprime el orden
#hay class object que esta detras y ordena se llama object
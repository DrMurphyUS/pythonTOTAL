#Herencia Polimorfismo Cohesion abstraccion acoplamiento encapsulamiento
#Hereda puedo sobreescribir algunos y ademas tener nuevos metodos
#Si quiero que herede entonces seria class Animal: pass -> class Pajaro(Animal): pass DRY Dont Repeat Yourself
class Animal:
    #Creo un atributo
    def __init__(self,edad,color):
        self.edad=edad
        self.color=color
    #Creo un metodo
    def nacer(self):
        print("Este animal a nacido")
class Pajaro(Animal):
    pass
print(Pajaro.__bases__)
#bases nos dice de quien hereda
print(Animal.__subclasses__())
#subclasses() me dice a quien hereda


piolin = Pajaro(2,"amarillo")
#piolin tiene el metodo nacer porq pertene a animal
piolin.nacer()
print(piolin.color)
print(piolin.edad)
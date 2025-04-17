class Pajaro:
# ahora atributos que todos mis clase pajaro tendran no modifcables pero si que tienen se llama atributo de clase
    alas = True
    #atributos que son personalisables
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
#def __init__(self, mi_parametro):
 #       self.atributo = mi_parametro
#mi_pajaro.atributo = mi_parametro





mi_pajaro = Pajaro('negro','Tucan')

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}.')
print(Pajaro.alas)
print(mi_pajaro.alas)
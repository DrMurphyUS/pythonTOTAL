from random import *

#importando libros de librerias 
# si quiero importar todo seria from random import * si solo quiero uno al final pongo el libro from random import randint

aleatorio = randint(1,50)
print(aleatorio)

aleatorio2 = round(uniform(1,5),1)
#un valor con decimales es uniform y con el uno final quqiero solo un uno del round
print(aleatorio2)

aleatorio3 = random()
#random es entre 0 y 1
print(aleatorio3)

colores = ['azul','rojo','amarillo','verde']
aleatorio4 = choice(colores)
print(aleatorio4)

numeros =list(range(5,50,5))
# shufle es mezclar a numeros
shuffle(numeros)
print(numeros)



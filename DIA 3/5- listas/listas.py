#ordenados distintos tipos de datos ["",""] las listas si son mutables
mi_lista = ["a","b","c"]
mi_lista2 = ["d","e","f"]
mi_lista3 = mi_lista2 + mi_lista
mi_lista3[0] = "alfa"
mi_lista3.append('g')
mi_lista3.append('h')
eliminado = mi_lista3.pop()
eliminado2 = mi_lista3.pop(1)
resultado = len(mi_lista)
resultado2 = mi_lista[0]
resultado3 = mi_lista[0:2]
otra_lista = ["hola",55,6.11]
print(mi_lista)
print(type(mi_lista))
print(otra_lista)
print(type(otra_lista))
print(resultado)
print(resultado2)
print(resultado3)
print(mi_lista+mi_lista2)
print(mi_lista3)
print(eliminado)
print(eliminado2)
lista4 =["g","o","b","m","c"]
lista4.sort()
#ordena nombre palabras y numeros
print(lista4)
#sort es nontype no tiene valor por lo que no lo podriamos guardar en una variable
lista4.reverse()
print(lista4)
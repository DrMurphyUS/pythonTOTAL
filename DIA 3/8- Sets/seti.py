#set ([]) solo admiten elementos unicos no se repiten
# {} no ordenados en indices sus elementos son inmutables debo poner un solo argumento set no es suscribible [0] para el primero oe l segundo no se pueden poner listas
#no diccionarios pero si tupples los tupples son inmuutables

mi_set = set([1,2,3,4,5,1,1,1,2,2,2,2])
print(type(mi_set))
print(mi_set)
otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)
print(len(mi_set))
print(2 in mi_set)

s1={1,2,3}
s2 ={3,4,5}
s3=s1.union(s2)
print(s3) 
s1.add(4)
print(s1)
s1.remove(2)
print(s1)
#discard es lo mismo que rmeove pero no hace error si no encuentra
s1.discard(0)
print(s1)
#si hace pop
sorteo = s1.pop()
print(sorteo)
s1.clear()
#se vacia el set 
print(s1) 

#son similiares a la lista pero  inmutables en ves de corchetes aprentesisi o sin encerrarlos en nada no soporta asignacion de items

mi_tuple = (1,2,3,4)
print(mi_tuple[-2])
print(mi_tuple[0])
print(mi_tuple)
print(type(mi_tuple))
#si puedo anidar
mi_tuple2 = (1,2,(10,20),4)
print(mi_tuple2[2][0])

mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

t = (1,2,3)
x,y,z = t
print(x,y,z)

u = (1,2,3,1)
print(len(u))
print(u.count(1))
print(u.index(1))

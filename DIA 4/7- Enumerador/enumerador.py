lista = ['a','b','c']
indice = 0
indice2 = 0
for item in lista:
    print(indice,item)
    indice += 1

for indice2,items in enumerate(range(50,55)):
    print(indice2,items)
     
mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1][0])
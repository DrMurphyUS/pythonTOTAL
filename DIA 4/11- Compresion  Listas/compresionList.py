palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
    print(lista)
print(lista)

palabra2 = 'panochita'
lista2 = [letra2 for letra2 in palabra2]
    
print(lista2)


lista3 = [numero/2 for numero in range(0,21,2)]
print(lista3)
lista4 = [numero2 if numero2 * 2 > 10 else 'no' for numero2 in range(0,21,2)]
print(lista4)

pies = [10,20,30,40,50]
metros = [pie*3.281 for pie in pies]
print(metros)
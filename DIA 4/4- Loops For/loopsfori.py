nombres = ['Juan','Jose','Andrea','Ana']

for element in nombres:
    numero_nombre = nombres.index(element) + 1
    print('hola ' + element)
    print(f"Nombre {numero_nombre}: {element}")

lista = ['Pablo', 'Luis','Julia','Laura','Julia']
for nombre in lista:
    if nombre.startswith('L'):
        print(nombre)
 
numeros = [1,2,3,4,5]
mi_valor = 0
for numero in numeros:
    mi_valor =mi_valor + numero
    print(mi_valor)
print(mi_valor)

palabra = 'python es chevere'
for letra in palabra:
    print(letra)

for lest in [[1,2],3,4]:
    print(lest)

for a,b in [[1,2],[3,4],[7,8]]:
    print(a)
    print(b)

dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic:
    print(item)
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for a,b in dic.items():
    print(a,b)

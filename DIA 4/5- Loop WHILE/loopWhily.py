monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")    
    monedas =- 1
else:
    print('No tengo mas monedas') 

respuesta = 's'
while respuesta == 's':
    respuesta = input('Quieres seguir? (s/n)')
else:
    print('Gracias')

#uso pass para pasar
#break salir del loop
#continue no sali sino que evita y continua

respuesta2 = 's'
while respuesta2 == 's':
    pass

    print('Gracias')
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r'
        break
    print(letra)
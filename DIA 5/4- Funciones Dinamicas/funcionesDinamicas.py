def cheque_3_cifras (numero):
    return numero in range(100,1000)

def verifica_3_cifras (lista):
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

def verifica_3_cifras2 (lista2):
    lista_3_cifras = []
    for n2 in lista2:
        if n2 in range(100,1000):
            lista_3_cifras.append(n2)
        else:
            pass
    return lista_3_cifras


suma = int(input('Ingresa cualquier numero: '))
resultado = cheque_3_cifras(suma)
print(resultado) 

resultado2 = verifica_3_cifras([551200,300,3000,99])
print(resultado2)

resultado3 = verifica_3_cifras2([551200,300,3000,99,500])
print(resultado3)
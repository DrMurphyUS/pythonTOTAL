from random import shuffle

#Lista Inicial
palitos = ['-','--','---','----']

#Mezclar palitos

def mezclar(lista):
    shuffle(palitos)
    return lista

#pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1','2','3','4']:
        intento = input("elige un numero del 1 al 4: ")
    
    return int(intento)

#Comprobar el intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == '-':
        print('A lavar los platos pringao!')
    else:
        print('Esta vez te has salvado')

    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

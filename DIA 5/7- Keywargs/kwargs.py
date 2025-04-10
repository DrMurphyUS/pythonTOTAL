#**kwargs =Key Words Args la clave son los ** 
#le podemos dar un nombre a los argumentos que ingresamos
def suma(**kwargs):
    print(type(kwargs))

suma(x=3, y=5,z=2)

def suma(**kwargs):
    for clave,valor in kwargs.items():
        print(f"{clave} es igual a {valor}")

suma(x=3, y=5,z=2)

def suma2(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        total += valor
    return total
print(suma2(x=3, y=5,z=2))

def prueba(num1, num2, *args, **kwargs):
    print( f"el primer valor es {num1}")
    print( f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg es igual a: {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} es igual a {valor}")
        
    

prueba(15,50,100,300,400,200,x='uno', y='dos',z='tres')

#podriamos remplazar con
args = [100,300,400,200]
kwargs = {'x':'uno', 'y':'dos','z':'tres'}
prueba(15,50,*args,**kwargs)

# y asi se remplazaria prueba para que siga
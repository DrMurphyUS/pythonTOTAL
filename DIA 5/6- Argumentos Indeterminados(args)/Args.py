def suma(a,b):
    return a+b
#paso mis argumentos que son 5 y  6
#solo puedo 2 si le pongo 3 me llevaria a 
print(suma(5,6))

def suma2(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma2(5,6,3,2,1,10,500))

def suma3(*args):
    return sum(args)
print(suma3(5,6,3,2,1,10,500))

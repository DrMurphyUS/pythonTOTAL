'''serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Motorola")
elif serie == "N-03":
    print("Nokia")
else:
    print("No existe el producto")'''
serie = "N-01"
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Motorola")
    case "N-03":
        print("Nokia")
    case _ :
        print("No existe el producto")


cliente = {'nombre':'Federico','edad':45,'ocupacion':'intructor'}
pelicula = {'titulo':'Matrix','ficha_tecnica':{'protagonista':'Keanu Reeves','director':'Lana y Lili Wachowsky'}}

elemento = [cliente,pelicula,'libro']

for e in elemento:
    match e:
        case {'nombre':nombre,'edad':edad,'ocupacion':ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo':titulo,'ficha_tecnica': {'protagonista':protagonista,'director':director}}:
            print("Esto es una pelicula")
            print(titulo,protagonista,director)
        case _ :
            print("No se que es esto")
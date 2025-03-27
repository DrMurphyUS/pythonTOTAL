#si no quiero convertir tipos puedo formatear con 2 tipos 1 formato {}.format las transforma en string
#y la otra forma es con f de cadenas literales y con las cadenas {}
x = 10
y = 15
print("mis numeros son " + str(x) + " y " + str(y))
print("la suma de {} y {} es igual a {}".format(x,y,x+y))
color = "rojo"
matricula = 541926
print(f"El auto es de color {color} y su matricula es {matricula}")
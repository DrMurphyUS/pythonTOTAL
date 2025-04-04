#unire 2 listas con zip para hacer un tuple grande
nombres = ['Ana','Hugo','Gimena']
edades = [65,29,42]
ciudades = ['Lima','Buenos Aires','Miami']

combinados  = list(zip(nombres,edades,ciudades))
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años. Y vive en {ciudad}.")
#no tiene un orden especifico no tiene indice
diccionario = {'c1':'valor1','c2':'valor3'}
print(diccionario)
print(type(diccionario))
resultado = diccionario['c2']
print(resultado)

cliente = {'nombre':'Juan','apellido':'Fuentes','peso':88,'talla':1.76}
consulta = cliente['apellido']
print(consulta)
dic = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}
print(dic['c2'][1])
print(dic['c3']['s2'])
dic1={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic1['c2'][1].upper())
#agregar elementos a dic
dic2 = {1:'a',2:'b'}

dic2['nuevo']='c'
print(dic2)
#sobreescribir nuevo valor a la clave
dic2[2]='comida'
print(dic2)
#imprime todas las llaves con keys que tien
print(dic2.keys())
#solo los valores
print(dic2.values())
print(dic2.items())
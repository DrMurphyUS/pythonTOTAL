#R LEE W ESCRIBE TODOS A ESCRIBE ALFINAL DEL TEXTO

#archivo = open('DIA 5/8- Abrir y Manipular Archivos/archivito.txt','w')
#archivo.write('soy el nuevo texto') 
#2
# \ n para espacio recuerda sino todo estara junto o podrias escribir ''' '''
#archivo.write('hOLA\n')
#archivo.write('mundo')
#3
#archivo.writelines(['HOLA','MUNDO','AQUI','ESTOY'])
#4 PARECIDO PERO CREEANDO LISTA
#lista = ['HOLA','MUNDO','AQUI','ESTOY']
#for p in lista:
#    archivo.writelines(p+'\n')
#5 registrado despues de todo el texto con a
archivo = open('DIA 5/8- Abrir y Manipular Archivos/archivito.txt','a')
archivo.write('Bienvenido')

archivo.close()

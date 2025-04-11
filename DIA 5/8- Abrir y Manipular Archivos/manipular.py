# open write read close
mi_archivo = open('DIA 5/8- Abrir y Manipular Archivos/archivito.txt')
#print(mi_archivo.read())
#son strings por lo que puedo usar sus propiedades
#2
#una_linea=mi_archivo.readline()
#print(una_linea.upper())

#una_linea=mi_archivo.readline()
#print(una_linea.rstrip())

#una_linea=mi_archivo.readline()
#print(una_linea)
#3
#for l in mi_archivo:
#    print('Aqui dice: ' + l)

#mi_archivo.close()

#4
todas = mi_archivo.readlines()
todas = todas.pop()
print(todas)
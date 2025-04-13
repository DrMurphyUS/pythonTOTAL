#PARA NAVEGAR NE WINDOWS ES CON LA DIRECCION PERO CON LA BARRA INVERTIDA \
#se resuelve con path
#ademas conoceremos a os
import os
#cdw current working directory
ruta = os.getcwd()
print(ruta)
#chdir que es change directory
ruta2= os.chdir('C:\\Users\\PC\\Downloads')
print(ruta2)
archivo = open('otro_archivo.txt')
print(archivo.read())
#para crear otro directorio hago mkdirs como ahora creo una carpeta otra
ruta = os.makedirs('C:\\Users\\PC\\Downloads\\otra')

ruta3 = 'C:\\Users\\PC\\Downloads\\otro_arhcivo.txt'
elemento = os.path.basename(ruta3)
print(elemento)
#imprime otro_archivo.txt
ruta4 = 'C:\\Users\\PC\\Downloads\\otro_arhcivo.txt'
elemento2 = os.path.dirname(ruta4)
print(elemento2)
#imprime la primera parte del archivo osea= ruta4 = 'C:\\Users\\PC\\Downloads
ruta5 = 'C:\\Users\\PC\\Downloads\\otro_arhcivo.txt'
elemento3 = os.path.split(ruta5)
print(elemento3)
# imprime separado tanto 'C:\\Users\\PC\\Downloads como otro_arhcivo.txt'
#tambien podemos elimar carpetas como por ejemplo eliminamor carpeta otra con rmdir remove directory
os.rmdir(('C:\\Users\\PC\\Downloads\\otra'))
# solo puedo abrir directamente si se encuentra en mi mismo archivo directorio o copiando directamente la direccion y ejecutamos
otro_archivo = open ('C:\\Users\\PC\\Downloads\\otro_arhcivo.txt')
print(otro_archivo.read())
#en mac o linyx puede que te salga error y ahi es donde deves usar un modulo distinto patth es un objeto
from pathlib import Path
carpeta= Path('C:/Users/PC/Downloads')
#eSTO FUNCIONA EN MAC Y LINUX
archivo = carpeta /'otro_archivo.txt'
mi_archivo =  open(archivo)
#asi puedo abrirlo tambien no me dio problemas
print(mi_archivo.read())

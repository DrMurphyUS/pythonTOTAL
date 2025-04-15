#cuando creas una lista con los distintos nombres puede guardarlos en gerarquia para despues generar como un archivo super rapido
from pathlib import Path
#guia = Path("Barcelona","Sagrada_Familia.txt")
#print(guia)
# entonces con este ejemplo vez que hace una ruta de acceso
#puedo agregar home para que sea una guia especifica la real
base = Path.home()
guia = Path(base,"Barcelona","Sagrada_Familia.txt")
guia = Path(base,"Europa","España",Path("Barcelona","Sagrada_Familia.txt"))
#imprime toda la direccion
guia2 = guia.with_name("La perrera.txt")
print(base)
print(guia)
print(guia2)
print(guia.parent.parent)
print(guia.parent.parent.parent)
print(guia.parent)

guia = Path(Path.home(),"Europa")
for txt in Path(guia).glob("**/*.txt"):
    print(txt)

#y a todos los tranforma en .txt

#otro con guia larga

guia3 = Path('Europa','España','Barceloma','LaSagradaFamilia.txt')
en_europa = guia3.relative_to(Path('Europa'))
en_espania = guia3.relative_to(Path('Europa','España'))
print(en_europa)
print(en_espania)
#permite manejar rutas de manera rapida

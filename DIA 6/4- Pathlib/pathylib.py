from pathlib import Path, PureWindowsPath
#purewindowspath para la direccion
carpeta = Path('DIA 5/8- Abrir y Manipular Archivos/archivito.txt')
#puede leer .readtext porque es un archivo path
print(carpeta.read_text())
print(carpeta.name)
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genius, el archivo existe le putitoooo")

ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)
#veo la ruta dodne esta mi archivo

#upper()pasar a mayusculas lower()pasar a minusculas split()separalo en partes join() unir items usando separador find()encontrar un sub string  replace() remplazar string uno por otro

texto = "Este es el texto de federico"
resultado = texto
print(resultado)
texto = "Este es el texto de federico"
resultado = texto.upper()
texto = "Este es el texto de federico"
resultado = texto[2].upper()
print(resultado)
texto = "Este es el texto de federico"
resultado = texto.lower()
print(resultado)
texto = "Este es el texto de federico"
resultado = texto.split()
print(resultado)
resultado = texto.split("t")
print(resultado)
a = "Aprender"
b = "python"
c = "es"
d = "genial."
e = " ".join([a,b,c,d])
print(e)
texto = "Este es el texto de federico"
resultado = texto.find("s")
print(resultado)
#cuando no encuentra el texto devuelve -1 a diferencia de index
texto = "Este es el texto de federico"
resultado = texto.replace("federico","Murphy")
print(resultado)
texto = "Este es el texto de federico"
resultado = texto.replace("e","i")
print(resultado)

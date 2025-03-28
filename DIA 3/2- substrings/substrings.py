#rebanar o SLICING recuerda el ultimo digito nunca se incluye y el tercero cada cuanto se selecciona

texto = "ABCDEFGHIJKLM"
fragmento = texto[2]
print(fragmento)
fragmento2 = texto[2:5]
print(fragmento2)
fragmento3 = texto[2:]
print(fragmento3)
fragmento4 = texto[:5]
print(fragmento4)
fragmento5 = texto[2:10:2]
print(fragmento5)
fragmento6 = texto[::3]
print(fragmento6)
fragmento7 = texto[::-1]
print(fragmento7)
fragmento8 = texto[::-2]
print(fragmento8)

import json

file_name = "datos.json"

with open(file_name) as data:
    datos = json.load(data)

# Imprimir los primeros 4 pares clave-valor, contando desde el valor 0
contador = 0
for key, value in datos.items():
    if contador < 4:
        if key == "version" and isinstance(value, list):
            print(f"{key}: {value[0]}")
        else:
            print(f"{key}: {value}")
        contador += 1
    else:
        break
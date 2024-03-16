import json
from tabulate import tabulate

file_name = "datos.json"

with open(file_name) as data:
    datos = json.load(data)

# Convertir el diccionario a una lista de listas para tabulate
tabla_datos = []
for key, value in datos.items():
    tabla_datos.append([key, value])

# Mostrar la tabla
print(tabulate(tabla_datos, headers=['Dato', 'Valor']))

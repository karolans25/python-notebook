"""
Enunciado
Manipulación básica con pandas: Crea un programa que utilice la biblioteca Pandas 
para realizar las siguientes tareas:

Crear un DataFrame llamado datos con las siguientes columnas: Nombre, Edad, Ciudad.
Mostrar por pantalla la información del DataFrame.
Filtrar las filas donde la edad sea mayor que 25.
Añadir una nueva columna llamada Categoría que clasifique a las personas en "Joven" 
si tienen 25 años o menos, y "Adulto" si tienen más de 25 años.
Mostrar por pantalla el DataFrame actualizado.
"""

import pandas as pd
from random import randint, choice

# Generate the data
names = ['Pedro', 'Pablo', 'Lorena', 'Ana', 'Cecilia', 'Raúl']
surnames = ['Parra', 'Pulido', 'Gómez', 'Sánchez', 'Toledo', 'Nazrath']
cities = ['Bogotá', 'Barranquilla', 'Duitama', 'Cali', 'Medellín', 'Tunja']

num_data = 30

users = [{'Nombre': choice(names) + ' ' + choice(surnames),
        'Edad': randint(8, 50),
        'Ciudad': choice(cities)
    } for i in range(num_data)]

# users = {
#     'Nombre': [choice(names) + ' ' + choice(surnames) for i in range(num_data)],
#     'Edad': [randint(9, 50) for i in range(num_data)],
#     'Ciudad': [choice(cities) for i in range(num_data)]
# }


# Create the data frame
datos = pd.DataFrame(users)
print(datos)

# Filter the data
age = 25
greater_25 = datos[datos['Edad'] > age]
# print(greater_25)


# Add a column with a condition
datos['Categoría'] = datos['Edad'].apply(lambda x: 'Joven' if x <= 25 else 'Adulto')

print()
print(datos)

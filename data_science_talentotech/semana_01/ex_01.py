"""
Enunciado
DataFrame: Crea un programa que utilice la librería Pandas para crear un DataFrame 
con la siguiente información sobre 5 estudiantes: nombres, edades y calificaciones. 
Muestra el DataFrame resultante.
"""

import pandas as pd
from random import randint, choice

# Generate the data
names = ['Pedro', 'Pablo', 'Lorena', 'Ana', 'Cecilia', 'Raúl']
surnames = ['Parra', 'Pulido', 'Gómez', 'Sánchez', 'Toledo', 'Nazrath']

num_data = 5

users = [{'Nombre': choice(names) + ' ' + choice(surnames),
        'Edad': randint(14, 18),
        'Calificación': randint(1, 5),
    } for i in range(num_data)]

# users = {
#     'Nombre': [choice(names) + ' ' + choice(surnames) for i in range(num_data)],
#     'Edad': [randint(9, 50) for i in range(num_data)],
#     'Calificación': [randint(1, 5) for i in range(num_data)],
# }


# Create the data frame
datos = pd.DataFrame(users)
print(datos)

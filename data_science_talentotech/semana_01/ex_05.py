"""
Enunciado
Concatenación de DataFrames: Crea un programa que utilice Pandas para realizar las 
siguientes tareas:

Crea dos DataFrames llamados df1 y df2 con las siguientes columnas: A, B, C.
Llena ambos DataFrames con datos.
Concatena verticalmente los dos DataFrames para crear un nuevo DataFrame llamado df_concat.
Muestra por pantalla el resultado de la concatenación.
"""
import pandas as pd
import numpy as np
from random import randint, choice

# Generate the data
names = ['Pedro', 'Rodrigo', 'Lorena', 'Ana', 'Constanza', 'Raúl', 'Nancy', 'Shahana', 'Ali', 'Reshma']
surnames = ['Pérez', 'Pulido', 'Gómez', 'Sánchez', 'Toledo', 'Nazrath', 'Nassiri', 'Vizcaino', 'Gáfaro', 'Flórez']

num_data = 5

# Create the data frame df1
users = [{'Nombre': choice(names) + ' ' + choice(surnames),
        'Edad': randint(14, 18),
        'Calificación': randint(1, 5),
    } for i in range(num_data)]
df1 = pd.DataFrame(users)
print(df1)

# Create the data frame df2
users = [{'Nombre': choice(names) + ' ' + choice(surnames),
        'Edad': randint(14, 18),
        'Calificación': randint(1, 5),
    } for i in range(num_data)]
df2 = pd.DataFrame(users)
print(df2)

#Concatenate the dataframes
df_concat = pd.concat([df1, df2])
print(df_concat)


###
df1 = pd.DataFrame(np.arange(9).reshape([3,3]), 
                   columns = ['a', 'b', 'c'])
print(df1)
df2 = pd.DataFrame(np.arange(12).reshape([4,3]), 
                   columns = ['b', 'c', 'd'])
print(df2)
df_concat = pd.concat([df1, df2], sort=False, axis=0, ignore_index=True)
print(df_concat)
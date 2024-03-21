"""
Enunciado
Operación básica con NumPy: Utiliza la biblioteca NumPy para realizar las 
siguientes operaciones:

Crea un array llamado vector con los números del 1 al 5.
Calcula la media y la desviación estándar del array vector.
Crea una matriz llamada matriz con 3 filas y 2 columnas, llenándola con 
números aleatorios entre 1 y 10.
Multiplica todos los elementos de la matriz por 2.
Muestra por pantalla el resultado de la multiplicación
"""

import numpy as np
from random import randint

# Vector
num_data = 5
vector = np.array([i for i in range(1, num_data + 1)])

print(f"Vector: {vector}")
print(f"La media del vector es: {np.mean(vector)}")
print(f"La desviacón estándar del vector es: {np.std(vector)}")

# Matriz
lines, cols = 3, 2 # Matrix 3 x 2
matriz = np.matrix([ [ randint(1,10) for i in range(cols) ] for j in range(lines) ])
print("\nMatriz: ")
print(matriz)
print("\nMatriz multiply by 2")
print(np.multiply(matriz, 2))

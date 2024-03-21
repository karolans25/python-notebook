"""
Enunciado
Filtrado con Pandas: Crea un programa que utilice Pandas para realizar las siguientes tareas:

Descarga el conjunto de datos de Iris desde la 
URL: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
Carga los datos en un DataFrame llamado iris.
Muestra las primeras 5 filas del DataFrame.
Filtra las filas donde la especie sea "setosa".
Calcula la media de la longitud de los sépalos para las filas filtradas.
"""

"""
# pip install ucimlrepo
"""

# from ucimlrepo import fetch_ucirepo 
# import pandas as pd

# # fetch dataset 
# data = fetch_ucirepo(id=53) 
  
# X = data.data.features 
# y = data.data.targets 

# iris = pd.merge(pd.DataFrame(X), pd.DataFrame(y), right_index=True, left_index=True)


import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

heads = ['sepal length', 'sepal width', 'petal length', 'petal width', 'specie']
iris = pd.read_csv(url, header=None, names=heads)

print('\n', iris.head())

filter_specie = "setosa"
filter_iris = iris[iris['specie'].apply(lambda x: filter_specie in x )]
print('\n', filter_iris)

media = iris['sepal length'].mean()
print('\n', media)
# media = iris['sepal width'].mean()
# print('\n', media)
# media = iris['petal length'].mean()
# print('\n', media)
# media = iris['petal width'].mean()
# print('\n', media)

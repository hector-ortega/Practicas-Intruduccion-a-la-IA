#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# k-NN (k-Nearest Neighbors):
# El algoritmo k-NN es un método de aprendizaje supervisado utilizado para la clasificación y regresión. Funciona de la siguiente manera:

# Utilización:
# - Clasificación: Cuando se utiliza para clasificar un nuevo punto de datos, se basa en las etiquetas de los puntos de datos más cercanos 
#     en el espacio de características.
# - Regresión: Cuando se utiliza para regresión, calcula el valor medio (o mediana) de los k puntos de datos más cercanos para predecir el 
#     valor de un nuevo punto de datos.
# Funcionamiento:
# - Calcula la distancia entre el punto de datos a clasificar y todos los puntos de datos en el conjunto de entrenamiento.
# - Selecciona los k puntos de datos más cercanos al punto a clasificar.
# - Para clasificación, asigna la etiqueta más común entre los k vecinos más cercanos al punto a clasificar. Para regresión, 
#     calcula el valor medio (o mediana) de los valores de los k vecinos más cercanos.

# k-Means:
# El algoritmo k-Means es un método de agrupamiento no supervisado utilizado para dividir un conjunto de datos en k grupos (clusters) 
#     basándose en las similitudes entre los puntos de datos. Funciona de la siguiente manera:

# Utilización:
# Segmentación de datos: Se utiliza para agrupar datos similares en distintos grupos con el objetivo de encontrar patrones o estructuras ocultas en los datos.
# Funcionamiento:
# - Se eligen aleatoriamente k centroides iniciales para representar los centroides de los clusters.
# - Se asignan todos los puntos de datos al cluster cuyo centroide es el más cercano.
# - Se recalculan los centroides de los clusters utilizando los puntos de datos asignados a cada cluster.
# - Se repiten los pasos 2 y 3 hasta que la convergencia se alcanza, es decir, hasta que no haya cambios significativos en la asignación 
#     de puntos a clusters o en la posición de los centroides.

# Clustering en general:
# Utilización:
# - Análisis exploratorio de datos: Se utiliza para explorar la estructura subyacente de un conjunto de datos y descubrir grupos o patrones inherentes.
# - Segmentación de mercado: Se utiliza para segmentar a los clientes en grupos homogéneos con características y comportamientos similares.
# - Compresión de datos: Se utiliza para reducir la dimensionalidad de un conjunto de datos agrupando puntos similares en clusters y representando cada 
#     cluster con su centroide.

# Funcionamiento:

# - Se divide el conjunto de datos en k grupos basándose en la similitud entre los puntos de datos.
# - Los puntos de datos dentro de un mismo cluster son más similares entre sí que con los puntos de datos en otros clusters.
# - Se busca minimizar la distancia intra-cluster (distancia entre puntos de datos dentro del mismo cluster) y maximizar la distancia inter-cluster 
#     (distancia entre puntos de datos en diferentes clusters).
#--------------- PROGRAMA --------------------------------------

# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Generar datos de ejemplo
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualizar los datos generados
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='viridis')
plt.title("Datos de ejemplo")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()

# Implementación de k-NN
# Crear un clasificador k-NN
knn = KNeighborsClassifier(n_neighbors=5)

# Entrenar el clasificador k-NN
knn.fit(X, y)

# Generar nuevos puntos para predecir
new_points = np.array([[2, 2], [0, 5]])

# Realizar predicciones con k-NN
predictions_knn = knn.predict(new_points)

# Imprimir las predicciones
print("Predicciones k-NN:", predictions_knn)

# Implementación de k-Means Clustering
# Crear un modelo de k-Means con 4 clusters
kmeans = KMeans(n_clusters=4)

# Entrenar el modelo de k-Means
kmeans.fit(X)

# Obtener los centroides de los clusters
centroids = kmeans.cluster_centers_

# Obtener las etiquetas de los clusters
labels = kmeans.labels_

# Visualizar los clusters y los centroides
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis', alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', c='red', s=200, label='Centroides')
plt.title("k-Means Clustering")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()

#--------------------------------------------------------------------------------------------------------------
# 1.- Importar las bibliotecas necesarias: Importamos las bibliotecas que necesitaremos, como NumPy, Matplotlib y scikit-learn.
# 2.-Generar datos de ejemplo: Utilizamos la función make_blobs de scikit-learn para generar datos de ejemplo con 4 centros (clusters) y una desviación estándar de 0.60.
# 3.- Visualizar los datos generados: Utilizamos Matplotlib para visualizar los datos generados en un gráfico de dispersión.
# 4.- Implementación de k-NN:
# - Creamos un clasificador k-NN con KNeighborsClassifier.
# - Entrenamos el clasificador con los datos generados utilizando el método fit.
# - Generamos nuevos puntos para predecir.
# - Realizamos predicciones con el clasificador k-NN utilizando el método predict.
# - Imprimimos las predicciones.
# 5.- Implementación de k-Means Clustering:
# - Creamos un modelo de k-Means con KMeans y especificamos el número de clusters.
# - Entrenamos el modelo de k-Means con los datos generados utilizando el método fit.
# - Obtenemos los centroides de los clusters y las etiquetas de los clusters.
# - Visualizamos los clusters y los centroides en un gráfico de dispersión.
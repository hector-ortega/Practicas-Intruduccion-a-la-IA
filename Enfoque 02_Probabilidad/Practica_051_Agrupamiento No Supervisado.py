#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# El agrupamiento no supervisado, también conocido como clustering, es una técnica de aprendizaje automático que se utiliza para encontrar 
# grupos o clusters dentro de un conjunto de datos. A diferencia del aprendizaje supervisado, donde se tienen datos etiquetados y se entrena 
# un modelo para predecir estas etiquetas, en el agrupamiento no supervisado no se tienen etiquetas y el algoritmo busca descubrir la estructura 
# subyacente en los datos por sí mismo.

# El objetivo del agrupamiento no supervisado es dividir un conjunto de datos en grupos homogéneos (clústeres) de manera que los elementos 
# dentro de cada grupo sean más similares entre sí que con los elementos de otros grupos. Esto puede ser útil para explorar patrones y relaciones
# ocultas en los datos, segmentar clientes en diferentes grupos según su comportamiento, comprimir datos eliminando redundancias o ruido, entre otros.

# Uno de los algoritmos más populares para el agrupamiento no supervisado es el algoritmo K-Means. El funcionamiento básico de K-Means es el siguiente:

# 1.- Inicialización de centroides: Se eligen aleatoriamente K centroides iniciales en el espacio de características. K representa el número 
#     de clústeres que se desean obtener.
# 2.- Asignación de puntos a clústeres: Se asigna cada punto de datos al clúster cuyo centroide está más cerca de él. Esto se hace calculando 
#     la distancia entre cada punto y cada centroide, generalmente utilizando la distancia euclidiana.
# 3.- Actualización de centroides: Se recalculan los centroides de cada clúster como el promedio de todos los puntos asignados a ese clúster.
# 4.- Reasignación de puntos y actualización de centroides: Los pasos 2 y 3 se repiten iterativamente hasta que se cumple algún criterio de detención,
#     como la convergencia de los centroides o un número máximo de iteraciones.
#--------------- PROGRAMA --------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generamos datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualizamos los datos
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Datos de ejemplo')
plt.show()

# Creamos el modelo K-Means
kmeans = KMeans(n_clusters=4)

# Ajustamos el modelo a los datos
kmeans.fit(X)

# Obtenemos las etiquetas de los clústeres y los centros de los clústeres
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Visualizamos los clústeres y los centros
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='*', c='red', s=200, label='Centroides')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Clustering con K-Means')
plt.legend()
plt.show()

#----------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias:
#   -numpy: Para operaciones numéricas.
#   -matplotlib.pyplot: Para visualización de datos.
#   -make_blobs: Para generar datos de ejemplo.
#   -Means: Para realizar el agrupamiento utilizando el algoritmo K-Means.
# 2.- Generamos datos de ejemplo utilizando la función make_blobs. Estos datos son útiles para demostrar el funcionamiento del algoritmo.
# 3.- Visualizamos los datos de ejemplo utilizando matplotlib.pyplot.scatter.
# 4.- Creamos una instancia del modelo K-Means con KMeans(n_clusters=4), especificando el número de clústeres que deseamos obtener.
# 5.- Ajustamos el modelo a los datos utilizando el método fit(X).
# 6.- Obtenemos las etiquetas de los clústeres para cada punto de datos utilizando kmeans.labels_ y los centros de los clústeres utilizando kmeans.cluster_centers_.
# 7.- Visualizamos los clústeres asignados a cada punto de datos y los centros de los clústeres utilizando matplotlib.pyplot.scatter.
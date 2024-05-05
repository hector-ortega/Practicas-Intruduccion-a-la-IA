#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# El algoritmo ID3 (Iterative Dichotomiser 3) es un algoritmo clásico de aprendizaje automático utilizado para construir árboles de decisión
# a partir de un conjunto de datos. Los árboles de decisión son estructuras de árbol que representan un conjunto de reglas de decisión y
# se utilizan para modelar relaciones entre características y clases en conjuntos de datos.

# Funcionamiento:
# 1.- Selección del Atributo de Mayor Ganancia de Información: El algoritmo ID3 utiliza la ganancia de información para seleccionar
#     el atributo que mejor divide el conjunto de datos en clases más homogéneas. La ganancia de información se calcula utilizando 
#     la entropía del conjunto de datos original y la entropía de los conjuntos de datos divididos por cada valor del atributo.

# 2.- Construcción Recursiva del Árbol: Una vez seleccionado el atributo de mayor ganancia de información, el conjunto
#     de datos se divide en función de los diferentes valores de ese atributo. Este proceso se realiza de forma recursiva 
#     para cada subconjunto de datos, construyendo así el árbol de decisión completo.

# 3.- Criterio de Parada: El proceso de construcción del árbol se detiene cuando se cumple uno de los siguientes criterios:
# - Todos los ejemplos en un nodo son de la misma clase.
# - No quedan atributos para dividir.
# - Se alcanza un límite predefinido en la profundidad del árbol o en el número mínimo de ejemplos en un nodo.

# 4.- Podado (Opcional): Después de construir el árbol, se puede aplicar un proceso de podado para eliminar ramas del
#     árbol que no aportan una mejora significativa en la precisión de la clasificación. Esto ayuda a prevenir el sobreajuste del modelo.

#--------------- PROGRAMA ------------------------------------
import numpy as np

def entropy(y):
    """Calcula la entropía de un conjunto de datos"""
    classes = np.unique(y)  # Obtiene las clases únicas en el conjunto de datos
    entropy = 0
    for c in classes:
        p = np.sum(y == c) / len(y)  # Calcula la probabilidad de cada clase
        entropy -= p * np.log2(p)  # Calcula la entropía para cada clase y la suma
    return entropy

def information_gain(X, y, feature_idx):
    """Calcula la ganancia de información de un atributo dado"""
    entropy_parent = entropy(y)  # Calcula la entropía del conjunto de datos original
    values = np.unique(X[:, feature_idx])  # Obtiene los valores únicos del atributo
    weighted_entropy_children = 0
    for v in values:
        # Divide el conjunto de datos en función del valor del atributo
        y_child = y[X[:, feature_idx] == v]
        # Calcula la entropía de cada subconjunto y suma ponderada
        weighted_entropy_children += (len(y_child) / len(y)) * entropy(y_child)
    # Calcula la ganancia de información
    information_gain = entropy_parent - weighted_entropy_children
    return information_gain

def id3(X, y, features):
    """Implementación del algoritmo ID3 para construir un árbol de decisión"""
    # Caso base: si todos los ejemplos tienen la misma clase, devolver ese nodo
    if len(np.unique(y)) == 1:
        return np.unique(y)[0]
    # Si no quedan atributos para dividir, devolver la clase mayoritaria
    if len(features) == 0:
        return np.argmax(np.bincount(y))
    # Seleccionar el atributo con la mayor ganancia de información
    gains = [information_gain(X, y, f) for f in features]
    best_feature_idx = features[np.argmax(gains)]
    best_feature = features[np.argmax(gains)]
    # Crear el nodo del árbol de decisión con el mejor atributo
    tree = {best_feature: {}}
    features = [f for f in features if f != best_feature]  # Eliminar el atributo seleccionado
    # Recursivamente construir el árbol para cada valor del mejor atributo
    for value in np.unique(X[:, best_feature_idx]):
        # Dividir el conjunto de datos en función del valor del mejor atributo
        X_subset = X[X[:, best_feature_idx] == value]
        y_subset = y[X[:, best_feature_idx] == value]
        # Si el subconjunto está vacío, devolver la clase mayoritaria
        if len(y_subset) == 0:
            tree[best_feature][value] = np.argmax(np.bincount(y))
        else:
            # Construir recursivamente el árbol con el subconjunto de datos
            tree[best_feature][value] = id3(X_subset, y_subset, features)
    return tree

# Ejemplo de uso del algoritmo ID3 con datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Ejemplos de características
y = np.array([0, 1, 1, 0])  # Ejemplos de clases
features = [0, 1]  # Índices de las características

# Construir el árbol de decisión
tree = id3(X, y, features)

# Imprimir el árbol de decisión
print("Árbol de decisión construido:")
print(tree)

#----------------------------------------------------------------------
# La función entropy(y) calcula la entropía del conjunto de datos y utilizando la fórmula de entropía de Shannon.
# La función information_gain(X, y, feature_idx) calcula la ganancia de información para un atributo dado feature_idx.
# La función id3(X, y, features) implementa el algoritmo ID3 recursivamente para construir el árbol de decisión.
# El ejemplo de uso al final muestra cómo utilizar el algoritmo ID3 con un conjunto de datos de ejemplo X y y.
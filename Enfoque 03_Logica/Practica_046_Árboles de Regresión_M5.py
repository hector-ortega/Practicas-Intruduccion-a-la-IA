#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# El algoritmo M5 es una extensión del algoritmo de árbol de decisión C4.5, pero está diseñado específicamente para problemas de regresión 
# en lugar de clasificación. A diferencia de los árboles de decisión estándar que predicen clases discretas, los árboles de regresión M5 predicen valores numéricos.

# Funcionamiento:
# 1.- Construcción del Árbol: El algoritmo M5 construye el árbol de regresión de manera similar a los árboles de decisión, pero utiliza 
#     criterios específicos para problemas de regresión. En lugar de maximizar la ganancia de información como en C4.5, M5 minimiza el 
#     error cuadrático medio ponderado en cada división.
# 2.- División de Nodos: Durante la construcción del árbol, se evalúan todas las características y umbrales posibles para determinar
#     la mejor división. Se selecciona la división que minimiza el error cuadrático medio ponderado entre los subconjuntos resultantes.
# 3.- Criterios de Parada: El algoritmo M5 tiene criterios de parada similares a los árboles de decisión estándar, como la profundidad 
#     máxima del árbol y el número mínimo de muestras requeridas para dividir un nodo.
# 4.- Predicción: Una vez que se ha construido el árbol, se puede utilizar para hacer predicciones sobre nuevos datos. Para cada instancia 
#     de datos, el algoritmo sigue el camino a través del árbol hasta llegar a un nodo hoja y devuelve el valor de predicción asociado a ese nodo.
# #--------------- PROGRAMA ------------------------------------
import numpy as np

class Node:
    def __init__(self, feature_index=None, threshold=None, value=None, left=None, right=None):
        self.feature_index = feature_index  # Índice de la característica para dividir el nodo
        self.threshold = threshold  # Umbral para dividir el nodo
        self.value = value  # Valor de predicción en el nodo (solo para nodos hoja)
        self.left = left  # Referencia al subárbol izquierdo
        self.right = right  # Referencia al subárbol derecho

class M5Tree:
    def __init__(self, max_depth=5, min_samples_split=2):
        self.max_depth = max_depth  # Profundidad máxima del árbol
        self.min_samples_split = min_samples_split  # Número mínimo de muestras requeridas para dividir un nodo
        self.tree = None

    def fit(self, X, y):
        self.tree = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        num_samples, num_features = X.shape
        num_classes = len(np.unique(y))

        # Caso base: si se alcanza la profundidad máxima o el número de muestras es menor que el mínimo
        if depth == self.max_depth or num_samples < self.min_samples_split or num_classes == 1:
            value = np.mean(y)  # Valor de predicción = media de los valores de y
            return Node(value=value)

        # Seleccionar el mejor divisor
        best_feature_index, best_threshold = self._find_best_split(X, y)

        # Dividir el conjunto de datos en dos subconjuntos
        left_indices = np.where(X[:, best_feature_index] <= best_threshold)[0]
        right_indices = np.where(X[:, best_feature_index] > best_threshold)[0]

        # Caso base: si no se puede realizar más división
        if len(left_indices) == 0 or len(right_indices) == 0:
            value = np.mean(y)  # Valor de predicción = media de los valores de y
            return Node(value=value)

        # Construir recursivamente los subárboles
        left = self._build_tree(X[left_indices, :], y[left_indices], depth + 1)
        right = self._build_tree(X[right_indices, :], y[right_indices], depth + 1)

        # Retornar el nodo actual con la mejor división
        return Node(feature_index=best_feature_index, threshold=best_threshold, left=left, right=right)

    def _find_best_split(self, X, y):
        num_samples, num_features = X.shape
        best_score = float('inf')
        best_feature_index = None
        best_threshold = None

        # Iterar sobre todas las características y umbrales para encontrar la mejor división
        for feature_index in range(num_features):
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                left_indices = np.where(X[:, feature_index] <= threshold)[0]
                right_indices = np.where(X[:, feature_index] > threshold)[0]

                if len(left_indices) < self.min_samples_split or len(right_indices) < self.min_samples_split:
                    continue

                # Calcular el error cuadrático medio ponderado
                mse_left = np.mean((y[left_indices] - np.mean(y[left_indices]))**2)
                mse_right = np.mean((y[right_indices] - np.mean(y[right_indices]))**2)
                score = mse_left * len(left_indices) + mse_right * len(right_indices)

                # Actualizar la mejor división si es necesario
                if score < best_score:
                    best_score = score
                    best_feature_index = feature_index
                    best_threshold = threshold

        return best_feature_index, best_threshold

    def predict(self, X):
        return np.array([self._predict_single(x, self.tree) for x in X])

    def _predict_single(self, x, node):
        if node.value is not None:
            return node.value

        if x[node.feature_index] <= node.threshold:
            return self._predict_single(x, node.left)
        else:
            return self._predict_single(x, node.right)

# Ejemplo de uso:
# Crear un conjunto de datos de ejemplo
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([2, 3, 4, 5, 6])

# Crear y ajustar el modelo de árbol de regresión M5
model = M5Tree(max_depth=3, min_samples_split=2)
model.fit(X, y)

# Predecir valores para nuevos datos
new_data = np.array([[2.5, 3.5], [4.5, 5.5]])
predictions = model.predict(new_data)
print("Predictions:", predictions)

#-----------------------------------------------------------------------
# 1.- Node: Esta clase representa un nodo en el árbol de regresión. Cada nodo tiene un índice de característica, un umbral, un valor de predicción 
#     (solo para nodos hoja) y referencias a los subárboles izquierdo y derecho.
# 2.- M5Tree: Esta clase representa el árbol de regresión M5. Tiene métodos para ajustar el modelo (fit) y para realizar predicciones (predict).
# 3.- fit: Este método construye el árbol de regresión de forma recursiva utilizando el algoritmo M5. Comienza en la raíz del árbol y divide el 
#     conjunto de datos en subconjuntos en función de los mejores divisores encontrados.
# 4.- _build_tree: Este método es utilizado internamente por fit para construir recursivamente el árbol. Se detiene cuando se alcanza la profundidad máxima,
#     el número mínimo de muestras para dividir un nodo no se cumple o todas las muestras en un nodo son de la misma clase.
# 5.- _find_best_split: Este método encuentra el mejor divisor para dividir el conjunto de datos en dos subconjuntos. Itera sobre todas las características 
#     y umbrales posibles y calcula el error cuadrático medio ponderado para cada posible división.
# 6.- predict: Este método realiza predicciones para nuevos datos utilizando el árbol de regresión construido. Para cada instancia de datos,
#     sigue el camino a través del árbol de decisión y devuelve el valor de predicción en el nodo hoja alcanzado.
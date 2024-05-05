#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Boosting es una técnica de conjunto utilizada principalmente en problemas de clasificación, aunque también se puede 
#     adaptar para problemas de regresión. Su objetivo es mejorar la precisión de un modelo combinando múltiples clasificadores débiles
#     (clasificadores que son solo ligeramente mejores que elegir al azar) para formar un clasificador fuerte.

# El funcionamiento del algoritmo de Boosting se puede describir en los siguientes pasos:

# 1.- Inicialización de pesos: Se asignan pesos iguales a todas las instancias de entrenamiento.
# 2.- Entrenamiento de clasificadores débiles: Se entrena un clasificador débil utilizando los datos de entrenamiento.
#     Un clasificador débil podría ser, por ejemplo, un árbol de decisión con una profundidad máxima limitada o una regresión logística simple.
# 3.- Cálculo del error ponderado: Se calcula el error ponderado del clasificador débil. Esto implica calcular el error del
#     clasificador ponderado por los pesos de las instancias, donde se da más peso a las instancias clasificadas incorrectamente.
# 4.- Asignación de peso al clasificador débil: Se asigna un peso al clasificador débil en función de su tasa de error.
#     Cuanto menor sea el error del clasificador, mayor será su peso en la combinación final.
# 5.- Actualización de pesos de las instancias: Se actualizan los pesos de las instancias de entrenamiento. Las instancias que 
#     fueron clasificadas incorrectamente por el clasificador débil actual recibirán un mayor peso en la siguiente iteración, 
#     lo que hace que el siguiente clasificador se enfoque más en ellas.
# 6.- Combinación de clasificadores débiles: Se combinan los clasificadores débiles entrenados en pasos anteriores para formar
#     un clasificador fuerte. La combinación se realiza ponderando las predicciones de cada clasificador débil por su peso asignado.
# 7.- Predicción final: Para hacer una predicción sobre nuevas instancias, se utilizan los clasificadores débiles combinados. 
#     La predicción final se calcula como la suma ponderada de las predicciones individuales de cada clasificador débil
# #--------------- PROGRAMA ------------------------------------
import numpy as np

class WeakClassifier:
    def __init__(self, threshold):
        self.threshold = threshold

    def predict(self, X):
        return np.where(X < self.threshold, -1, 1)

class Boosting:
    def __init__(self, num_classifiers=10):
        self.num_classifiers = num_classifiers
        self.classifiers = []
        self.alphas = []

    def fit(self, X, y):
        n_samples, n_features = X.shape
        weights = np.ones(n_samples) / n_samples  # Inicializar pesos de las instancias

        for _ in range(self.num_classifiers):
            weak_classifier = WeakClassifier(np.random.rand())  # Crear un clasificador débil aleatorio
            predictions = weak_classifier.predict(X)           # Predecir con el clasificador débil
            error = np.sum(weights[y != predictions])         # Calcular el error ponderado

            alpha = 0.5 * np.log((1 - error) / (error + 1e-10))  # Calcular el peso del clasificador
            self.classifiers.append(weak_classifier)             # Almacenar el clasificador débil
            self.alphas.append(alpha)                            # Almacenar el peso del clasificador

            weights *= np.exp(-alpha * y * predictions)  # Actualizar los pesos de las instancias

            # Normalizar los pesos
            weights /= np.sum(weights)

    def predict(self, X):
        classifier_predictions = np.array([classifier.predict(X) for classifier in self.classifiers])
        weighted_predictions = np.dot(self.alphas, classifier_predictions)
        return np.sign(weighted_predictions)

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
    y = np.array([-1, -1, -1, 1, 1, 1])

    # Crear y entrenar el modelo de Boosting
    model = Boosting(num_classifiers=5)
    model.fit(X, y)

    # Predecir y mostrar resultados
    print("Predictions:", model.predict(X))

#----------------------------------------------------------------------
# - WeakClassifier: Define un clasificador débil que simplemente compara una característica con un umbral y devuelve -1 o 1.
# - Boosting: Define la clase de Boosting que entrena varios clasificadores débiles y combina sus predicciones ponderadas para hacer una predicción final.
# - fit: Método para entrenar el modelo. En cada iteración, se entrena un clasificador débil, se calcula el error ponderado y se actualizan los pesos de las instancias.
# - predict: Método para hacer predicciones. Combina las predicciones de todos los clasificadores débiles ponderadas por sus pesos.
#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El algoritmo de Naïve-Bayes es un método de clasificación supervisada que se basa en el teorema de Bayes con una fuerte suposición de 
# independencia condicional entre las características. Se utiliza para predecir la clase de un objeto en función de las características observadas del objeto.

# El algoritmo de Naïve-Bayes se basa en el teorema de Bayes, que establece la relación entre la probabilidad condicional de dos eventos dados
# y sus probabilidades marginales.
#--------------- PROGRAMA --------------------------------------
import numpy as np

class NaiveBayes:
    def __init__(self):
        self.class_probs = None
        self.feature_probs = None

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)
        n_classes = len(self.classes)

        # Calcular la probabilidad a priori de cada clase
        self.class_probs = np.zeros(n_classes)
        for i, c in enumerate(self.classes):
            self.class_probs[i] = np.sum(y == c) / float(n_samples)

        # Calcular la probabilidad condicional de cada característica dada la clase
        self.feature_probs = np.zeros((n_classes, n_features))
        for i, c in enumerate(self.classes):
            X_c = X[y == c]
            self.feature_probs[i] = (X_c.sum(axis=0) + 1) / (np.sum(X_c) + n_features)

    def predict(self, X):
        predictions = []
        for x in X:
            # Calcular la probabilidad posterior de cada clase dado el ejemplo x
            posteriors = []
            for i, c in enumerate(self.classes):
                likelihood = np.prod(self.feature_probs[i] ** x * (1 - self.feature_probs[i]) ** (1 - x))
                posterior = self.class_probs[i] * likelihood
                posteriors.append(posterior)
            # Predecir la clase con la probabilidad posterior más alta
            predictions.append(self.classes[np.argmax(posteriors)])
        return predictions

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo
    X_train = np.array([[1, 0, 1], [0, 1, 1], [1, 1, 1], [0, 1, 0], [1, 1, 0]])
    y_train = np.array([0, 1, 0, 1, 0])
    X_test = np.array([[1, 0, 0], [0, 1, 1]])

    # Inicializar y ajustar el modelo Naive Bayes
    model = NaiveBayes()
    model.fit(X_train, y_train)

    # Realizar predicciones sobre datos de prueba
    predictions = model.predict(X_test)

    # Imprimir las predicciones
    print("Predicciones:", predictions)

#---------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias, como numpy.
# 2.- Definimos una clase NaiveBayes que contendrá los métodos fit y predict para entrenar y realizar predicciones con el modelo Naïve-Bayes.
# 3.- En el método fit, calculamos las probabilidades a priori de las clases y las probabilidades condicionales de las características dadas las clases.
# 4.- En el método predict, utilizamos las probabilidades calculadas para realizar predicciones sobre nuevos datos.
# 5.- En el bloque de código principal, creamos datos de ejemplo, inicializamos y ajustamos el modelo Naïve-Bayes y realizamos predicciones sobre los datos de prueba.
# 6.- Imprimimos las predicciones.
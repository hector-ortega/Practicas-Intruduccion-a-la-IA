#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Perceptrón:
# El Perceptrón es un algoritmo de aprendizaje supervisado para clasificación de datos linealmente separables. 
# Utiliza una función de activación escalón unitario para determinar la clase de una muestra. Aquí está cómo funciona:

# 1.-Inicialización de pesos: Inicializa los pesos y el sesgo a cero o pequeños valores aleatorios.
# 2.- Iteración: Itera sobre el conjunto de datos de entrenamiento y ajusta los pesos basados en el error de clasificación.
# 3.- Función de activación: Utiliza una función de activación escalón unitario para clasificar las muestras. Si la suma ponderada de las 
#     características de entrada y los pesos más el sesgo es mayor o igual que cero, clasifica la muestra como una clase (1), de lo contrario, 
#     como la otra clase (-1).
# 4.- Actualización de pesos: Actualiza los pesos en función de la tasa de aprendizaje y el error de clasificación. Los pesos se ajustan para
#     reducir el error durante el entrenamiento.

# El Perceptrón puede clasificar muestras en dos clases y encontrar un hiperplano que separa las clases si son linealmente separables.

# ADALINE (Adaptive Linear Neuron):

# ADALINE es una versión mejorada del Perceptrón que utiliza una función de activación lineal y una regla de aprendizaje 
# basada en el descenso de gradiente. Aquí está cómo funciona:

# 1.- Inicialización de pesos: Inicializa los pesos y el sesgo a cero o valores aleatorios pequeños.
# 2.- Iteración: Itera sobre el conjunto de datos de entrenamiento y ajusta los pesos basados en el error cuadrático medio.
# 3.- Función de activación: Utiliza una función de activación lineal que produce una salida proporcional a la suma ponderada de 
#     las características de entrada y los pesos más el sesgo.
# 4.- Actualización de pesos: Utiliza el descenso de gradiente para ajustar los pesos y el sesgo para minimizar el error cuadrático medio.
#     Los pesos se ajustan en la dirección opuesta al gradiente de la función de costo.

# ADALINE puede clasificar muestras en múltiples clases y encontrar un hiperplano óptimo que minimiza el error cuadrático medio.

# MADALINE (Many Adalines):
# MADALINE es una red neuronal de una sola capa que consta de múltiples ADALINE conectados en paralelo.
# Cada ADALINE calcula una salida y luego estas salidas se combinan para obtener la salida final. Aquí está cómo funciona:

# 1.- Inicialización de pesos: Inicializa los pesos y el sesgo de cada ADALINE a cero o valores aleatorios pequeños.
# 2.- Iteración: Itera sobre el conjunto de datos de entrenamiento y ajusta los pesos de cada ADALINE basados en el error cuadrático medio.
# 3.- Función de activación: Cada ADALINE utiliza una función de activación lineal que produce una salida proporcional a la suma ponderada 
#     de las características de entrada y los pesos más el sesgo.
# 4.- Combinación de salidas: Combina las salidas de todos los ADALINE para obtener la salida final. Esto puede hacerse mediante la suma de 
#     las salidas ponderadas o mediante una función de activación adicional.
#--------------- PROGRAMA --------------------------------------
import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.errors = []

        for _ in range(self.n_iterations):
            error = 0
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update
                error += int(update != 0.0)
            self.errors.append(error)
        return self

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)


class Adaline:
    def __init__(self, learning_rate=0.01, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.cost = []

        for _ in range(self.n_iterations):
            output = self.net_input(X)
            errors = (y - output)
            self.weights[1:] += self.learning_rate * X.T.dot(errors)
            self.weights[0] += self.learning_rate * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def activation(self, X):
        return X

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


class Madaline:
    def __init__(self, learning_rate=0.01, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        self.weights = np.zeros(1 + X.shape[1])
        self.errors = []

        for _ in range(self.n_iterations):
            error = 0
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update
                error += int(update != 0.0)
            self.errors.append(error)
        return self

    def net_input(self, X):
        return np.dot(X, self.weights[1:]) + self.weights[0]

    def activation(self, X):
        return X

    def predict(self, X):
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)


# Ejemplo de uso de los algoritmos

# Datos de ejemplo
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y = np.array([-1, -1, 1, 1])

# Crear y entrenar el Perceptron
perceptron = Perceptron(learning_rate=0.1, n_iterations=10)
perceptron.fit(X, y)
print("Pesos del Perceptron:", perceptron.weights)

# Crear y entrenar ADALINE
adaline = Adaline(learning_rate=0.01, n_iterations=100)
adaline.fit(X, y)
print("Pesos de ADALINE:", adaline.weights)

# Crear y entrenar MADALINE
madaline = Madaline(learning_rate=0.1, n_iterations=10)
madaline.fit(X, y)
print("Pesos de MADALINE:", madaline.weights)
#--------------------------------------------------------------------------------------------
# 1.- Perceptron: Implementamos el algoritmo del Perceptron, que es un clasificador lineal. Entrenamos el modelo ajustando los pesos 
#   iterativamente 
#   para minimizar los errores de clasificación.
# 2.- Adaline: Implementamos el algoritmo de Adaline (Adaptive Linear Neuron), que es una versión mejorada del Perceptron. Adaline utiliza una
#     función de activación lineal y ajusta los pesos para minimizar el error cuadrático medio.
# 3.- Madaline: Implementamos el algoritmo de MADALINE (Many Adalines), que es una red neuronal de una sola capa que consta de múltiples
#     Adalines conectados en paralelo. Cada Adaline calcula una salida y luego estas salidas se combinan para obtener la salida final.
# 4.- Ejemplo de uso: Creamos datos de ejemplo y entrenamos cada algoritmo con esos datos. Luego, imprimimos los pesos aprendidos por cada modelo.
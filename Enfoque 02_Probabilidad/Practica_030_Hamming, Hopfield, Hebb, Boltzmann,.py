#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# 1.- Algoritmo de Hamming: Se utiliza para calcular la distancia de Hamming entre dos secuencias binarias. Esta distancia mide
#     el número de posiciones en las que las secuencias difieren.
# 2.- Red de Hopfield: Es un tipo de red neuronal recurrente utilizada para el almacenamiento y recuperación de patrones. Los patrones
#     se almacenan como vectores de pesos sinápticos y la red se entrena para converger a estos patrones cuando se le presenta una entrada.
# 3.- Regla de Hebb: Es un principio de aprendizaje asociativo que establece que la fuerza de una conexión sináptica entre dos neuronas se
#     incrementa si ambas neuronas se activan simultáneamente.
# 4.- Máquina de Boltzmann: Es un tipo de red neuronal estocástica que utiliza el principio de máxima entropía para modelar la
#     distribución de probabilidad de un conjunto de datos. Se utiliza en problemas de optimización y modelado generativo.
#--------------- PROGRAMA --------------------------------------
import numpy as np

class NeuralNetwork:
    def __init__(self, size):
        """
        Inicializa una red neuronal con el tamaño dado.

        Args:
        size (int): El número de neuronas en la red.
        """
        self.size = size
        self.weights = np.zeros((size, size))  # Inicializa la matriz de pesos sinápticos

    def hamming_distance(self, seq1, seq2):
        """
        Calcula la distancia de Hamming entre dos secuencias binarias.

        Args:
        seq1 (array): Primera secuencia binaria.
        seq2 (array): Segunda secuencia binaria.

        Returns:
        int: La distancia de Hamming entre las dos secuencias.
        """
        if len(seq1) != len(seq2):
            raise ValueError("Las secuencias deben tener la misma longitud.")

        distance = 0
        for bit1, bit2 in zip(seq1, seq2):
            if bit1 != bit2:
                distance += 1
        return distance

    def train_hopfield(self, patterns):
        """
        Entrena una red de Hopfield con un conjunto de patrones.

        Args:
        patterns (array): Una matriz donde cada fila es un patrón.

        Returns:
        array: La matriz de pesos sinápticos entrenada.
        """
        num_patterns = len(patterns)
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern) / self.size
        return self.weights

    def hebb_rule(self, input_vector):
        """
        Aplica la regla de Hebb para actualizar la matriz de pesos sinápticos.

        Args:
        input_vector (array): El vector de entrada.

        Returns:
        array: La matriz de pesos sinápticos actualizada.
        """
        return np.outer(input_vector, input_vector)

    def boltzmann_machine(self, data, learning_rate=0.1, epochs=100):
        """
        Entrena una máquina de Boltzmann usando el método de Monte Carlo.

        Args:
        data (array): Los datos de entrada.
        learning_rate (float): La tasa de aprendizaje.
        epochs (int): El número de épocas de entrenamiento.

        Returns:
        array: La matriz de pesos sinápticos entrenada.
        """
        num_data, input_size = data.shape
        weights = np.random.randn(input_size, input_size)  # Inicializa los pesos sinápticos aleatoriamente

        for _ in range(epochs):
            for i in range(num_data):
                sample = data[i]
                for _ in range(10):  # Realiza 10 pasos de actualización de Gibbs por cada muestra
                    neuron = np.random.randint(0, input_size)
                    activation = np.dot(weights[neuron], sample)
                    sample[neuron] = 1 if activation > 0 else -1
                weights += learning_rate * np.outer(sample, sample)

        return weights

# Ejemplo de uso
network = NeuralNetwork(size=4)
seq1 = np.array([1, 0, 1, 0])
seq2 = np.array([0, 1, 0, 1])
print("Distancia de Hamming entre las secuencias:", network.hamming_distance(seq1, seq2))

patterns = np.array([[1, 1, -1, -1],
                     [-1, 1, -1, 1],
                     [-1, -1, 1, 1]])
print("Matriz de pesos sinápticos de la red de Hopfield:")
print(network.train_hopfield(patterns))

input_vector = np.array([1, 0, 1, 0])
print("Matriz de pesos sinápticos después de aplicar la regla de Hebb:")
print(network.hebb_rule(input_vector))

data = np.array([[1, 1, 1, 1],
                 [-1, -1, -1, -1],
                 [1, -1, 1, -1]])
print("Matriz de pesos sinápticos de la máquina de Boltzmann:")
print(network.boltzmann_machine(data))
#------------------------------------------------------------------------------------------------

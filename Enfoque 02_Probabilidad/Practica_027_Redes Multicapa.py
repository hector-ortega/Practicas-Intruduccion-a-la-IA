#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Funcionamiento:
# 1.- Propagación hacia adelante (Forward Propagation): Durante esta fase, los datos de entrada se propagan a través de la red capa por capa.
#     Cada neurona en una capa está conectada a todas las neuronas de la capa siguiente mediante pesos. En cada neurona, se calcula una suma 
#     ponderada de las entradas, seguida de la aplicación de una función de activación no lineal, como la función sigmoide, tangente hiperbólica
#     o ReLU.
# 2.- Retropropagación (Backpropagation): Una vez que se ha realizado la propagación hacia adelante y se han generado las predicciones,
#      se calcula el error entre las predicciones y las etiquetas verdaderas utilizando una función de pérdida, como el error cuadrático medio.   
#     Luego, este error se propaga hacia atrás a través de la red, ajustando los pesos y sesgos en cada capa para minimizar el error utilizando 
#     el algoritmo de optimización, como el descenso del gradiente estocástico (SGD) o algoritmos más avanzados como Adam o RMSProp.
# 3.- Entrenamiento: Durante el proceso de entrenamiento, se repite el proceso de propagación hacia adelante y retropropagación a lo largo de
#     múltiples épocas, ajustando gradualmente los pesos y sesgos de la red para mejorar el rendimiento en los datos de entrenamiento.
# 4.- Validación y Evaluación: Una vez entrenada la red, se evalúa su rendimiento en un conjunto de datos de validación o prueba para verificar 
#     su capacidad para generalizar a datos no vistos.
#--------------- PROGRAMA --------------------------------------
import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Inicializamos los pesos y sesgos aleatorios para las capas oculta y de salida
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    def sigmoid(self, x):
        # Función de activación sigmoide
        return 1 / (1 + np.exp(-x))

    def forward(self, X):
        # Propagación hacia adelante a través de la red
        self.hidden_output = self.sigmoid(np.dot(X, self.weights_input_hidden) + self.bias_hidden)
        self.predictions = self.sigmoid(np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output)
        return self.predictions

    def backward(self, X, y, learning_rate):
        # Retropropagación a través de la red para actualizar los pesos y sesgos
        output_error = y - self.predictions
        output_delta = output_error * (self.predictions * (1 - self.predictions))
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * (self.hidden_output * (1 - self.hidden_output))

        self.weights_hidden_output += learning_rate * np.dot(self.hidden_output.T, output_delta)
        self.bias_output += learning_rate * np.sum(output_delta, axis=0, keepdims=True)
        self.weights_input_hidden += learning_rate * np.dot(X.T, hidden_delta)
        self.bias_hidden += learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

    def train(self, X, y, epochs, learning_rate):
        # Entrenamiento de la red durante un número determinado de épocas
        for epoch in range(epochs):
            predictions = self.forward(X)
            self.backward(X, y, learning_rate)
            if epoch % 100 == 0:
                loss = np.mean(np.square(y - predictions))
                print(f'Epoch {epoch}: Loss = {loss}')

# Ejemplo de uso
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Features
y = np.array([[0], [1], [1], [0]])  # Etiquetas

# Inicializamos la red neuronal con 2 neuronas en la capa oculta
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Entrenamos la red durante 1000 épocas con una tasa de aprendizaje de 0.1
nn.train(X, y, epochs=1000, learning_rate=0.1)

# Probamos la red con nuevos datos
new_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predictions = nn.forward(new_data)
print("Predictions:")
print(predictions)
#-----------------------------------------------------------------------------------------------
# 1.- La clase NeuralNetwork representa la red neuronal. En su inicialización, se definen los pesos y sesgos aleatorios para las capas oculta 
#     y de salida.
# 2.- La función sigmoid es la función de activación sigmoide, que se utiliza para introducir no linealidad en la red.
# 3.- La función sigmoid_derivative calcula la derivada de la función sigmoide, que es necesaria durante el proceso de retropropagación.
# 4.- El método forward realiza la propagación hacia adelante a través de la red, calculando las salidas de las capas oculta y de salida.
# 5.- El método backward realiza la retropropagación a través de la red para actualizar los pesos y sesgos utilizando el algoritmo de
#     retropropagación del error.
# 6.- El método train entrena la red durante un número determinado de épocas, imprimiendo el valor de pérdida (loss) cada cierto número de épocas.
# 7.- Se crea una instancia de la red neuronal (nn) y se la entrena con los datos de entrada (X) y las etiquetas (y).
# 8.- Finalmente, se realizan predicciones utilizando la red entrenada con nuevos datos (new_data). Las predicciones se imprimen en la consola.
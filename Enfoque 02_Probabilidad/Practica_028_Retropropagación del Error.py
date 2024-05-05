#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# La retropropagación del error, o backpropagation en inglés, es un algoritmo fundamental en el entrenamiento de redes neuronales artificiales, 
# especialmente en redes neuronales multicapa. Su objetivo es ajustar los pesos de la red para minimizar una función de pérdida, que mide la 
# discrepancia entre las salidas predichas por la red y las salidas reales esperadas.

# Funcionamiento:
# 1.- Propagación hacia adelante (Forward Propagation):
# - Durante esta fase, los datos de entrada se propagan a través de la red desde la capa de entrada hasta la capa de salida.
# - En cada capa, se calculan las activaciones utilizando las funciones de activación asociadas a cada neurona.
# - Las activaciones se propagan hacia adelante capa por capa hasta obtener las predicciones de la red.

# 2.- Cálculo de la pérdida (Loss Calculation):
# - Una vez que se obtienen las predicciones de la red, se calcula la pérdida, que es una medida de la discrepancia entre las predicciones y 
#     las etiquetas reales.

# 3.- Retropropagación del error (Backward Propagation):
# - En esta fase, el algoritmo calcula el gradiente de la función de pérdida con respecto a los pesos de la red.
# - Este cálculo se realiza utilizando el algoritmo de la cadena, que permite calcular la contribución de cada peso en la pérdida final.
# - El gradiente calculado se utiliza luego para ajustar los pesos de la red utilizando un algoritmo de optimización como el descenso de gradiente.

# 4.- Actualización de los pesos (Weights Update):
# - Una vez que se ha calculado el gradiente de la función de pérdida con respecto a los pesos, se utilizan los valores del gradiente para
#     actualizar los pesos de la red.
# - Este proceso se repite iterativamente durante múltiples épocas de entrenamiento hasta que la red converge a una solución óptima o
#     hasta que se alcanza un número máximo de épocas.
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

    def sigmoid_derivative(self, x):
        # Derivada de la función sigmoide
        return x * (1 - x)

    def forward(self, X):
        # Propagación hacia adelante a través de la red
        self.hidden_output = self.sigmoid(np.dot(X, self.weights_input_hidden) + self.bias_hidden)
        self.predictions = self.sigmoid(np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output)
        return self.predictions

    def backward(self, X, y, learning_rate):
        # Retropropagación a través de la red para actualizar los pesos y sesgos
        output_error = y - self.predictions
        output_delta = output_error * self.sigmoid_derivative(self.predictions)
        
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_output)
        
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
#1.- La clase NeuralNetwork representa la red neuronal. En su inicialización, se definen los pesos y sesgos aleatorios para las capas oculta 
#   y de salida.
#2.- La función sigmoid es la función de activación sigmoide, que se utiliza para introducir no linealidad en la red.
#3.- La función sigmoid_derivative calcula la derivada de la función sigmoide, que es necesaria durante el proceso de retropropagación.
#4.- El método forward realiza la propagación hacia adelante a través de la red, calculando las salidas de las capas oculta y de salida.
#5.- El método backward realiza la retropropagación a través de la red para actualizar los pesos y sesgos utilizando el algoritmo de 
#    retropropagación del error.
#6.- El método train entrena la red durante un número determinado de épocas, imprimiendo el valor de pérdida (loss) cada cierto número de épocas.
#7.- Se crea una instancia de la red neuronal (nn) y se la entrena con los datos de entrada (X) y las etiquetas (y).
#8.- Finalmente, se realizan predicciones utilizando la red entrenada con nuevos datos (new_data). Las predicciones se imprimen en la consola.
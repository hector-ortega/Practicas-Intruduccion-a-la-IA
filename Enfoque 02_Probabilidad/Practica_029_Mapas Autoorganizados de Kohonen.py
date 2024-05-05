#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# Los Mapas Autoorganizados de Kohonen (SOM, por sus siglas en inglés) son una técnica de aprendizaje no supervisado utilizada para la 
# reducción de dimensionalidad, visualización de datos y clustering. Fueron desarrollados por el científico finlandés Teuvo Kohonen en 
# la década de 1980.

# Funcionamiento:
# 1.- Inicialización de pesos: Los pesos de las neuronas en el mapa SOM se inicializan aleatoriamente.
# 2.- Presentación de datos: Los datos de entrada se presentan al SOM de manera secuencial o en lotes.
# 3.- Competencia: Para cada dato de entrada, se encuentra la neurona ganadora o BMU (Best Matching Unit) que tiene los pesos más 
#     cercanos al dato de entrada.
# 4.- Actualización de pesos: Los pesos de las neuronas se actualizan para moverse más cerca del dato de entrada. Las neuronas cercanas a 
#     la BMU también se actualizan, pero en menor medida, lo que permite que la estructura del mapa se ajuste para reflejar la distribución 
#     de los datos.
# 5.- Aprendizaje competitivo: A medida que se presentan más datos, el mapa SOM se ajusta gradualmente para representar la distribución de 
#     los datos de entrada.
# 6.- Convergencia: Después de un número de iteraciones (o épocas), el mapa SOM converge hacia una representación estable de los datos de entrada.
#--------------- PROGRAMA --------------------------------------
import numpy as np
import matplotlib.pyplot as plt

class SOM:
    def __init__(self, input_dim, output_dim, learning_rate=0.1, sigma=1.0):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.learning_rate = learning_rate
        self.sigma = sigma
        self.weights = np.random.rand(output_dim[0], output_dim[1], input_dim)

    def train(self, data, epochs):
        for epoch in range(epochs):
            for i, x in enumerate(data):
                bmu = self.find_best_matching_unit(x)
                self.update_weights(x, bmu, epoch, len(data))

    def find_best_matching_unit(self, x):
        min_dist = np.inf
        bmu = (0, 0)
        for i in range(self.output_dim[0]):
            for j in range(self.output_dim[1]):
                w = self.weights[i, j]
                dist = np.linalg.norm(x - w)
                if dist < min_dist:
                    min_dist = dist
                    bmu = (i, j)
        return bmu

    def update_weights(self, x, bmu, epoch, num_data):
        for i in range(self.output_dim[0]):
            for j in range(self.output_dim[1]):
                w = self.weights[i, j]
                dist_to_bmu = np.linalg.norm(np.array(bmu) - np.array([i, j]))
                lr = self.learning_rate * (1 - epoch / num_data)
                theta = np.exp(-dist_to_bmu**2 / (2 * self.sigma**2))
                self.weights[i, j] = w + lr * theta * (x - w)

    def predict(self, data):
        predictions = []
        for x in data:
            bmu = self.find_best_matching_unit(x)
            predictions.append(bmu)
        return predictions

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de ejemplo (2D)
    data = np.array([[1, 2], [5, 6], [2, 2], [8, 9], [1, 7], [9, 1]])
    
    # Configuración de la red SOM
    input_dim = 2  # Dimension de entrada
    output_dim = (5, 5)  # Dimension de la cuadricula de neuronas
    epochs = 100  # Numero de epocas
    learning_rate = 0.1  # Tasa de aprendizaje
    sigma = 1.0  # Sigma para calcular el vecindario
    
    # Crear y entrenar la red SOM
    som = SOM(input_dim, output_dim, learning_rate, sigma)
    som.train(data, epochs)
    
    # Obtener las predicciones de la red
    predictions = som.predict(data)
    
    # Visualizar los resultados
    plt.scatter(data[:,0], data[:,1], color='blue')
    for pred in predictions:
        plt.scatter(pred[0], pred[1], color='red', marker='x')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Mapas Autoorganizados de Kohonen')
    plt.grid(True)
    plt.show()
#------------------------------------------------------------------------------------------------
# 1.- Clase SOM:
# - Creamos una clase llamada SOM que implementa el algoritmo de Mapas Autoorganizados de Kohonen.
# - El constructor __init__ inicializa los parámetros de la red SOM, como las dimensiones de entrada y salida, la tasa de aprendizaje y el radio sigma.
# - train es el método para entrenar la red SOM con los datos de entrada.
# 2.- Método find_best_matching_unit:
# - Este método busca la mejor unidad de coincidencia para un vector de entrada dado.
# 3.- Método update_weights:
# - Este método actualiza los pesos de la red SOM utilizando el algoritmo de Kohonen.
# 4.- Método predict:
# - Realiza predicciones utilizando la red SOM entrenada.
# 5.- Ejemplo de uso:
# Creamos una instancia de la clase SOM con los parámetros deseados.
# Entrenamos la red SOM con datos de ejemplo.
# Obtenemos predicciones utilizando la red entrenada.
# Visualizamos los resultados.
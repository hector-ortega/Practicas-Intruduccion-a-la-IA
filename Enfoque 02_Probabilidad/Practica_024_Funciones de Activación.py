#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Funcionamiento de las Funciones de Activación:
# 1.- Sigmoide: La función sigmoide transforma los valores de entrada a un rango entre 0 y 1, lo que la hace útil para problemas de 
# clasificación binaria donde se necesita una salida en forma de probabilidad.
# 2.- ReLU (Rectified Linear Unit): La función ReLU devuelve 0 para valores de entrada negativos y el mismo valor de entrada para valores positivos. 
# Es simple y eficaz, y se usa comúnmente en las capas ocultas de las redes neuronales.Función: 
# angente Hiperbólica (Tanh): La función tanh mapea los valores de entrada a un rango entre -1 y 1. Es similar a la función sigmoide pero centrada 
# en cero, lo que la hace más adecuada para la convergencia en el entrenamiento.Función: 
#--------------- PROGRAMA --------------------------------------
import numpy as np

# Definimos las funciones de activación

def sigmoid(x):
    """
    Función sigmoide: mapea los valores de entrada a un rango entre 0 y 1.
    """
    return 1 / (1 + np.exp(-x))

def relu(x):
    """
    Función ReLU (Rectified Linear Unit): devuelve x si x > 0, 0 en caso contrario.
    """
    return np.maximum(0, x)

def tanh(x):
    """
    Función Tangente Hiperbólica (Tanh): mapea los valores de entrada a un rango entre -1 y 1.
    """
    return np.tanh(x)


# Ejemplo de uso de las funciones de activación

# Definimos un array de entrada
x = np.array([-2, -1, 0, 1, 2])

# Calculamos las salidas utilizando cada función de activación
sigmoid_output = sigmoid(x)
relu_output = relu(x)
tanh_output = tanh(x)

# Imprimimos los resultados
print("Entrada:", x)
print("Salida de la función sigmoide:", sigmoid_output)
print("Salida de la función ReLU:", relu_output)
print("Salida de la función Tangente Hiperbólica:", tanh_output)
#--------------------------------------------------------------------------------------------
# 1.- Definición de las funciones de activación: Implementamos tres funciones de activación comunes: sigmoide, ReLU y tangente hiperbólica.
#     Cada función toma como entrada un array de números y aplica la operación correspondiente para calcular la salida.
# 2.- Ejemplo de uso de las funciones de activación: Definimos un array de entrada x con algunos valores para probar las funciones de activación. 
#     Luego, calculamos las salidas utilizando cada función de activación.
# 3.- Impresión de los resultados: Imprimimos los valores de entrada y las salidas de cada función de activación para ver cómo transforman los 
#     valores de entrada.

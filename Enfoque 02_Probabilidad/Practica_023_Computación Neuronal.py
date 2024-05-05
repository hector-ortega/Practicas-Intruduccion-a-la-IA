#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# La "Computación Neuronal" se refiere al procesamiento de información inspirado en el funcionamiento del cerebro humano, particularmente 
# en la forma en que las neuronas se comunican entre sí. Los algoritmos de computación neuronal, también conocidos como modelos neuronales
# o redes neuronales, son una clase de modelos de aprendizaje automático que intentan emular el comportamiento de las redes neuronales biológicas
# para realizar tareas de inteligencia artificial.

# Un algoritmo de computación neuronal utiliza una estructura de red formada por "neuronas" artificiales interconectadas para procesar datos. 
# Cada neurona toma una o más entradas, las combina linealmente mediante la aplicación de pesos, y luego aplica una función de activación no 
# lineal para producir una salida. La salida de una neurona puede ser utilizada como entrada para otras neuronas en la red.

# El proceso de entrenamiento de una red neuronal implica ajustar los pesos de cada neurona de la red para minimizar una función de pérdida,
# que mide la diferencia entre las salidas predichas por la red y las salidas reales del conjunto de datos de entrenamiento. Esto se logra
# utilizando algoritmos de optimización como el descenso del gradiente estocástico (SGD) o variantes más avanzadas como Adam.

# Una vez que la red neuronal ha sido entrenada, puede ser utilizada para realizar una variedad de tareas, como clasificación, regresión,
# generación de imágenes y texto, reconocimiento de patrones, entre otras.
#--------------- PROGRAMA --------------------------------------
# Paso 1: Importar las bibliotecas necesarias
import numpy as np

# Paso 2: Definir la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Paso 3: Definir los datos de entrada
# Supongamos que tenemos 3 características de entrada para un solo ejemplo
x = np.array([0.5, 0.3, 0.2])

# Paso 4: Definir los pesos y el sesgo de la neurona
# Inicializamos los pesos de forma aleatoria y el sesgo como cero
weights = np.random.rand(3)  # 3 pesos para cada característica
bias = 0

# Paso 5: Calcular la suma ponderada de las entradas
weighted_sum = np.dot(x, weights) + bias

# Paso 6: Aplicar la función de activación sigmoide
output = sigmoid(weighted_sum)

# Paso 7: Imprimir el resultado
print("El resultado de la neurona es:", output)
#--------------------------------------------------------------------------------------------
# 1.- Importar las bibliotecas necesarias: Importamos NumPy para realizar cálculos numéricos eficientes.
# 2.- Definir la función de activación sigmoide: La función sigmoid(x) calcula la salida de una neurona utilizando 
#     la función de activación sigmoide, que mapea cualquier valor real a un rango entre 0 y 1.
# 3.- Definir los datos de entrada: Definimos un ejemplo de entrada con 3 características.
# 4.- Definir los pesos y el sesgo de la neurona: Inicializamos los pesos de manera aleatoria y el sesgo como cero.
#     Estos valores son los parámetros que la neurona aprenderá durante el entrenamiento.
# 5.- Calcular la suma ponderada de las entradas: Calculamos la suma ponderada de las entradas multiplicando cada característica 
#     por su peso correspondiente y sumando el sesgo.
# 6.- Aplicar la función de activación sigmoide: Pasamos la suma ponderada a través de la función de activación sigmoide para obtener 
#     la salida de la neurona.
# 7.- Imprimir el resultado: Imprimimos la salida de la neurona.
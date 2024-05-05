#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# Utilización del Algoritmo Hacia Delante-Atrás:
# El algoritmo Hacia Delante-Atrás funciona en dos etapas principales:

# - Paso hacia adelante (Forward Step):
# En esta etapa, se calcula la probabilidad de estar en cada estado en cada instante de tiempo dado las observaciones hasta ese momento.
# Se utilizan las observaciones y la matriz de transición de estado para calcular estas probabilidades utilizando la recursión hacia adelante.
# - Paso hacia atrás (Backward Step):
# En esta etapa, se calcula la probabilidad de observar las observaciones futuras dada cada estado en cada instante de tiempo.
# Se utilizan las observaciones y la matriz de transición de estado para calcular estas probabilidades utilizando la recursión hacia atrás.

# Finalmente, se combinan los resultados de los pasos hacia adelante y hacia atrás para obtener la distribución de probabilidad posterior 
# de estados para cada instante de tiempo. Esta distribución proporciona información sobre la probabilidad de estar en cada estado en cada momento,
# dada la secuencia completa de observaciones.
#--------------- PROGRAMA ------------------------------------
import numpy as np

def forward_backward(observaciones, A, B, pi):
    """
    Implementación del algoritmo Hacia Delante-Atrás.
    
    Argumentos:
    - observaciones: Secuencia de observaciones.
    - A: Matriz de transición de estado.
    - B: Matriz de emisión.
    - pi: Distribución inicial de estado.
    
    Retorna:
    - gamma: Distribución de probabilidad posterior de estados para cada instante de tiempo.
    """
    T = len(observaciones)  # Número de pasos de tiempo
    N = A.shape[0]  # Número de estados
    
    # Paso hacia adelante
    alpha = np.zeros((T, N))  # Inicialización de la matriz de avance
    alpha[0] = pi * B[:, observaciones[0]]  # Inicialización del primer paso
    for t in range(1, T):
        alpha[t] = np.dot(alpha[t - 1], A) * B[:, observaciones[t]]
    
    # Paso hacia atrás
    beta = np.zeros((T, N))  # Inicialización de la matriz de retroceso
    beta[-1] = 1  # Inicialización del último paso
    for t in range(T - 2, -1, -1):
        beta[t] = np.dot(A, B[:, observaciones[t + 1]] * beta[t + 1])
    
    # Cálculo de la distribución de probabilidad posterior de estados
    gamma = alpha * beta
    gamma /= np.sum(gamma, axis=1, keepdims=True)  # Normalización
    
    return gamma

# Definición de parámetros del modelo HMM
A = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición de estado
B = np.array([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])  # Matriz de emisión
pi = np.array([0.6, 0.4])  # Distribución inicial de estado

# Secuencia de observaciones
observaciones = [0, 1, 2, 1, 0]

# Aplicación del algoritmo Hacia Delante-Atrás
gamma = forward_backward(observaciones, A, B, pi)

# Impresión de la distribución de probabilidad posterior de estados
print("Distribución de probabilidad posterior de estados:")
print(gamma)

#---------------------------------------------------------------------------------
# 1.- Definición de la función forward_backward: Esta función implementa el algoritmo Hacia Delante-Atrás. Toma como entrada la secuencia de observaciones,
#     la matriz de transición de estado A, la matriz de emisión B y la distribución inicial de estado pi. Devuelve la distribución de probabilidad posterior de
#     estados para cada instante de tiempo.
# 2.- Paso hacia adelante: En este paso, calculamos la probabilidad de estar en cada estado en cada instante de tiempo dada la secuencia de observaciones
#     hasta ese momento. Utilizamos la recursión hacia adelante para calcular estas probabilidades.
# 3.- Paso hacia atrás: En este paso, calculamos la probabilidad de observar las observaciones futuras dada cada estado en cada instante de tiempo.
#     Utilizamos la recursión hacia atrás para calcular estas probabilidades.
# 4.- Cálculo de la distribución de probabilidad posterior de estados: Combinamos la información de los pasos hacia adelante y hacia atrás para obtener la
#     distribución de probabilidad posterior de estados para cada instante de tiempo.
# 5.- Definición de parámetros del modelo HMM: Definimos la matriz de transición de estado A, la matriz de emisión B y la distribución inicial de estado pi.
# 6.- Secuencia de observaciones: Definimos una secuencia de observaciones para utilizar en la aplicación del algoritmo.
# 7.- Aplicación del algoritmo Hacia Delante-Atrás: Llamamos a la función forward_backward con las observaciones y los parámetros del modelo HMM.
# 8.- Impresión de la distribución de probabilidad posterior de estados: Imprimimos la distribución de probabilidad posterior de estados calculada por el algoritmo.
#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# La Hipótesis de Markov, en el contexto de los Procesos de Markov, es una suposición fundamental que establece que el futuro comportamiento de un sistema 
# estocástico depende únicamente del estado presente y no de la secuencia de eventos pasados que llevaron a ese estado. En otras palabras, dado el estado presente, 
# el futuro del sistema es independiente de cómo se llegó a ese estado.

# Funcionamiento de un Algoritmo de Procesos de Markov:
# 1.- Definición de Estados y Transiciones: En primer lugar, se define un conjunto de estados posibles para el sistema y las probabilidades de transición entre 
#     estos estados. Esto se puede representar mediante una matriz de transición, donde cada entrada indica la probabilidad de transición de un estado a otro.
# 2.- Simulación del Proceso: Se simula el proceso de Markov comenzando desde un estado inicial dado. En cada paso, se elige el próximo estado basado en las  
#     probabilidades de transición desde el estado actual.
# 3.- Análisis y Predicción: Una vez que se ha simulado el proceso, se pueden realizar análisis y predicciones sobre el comportamiento futuro del sistema. 
#     Esto puede incluir calcular la probabilidad de llegar a ciertos estados en un número dado de pasos, identificar patrones de comportamiento, etc.
#--------------- PROGRAMA ------------------------------------
import numpy as np

# Definimos la matriz de transición de estados
matriz_transicion = np.array([[0.7, 0.3],  # Probabilidades de transición del estado 0 al 0 y al 1
                               [0.4, 0.6]]) # Probabilidades de transición del estado 1 al 0 y al 1

# Definimos la función para simular el proceso de Markov
def simular_proceso_markov(inicial, num_pasos):
    estado_actual = inicial
    estados_simulados = [estado_actual]
    
    for _ in range(num_pasos):
        # Determinamos el próximo estado basado en la matriz de transición y el estado actual
        proximo_estado = np.random.choice([0, 1], p=matriz_transicion[estado_actual])
        estados_simulados.append(proximo_estado)
        estado_actual = proximo_estado
    
    return estados_simulados

# Estado inicial (0 o 1)
estado_inicial = 0
# Número de pasos en la simulación
num_pasos = 10

# Simulamos el proceso de Markov
estados_simulados = simular_proceso_markov(estado_inicial, num_pasos)

# Imprimimos los estados simulados
print("Estados simulados del proceso de Markov:")
print(estados_simulados)
#-------------------------------------------------------------------

# 1.- Definición de la Matriz de Transición: La matriz matriz_transicion representa las probabilidades de transición entre los estados del proceso de Markov. 
#     En este ejemplo, hemos definido una matriz de 2x2 donde cada fila representa las probabilidades de transición desde un estado hacia los otros dos posibles estados.
# 2.- Función simular_proceso_markov: Esta función simula el proceso de Markov dado un estado inicial y un número de pasos. Iteramos a través de cada paso y en cada paso 
#     determinamos el próximo estado basado en la matriz de transición y el estado actual. Utilizamos np.random.choice para seleccionar aleatoriamente el 
#     próximo estado basado en las probabilidades de transición.
# 3.- Simulación del Proceso de Markov: Simulamos el proceso de Markov llamando a la función simular_proceso_markov con el estado inicial y el número de pasos
#     especificados.
# 4.- Impresión de los Estados Simulados: Imprimimos los estados simulados del proceso de Markov para verificar que la simulación haya funcionado correctamente.
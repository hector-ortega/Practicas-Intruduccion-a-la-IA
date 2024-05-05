#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------

# Los Modelos Ocultos de Markov (HMM, por sus siglas en inglés) son herramientas poderosas utilizadas en una variedad de aplicaciones en inteligencia artificial,
# procesamiento de señales, bioinformática y más. Se utilizan para modelar sistemas estocásticos secuenciales donde hay incertidumbre sobre el estado del sistema
# en cada momento, pero se pueden observar algunas señales relacionadas con el estado.

# Funcionamiento de los Modelos Ocultos de Markov:
# 1.- Estados Ocultos: Un HMM consiste en una serie de estados ocultos que el sistema puede estar en cualquier momento. Estos estados son desconocidos 
#     y no observables directamente.
# 2.- Observaciones: En cada estado, el sistema emite una observación observable. La observación puede ser discreta (como palabras en el habla) o continua
#     (como valores de sensores).
# 3.- Transiciones de Estado: El sistema cambia de un estado a otro con ciertas probabilidades de transición. Estas probabilidades están definidas por una
#     matriz de transición de estado.
# 4.- Emisiones de Observación: Cuando el sistema está en un estado, emite una observación con cierta probabilidad. Estas probabilidades están definidas por 
#     una matriz de emisión.
# 5.- Secuencia de Observaciones: Dada una secuencia de observaciones, el objetivo es inferir la secuencia de estados más probable que generó esas observaciones.
# 6.- Algoritmos de Inferencia: Existen varios algoritmos para resolver problemas relacionados con los HMM, como el algoritmo de Viterbi para la decodificación 
#     de secuencias más probables, el algoritmo de hacia adelante para calcular la probabilidad de una secuencia dada y el algoritmo de hacia adelante-atrás para el suavizado y la estimación de la probabilidad de estados en cada momento dado una secuencia completa de observaciones.
#--------------- PROGRAMA ------------------------------------
import numpy as np

class HiddenMarkovModel:
    def __init__(self, states, observations, transition_probs, emission_probs, initial_probs):
        """
        Inicializa el Modelo Oculto de Markov (HMM) con los parámetros especificados.
        
        Argumentos:
        - states: Lista de estados posibles del modelo.
        - observations: Lista de observaciones posibles del modelo.
        - transition_probs: Matriz de probabilidades de transición entre estados.
        - emission_probs: Matriz de probabilidades de emisión de observaciones dada cada estado.
        - initial_probs: Distribución de probabilidad inicial de los estados.
        """
        self.states = states
        self.observations = observations
        self.transition_probs = transition_probs
        self.emission_probs = emission_probs
        self.initial_probs = initial_probs
    
    def forward(self, observations):
        """
        Calcula las probabilidades hacia adelante (forward) para la secuencia de observaciones dada.
        
        Argumentos:
        - observations: Lista de observaciones.
        
        Retorna:
        - forward_probs: Matriz de probabilidades hacia adelante.
        """
        T = len(observations)
        N = len(self.states)
        
        forward_probs = np.zeros((T, N))
        forward_probs[0] = self.initial_probs * self.emission_probs[:, observations[0]]
        
        for t in range(1, T):
            for j in range(N):
                forward_probs[t, j] = np.sum(forward_probs[t - 1] * self.transition_probs[:, j]) * self.emission_probs[j, observations[t]]
        
        return forward_probs
    
    def backward(self, observations):
        """
        Calcula las probabilidades hacia atrás (backward) para la secuencia de observaciones dada.
        
        Argumentos:
        - observations: Lista de observaciones.
        
        Retorna:
        - backward_probs: Matriz de probabilidades hacia atrás.
        """
        T = len(observations)
        N = len(self.states)
        
        backward_probs = np.zeros((T, N))
        backward_probs[-1] = 1
        
        for t in range(T - 2, -1, -1):
            for i in range(N):
                backward_probs[t, i] = np.sum(self.transition_probs[i, :] * self.emission_probs[:, observations[t + 1]] * backward_probs[t + 1])
        
        return backward_probs
    
    def forward_backward(self, observations):
        """
        Calcula las probabilidades hacia adelante y hacia atrás para la secuencia de observaciones dada.
        
        Argumentos:
        - observations: Lista de observaciones.
        
        Retorna:
        - forward_probs: Matriz de probabilidades hacia adelante.
        - backward_probs: Matriz de probabilidades hacia atrás.
        """
        forward_probs = self.forward(observations)
        backward_probs = self.backward(observations)
        
        return forward_probs, backward_probs

# Ejemplo de uso
states = ['Sunny', 'Rainy']
observations = ['Dry', 'Dry', 'Wet']
transition_probs = np.array([[0.8, 0.2], [0.3, 0.7]])
emission_probs = np.array([[0.4, 0.6], [0.6, 0.4]])
initial_probs = np.array([0.6, 0.4])

hmm = HiddenMarkovModel(states, observations, transition_probs, emission_probs, initial_probs)

# Calcula las probabilidades hacia adelante y hacia atrás
forward_probs, backward_probs = hmm.forward_backward([0, 0, 1])

print("Probabilidades hacia adelante:")
print(forward_probs)
print("\nProbabilidades hacia atrás:")
print(backward_probs)
#--------------------------------------------------------------------------------------
# 1.- Definición de la clase HiddenMarkovModel: Creamos una clase que representa un Modelo Oculto de Markov. Esta clase contiene métodos para calcular 
#     las probabilidades hacia adelante, hacia atrás y combinadas.
# 2.- Método __init__: Este método inicializa un objeto HMM con los parámetros especificados: estados posibles, observaciones posibles, probabilidades 
#     de transición, probabilidades de emisión y distribución inicial de estados.
# 3.- Método forward: Calcula las probabilidades hacia adelante para una secuencia de observaciones dada utilizando el algoritmo de avance.
# 4.- Método backward: Calcula las probabilidades hacia atrás para una secuencia de observaciones dada utilizando el algoritmo de retroceso.
# 5.- Método forward_backward: Calcula las probabilidades hacia adelante y hacia atrás para una secuencia de observaciones dada utilizando los métodos 
#     forward y backward.
# 6.- Ejemplo de uso: Creamos una instancia de la clase HiddenMarkovModel con parámetros de ejemplo y calculamos las probabilidades hacia adelante y 
#     hacia atrás para una secuencia de observaciones dada. Luego, imprimimos los resultados en la consola.
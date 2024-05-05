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
from hmmlearn import hmm
import numpy as np

# Definir los posibles estados del clima
states = ["Soleado", "Nublado", "Lluvioso"]
n_states = len(states)

# Definir las observaciones (llevar paraguas: Sí o No)
observations = ["Sí", "No"]
n_observations = len(observations)

# Crear el modelo de HMM
model = hmm.MultinomialHMM(n_components=n_states)

# Probabilidades iniciales de los estados del clima
model.startprob_ = np.array([0.3, 0.4, 0.3])

# Matriz de transición: probabilidad de cambiar de un estado a otro
model.transmat_ = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.1, 0.3, 0.6]
])

# Probabilidades de observación para cada estado del clima
model.emissionprob_ = np.array([
    [0.7, 0.3],
    [0.4, 0.6],
    [0.2, 0.8]
])

# Secuencia de observaciones
observations_sequence = np.array([[1, 0, 1, 1, 0]]).T  # "No", "Sí", "No", "No", "Sí"

# Entrenar el modelo con la secuencia de observaciones
model.fit(observations_sequence)

# Predecir la secuencia de estados del clima
predicted_states = model.predict(observations_sequence)

# Mapear los estados predichos a su significado
predicted_states_labels = [states[state] for state in predicted_states]

print("Secuencia de observaciones:", [observations[o] for o in observations_sequence.ravel()])
print("Secuencia de estados predichos:", predicted_states_labels)
#--------------------------------------------------------------------------------------
# 1.- Importamos las bibliotecas necesarias: hmmlearn para el modelo HMM y numpy para manipular matrices eficientemente.
# 2.- Definimos los posibles estados del clima y las observaciones.
# 3.- Creamos el modelo de HMM con tres estados (soleado, nublado, lluvioso).
# 4.- Especificamos las probabilidades iniciales de los estados del clima.
# 5.- Definimos la matriz de transición, que especifica las probabilidades de cambiar de un estado a otro.
# 6.- Especificamos las probabilidades de observación para cada estado del clima.
# 7.- Creamos una secuencia de observaciones para entrenar el modelo.
# 8.- Entrenamos el modelo con la secuencia de observaciones.
# 9.- Predecimos la secuencia de estados del clima basados en las observaciones.
# 10.- Convertimos los estados predichos a sus etiquetas correspondientes.
# 11.- Imprimimos la secuencia de observaciones y la secuencia de estados predichos.
#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------


#--------------- PROGRAMA ------------------------------------
import numpy as np

class DynamicBayesianNetwork:
    def __init__(self, graph, initial_state_probs, transition_probs, emission_probs):
        self.graph = graph  # Grafo que representa la DBN
        self.initial_state_probs = initial_state_probs  # Probabilidades iniciales del estado oculto
        self.transition_probs = transition_probs  # Probabilidades de transición entre estados ocultos
        self.emission_probs = emission_probs  # Probabilidades de emisión de las observaciones

    def belief_propagation(self, observations):
        num_states = len(self.graph)
        belief_state = self.initial_state_probs.copy()  # Inicializamos el estado de creencias con las probabilidades iniciales

        # Actualizamos el estado de creencias para cada observación
        for obs in observations:
            # Actualizamos el estado de creencias utilizando las probabilidades de transición y emisión
            for state in range(num_states):
                belief_state[state] *= self.emission_probs[state, obs]
                for parent_state in self.graph[state]:
                    belief_state[state] *= self.transition_probs[parent_state, state]

            # Normalizamos el estado de creencias para que sume 1
            belief_state /= np.sum(belief_state)

        return belief_state

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos la estructura del grafo, probabilidades iniciales, de transición y de emisión
    graph = {0: [1], 1: [2], 2: [0]}  # Ejemplo de grafo: nodo 0 -> nodo 1 -> nodo 2
    initial_state_probs = np.array([0.6, 0.4, 0.0])  # Probabilidades iniciales del estado oculto
    transition_probs = np.array([[0.7, 0.3, 0.0],  # Probabilidades de transición entre estados ocultos
                                 [0.2, 0.7, 0.1],
                                 [0.0, 0.1, 0.9]])
    emission_probs = np.array([[0.9, 0.1],  # Probabilidades de emisión de las observaciones para cada estado oculto
                                [0.2, 0.8],
                                [0.6, 0.4]])

    # Creamos una instancia de DynamicBayesianNetwork
    dbn = DynamicBayesianNetwork(graph, initial_state_probs, transition_probs, emission_probs)

    # Ejecutamos el algoritmo de propagación de creencias para obtener la distribución de probabilidad del estado oculto
    observations = [0, 1, 0]  # Ejemplo de observaciones
    belief_state = dbn.belief_propagation(observations)
    print("Distribución de probabilidad del estado oculto:", belief_state)
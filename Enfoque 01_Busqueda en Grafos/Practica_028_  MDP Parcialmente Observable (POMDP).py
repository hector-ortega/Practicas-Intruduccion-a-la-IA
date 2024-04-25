#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de MDP Parcialmente Observable (POMDP) es una técnica de búsqueda utilizada en inteligencia artificial 
# para resolver problemas en los que un agente debe tomar decisiones en un entorno incierto y parcialmente observable.
#--------------- PROGRAMA ------------------------------------
import numpy as np

class GraphSearchPOMDP:
    def __init__(self, graph, actions, observations, transition_model, observation_model, reward_model, discount_factor):
        self.graph = graph  # Grafo que representa el espacio de estados
        self.actions = actions  # Lista de acciones disponibles
        self.observations = observations  # Lista de observaciones posibles
        self.transition_model = transition_model  # Modelo de transición: P(s'|s, a)
        self.observation_model = observation_model  # Modelo de observación: P(o|s', a)
        self.reward_model = reward_model  # Modelo de recompensa: R(s, a)
        self.discount_factor = discount_factor  # Factor de descuento γ

    def value_iteration(self, max_iterations=100, tolerance=1e-6):
        num_states = len(self.graph)
        num_actions = len(self.actions)
        num_observations = len(self.observations)

        # Inicializamos el valor de cada estado a 0
        V = np.zeros(num_states)
        for _ in range(max_iterations):
            V_new = np.zeros(num_states)
            for s in range(num_states):
                # Calculamos el valor para cada acción
                action_values = np.zeros(num_actions)
                for a in range(num_actions):
                    # Sumamos las recompensas esperadas de todas las observaciones posibles
                    for o in range(num_observations):
                        # Calculamos la expectativa de la recompensa futura
                        expected_reward = self.reward_model[s, a]
                        for s_prime in range(num_states):
                            expected_reward += self.transition_model[s_prime, s, a] * \
                                               V[s_prime] * \
                                               self.observation_model[s_prime, o, a]
                        action_values[a] += self.observations[o] * action_values[a]
                # Actualizamos el valor del estado como el máximo de los valores de las acciones
                V_new[s] = np.max(action_values)
            # Comprobamos si el cambio en los valores es menor que la tolerancia
            if np.max(np.abs(V_new - V)) < tolerance:
                break
            V = V_new
        return V

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el grafo, acciones, observaciones y modelos
    graph = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])  # Ejemplo de grafo (matriz de adyacencia)
    actions = ['accion1', 'accion2', 'accion3']  # Ejemplo de lista de acciones disponibles
    observations = ['obs1', 'obs2', 'obs3']  # Ejemplo de lista de observaciones posibles
    transition_model = np.zeros((len(graph), len(graph), len(actions)))  # Modelo de transición: P(s'|s, a)
    observation_model = np.zeros((len(graph), len(observations), len(actions)))  # Modelo de observación: P(o|s', a)
    reward_model = np.zeros((len(graph), len(actions)))  # Modelo de recompensa: R(s, a)
    discount_factor = 0.9  # Factor de descuento γ

    # Creamos una instancia de GraphSearchPOMDP
    pomdp_solver = GraphSearchPOMDP(graph, actions, observations, transition_model, observation_model, reward_model, discount_factor)

    # Ejecutamos el algoritmo de Value Iteration
    optimal_values = pomdp_solver.value_iteration()
    print("Valores óptimos:", optimal_values)
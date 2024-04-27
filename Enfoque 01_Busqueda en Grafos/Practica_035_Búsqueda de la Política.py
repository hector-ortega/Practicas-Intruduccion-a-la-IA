#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El aprendizaje de búsqueda de política es un enfoque fundamental en el campo del aprendizaje por refuerzo. 
# Su objetivo es encontrar la mejor política, es decir, la mejor manera de comportarse en cada estado de un entorno, 
# de modo que se maximice la recompensa total a largo plazo. La política define la estrategia que el agente debe seguir para tomar decisiones 
# óptimas en cada paso, lo que a su vez determina la secuencia de acciones que el agente debe tomar en función del estado actual del entorno.

# ¿Cómo funciona?
# El proceso de búsqueda de política implica generalmente dos pasos principales:

# Evaluación de la política: En este paso, se evalúa la política actual para determinar su calidad. Esto se hace calculando los valores
# de estado para cada estado del entorno. Los valores de estado representan la recompensa esperada que el agente puede obtener si sigue 
# la política desde ese estado. Este proceso se realiza iterativamente hasta que los valores de estado convergen.
# Mejora de la política: Una vez que se han calculado los valores de estado, se utiliza esta información para mejorar la política. 
# Esto implica revisar la política actual y actualizarla de manera que se elijan las acciones que maximicen el valor de estado
# esperado en cada estado. Este proceso se repite iterativamente hasta que la política converge a la política óptima.
#--------------- PROGRAMA ------------------------------------
import numpy as np

class PolicyIteration:
    def __init__(self, num_states, num_actions, transition_probs, rewards, discount_factor):
        """
        Constructor de la clase PolicyIteration.

        Args:
            num_states (int): Número de estados en el entorno.
            num_actions (int): Número de acciones posibles.
            transition_probs (numpy array): Matriz de transición de probabilidades.
            rewards (numpy array): Matriz de recompensas para cada estado.
            discount_factor (float): Factor de descuento γ.
        """
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_probs = transition_probs
        self.rewards = rewards
        self.discount_factor = discount_factor

        # Inicializamos la política aleatoriamente
        self.policy = np.random.randint(0, num_actions, size=num_states)

    def evaluate_policy(self):
        """
        Método para evaluar la política actual y calcular los valores de estado V.
        
        Returns:
            numpy array: Valores de estado V para la política actual.
        """
        V = np.zeros(self.num_states)  # Inicializamos los valores de estado a cero

        # Iteramos hasta que los valores de estado converjan
        while True:
            prev_V = np.copy(V)
            for s in range(self.num_states):
                # Calculamos el valor de estado para el estado s según la política actual
                action = self.policy[s]
                V[s] = np.sum(self.transition_probs[s, action] * (self.rewards[s, action] + self.discount_factor * prev_V))

            # Si los valores de estado convergen, salimos del bucle
            if np.all(np.isclose(V, prev_V)):
                break

        return V

    def improve_policy(self, V):
        """
        Método para mejorar la política basada en los valores de estado V.
        
        Args:
            V (numpy array): Valores de estado para la política actual.
        """
        for s in range(self.num_states):
            # Calculamos los valores Q para todas las acciones en el estado s
            Q = np.zeros(self.num_actions)
            for a in range(self.num_actions):
                Q[a] = np.sum(self.transition_probs[s, a] * (self.rewards[s, a] + self.discount_factor * V))

            # Mejoramos la política seleccionando la acción con el mayor valor Q
            self.policy[s] = np.argmax(Q)

    def policy_iteration(self, max_iterations=1000):
        """
        Método para realizar la iteración de política.

        Args:
            max_iterations (int): Número máximo de iteraciones permitidas.
        
        Returns:
            numpy array: Política óptima encontrada.
        """
        for i in range(max_iterations):
            # Evaluar la política actual
            V = self.evaluate_policy()

            # Mejorar la política basada en los valores de estado
            self.improve_policy(V)

        return self.policy

# Definir el entorno (grafo) con transiciones de estado y recompensas
num_states = 5
num_actions = 2
transition_probs = np.array([
    [[0.7, 0.3], [0.4, 0.6], [0.2, 0.8], [0.1, 0.9], [0.0, 1.0]],
    [[0.3, 0.7], [0.6, 0.4], [0.8, 0.2], [0.9, 0.1], [1.0, 0.0]],
    [[0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0], [0.0, 1.0]],
    [[1.0, 0.0], [1.0, 0.0], [1.0, 0.0], [1.0, 0.0], [1.0, 0.0]],
    [[1.0, 0.0], [1.0, 0.0], [1.0, 0.0], [1.0, 0.0], [1.0, 0.0]]
])
rewards = np.array([
    [[10, 0], [0, 0], [0, 0], [0, 0], [0, -50]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [-50, 10]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
])
discount_factor = 0.9

# Crear instancia del agente de iteración de política
agent = PolicyIteration(num_states, num_actions, transition_probs, rewards, discount_factor)

# Realizar la iteración de política para encontrar la política óptima
optimal_policy = agent.policy_iteration()

# Imprimir la política óptima encontrada
print("Política óptima encontrada:")
print(optimal_policy)

#------------------------------------------------------------------------------------------------------------------------------
# 1.-Importamos la biblioteca numpy para realizar cálculos numéricos eficientes.
# 2.-Definimos la clase PolicyIteration, que representa el agente que realiza la búsqueda de política en el grafo. 
# En el constructor __init__, inicializamos los parámetros del entorno, como el número de estados, el número de acciones, 
# las probabilidades de transición y las recompensas.
# 3.-Implementamos el método evaluate_policy para evaluar la política actual y calcular los valores de estado V.
# 4.-Implementamos el método improve_policy para mejorar la política basada en los valores de estado  V.
# 5.-Implementamos el método policy_iteration para realizar la iteración de política, que consiste en iterativamente 
# evaluar y mejorar la política hasta que se encuentra la política óptima.
# 6.-Definimos el entorno (grafo) con transiciones de estado y recompensas.
# 7.-Creamos una instancia del agente PolicyIteration con los parámetros del entorno.
# 8.-Realizamos la iteración de política para encontrar la política óptima.
# 9.-Imprimimos la política óptima encontrada.
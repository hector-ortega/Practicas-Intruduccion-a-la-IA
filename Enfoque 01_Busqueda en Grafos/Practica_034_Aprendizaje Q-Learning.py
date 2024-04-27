#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo Q-Learning es un método de aprendizaje por refuerzo que permite a un agente aprender una política óptima para tomar decisiones secuenciales en un entorno.
# Es especialmente útil en entornos donde las acciones del agente afectan directamente al estado futuro del entorno y donde no se dispone de un modelo explícito
# del entorno.

# ¿Cómo funciona?
# Tabla Q: El corazón del algoritmo Q-Learning es la tabla Q, que es una matriz que almacena el valor de cada par estado-acción. El valor Q representa la "calidad"
# de una acción en un estado dado, es decir, cuánto valor espera el agente recibir en el futuro si toma esa acción en ese estado.
# Inicialización: La tabla Q se inicializa con valores arbitrarios o a cero para todos los pares estado-acción.
# Exploración vs. Explotación: Durante la fase de entrenamiento, el agente selecciona acciones basadas en una política de exploración y explotación. 
# La exploración implica seleccionar acciones aleatorias para descubrir nuevos estados y acciones, mientras que la explotación implica seleccionar 
# la acción con el mayor valor Q conocido para un estado dado.
# Actualización de la tabla Q: Después de tomar una acción y observar el siguiente estado y la recompensa recibida, el agente actualiza el valor 
# Q correspondiente utilizando la regla de actualización de Q-Learning

#--------------- PROGRAMA ------------------------------------
import numpy as np

class QLearning:
    def __init__(self, num_states, num_actions, learning_rate, discount_factor, exploration_rate):
        """
        Constructor de la clase QLearning.
        
        Args:
            num_states (int): Número de estados en el entorno.
            num_actions (int): Número de acciones posibles.
            learning_rate (float): Tasa de aprendizaje α.
            discount_factor (float): Factor de descuento γ.
            exploration_rate (float): Tasa de exploración ε para la política ε-greedy.
        """
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        # Inicializamos la tabla Q con valores arbitrarios
        self.Q_table = np.zeros((num_states, num_actions))

    def select_action(self, state):
        """
        Método para seleccionar una acción usando la política ε-greedy.
        
        Args:
            state (int): Estado actual del agente.
        
        Returns:
            int: Acción seleccionada por el agente.
        """
        if np.random.uniform(0, 1) < self.exploration_rate:
            # Exploración: seleccionamos una acción aleatoria
            return np.random.choice(self.num_actions)
        else:
            # Explotación: seleccionamos la acción con el valor Q más alto para el estado actual
            return np.argmax(self.Q_table[state])

    def update_Q_table(self, state, action, reward, next_state):
        """
        Método para actualizar la tabla Q utilizando el algoritmo Q-Learning.
        
        Args:
            state (int): Estado actual del agente.
            action (int): Acción tomada por el agente.
            reward (float): Recompensa recibida por tomar la acción en el estado actual.
            next_state (int): Próximo estado del agente después de tomar la acción.
        """
        best_next_action = np.argmax(self.Q_table[next_state])
        self.Q_table[state, action] += self.learning_rate * (
                reward + self.discount_factor * self.Q_table[next_state, best_next_action] - self.Q_table[state, action])

# Crear instancia del agente de aprendizaje Q-Learning
num_states = 5  # Número de estados en el entorno
num_actions = 3  # Número de acciones posibles
learning_rate = 0.1  # Tasa de aprendizaje α
discount_factor = 0.9  # Factor de descuento γ
exploration_rate = 0.1  # Tasa de exploración ε

agent = QLearning(num_states, num_actions, learning_rate, discount_factor, exploration_rate)

# Ejemplo de interacción del agente con el entorno
for episode in range(100):
    # Estado inicial
    state = np.random.randint(0, num_states)
    total_reward = 0

    # Ejecutar un episodio
    for step in range(10):  # 10 pasos en cada episodio
        # Seleccionar acción
        action = agent.select_action(state)

        # Simular la acción en el entorno
        # Supongamos que el entorno devuelve una recompensa aleatoria entre -1 y 1
        reward = np.random.uniform(-1, 1)

        # Próximo estado (aleatorio en este ejemplo)
        next_state = np.random.randint(0, num_states)

        # Actualizar la tabla Q
        agent.update_Q_table(state, action, reward, next_state)

        total_reward += reward
        state = next_state

    print("Episodio:", episode, "Recompensa total:", total_reward)

# Imprimir la tabla Q después del entrenamiento
print("Tabla Q después del entrenamiento:")
print(agent.Q_table)
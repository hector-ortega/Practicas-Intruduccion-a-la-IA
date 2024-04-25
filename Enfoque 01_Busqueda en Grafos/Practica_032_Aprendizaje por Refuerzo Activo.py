#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# El Aprendizaje por Refuerzo Activo es una rama del aprendizaje automático en la que un agente interactúa con un entorno para aprender
# a realizar acciones que maximicen alguna forma de recompensa acumulada a lo largo del tiempo. Este enfoque es particularmente útil en 
# situaciones en las que el agente no tiene acceso a un conjunto de datos predefinido, sino que debe explorar y aprender de la interacción 
# directa con el entorno.

# ¿Cómo funciona?
# El Aprendizaje por Refuerzo Activo se basa en un proceso de toma de decisiones secuenciales. Aquí hay una descripción general de cómo funciona:

# Agente: El agente es el sistema de inteligencia artificial que aprende a realizar acciones en un entorno dado.
# Entorno: Es el mundo con el que interactúa el agente. El entorno podría ser un juego, un simulador físico, un robot en el mundo real, etc.
# Estado: El estado representa la situación actual del entorno en un momento dado. El agente toma decisiones basadas en el estado actual.

# Acción: Son las acciones que el agente puede realizar en respuesta a un estado dado. El objetivo del agente es aprender la mejor acción
# a tomar en cada estado para maximizar su recompensa acumulada.

# Recompensa: Es una señal de retroalimentación que el entorno proporciona al agente después de que realiza una acción en un estado particular. 
# La recompensa puede ser positiva, negativa o neutral, y su objetivo es guiar al agente hacia comportamientos deseable
#--------------- PROGRAMA ------------------------------------
import numpy as np

class ActiveRL:
    def __init__(self, num_states, num_actions, learning_rate, discount_factor, exploration_rate):
        """
        Constructor de la clase ActiveRL.
        
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

# Crear instancia del agente de aprendizaje por refuerzo activo
num_states = 5  # Número de estados en el entorno
num_actions = 3  # Número de acciones posibles
learning_rate = 0.1  # Tasa de aprendizaje α
discount_factor = 0.9  # Factor de descuento γ
exploration_rate = 0.1  # Tasa de exploración ε

agent = ActiveRL(num_states, num_actions, learning_rate, discount_factor, exploration_rate)

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
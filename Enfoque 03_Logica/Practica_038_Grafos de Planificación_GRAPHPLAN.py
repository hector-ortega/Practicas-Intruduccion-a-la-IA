#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo GRAPHPLAN es un algoritmo de planificación utilizado en inteligencia artificial para encontrar secuencias de acciones que
# permitan alcanzar un estado objetivo a partir de un estado inicial en un entorno determinado. Fue propuesto por Blai Bonet y Héctor Geffner en 2001.

# Funcionamiento del algoritmo GRAPHPLAN:

# 1.- Representación del problema: El problema de planificación se representa mediante un conjunto de acciones posibles, un estado inicial y un estado objetivo.
# 2.- Creación del grafo de planificación: El algoritmo construye un grafo donde los nodos representan estados del mundo y las aristas representan acciones
#     que pueden transformar un estado en otro.
# 3.- Expansión del grafo: Se expande el grafo de planificación añadiendo nodos y aristas para representar los posibles estados y acciones.
# 4.- Búsqueda de soluciones: Se busca un plan que permita alcanzar el estado objetivo a partir del estado inicial. Esto se hace explorando el grafo de 
#     planificación y buscando una secuencia de acciones que conduzcan desde el estado inicial hasta el estado objetivo.
# 5.- Optimización del plan: En algunos casos, se puede aplicar técnicas de optimización para mejorar el plan encontrado, como la búsqueda de 
#     rutas más cortas o la eliminación de acciones redundantes.
#--------------- PROGRAMA ------------------------------------
from collections import defaultdict

class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name  # Nombre de la acción
        self.preconditions = preconditions  # Precondiciones necesarias para que la acción sea aplicable
        self.effects = effects  # Efectos de la acción sobre el estado del mundo

    def is_applicable(self, state):
        # Comprueba si todas las precondiciones de la acción están presentes en el estado actual
        return all(p in state for p in self.preconditions)

    def apply(self, state):
        # Aplica los efectos de la acción al estado actual si la acción es aplicable
        if self.is_applicable(state):
            return state.union(self.effects)  # Devuelve el nuevo estado
        else:
            return state  # Si la acción no es aplicable, el estado permanece sin cambios

class GraphPlan:
    def __init__(self, actions, initial_state, goal_state):
        self.actions = actions  # Lista de acciones disponibles
        self.initial_state = initial_state  # Estado inicial del mundo
        self.goal_state = goal_state  # Estado objetivo que se desea alcanzar
        self.levels = []  # Niveles del grafo de planificación

    def expand_graph(self, level):
        current_level = self.levels[level]  # Obtiene el nivel actual del grafo
        next_level = set()  # Inicializa el siguiente nivel del grafo

        # Itera sobre todas las acciones disponibles
        for action in self.actions:
            # Verifica si todas las precondiciones de la acción están presentes en el nivel actual
            if all(precondition in current_level for precondition in action.preconditions):
                next_level.add(action)  # Agrega la acción al siguiente nivel
                # Agrega los efectos de la acción al siguiente nivel
                self.levels[level + 1].add(action)
                for effect in action.effects:
                    self.levels[level + 1].add(effect)

        return next_level  # Devuelve el conjunto de acciones del siguiente nivel

    def extract_solution(self, level):
        # Verifica si el estado objetivo está presente en el último nivel del grafo
        if not self.goal_state.issubset(self.levels[level]):
            return None  # Si no está presente, no hay solución

        solution = []  # Lista para almacenar el plan de acciones
        current_state = self.goal_state.copy()  # Copia del estado objetivo
        # Itera desde el último nivel hasta el primer nivel del grafo
        for i in range(level, 0, -1):
            current_level = self.levels[i]  # Obtiene el nivel actual
            # Filtra las acciones aplicables en el nivel actual
            applicable_actions = [action for action in current_level if action.is_applicable(current_state)]
            # Selecciona cualquier acción aplicable (podrías querer mejorar esta selección)
            action = applicable_actions[0]
            solution.append(action.name)  # Agrega el nombre de la acción al plan
            current_state = action.preconditions.union(current_state)  # Actualiza el estado actual

        return solution[::-1]  # Devuelve el plan invertido para que esté en orden cronológico

    def find_plan(self):
        # Añade el estado inicial al primer nivel del grafo
        self.levels.append(self.initial_state)
        # Inicializa el siguiente nivel del grafo
        self.levels.append(set())

        level = 0  # Inicializa el nivel actual
        while True:
            next_level = self.expand_graph(level)  # Expande el grafo al siguiente nivel
            if not next_level:
                return None  # Si no hay acciones en el siguiente nivel, no hay solución
            elif self.goal_state.issubset(self.levels[level + 1]):
                return self.extract_solution(level + 1)  # Extrae el plan si el objetivo se alcanzó
            else:
                self.levels.append(set())  # Agrega un nuevo nivel al grafo
                level += 1  # Incrementa el nivel actual

# Definimos las acciones del problema
actions = [
    Action("agarrar_herramienta", {"sin_herramienta"}, {"con_herramienta"}),
    Action("usar_herramienta", {"con_herramienta"}, {"tarea_realizada"})
]

# Definimos el estado inicial y el estado objetivo
initial_state = {"sin_herramienta"}
goal_state = {"tarea_realizada"}

# Creamos una instancia de GraphPlan
planner = GraphPlan(actions, initial_state, goal_state)

# Encontramos el plan
plan = planner.find_plan()

# Imprimimos el plan encontrado
if plan:
    print("Plan encontrado:")
    for action in plan:
        print(action)
else:
    print("No se encontró un plan.")

#------------------------------------------------------------------------------
# Este código implementa el algoritmo GRAPHPLAN para la planificación de acciones. Primero, definimos la clase Action para representar las acciones del problema. 
# Luego, creamos la clase GraphPlan que implementa el algoritmo. Finalmente, definimos las acciones, el estado inicial y el estado objetivo del problema y 
# encontramos un plan utilizando el algoritmo GRAPHPLAN.
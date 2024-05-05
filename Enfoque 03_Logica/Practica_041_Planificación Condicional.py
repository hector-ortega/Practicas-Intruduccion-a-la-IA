#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La planificación condicional es un enfoque utilizado en inteligencia artificial para encontrar secuencias de acciones que permitan alcanzar ciertos
# objetivos, dadas ciertas condiciones iniciales y restricciones adicionales. Este enfoque es especialmente útil cuando las acciones que pueden llevarse
# a cabo dependen del estado actual del entorno y pueden tener efectos no deterministas.

# En un problema de planificación condicional, se definen los siguientes elementos:

# 1.- Acciones: Cada acción tiene precondiciones que deben cumplirse para que la acción pueda llevarse a cabo, así como 
#     efectos que se producen después de que la acción se ejecuta con éxito.
# 2.- Estado inicial: Especifica las condiciones iniciales del entorno en el que se va a planificar. Describe el estado del 
#     entorno antes de que se realice ninguna acción.
# 3.- Objetivos: Son las condiciones que se desean lograr al final del plan. Representan el estado del entorno que se desea alcanzar.

# El algoritmo de planificación condicional busca encontrar una secuencia de acciones que, cuando se ejecutan en el estado inicial,
# lleven al entorno desde ese estado hasta un estado en el que se cumplan todos los objetivos. Esto implica seleccionar las acciones 
# adecuadas en el momento adecuado, teniendo en cuenta las precondiciones de las acciones y los efectos que estas producen.
#--------------- PROGRAMA ------------------------------------

from collections import defaultdict


class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = {node: False for node in self.graph}
        stack = []
        for node in self.graph:
            if not visited[node]:
                self.dfs(node, visited, stack)
        return stack[::-1]


def is_goal_state(state, goals):
    return all(goal in state for goal in goals)


def apply_effects(state, effects):
    new_state = state.copy()
    for effect in effects:
        new_state.add(effect)
    return new_state


def plan(graph, initial_state, goals):
    ordered_actions = graph.topological_sort()
    state = initial_state
    plan = []

    for action_name in ordered_actions:
        action = actions[action_name]
        if all(precondition in state for precondition in action.preconditions):
            plan.append(action.name)
            state = apply_effects(state, action.effects)
        if is_goal_state(state, goals):
            return plan
    return None


# Definir las acciones y sus precondiciones y efectos
actions = {
    "action1": Action("action1", {"A"}, {"B"}),
    "action2": Action("action2", {"B"}, {"C"}),
    "action3": Action("action3", {"C"}, {"D"}),
    "action4": Action("action4", {"D"}, {"E"}),
}

# Definir las condiciones iniciales y los objetivos
initial_state = {"A"}
goals = {"E"}

# Construir el grafo de dependencias entre acciones
graph = Graph()
for action in actions.values():
    for precondition in action.preconditions:
        for effect in action.effects:
            graph.add_edge(precondition, effect)

# Encontrar un plan para lograr los objetivos desde el estado inicial
plan_result = plan(graph, initial_state, goals)

if plan_result:
    print("Plan encontrado:")
    print(plan_result)
else:
    print("No se encontró un plan para alcanzar los objetivos.")

#---------------------------------------------------------------
# 1.- Se define una clase Action para representar las acciones del plan, con atributos para el nombre, las precondiciones y los efectos de la acción.
# 2.- Se define una clase Graph para representar el grafo de dependencias entre las acciones.
# 3.- Se implementa una función is_goal_state para verificar si el estado actual cumple con todos los objetivos.
# 4.- Se implementa una función apply_effects para aplicar los efectos de una acción al estado actual.
# 5.- Se implementa la función plan que toma el grafo de dependencias, el estado inicial y los objetivos como entrada, 
#     y devuelve un plan que cumple con los objetivos, si es posible.
# 6.- Se definen las acciones, el estado inicial y los objetivos del problema.
# 7.- Se construye el grafo de dependencias entre acciones a partir de las precondiciones y efectos de las acciones.
# 8.- Se llama a la función plan para encontrar un plan que logre los objetivos desde el estado inicial.
# 9.- Se imprime el plan encontrado, si existe, o se muestra un mensaje indicando que no se encontró un plan.
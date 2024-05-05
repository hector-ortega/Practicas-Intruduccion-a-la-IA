#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los algoritmos de planificación, como STRIPS (Stanford Research Institute Problem Solver) y ADL (Action Description Language), 
# son herramientas esenciales en el campo de la inteligencia artificial para resolver problemas de planificación. Estos algoritmos se
# utilizan para generar secuencias de acciones que permiten alcanzar un objetivo deseado a partir de un estado inicial dado.

# STRIPS (Stanford Research Institute Problem Solver):
# STRIPS es uno de los algoritmos más conocidos y ampliamente utilizados en la planificación automatizada. Se basa en una representación 
# simbólica del problema de planificación, donde el mundo se modela como un conjunto de estados y acciones que transforman esos estados.
# La representación de estados se realiza mediante predicados lógicos que describen propiedades del mundo, mientras que las acciones se 
# definen mediante precondiciones (condiciones que deben ser verdaderas para que la acción pueda ejecutarse), efectos 
# (cómo cambian los estados cuando se ejecuta la acción) y costos (opcional).

# El algoritmo STRIPS funciona de la siguiente manera:

# 1.- Se define un estado inicial y un estado objetivo.
# 2.- Se especifican las acciones posibles con sus precondiciones y efectos.
# 3.- El algoritmo busca una secuencia de acciones que, cuando se aplican en el estado inicial, conduzcan al estado objetivo.
# 4.- Utiliza búsqueda heurística o búsqueda ciega para encontrar esta secuencia de acciones.

# ADL (Action Description Language):
# ADL es un lenguaje más expresivo que STRIPS para describir acciones en problemas de planificación. Permite condiciones y efectos más complejos,
# como la adición y eliminación de literales, y se puede utilizar para representar problemas de planificación más complejos.

# El algoritmo ADL funciona de manera similar a STRIPS, pero permite una representación más detallada y precisa de las acciones y los estados del mundo. 
# Esto permite modelar problemas de planificación más complejos y realistas.
#--------------- PROGRAMA ------------------------------------
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class State:
    def __init__(self, predicates):
        self.predicates = predicates

class Planner:
    def __init__(self, initial_state, goal_state, actions):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions

    def plan(self):
        plan = []
        current_state = self.initial_state

        while not self.satisfied(current_state, self.goal_state):
            applicable_actions = [action for action in self.actions if self.applicable(action, current_state)]
            chosen_action = self.choose_action(applicable_actions)
            plan.append(chosen_action)
            current_state = self.apply(chosen_action, current_state)

        return plan

    def satisfied(self, state, goal_state):
        return all(predicate in state.predicates for predicate in goal_state.predicates)

    def applicable(self, action, state):
        return all(predicate in state.predicates for predicate in action.preconditions)

    def apply(self, action, state):
        new_state_predicates = state.predicates.copy()
        for effect in action.effects:
            if effect[0] == '+':
                new_state_predicates.add(effect[1:])
            elif effect[0] == '-':
                new_state_predicates.remove(effect[1:])
        return State(new_state_predicates)

    def choose_action(self, applicable_actions):
        # En este ejemplo simple, simplemente elegimos la primera acción aplicable
        return applicable_actions[0]

# Definición de acciones
actions = [
    Action("move", {"at(robot, X)", "adjacent(X, Y)", "-at(robot, X)"}, {"+at(robot, Y)", "-at(robot, X)"}),
    Action("push", {"at(robot, X)", "at(box, X)", "adjacent(X, Y)", "empty(Y)"}, {"+at(box, Y)", "-at(box, X)", "+empty(X)", "-empty(Y)"})
]

# Definición del estado inicial y estado objetivo
initial_state = State({"at(robot, A)", "at(box, B)", "adjacent(A, B)", "empty(C)"})
goal_state = State({"at(robot, C)"})

# Creación del planificador y planificación
planner = Planner(initial_state, goal_state, actions)
plan = planner.plan()

# Impresión del plan generado
print("Plan:")
for action in plan:
    print(action.name)
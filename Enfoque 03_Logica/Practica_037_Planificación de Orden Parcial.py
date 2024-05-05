#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# Los algoritmos de planificación de orden parcial buscan encontrar un plan que logre el objetivo deseado, teniendo en cuenta las acciones disponibles, 
# sus precondiciones y efectos, así como el estado inicial y el estado objetivo del sistema.

# El proceso de planificación de orden parcial generalmente involucra los siguientes pasos:

# 1.- Definición del problema: Se define el estado inicial del sistema, el estado objetivo que se desea alcanzar y las acciones disponibles
#     que pueden cambiar el estado del sistema.
# 2.- Generación de acciones aplicables: Se identifican las acciones que pueden ser aplicadas en el estado actual, es decir, aquellas
#     cuyas precondiciones son satisfechas por el estado actual.
# 3.- Selección de acciones: Se elige una acción aplicable para ejecutar. Esto puede involucrar la consideración de varios criterios, como la relevancia
#     de la acción para alcanzar el objetivo, la eficiencia en la consecución del objetivo, entre otros.
# 4.- Ejecución de acciones y actualización del estado: Se ejecuta la acción seleccionada y se actualiza el estado del sistema de acuerdo con los efectos de la acción.
# 5.- Repetición del proceso: Se repiten los pasos anteriores hasta que se alcance el estado objetivo o se determine que no es posible alcanzarlo desde el estado actual.
#--------------- PROGRAMA ------------------------------------
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

class PartialOrderPlanner:
    def __init__(self, actions, initial_state, goal_state):
        self.actions = actions
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.plan = []

    def plan_order(self):
        while self.goal_state != self.initial_state:
            applicable_actions = []
            for action in self.actions:
                if self.applicable(action):
                    applicable_actions.append(action)

            chosen_action = self.choose_action(applicable_actions)
            self.execute_action(chosen_action)
            self.plan.append(chosen_action)

    def applicable(self, action):
        return all(cond in self.initial_state for cond in action.preconditions)

    def choose_action(self, applicable_actions):
        return applicable_actions[0]  # Aquí se podría implementar una estrategia de selección más sofisticada

    def execute_action(self, action):
        for effect in action.effects:
            self.initial_state.add(effect)
            if effect in self.goal_state:
                self.goal_state.remove(effect)

# Ejemplo de uso
initial_state = {'A', 'B'}
goal_state = {'C', 'D'}
actions = [
    Action('Action1', {'A'}, {'B'}),
    Action('Action2', {'B'}, {'C'}),
    Action('Action3', {'C'}, {'D'})
]

planner = PartialOrderPlanner(actions, initial_state, goal_state)
planner.plan_order()
print("Plan:", [action.name for action in planner.plan])

#-----------------------------------------------------------------------
# 1.- Definimos la clase Action, que representa una acción con nombre, precondiciones y efectos.
# 2.- Creamos la clase PartialOrderPlanner, que toma una lista de acciones, un estado inicial y un estado objetivo. 
#     También tiene un método plan_order() que busca el plan para alcanzar el estado objetivo desde el estado inicial.
# 3.- En el método plan_order(), iteramos hasta que el estado objetivo sea igual al estado inicial. En cada iteración, 
#     encontramos las acciones aplicables, elegimos una acción y la ejecutamos.
# 4.- El método applicable() verifica si una acción es aplicable en el estado actual.
# 5.- El método choose_action() elige una acción aplicable. En este ejemplo, simplemente elegimos la primera acción aplicable,
#     pero aquí podrías implementar una estrategia de selección más sofisticada.
# 6.- El método execute_action() ejecuta una acción actualizando el estado inicial y el estado objetivo.
# 7.- Finalmente, creamos un ejemplo de uso donde definimos un estado inicial, un estado objetivo y una lista de acciones.
#     Luego, creamos un planificador de orden parcial y ejecutamos el método plan_order(). Imprimimos el plan resultante.

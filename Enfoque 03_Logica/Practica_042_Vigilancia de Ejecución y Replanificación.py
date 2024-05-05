#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Vigilancia de Ejecución y Replanificación se utiliza en sistemas de inteligencia artificial para controlar 
# agentes autónomos que operan en entornos dinámicos y cambiantes. El objetivo principal de este algoritmo es permitir que un 
# agente realice tareas de forma autónoma, monitoreando continuamente su ejecución y replanificando su comportamiento cuando surgen 
# cambios en el entorno o en las condiciones de la tarea.

# El proceso típico de Vigilancia de Ejecución y Replanificación funciona de la siguiente manera:

# 1.- Planificación inicial: El agente comienza con un plan inicial que especifica una secuencia de acciones para lograr un objetivo
#     determinado. Este plan se crea antes de que el agente comience su ejecución.
# 2.- Ejecución del plan: El agente comienza a ejecutar el plan, moviéndose a través del entorno y realizando las acciones especificadas en el plan.
# 3.- Monitoreo continuo: Mientras el agente está ejecutando su plan, monitorea constantemente su entorno para detectar cambios. 
#     Estos cambios pueden incluir la aparición de obstáculos, cambios en las condiciones del entorno o eventos imprevistos.
# 4.- Detección de cambios: Si el agente detecta algún cambio que afecte su capacidad para completar la tarea según lo planeado, 
#     como la presencia de un obstáculo en su camino, interrumpe su ejecución actual y pasa al siguiente paso.
# 5.- Replanificación: Una vez que se detecta un cambio en el entorno, el agente debe replanificar su comportamiento para adaptarse 
#     a la nueva situación. Esto implica generar un nuevo plan que tenga en cuenta el cambio detectado y que permita al agente alcanzar
#     su objetivo de manera efectiva y segura.
# 6.- Ejecución del nuevo plan: Finalmente, el agente ejecuta el nuevo plan generado y continúa con su tarea.
#--------------- PROGRAMA ------------------------------------
class Environment:
    def __init__(self, size):
        self.size = size
        self.obstacles = set()  # Conjunto para almacenar las posiciones de los obstáculos

    def add_obstacle(self, position):
        """Añade un obstáculo a la posición dada."""
        self.obstacles.add(position)

    def is_obstacle(self, position):
        """Verifica si la posición dada es un obstáculo."""
        return position in self.obstacles

class Agent:
    def __init__(self, environment, start, goal):
        self.environment = environment
        self.position = start
        self.goal = goal
        self.plan = self.plan_route()  # Planifica la ruta inicial

    def plan_route(self):
        """Planifica la ruta inicial desde la posición inicial hasta el objetivo."""
        route = [self.position]  # Lista para almacenar la ruta
        # Simulación de la planificación de la ruta
        while route[-1] != self.goal:
            next_move = (route[-1][0] + 1, route[-1][1])  # Movimiento hacia adelante
            # Verifica si el siguiente movimiento está dentro del entorno y no es un obstáculo
            if next_move[0] < self.environment.size and not self.environment.is_obstacle(next_move):
                route.append(next_move)  # Agrega el siguiente movimiento a la ruta
            else:
                break  # Si el movimiento no es posible, termina la planificación
        return route

    def execute_plan(self):
        """Ejecuta el plan del agente."""
        for step in self.plan:
            print("Moving to:", step)  # Imprime el paso actual
            self.position = step  # Actualiza la posición del agente
            if self.position == self.goal:
                print("Goal reached!")  # Si el objetivo es alcanzado, imprime un mensaje y termina
                return
            if self.environment.is_obstacle(step):
                print("Obstacle detected! Replanning...")  # Si se detecta un obstáculo, imprime un mensaje
                self.plan = self.plan_route()  # Replanifica la ruta
                self.execute_plan()  # Ejecuta el nuevo plan
                return

# Crear un entorno y añadir obstáculos
env = Environment(5)
env.add_obstacle((2, 1))
env.add_obstacle((3, 1))
env.add_obstacle((3, 2))

# Crear un agente con posición inicial y objetivo
agent = Agent(env, (0, 0), (4, 4))

# Ejecutar el plan del agente
agent.execute_plan()

#.-------------------------------------------------------------

# 1.- Environment es una clase que representa el entorno del agente. Tiene un atributo size que indica el tamaño del entorno y un conjunto 
#     obstacles para almacenar las posiciones de los obstáculos.
# 2.- Agent es una clase que representa al agente. Almacena su posición actual, su objetivo y su plan de ruta. Tiene métodos para planificar 
#     la ruta inicial (plan_route) y ejecutar el plan (execute_plan).
# 3.- En el método execute_plan, el agente avanza paso a paso por su plan. Si encuentra un obstáculo en su camino, imprime un mensaje, 
#     replanifica su ruta y ejecuta el nuevo plan recursivamente.
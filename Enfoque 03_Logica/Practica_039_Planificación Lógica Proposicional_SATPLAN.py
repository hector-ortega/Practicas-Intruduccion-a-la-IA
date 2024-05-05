#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# SATPLAN es un algoritmo de planificación lógica proposicional que se utiliza para resolver problemas de planificación en inteligencia artificial. 
# En lugar de utilizar representaciones simbólicas complejas como en otros enfoques de planificación, SATPLAN convierte el problema de planificación
# en una fórmula proposicional en conjunción normal (CNF) y luego utiliza un solucionador SAT (Satisfiability) para encontrar una solución.

# ¿Cómo funciona SATPLAN?
# 1.- Codificación del problema: SATPLAN convierte el problema de planificación en una fórmula proposicional en CNF. Esto implica representar el estado 
#     inicial, las acciones posibles y el estado objetivo como variables proposicionales y cláusulas lógicas que describan las condiciones y efectos de las acciones.
# 2.- Creación de la fórmula CNF: Se crean cláusulas lógicas que codifican las condiciones previas y los efectos de cada acción, así como las restricciones
#     que deben cumplirse para alcanzar el estado objetivo.
# 3.- Resolución con un solucionador SAT: La fórmula CNF se pasa a un solucionador SAT, que intenta encontrar una asignación de verdad que satisfaga todas 
#     las cláusulas. Si se encuentra una solución, representa un plan válido para alcanzar el estado objetivo.
# 4.- Extracción del plan: Si el solucionador SAT encuentra una solución, se extrae el plan a partir de la asignación de verdad encontrada. 
#     El plan consiste en una secuencia de acciones que conducen desde el estado inicial hasta el estado objetivo.
# 5.- Verificación del plan: El plan encontrado se verifica para asegurarse de que sea válido, es decir, que todas las acciones cumplan 
#     con las condiciones previas y los efectos especificados y que conduzcan al estado objetivo.
# 6.- Ejecución del plan: Una vez verificado, el plan puede ser ejecutado por el agente o el sistema de planificación para llevar a cabo 
#     la secuencia de acciones necesarias para alcanzar el objetivo deseado.
#--------------- PROGRAMA ------------------------------------
from pysat.solvers import Glucose3

def translate_to_sat(actions, initial_state, goal_state):
    """
    Función para traducir el problema de planificación a una fórmula SAT.
    """
    num_actions = len(actions)
    num_variables = num_actions + 1  # Una variable por acción y una variable extra para el estado inicial

    cnf = []

    # Adición de cláusulas para el estado inicial
    for prop in initial_state:
        cnf.append([prop])

    # Adición de cláusulas para el estado objetivo
    for prop in goal_state:
        cnf.append([-(num_variables + prop)])

    # Adición de cláusulas para las acciones
    for i, action in enumerate(actions):
        preconditions, effects = action

        # Si la acción no tiene precondiciones, la agregamos como cláusula unitaria
        if not preconditions:
            cnf.append([i + 1])
            continue

        # Si la acción tiene precondiciones, agregamos una cláusula que requiere que todas las precondiciones sean verdaderas
        clause = [-prop for prop in preconditions]
        clause.append(i + 1)
        cnf.append(clause)

        # Agregamos cláusulas que garantizan que los efectos de la acción se cumplan si la acción se realiza
        for prop in effects:
            cnf.append([-prop, num_variables + prop])

    return cnf, num_variables

def satplan(actions, initial_state, goal_state):
    """
    Función principal que resuelve el problema de planificación utilizando SAT.
    """
    cnf, num_variables = translate_to_sat(actions, initial_state, goal_state)

    # Crear un solucionador SAT
    solver = Glucose3()

    # Agregar cláusulas al solucionador SAT
    for clause in cnf:
        solver.add_clause(clause)

    # Resolver el problema de satisfacibilidad
    if solver.solve():
        # Si se encuentra una solución, extraemos las acciones que satisfacen la solución
        solution = [i + 1 for i in range(num_variables) if solver.get_model()[i] > 0]
        return solution
    else:
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Definir acciones, estado inicial y estado objetivo
    actions = [([1], [2]), ([2], [3]), ([3], [4]), ([4], [])]
    initial_state = [1]
    goal_state = [4]

    # Resolver el problema de planificación
    plan = satplan(actions, initial_state, goal_state)

    # Imprimir el plan encontrado
    if plan:
        print("Plan encontrado:")
        print(plan)
    else:
        print("No se encontró ningún plan.")

#------------------------------------------------------------------------
# 1.- translate_to_sat: Esta función traduce el problema de planificación a una fórmula proposicional en CNF. Recibe una lista de acciones, 
#     un estado inicial y un estado objetivo como entrada y devuelve la fórmula CNF y el número de variables.
# 2.- satplan: Esta es la función principal que resuelve el problema de planificación utilizando SAT. Primero traduce el problema a una 
#     fórmula SAT, luego crea un solucionador SAT y agrega las cláusulas correspondientes al solucionador. Luego, resuelve el problema y
#     devuelve el plan encontrado si existe.
# 3.- El ejemplo de uso al final del script define un conjunto de acciones, un estado inicial y un estado objetivo, y luego llama a la función 
#     satplan para resolver el problema de planificación. Finalmente, imprime el plan encontrado, si existe.
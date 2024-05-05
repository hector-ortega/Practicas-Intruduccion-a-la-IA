#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# ¿Cómo funciona un algoritmo de Espacio de Estados?
# Los algoritmos que trabajan con espacios de estados suelen estar diseñados para explorar sistemáticamente todas las posibles configuraciones
# del sistema para alcanzar un objetivo específico. Aquí hay algunos conceptos clave sobre cómo funcionan estos algoritmos:

# 1.- Representación del espacio de estados: El espacio de estados se representa generalmente como un grafo o una estructura de datos similar, 
#     donde los nodos representan los estados y las aristas representan las transiciones entre estados.
# 2.- Exploración del espacio de estados: Los algoritmos exploran el espacio de estados de manera sistemática, siguiendo diferentes estrategias de búsqueda 
#     como búsqueda en anchura, búsqueda en profundidad, búsqueda de costo uniforme, entre otras. Estas estrategias determinan el orden en que se exploran 
#     los estados y pueden afectar la eficiencia y completitud del algoritmo.
# 3.- Selección de acciones: En cada estado, el algoritmo selecciona las acciones posibles y evalúa su impacto en el estado siguiente. 
#     Esto puede implicar la aplicación de heurísticas para priorizar ciertas acciones sobre otras, dependiendo del objetivo del problema.
# 4.- Criterio de parada: El algoritmo termina cuando se alcanza un estado objetivo o cuando se agota el espacio de búsqueda sin encontrar una solución. 
#     Es importante tener en cuenta que algunos problemas pueden tener soluciones infinitas o no tener solución en absoluto.
#--------------- PROGRAMA ------------------------------------
from collections import deque

class StateSpace:
    def __init__(self, graph):
        self.graph = graph
    
    def bfs(self, start, goal):
        # Inicializamos la cola para almacenar los estados a visitar
        queue = deque([(start, [])])
        visited = set()  # Conjunto para almacenar los estados visitados
        
        while queue:
            current_state, path = queue.popleft()  # Sacamos el primer estado de la cola
            
            # Si el estado actual es el estado objetivo, devolvemos el camino
            if current_state == goal:
                return path + [current_state]
            
            # Marcamos el estado actual como visitado
            visited.add(current_state)
            
            # Generamos los sucesores del estado actual
            successors = self.graph[current_state]
            
            # Añadimos los sucesores a la cola si no han sido visitados
            for successor in successors:
                if successor not in visited:
                    queue.append((successor, path + [current_state]))
        
        # Si no se encuentra una solución, devolvemos None
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos el grafo que representa el espacio de estados (laberinto)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }

    # Creamos el espacio de estados
    state_space = StateSpace(graph)
    
    # Definimos el punto de inicio y el objetivo
    start = 'A'
    goal = 'G'
    
    # Realizamos la búsqueda en anchura
    solution = state_space.bfs(start, goal)
    
    # Imprimimos la solución
    if solution:
        print("El camino encontrado es:", solution)
    else:
        print("No se encontró solución.")

#---------------------------------------------------------------
# Este código define una clase StateSpace que representa el espacio de estados y contiene un método bfs() que realiza la búsqueda en anchura. 
# Luego, creamos un ejemplo de un laberinto representado como un grafo y encontramos el camino más corto desde el punto de inicio hasta la
# salida utilizando el algoritmo de búsqueda en anchura. Finalmente, imprimimos la solución encontrada.
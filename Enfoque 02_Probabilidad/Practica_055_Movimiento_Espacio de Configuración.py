#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.
#-----------------TEORIA----------------------------------------
# El algoritmo de Movimiento en el Espacio de Configuración (C-Space) es una técnica utilizada en robótica para planificar el movimiento de un
# robot desde un punto inicial a un punto objetivo en un entorno con obstáculos. La idea principal es representar todas las posibles configuraciones
# del robot, es decir, todas las posiciones y orientaciones posibles, y luego encontrar una ruta segura que evite colisiones con los obstáculos.

# El proceso general del algoritmo de Movimiento en el Espacio de Configuración implica los siguientes pasos:

# 1.- Representación del Espacio de Configuración: Se define un espacio de configuración que describe todas las posibles posiciones y orientaciones
#     del robot en el entorno. Esto puede ser un espacio bidimensional (2D) para movimientos en un plano o un espacio tridimensional (3D) para movimientos 
#     en el espacio tridimensional.
# 2.- Definición de Obstáculos: Se identifican y se representan los obstáculos en el espacio de configuración. Estos obstáculos pueden ser paredes, 
#     objetos o cualquier otra entidad que pueda bloquear el movimiento del robot.
# 3.- Generación de Rutas: Se utiliza un algoritmo de planificación de ruta, como A* (A estrella), Dijkstra o RRT (Árbol de Búsqueda Aleatoria), 
#     para encontrar una ruta segura y óptima desde el punto inicial del robot hasta el punto objetivo. Este algoritmo evalúa las posibles configuraciones
#     del robot y busca la ruta que minimice el costo total, que puede ser una combinación de la distancia recorrida y cualquier otra métrica relevante.
# 4.- Validación de la Ruta: Se verifica que la ruta generada no colisione con ningún obstáculo en el espacio de configuración. Si la ruta pasa a través de un 
#     obstáculo, se ajusta o se genera una nueva ruta que evite la colisión.
# 5.- Ejecución del Movimiento: Una vez que se ha encontrado una ruta válida, el robot sigue la ruta planificada, moviéndose desde el punto inicial al punto
#     objetivo mientras evita los obstáculos en el espacio de configuración.
#--------------- PROGRAMA --------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from queue import PriorityQueue

# Definir la clase Nodo para representar cada punto en el espacio de configuración
class Node:
    def __init__(self, x, y, cost, parent=None):
        self.x = x  # Coordenada x del nodo
        self.y = y  # Coordenada y del nodo
        self.cost = cost  # Costo acumulado para llegar a este nodo
        self.parent = parent  # Nodo padre en el camino hacia este nodo
    
    def __lt__(self, other):
        return self.cost < other.cost

# Función de distancia euclidiana entre dos puntos
def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Función de generación de vecinos para un nodo dado
def get_neighbors(node, obstacle_map):
    neighbors = []
    # Definir movimientos posibles: arriba, abajo, izquierda, derecha
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in movements:
        x_new, y_new = node.x + dx, node.y + dy
        # Verificar si el vecino está dentro del mapa y no está bloqueado por un obstáculo
        if 0 <= x_new < obstacle_map.shape[0] and 0 <= y_new < obstacle_map.shape[1] and not obstacle_map[x_new, y_new]:
            neighbors.append(Node(x_new, y_new, 0, node))
    return neighbors

# Función para encontrar la ruta óptima utilizando el algoritmo A*
def find_path(start, goal, obstacle_map):
    # Inicializar la cola de prioridad para almacenar los nodos abiertos
    open_set = PriorityQueue()
    open_set.put(start)
    # Inicializar un diccionario para almacenar el costo acumulado de llegar a cada nodo
    cost_so_far = {start: 0}
    
    while not open_set.empty():
        # Obtener el nodo con el menor costo acumulado de la cola de prioridad
        current = open_set.get()
        # Verificar si se ha alcanzado el objetivo
        if current.x == goal.x and current.y == goal.y:
            # Reconstruir el camino óptimo desde el nodo objetivo hasta el nodo inicial
            path = []
            while current is not None:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]  # Invertir el camino para obtener el camino desde el inicio hasta el objetivo
        
        # Obtener los vecinos del nodo actual
        neighbors = get_neighbors(current, obstacle_map)
        for neighbor in neighbors:
            # Calcular el nuevo costo acumulado para llegar al vecino desde el nodo actual
            new_cost = cost_so_far[current] + 1  # Costo uniforme de movimiento
            # Si el vecino aún no se ha visitado o el nuevo costo es menor que el costo anterior
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                # Calcular la prioridad del vecino (costo acumulado + distancia heurística al objetivo)
                priority = new_cost + euclidean_distance(neighbor.x, neighbor.y, goal.x, goal.y)
                neighbor.cost = priority
                neighbor.parent = current
                open_set.put(neighbor)  # Agregar el vecino a la cola de prioridad
    
    return None  # No se encontró un camino válido

# Definir el tamaño del mapa y los obstáculos
map_size = (10, 10)
obstacle_map = np.zeros(map_size, dtype=bool)
obstacle_map[3:7, 4] = True
obstacle_map[4, 1:8] = True

# Definir el punto inicial y el punto objetivo
start_node = Node(1, 1, 0)
goal_node = Node(8, 8, 0)

# Encontrar la ruta óptima
path = find_path(start_node, goal_node, obstacle_map)

# Visualizar el mapa y la ruta encontrada
plt.figure(figsize=(8, 6))
plt.imshow(obstacle_map.T, cmap='binary', origin='lower')
plt.plot(start_node.x, start_node.y, 'go', markersize=10, label='Inicio')
plt.plot(goal_node.x, goal_node.y, 'ro', markersize=10, label='Objetivo')
if path:
    path_x, path_y = zip(*path)
    plt.plot(path_x, path_y, 'b-', linewidth=2, label='Ruta Óptima')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Espacio de Configuración y Ruta Óptima')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
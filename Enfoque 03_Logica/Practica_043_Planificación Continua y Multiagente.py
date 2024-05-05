#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Planificación Continua y Multiagente es un campo de la inteligencia artificial que se encarga de planificar las acciones de múltiples
# agentes en un entorno compartido, donde estos agentes pueden tener objetivos conflictivos y deben coordinarse para evitar colisiones
# y lograr sus metas de manera eficiente. Este enfoque es útil en diversos escenarios, como la coordinación de robots móviles, la gestión 
# de tráfico aéreo, la logística de almacenes, entre otros.

# Los algoritmos de Planificación Continua y Multiagente buscan encontrar una secuencia de acciones para cada agente, respetando las
# restricciones del entorno y evitando conflictos entre los agentes. Estos algoritmos a menudo se basan en la búsqueda heurística, 
# como el algoritmo A*, y en técnicas de búsqueda de conflictos, donde se identifican y resuelven las situaciones en las que los agentes
# podrían colisionar entre sí.

# El algoritmo MAPFM (Multi-Agent Path Finding with Conflict-Based Search) es un ejemplo de un algoritmo utilizado en Planificación Continua
# y Multiagente. Este algoritmo combina la búsqueda heurística con la resolución de conflictos para encontrar caminos para múltiples 
# agentes en un entorno compartido. Utiliza una estrategia de búsqueda por adelantado para encontrar caminos óptimos para cada agente,
# evitando colisiones y minimizando el tiempo total de planificación.
#--------------- PROGRAMA ------------------------------------
import networkx as nx
import heapq

class MAPFM:
    def __init__(self, graph, agents):
        """
        Constructor de la clase MAPFM.

        graph: grafo que representa el entorno
        agents: lista de agentes con sus respectivas posiciones de inicio y objetivo
        """
        self.graph = graph
        self.agents = agents

    def find_path(self):
        """
        Encuentra el camino para cada agente para llegar a su objetivo
        sin colisionar con otros agentes.
        """
        paths = {}  # Almacena los caminos encontrados para cada agente

        for agent in self.agents:  # Itera sobre cada agente
            start, goal = agent  # Obtiene la posición inicial y objetivo del agente
            path = self.a_star(start, goal)  # Encuentra el camino usando A* para el agente
            paths[agent] = path  # Almacena el camino encontrado

            if not path:  # Si no se puede encontrar un camino para el agente
                return None

            self.update_graph(path)  # Actualiza el grafo para evitar colisiones con otros agentes

        return paths  # Devuelve los caminos encontrados para todos los agentes

    def a_star(self, start, goal):
        """
        Encuentra el camino más corto desde el punto de inicio hasta el objetivo utilizando el algoritmo A*.

        start: punto de inicio
        goal: punto de destino
        """
        frontier = [(0, start)]  # Cola de prioridad para almacenar los nodos por explorar
        came_from = {}  # Diccionario para almacenar el camino desde el inicio
        cost_so_far = {start: 0}  # Diccionario para almacenar el costo acumulado desde el inicio

        while frontier:
            current_cost, current_node = heapq.heappop(frontier)  # Obtener el nodo actual de la cola de prioridad
            
            if current_node == goal:  # Si el nodo actual es el destino, se ha encontrado la ruta
                break

            for next_node in self.graph.neighbors(current_node):  # Iterar sobre los nodos vecinos del nodo actual
                new_cost = current_cost + self.graph.cost(current_node, next_node)  # Calcular el nuevo costo desde el inicio
                
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:  # Si se encuentra un camino más corto hacia el siguiente nodo
                    cost_so_far[next_node] = new_cost  # Actualizar el costo acumulado
                    priority = new_cost + self.heuristic(goal, next_node)  # Calcular la prioridad (costo + heurística)
                    heapq.heappush(frontier, (priority, next_node))  # Agregar el nodo a la cola de prioridad
                    came_from[next_node] = current_node  # Registrar el camino desde el inicio hacia el nodo actual
        
        path = self.reconstruct_path(start, goal, came_from)  # Reconstruir el camino desde el inicio hasta el destino
        return path

    def heuristic(self, goal, next_node):
        """
        Heurística para estimar el costo restante desde un nodo hasta el objetivo.

        goal: punto de destino
        next_node: nodo actual
        """
        # En este ejemplo, se utiliza la distancia euclidiana como heurística
        return self.graph.distance(goal, next_node)

    def reconstruct_path(self, start, goal, came_from):
        """
        Reconstruir el camino desde el inicio hasta el destino.

        start: punto de inicio
        goal: punto de destino
        came_from: diccionario que contiene el camino desde el inicio
        """
        current_node = goal
        path = []

        while current_node != start:  # Recorrer el camino desde el destino hasta el inicio
            path.append(current_node)
            current_node = came_from[current_node]

        path.append(start)
        path.reverse()
        return path

    def update_graph(self, path):
        """
        Actualiza el grafo para evitar colisiones con otros agentes.

        path: camino encontrado para un agente
        """
        for i in range(len(path) - 1):  # Itera sobre las aristas del camino
            node1, node2 = path[i], path[i + 1]
            self.graph.remove_edge(node1, node2)  # Remueve la arista entre los nodos

# Definición de la clase Graph
class Graph:
    def __init__(self):
        """
        Constructor de la clase Graph.
        """
        self.graph = nx.Graph()

    def add_edge(self, node1, node2, cost):
        """
        Agregar una arista al grafo.

        node1: nodo inicial
        node2: nodo final
        cost: costo de la arista
        """
        self.graph.add_edge(node1, node2, weight=cost)

    def remove_edge(self, node1, node2):
        """
        Remover una arista del grafo.

        node1: nodo inicial
        node2: nodo final
        """
        self.graph.remove_edge(node1, node2)

    def neighbors(self, node):
        """
        Obtener los nodos vecinos de un nodo dado.

        node: nodo del que se desean obtener los vecinos
        """
        return list(self.graph.neighbors(node))

    def cost(self, node1, node2):
        """
        Obtener el costo de la arista entre dos nodos.

        node1: nodo inicial
        node2: nodo final
        """
        return self.graph[node1][node2]['weight']

    def distance(self, node1, node2):
        """
        Calcular la distancia euclidiana entre dos nodos.

        node1: primer nodo
        node2: segundo nodo
        """
        x1, y1 = node1
        x2, y2 = node2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Ejemplo de uso
graph = Graph()
graph.add_edge((0, 0), (1, 0), 1)
graph.add_edge((1, 0), (1, 1), 1)
graph.add_edge((1, 1), (2, 1), 1)

agents = [((0, 0), (2, 1)), ((1, 0), (0, 0))]  # Dos agentes con posiciones de inicio y objetivo

mapfm = MAPFM(graph, agents)
paths = mapfm.find_path()

if paths:
    print("Caminos encontrados:")
    for agent, path in paths.items():
        print(f"Agente {agent}: {path}")
else:
    print("No se puede encontrar una solución para los agentes.")
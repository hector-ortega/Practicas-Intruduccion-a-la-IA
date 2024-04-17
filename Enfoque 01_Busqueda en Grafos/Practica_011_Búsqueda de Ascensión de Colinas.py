#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

#--------------- PROGRAMA ------------------------------------
import networkx as nx

def hill_climbing(graph, start_node, goal_node):
    current_node = start_node
    while current_node != goal_node:
        neighbors = list(graph.neighbord(current_node))
        best_neighbor = max(neighbors, key = lambda node: graph.nodes[node]['value'])
        if graph.nodes[best_neighbor]['value'] > graph.nodes[current_node]['value']:
            current_node = best_neighbor
        else:
            break
    return current_node

G = nx.Graph()
G.add_node(0, value = 5)
G.add_node(1, value = 8)
G.add_node(2, value = 3)
G.add_node(3, value = 7)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)

start_node = 0
goal_node = 3

solution = hill_climbing(G, start_node, goal_node)
print("solucion encontrada: ", solution)
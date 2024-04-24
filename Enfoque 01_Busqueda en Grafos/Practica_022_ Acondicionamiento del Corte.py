#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Acondicionamiento del Corte (también conocido como "Corte Mínimo") es utilizado en teoría de grafos y optimización 
# combinatoria para encontrar y eliminar cortes mínimos en un grafo. Un corte mínimo en un grafo es un conjunto de arcos cuya eliminación 
# divide el grafo en dos componentes disjuntas, donde una componente contiene el nodo de origen y la otra componente contiene el nodo de destino, 
# con la menor cantidad posible de arcos cruzando entre ellas.
# #--------------- PROGRAMA ------------------------------------
def cut_conditioning(graph, source, sink):
    residual_graph = graph.copy()  # Copiar el grafo original para trabajar con él
    while True:  # Bucle principal para aplicar el acondicionamiento del corte
        cut = find_min_cut(residual_graph, source, sink)  # Encontrar un corte mínimo en el grafo residual
        if cut is None:  # Si no se encuentra ningún corte mínimo, salir del bucle
            break
        augment_flow(residual_graph, cut)  # Aumentar el flujo en el corte encontrado
    return residual_graph  # Retornar el grafo residual modificado después del acondicionamiento del corte

def find_min_cut(graph, source, sink):
    visited = set()  # Conjunto para llevar un registro de los nodos visitados durante la búsqueda de corte
    queue = [source]  # Cola para realizar la búsqueda en anchura desde el nodo fuente
    while queue:  # Bucle mientras la cola no esté vacía
        node = queue.pop(0)  # Obtener el primer nodo de la cola
        visited.add(node)  # Marcar el nodo como visitado
        for neighbor, capacity in graph[node].items():  # Iterar sobre los vecinos del nodo y sus capacidades
            if neighbor not in visited and capacity > 0:  # Si el vecino no ha sido visitado y tiene capacidad positiva
                queue.append(neighbor)  # Agregar el vecino a la cola para visitarlo
    if sink in visited:  # Si el nodo sumidero está en el conjunto de nodos visitados
        return None  # No se encuentra ningún corte mínimo, retornar None
    cut = set()  # Conjunto para almacenar los nodos que forman el corte mínimo
    for node in visited:  # Iterar sobre los nodos visitados durante la búsqueda de corte
        cut.add(node)  # Agregar el nodo al corte
        for neighbor in graph[node]:  # Iterar sobre los vecinos del nodo en el grafo original
            if neighbor not in visited:  # Si el vecino no fue visitado durante la búsqueda de corte
                cut.add(neighbor)  # Agregar el vecino al corte
    return cut  # Retornar el corte mínimo encontrado

def augment_flow(graph, cut):
    for node in cut:  # Iterar sobre los nodos en el corte
        for neighbor in graph[node]:  # Iterar sobre los vecinos de cada nodo en el corte
            if neighbor not in cut:  # Si el vecino no está en el corte
                graph[node][neighbor] = 0  # Reducir la capacidad entre el nodo y el vecino a cero


graph = {
    'A': {'B': 3, 'C': 4},
    'B': {'A': 3, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_node = 'A'
sink_node = 'D'

residual_graph = cut_conditioning(graph, source_node, sink_node)
print("Grafo residual después del acondicionamiento del corte:")
print(residual_graph)
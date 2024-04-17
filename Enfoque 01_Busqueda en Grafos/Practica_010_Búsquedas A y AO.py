#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Búsqueda Informada A* (A-Star) es un algoritmo de búsqueda informada que combina las características de la búsqueda en anchura y la búsqueda en profundidad,
# utilizando una función heurística para determinar qué nodo explorar a continuación. A* es ampliamente utilizado en problemas de búsqueda de caminos en grafos, 
# como la planificación de rutas, los videojuegos y la robótica.

# El algoritmo A* evalúa cada nodo en función de dos valores: el costo real para llegar al nodo desde el nodo inicial (denominado g(n)), y una estimación 
# del costo restante para llegar al nodo objetivo desde el nodo actual (denominado h(n)). El algoritmo selecciona el nodo con el valor f(n) = g(n) + h(n) 
# más bajo para expandir, lo que significa que prioriza los nodos que tienen un costo total más bajo estimado.

# El algoritmo A* es óptimo y completo bajo ciertas condiciones, siempre que la función heurística sea admisible (nunca sobreestima el costo restante) y
# consistente (satisface la desigualdad de triangulación para cualquier par de nodos y sus respectivos vecinos).
#--------------- PROGRAMA ------------------------------------

import heapq # Proporciona operaciones de cola de prioridad.

def astar(grafo, comienzo, objetivo, hueristica):
    visitado = set() # Se setea el conjunto de nodos visitados
    cola = [] # Se declara la cola para almacenra los nodos por visitar
    heapq.heappush(cola, (0 + hueristica(comienzo,objetivo), 0, comienzo, []))# Se Inicializa la cola de prioridad con el nodo de inicio y su costo estimado al objetivo

    while cola: # Se inicia un bucle que se ejecutará mientras la cola de prioridad no esté vacia
        f, g, actual, camino = heapq.heappop(cola) # Extrae el nondo actual, su costo real, su costo estimado hasta el objetivo y el camino hasta el nodod actual de la cola de prioridad
        if actual == objetivo: # comprueba si el nodo actual es el objetivo.
            print("Camino encontrado: ", camino + [actual]) # si se cumple la condiciona, se devuelve el camino hacia el
            return camino + [actual]
        
        # si el nodo actual no ha sido visitado, se marca como visistado y se recorren sus
        #Vecinos, agregandolos a la cola de prioridad segun su valor f(n) = g(n) + h(n), donde g(n) es el
        # Costo real hasta el nodo actual y h(n) es la estimacion del costo restante hasta el objetivo
        if actual not in visitado: 
            visitado.add(actual)

            for vecino, costo in grafo[actual].items():
                if vecino not in visitado:
                    heapq.heappush(cola, (g + costo + hueristica(vecino, objetivo), g + costo, vecino, camino + [actual]))
    # si no se encuentra un camino, imprime un mensaje indicando que no se encontró un camino desde el nodo inicial hasta el nodo objetivo
    print (f"No se encontro un camino desde {comienzo} hacia {objetivo}")
    return None

# La funcion de distancia calcula la distancia entre los dos nodos en una cuadricula
def distancia(nodo, objetivo):
    x1, y1 = nodo
    x2, y2 = objetivo
    return abs (x1 - x2) + abs(y1 - y2)

grafo = {
    (0,0): {(0,1): 1, (1,0): 1},
    (0,1): {(0,0): 1, (0,2): 1},
    (0,2): {(0,1): 1, (0,2): 1},
    (1,0): {(0,0): 1, (1,1): 1},
    (1,1): {(1,0): 1, (1,2): 1},
    (1,2): {(0,2): 1, (1,1): 1}
}

nodo_inicial = (0,0)
nodo_objetivo = (1,2)

astar(grafo, nodo_inicial, nodo_objetivo, distancia)
#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------

# Una heurística es una técnica o estrategia que se utiliza para resolver problemas de manera aproximada cuando 
# no es posible encontrar una solución óptima o cuando encontrarla llevaría demasiado tiempo computacional. 
# En otras palabras, una heurística es una regla general o guía que puede ayudar a tomar decisiones o encontrar soluciones en situaciones complejas.


# La Búsqueda Informada Heurística es un enfoque de búsqueda que utiliza información adicional sobre el problema en forma de una función heurística
# para guiar la exploración del espacio de búsqueda hacia la solución más prometedora. Esta función heurística proporciona una estimación del costo desde 
# el estado actual hasta el objetivo, lo que permite priorizar las acciones que conducen a estados más prometedores y potencialmente reducir el tiempo de búsqueda.

# La búsqueda informada heurística es útil cuando se dispone de información adicional sobre el problema en forma de una función heurística bien definida, 
# lo que puede conducir a una búsqueda más eficiente y una solución más rápida.
#--------------- PROGRAMA ------------------------------------

import heapq # este modulo proporciona operaciones de cola de prioridad.

def astar (grafo, comienzo, objetivo, huueristica):
    visitado = set() # Se crea conjunto para almacenar los nodos visitados.
    cola = [] # Se crea una cola de prioridad para almacenar los nodos por visitar
    heapq.heappush(cola, (0, comienzo, [comienzo])) #inicializa la cola de prioridad con el nodo de inicio y un costo inicial de 0

    while cola: # Se ejecuta el bucle siempre y cuando la cola de prioridad no esté vacia
        costo, actual, camino = heapq.heappop(cola) # Extrae del nodo actual el costo acumulado hasta el y el camino recorrido desde la cola de prioridad

        if actual not in visitado: #comprueba si el nodo actual no ha sido visitado.
            visitado.add(actual) #MArca el nodo como visitado
            print (f"Se visitó a: {visitado}")

            if actual == objetivo: #Comprueba si el nodo actual es el nodo objetido, Si es asi, devuelve el camino hacia el
                print ("camino encontrado: ", camino)
                return camino

            #Recorre los vecinos del nodo actual y calcula el costo total para llegar a cada vecino.
            #El costo total se calcula sumando el costo acumulado, el peso de la arista y la estimacion hueristica del costa
            #restanta hasta el objetivo
            for vecino, peso in grafo[actual].items():
                if vecino not in visitado:
                    costo_total = costo + peso + huueristica(vecino, objetivo)
                    print(f"Costo: {costo}, peso: {peso}, hueristica {huueristica}, costo total {costo_total}")
                    heapq.heappush(cola, (costo_total, vecino, camino + [vecino])) # Agrega alos vecinos a la cola de prioridad.

    #Si no se encuentra un camino, imprime un mensaje indicando que no se encontro un camino desde el nodo inicial hasta el nodo objetivo
    print(f"no se encontro un camino desde {comienzo}, hasta {objetivo}")
    return None

def distancia(nodo, objetivo): #Esta funcion calcula la distancia entre dos nodos en una cuadricula
    x1, y1 = nodo
    x2, y2 = objetivo

    return abs(x1 - x2) + abs(y1 - y2)

grafo = {
    (0,0): {(0,1): 1, (1,0): 1},
    (0,1): {(0,0): 1, (0,2): 1},
    (0,2): {(0,1): 1, (1,2): 1},
    (1,0): {(0,0): 1, (1,1): 1},
    (1,1): {(1,0): 1, (1,2): 1},
    (1,2): {(0,2): 1, (1,1): 1}
}    

nodo_inicial = (0,0)
nodo_objetivo = (1,2)

astar(grafo, nodo_inicial, nodo_objetivo, distancia)
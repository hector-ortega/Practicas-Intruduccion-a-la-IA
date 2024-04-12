#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Búsqueda Informada Voraz (también conocida como "Primero el Mejor" o "Greedy Best-First Search" en inglés) es un algoritmo de búsqueda
# que se utiliza para encontrar una solución aproximada en problemas de búsqueda en grafos. Este algoritmo utiliza una función heurística para
# evaluar la "bondad" de cada nodo y luego expande el nodo más prometedor en cada paso, es decir, el nodo que tiene el valor heurístico más bajo 
# según la función heurística.

# La Búsqueda Informada Voraz es útil cuando se desea encontrar una solución rápidamente, aunque no garantiza que esta solución sea óptima. 
# Por lo tanto, se utiliza en situaciones donde la optimización de tiempo es más importante que la optimización del resultado.
#--------------- PROGRAMA ------------------------------------
import heapq # Proporciona operaciones de cola de prioridad.

def primero_el_mejor(grafo, comienzo, objetivo, hueristica):
    visitado = set() # Se setea el conjunto de "visitado" para almacenar los nodos visitados
    cola = [] #Se define una lista vacia de "Cola" para almacenar los nodos a visitar
    heapq.heappush(cola, (hueristica(comienzo, objetivo), comienzo)) #inicializa la cola de prioridad con el nodo de inicio y su valor hueristico

    while cola: #Inicia un bucle que se ejecutará mientras la cola de prioridad no esté vacía.
        _, actual = heapq.heappop(cola) #Extra el nodo msas prometedor de la cola de prioridaad

        if actual == objetivo: #Comprueba si el nodo actual es el nodo objetivo. 
            print("nodo objetivo encontrado: ", actual) # Si la condicion es cumpla muestra el mensaje y devuelve verdadero
            return True
        
        if actual not in visitado: # si el nodo actual no ha sido visitado 
            visitado.add(actual) # se agrega al conjunto de visitados
            print(f"visitando nodo: {actual}") # Se imprime que nodo se acaba de vicitar

            for vecino in grafo.get(actual,[]): #Se recorren sus vecinos
                if vecino not in visitado: # Si el vecino no se ha visitado
                    heapq.heappush(cola, (hueristica(vecino, objetivo), vecino)) # Se agraga a la cola de prioridaad segun su valor hueristico

    #Si no se encuentra el camino se imprime el siguiente mensaje y retorna falso            
    print(f"no se encontró un camino desde {comienzo} hacia {objetivo}")
    return False

# Se define la funcion distancia que calcula la distancia ente dos nodos en la cuadricula
def distancia(nodo, objetivo):
    x1, y1 = nodo
    x2, y2 = objetivo

    return abs(x1 - x2) + abs (y1 - y2)

grafo = {
    (0,0): {(0,1), (1,0)},
    (0,1): {(0,0), (0,2)},
    (0,2): {(0,1), (1,2)},
    (1,0): {(0,0), (1,1)},
    (1,1): {(1,0), (1,2)},
    (1,2): {(0,2), (1,1)}
}

nodo_inicial = (0,0)
nodo_objetivo = (1,2)

primero_el_mejor(grafo, nodo_inicial, nodo_objetivo, distancia)
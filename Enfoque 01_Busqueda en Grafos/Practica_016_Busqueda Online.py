#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La "Búsqueda Online" en grafos es una técnica que se centra en explorar el grafo de manera incremental y en tiempo real, 
# sin tener una visión completa del grafo desde el principio. Este enfoque es útil cuando el grafo es demasiado grande para almacenar
# y procesar en su totalidad de una vez, o cuando los nodos y las conexiones están en constante cambio.
#--------------- PROGRAMA ------------------------------------

from collections import deque # Se importa la clase deque del modulo collection deque es una estructura de datos de cola (double-ended-queue) que permite agragar y eliminar elementos de ambos extremos 

# Se define el grafo como lista de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def busqueda_online(grafo, inicio, objetivo): # Funcion de busqueda online
    cola = deque() # Inicializar una cola para almacenar los nodos a visitar
    cola.append(inicio) # Agregar el nodo inicial a la cola
    visitados = set() #Inicializamos un conjunto para mantener registro de los nodos visitados

    while cola: #Bucle principal de busqueda
        nodo_actual = cola.popleft() # Sacar el primer nodo de la cola
        visitados.add(nodo_actual) # MArcar el nodo actual como visitado
        if nodo_actual == objetivo: # Verificar si el nodo actual es el objetivo
            return True  # Si el objetivo es alcanzado, retorna true
        for vecino in grafo[nodo_actual]: # Si no es el objetivo, expandir los nodos vecinos
            if vecino not in visitados and vecino not in cola: # Verificar si el vecino no ha sido visitado ni está en la cola
                cola.append(vecino) # Agregar el vecino a la cola 
    return False # Si no se encuentra el objetivo, retornar False

inicio = 'A'
objetivo = 'F'
resultado = busqueda_online(grafo, inicio, objetivo)
print("¿Se puede llegar desde", inicio, "a", objetivo + "?", resultado)
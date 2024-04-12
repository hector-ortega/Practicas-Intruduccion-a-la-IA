#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La Búsqueda Bidireccional es un algoritmo de búsqueda que se utiliza para encontrar el camino más corto entre un nodo de inicio y un nodo objetivo en un grafo.
# A diferencia de la búsqueda unidireccional que parte desde el nodo de inicio y explora hacia adelante, la búsqueda bidireccional parte desde el nodo de inicio 
# y el nodo objetivo simultáneamente, explorando desde ambos extremos hasta que se encuentran en algún punto intermedio. 
# Esto puede reducir significativamente el tiempo de búsqueda, especialmente en grafos grandes, ya que disminuye la cantidad de nodos que se deben explorar.

# La búsqueda bidireccional es útil cuando se conoce tanto el nodo de inicio como el nodo objetivo, y se desea encontrar el camino más corto entre ellos.
#--------------- PROGRAMA ------------------------------------

def busqueda_bidireccional(grafo, comienzo, objetivo):
    #Inicializa conjuntos para almacenar los nodos visitados desde el inicia y desde el objetivo,
    #Se agrefan los nodos de inicio y objetivos visitados inicialmente.
    visitado_inicio =  {comienzo}
    visitado_objetivo = {objetivo}

    #Inicializa colas para nodos por visitar desde el inicio y desde el objetivi¿o.
    #Se agrega el nodo de inicio a la cola desde el inicio, y el objetivo a la cola desde el objetivo
    cola_inicio = [comienzo]
    cola_objetivo = [objetivo]

    print(f"El nodo de partida es : {comienzo}")
    print(f"El objetivo es: {objetivo}")

    #Inicia un bucle que se ejecutará mientras haya nodos por visitar desde ambos extremos
    while cola_inicio and cola_objetivo:
        #expandir desde el inicio
        comienzo_actual = cola_inicio.pop(0) # Obtiene el proximo nodo a explorar desde las colas desde el inicio

        for vecino in grafo[comienzo_actual]:# Explora los vecinos de los nodos actuales y agragandolos a las colas y conjuntos de nosos visitados
            if vecino not in visitado_inicio:
                visitado_inicio.add(vecino)
                cola_inicio.append(vecino)
                print(f"cola de comienzo: {cola_inicio}")

            # Si se encuentra un nodo visitado desde el objetivo, se ha encontrado una interseccion
            if vecino in visitado_objetivo:
                print("interseccion encontrada en el nodo: ", vecino)
                return
            
        
        #Expandir desde el objetivo 
        objetivo_actual = cola_objetivo.pop(0) # Obtiene el proximo nodo a explorar desde la cola desde el objetivo
        
        for vecino in grafo[objetivo_actual]: #Explora los vecinos de los nodos actuales y agragandolos a las colas y conjuntos de nosos visitados
            if vecino not in visitado_objetivo:
                visitado_objetivo.add(vecino)
                cola_objetivo.append(vecino)
                print (f"Cola de visitados desde el objetivo: {cola_objetivo}")
            
            # Si se encuentra uun nodo visitado desde el inicio, se ha encontrado una interseccion 
            if vecino in visitado_inicio:
                print("Interseccion encontrada: ", vecino)
                return
            
    print("No se encontró una ruta entre el nodo inicial y el nodo objetivo.")

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C', 'K'],
    'H': ['D', 'L'],
    'I': ['E', 'M'],
    'J': ['F'],
    'K': ['G'],
    'L': ['H'],
    'M': ['I', 'N'],
    'N': ['M', 'O'],
    'O': ['N']
}

nodo_inicio = 'A'
nodo_objetivo = 'H'

busqueda_bidireccional(grafo, nodo_inicio, nodo_objetivo)
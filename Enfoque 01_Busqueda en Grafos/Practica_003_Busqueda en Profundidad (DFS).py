#Hecho por:

#Hector Alejandro Ortega Garcia  Grupo: 6E2  Registro: 21310248

#------------------------EXPLICACION------------------------------------
#Búsqueda en Profundidad (Depth-First Search, DFS)
# La Búsqueda en Profundidad (Depth-First Search, DFS) es un algoritmo utilizado para recorrer o buscar estructuras de datos como árboles o grafos. A continuación, te explico su utilidad y algunas aplicaciones:

# Recorrido de Grafos:
# El DFS permite visitar todos los nodos de un grafo o árbol de manera ordenada, pero no uniforme.
# Se inicia desde un nodo arbitrario (generalmente la raíz) y explora lo más profundo posible a lo largo de cada rama antes de retroceder.
# Aplicaciones:
# Encontrar Componentes Conectados:
# El DFS ayuda a encontrar todos los nodos conectados a un nodo dado.
# Por ejemplo, en redes sociales, se puede usar para identificar grupos de amigos o comunidades.
# Ordenamiento Topológico:
# En grafos dirigidos acíclicos (DAG), el DFS proporciona un ordenamiento lineal de los nodos.
# Útil en planificación de proyectos, compilación de código y resolución de dependencias.
# Resolución de Laberintos:
# El DFS se utiliza para encontrar caminos en laberintos o mapas.
# Búsqueda de Puentes y Articulaciones:
# Ayuda a identificar conexiones críticas en redes.
# Análisis de Componentes Fuertemente Conectados:
# En grafos dirigidos, el DFS encuentra componentes fuertemente conectados.
# Implementación:
# Puede ser recursivo o iterativo.
# La versión recursiva es simple pero puede causar desbordamiento de pila en grafos grandes.
# La versión iterativa utiliza una pila o una cola para evitar el desbordamiento de pila.
# En resumen, el DFS es ampliamente utilizado en problemas de búsqueda, análisis de redes, inteligencia artificial y más. Su flexibilidad y aplicabilidad lo convierten en una herramienta poderosa en ciencias de la computación y matemáticas


#-----------------------PROGRAMA--------------------------------------------------
#Primero se crea nuestro grafo (diccionario) en donde se encontraran nuestros 
#nodos y sus respectivos vertices
grafo = {
   'A': ['B', 'C'],
   'B': ['D', 'E'],
   'C': ['F', 'A'],
   'D': ['H', 'F'],
   'E': [],
   'F': [],
   'H': []

}

def dfs(grafo, nodo, visitado): # Se crea la funcion que se encargará de hacer  la busqueda en profundidad
    visitado.add(nodo) #Se agrega el nodo actual en el conjunto de visitado
    print(f"Visitando al nodo: {nodo}") #Se imprime en pantalla el nodo en el que se encuentra

    for vecino in grafo[nodo]: #Accedemos a los "vecinos" de cada nodo, que son los otros nodos que se interconectan mediante vetices con el nodo actual
        if vecino not in visitado: #Si el vecino del nodo en cuestion no se encuentra en nuestro conjunto de nodos se adjunta al mismo
            dfs(grafo, vecino, visitado)

nodo_inicio = "A" # Es el nodo en el que vamos a empezar la busqueda de las relaciones existentes entre los nodos de nuestro grafo
visitados = set()
print(f"Recorrido en profundidad desde el nodo: {nodo_inicio}")
dfs(grafo, nodo_inicio, visitados)
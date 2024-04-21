#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de backtracking es una técnica de búsqueda exhaustiva que intenta construir soluciones de manera incremental, 
# retrocediendo cuando se alcanza una solución parcial inválida. 
#--------------- PROGRAMA ------------------------------------
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def backtracking(grafo, inicio, objetivo, visitados = []): # Funcion de busqueda de vuelta atrás
    visitados.append(inicio) # Agregar el nodo actual a la lista de visitados
    
    if inicio == objetivo: # Verificar si el nodo actual es el objetivo
        return True, visitados
    
    for vecino in grafo[inicio]: # Recorrer los vecinos del nodo actual
        if vecino not in visitados: # si el vecino no ha sido visitado
            encontrado, camino = backtracking(grafo, vecino, objetivo, visitados.copy()) # Realizar busqueda de vuelta atrás desde el vecino
            if encontrado: # Si se encuentra el objetivo, retornar el caino
                return True, camino
    
    return False, visitados[:-1] # si no se encuentra el objetivo, retroceder

inicio = 'A'
objetivo = 'F'
encontrado, camino = backtracking(grafo, inicio, objetivo)
if encontrado:
    print("Se encontró un camino:", camino)
else:
    print("No se encontró ningún camino.")
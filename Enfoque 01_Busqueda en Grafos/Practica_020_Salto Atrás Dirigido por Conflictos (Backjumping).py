#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Salto Atrás Dirigido por Conflictos (Backjumping) es una técnica utilizada en la resolución de problemas de búsqueda en grafos, 
# particularmente en problemas de Satisfacción de Restricciones (CSP), para encontrar soluciones de manera eficiente al reducir el espacio de búsqueda.
#--------------- PROGRAMA ------------------------------------
# Definición del grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función de búsqueda con backjumping
def backjumping(grafo, asignacion):
    stack = []  # Pila para llevar un registro de los nodos visitados
    nodos_visitados = set()  # Conjunto para llevar un registro de los nodos visitados
    nodo_actual = 'A'  # Nodo inicial
    while True:  # Bucle infinito para continuar la búsqueda
        if nodo_actual not in nodos_visitados:  # Si el nodo actual no ha sido visitado
            asignacion[nodo_actual] = None  # Asignar None al nodo actual en la asignación (variable no asignada)
            stack.append(nodo_actual)  # Agregar el nodo actual a la pila
            nodos_visitados.add(nodo_actual)  # Agregar el nodo actual al conjunto de nodos visitados
        conflictos = encontrar_conflictos(grafo, asignacion)  # Encontrar conflictos en la asignación actual
        if not conflictos:  # Si no hay conflictos
            if len(asignacion) == len(grafo):  # Si se ha asignado a todos los nodos (solución encontrada)
                return asignacion  # Retornar la asignación
            vecinos_no_asignados = [vecino for vecino in grafo[nodo_actual] if vecino not in asignacion]
            if vecinos_no_asignados:  # Si hay vecinos no asignados
                nodo_actual = vecinos_no_asignados[0]  # Avanzar al primer vecino no asignado
            else:  # Si no hay vecinos no asignados
                if stack:  # Si la pila no está vacía
                    nodo_actual = stack.pop()  # Retroceder al último nodo en la pila
                else:  # Si la pila está vacía
                    return None  # No se encontró ninguna solución
        else:  # Si hay conflictos
            nodo_conflicto, valor_conflicto = conflictos[0]  # Obtener el primer conflicto
            if nodo_conflicto in stack:  # Si el nodo en conflicto está en la pila
                while stack and stack[-1] != nodo_conflicto:  # Retroceder hasta el nodo en conflicto en la pila
                    stack.pop()
            nodo_actual = nodo_conflicto  # Avanzar al nodo en conflicto
            asignacion[nodo_actual] = valor_conflicto  # Asignar el valor en conflicto al nodo actual

# Función para encontrar conflictos en la asignación actual
def encontrar_conflictos(grafo, asignacion):
    conflictos = []  # Lista para almacenar los conflictos
    for nodo, valor in asignacion.items():  # Iterar sobre los nodos asignados
        if valor is not None:  # Si el nodo está asignado
            for vecino in grafo[nodo]:  # Iterar sobre los vecinos del nodo
                if vecino in asignacion and asignacion[vecino] == valor:  # Si hay un conflicto
                    conflictos.append((nodo, valor))  # Agregar el conflicto a la lista
                    break  # Salir del bucle interior para evitar duplicados
    return conflictos  # Retornar la lista de conflictos

# Ejemplo de uso
asignacion_inicial = {'A': 1, 'B': 3, 'C': 3, 'D': None, 'E': 12, 'F': None}  # Asignación inicial 
solucion = backjumping(grafo, asignacion_inicial)  # Aplicar backjumping para encontrar una solución
print("Solución encontrada:", solucion)  # Imprimir la solución encontrada
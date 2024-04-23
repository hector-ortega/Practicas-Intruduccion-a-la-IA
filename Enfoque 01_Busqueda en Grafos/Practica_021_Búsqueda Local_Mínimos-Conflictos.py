#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Búsqueda Local: Mínimos-Conflictos es una técnica utilizada en problemas de Satisfacción de Restricciones (CSP)
# para encontrar una asignación de valores a un conjunto de variables que cumpla con ciertas restricciones, minimizando el número de conflictos entre ellas.

# Su propósito principal es encontrar una solución viable para un CSP, donde se busca asignar valores a un conjunto de variables 
# de manera que se satisfagan todas las restricciones. Sin embargo, en lugar de buscar exhaustivamente todas las posibles combinaciones de asignaciones,
# como lo hacen otros enfoques como la Búsqueda Exhaustiva o la Búsqueda con Retroceso, la Búsqueda Local: Mínimos-Conflictos se centra en mejorar 
# gradualmente una asignación inicial hasta que se encuentra una solución satisfactoria o se alcanza un criterio de terminación.
# #--------------- PROGRAMA ------------------------------------

import random

# Función de búsqueda local: Mínimos-Conflictos
def minimos_conflictos(grafo, max_iteraciones):
    asignacion = {}  # Inicializar una asignación vacía
    for nodo in grafo.keys():  # Para cada nodo en el grafo
        asignacion[nodo] = random.choice(list(range(1, 5)))  # Asignar un valor aleatorio al nodo
        print("Valor asignado a: ",nodo,"de", asignacion[nodo])
    for _ in range(max_iteraciones):  # Realizar un número máximo de iteraciones
        conflicto_nodo = encontrar_conflicto(grafo, asignacion)  # Encontrar un nodo en conflicto
        if not conflicto_nodo:  # Si no hay conflictos, se ha encontrado una solución
            return asignacion  # Retornar la asignación
        nodo, valor = conflicto_nodo  # Obtener el nodo y el valor en conflicto
        asignacion[nodo] = valor  # Asignar el valor que minimiza el conflicto al nodo
    return None  # Si se alcanza el número máximo de iteraciones sin encontrar una solución, retornar None

# Función para encontrar un nodo en conflicto en la asignación actual
def encontrar_conflicto(grafo, asignacion):
    for nodo, valor in asignacion.items():  # Para cada nodo y su valor en la asignación
        for vecino in grafo[nodo]:  # Para cada vecino del nodo
            if vecino in asignacion and asignacion[vecino] == valor:  # Si hay un conflicto
                return (nodo, random.choice(list(range(1, 5))))  # Retornar el nodo y un valor aleatorio que minimice el conflicto
    return None  # Si no se encuentra ningún conflicto, retornar None

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
max_iteraciones = 1000  # Número máximo de iteraciones
solucion = minimos_conflictos(grafo, max_iteraciones)  # Aplicar el algoritmo de mínimos conflictos
print("Solución encontrada:", solucion)  # Imprimir la solución encontrada
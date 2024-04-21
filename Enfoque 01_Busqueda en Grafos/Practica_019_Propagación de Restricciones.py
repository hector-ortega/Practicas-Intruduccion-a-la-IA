#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Propagación de Restricciones es una técnica utilizada en la resolución de problemas de Satisfacción de Restricciones (CSP) 
# para reducir el espacio de búsqueda mediante la propagación de información sobre las restricciones entre las variables. Su objetivo principal es identificar 
# y eliminar de manera proactiva las asignaciones inválidas, lo que ayuda a reducir el espacio de búsqueda y mejorar la eficiencia de la búsqueda de soluciones viables.
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

# Función para propagar restricciones
def propagacion_restricciones(grafo, asignacion, cola=[]):
    while cola:  # Mientras la cola no esté vacía
        nodo_actual = cola.pop(0)  # Obtener el primer nodo de la cola
        for vecino in grafo[nodo_actual]:  # Iterar sobre los vecinos del nodo actual
            if vecino not in asignacion:  # Si el vecino no está asignado
                valores_posibles = [valor for valor in range(1, 5) if valor not in asignacion.values()]  # Calcular los valores posibles para el vecino
                for valor in valores_posibles:  # Iterar sobre los valores posibles
                    if es_consistente(grafo, asignacion, vecino, valor):  # Verificar si la asignación es consistente
                        asignacion[vecino] = valor  # Asignar el valor al vecino en la asignación
                        cola.append(vecino)  # Agregar el vecino a la cola para propagación adicional

# Función para verificar si una asignación es consistente
def es_consistente(grafo, asignacion, variable, valor):
    for vecino in grafo[variable]:  # Iterar sobre los vecinos de la variable
        if vecino in asignacion and asignacion[vecino] == valor:  # Si el vecino está asignado y tiene el mismo valor
            return False  # La asignación no es consistente
    return True  # La asignación es consistente


asignacion = {'A': 1}  # Asignación inicial
cola = ['A']  # Iniciar la cola con el nodo inicial
propagacion_restricciones(grafo, asignacion, cola)  # Aplicar propagación de restricciones
print("Asignación después de la propagación de restricciones:", asignacion)  # Imprimir la asignación resultante

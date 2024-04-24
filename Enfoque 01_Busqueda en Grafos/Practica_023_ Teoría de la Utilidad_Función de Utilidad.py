#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# La "Teoría de la Utilidad" es un concepto clave en la economía y la toma de decisiones, que busca modelar y entender cómo los individuos 
# toman decisiones en situaciones donde enfrentan opciones con diferentes grados de preferencia. La "Función de Utilidad" es una herramienta fundamental en esta teoría, 
# ya que permite asignar valores numéricos a las diferentes opciones disponibles, reflejando así las preferencias del individuo.

# En el contexto de la búsqueda en grafos, la "Función de Utilidad" puede ser utilizada para evaluar y comparar diferentes caminos o soluciones. 
# Por ejemplo, en un problema de ruteo de vehículos, donde se busca encontrar la ruta óptima para entregar mercancías, la función de utilidad puede 
# considerar factores como la distancia recorrida, el tiempo de viaje, el costo de combustible, etc. La idea es asignar un valor numérico a cada camino 
# que represente su "utilidad" o "calidad", de modo que se puedan tomar decisiones informadas sobre cuál es la mejor opción.
# #--------------- PROGRAMA ------------------------------------
def utilidad_camino(grafo, camino):
    """
    Calcula la utilidad de un camino en un grafo.

    Args:
    - grafo: Diccionario que representa el grafo.
    - camino: Lista de nodos que representan el camino en el grafo.

    Returns:
    - utilidad: Valor numérico que representa la utilidad del camino.
    """
    utilidad = 0  # Inicializar la utilidad del camino

    # Iterar sobre los nodos en el camino
    for i in range(len(camino) - 1):
        nodo_actual = camino[i]
        nodo_siguiente = camino[i + 1]

        # Sumar la distancia entre nodos al valor de utilidad
        if nodo_siguiente in grafo[nodo_actual]:  # Verificar si hay una conexión entre los nodos
            utilidad += grafo[nodo_actual][nodo_siguiente]  # Sumar la distancia al valor de utilidad
        else:
            # Si no hay una conexión directa entre los nodos, asignar una penalización
            utilidad += 1000  # Penalización arbitraria por no conexión directa

    return utilidad

# Ejemplo de uso
grafo = {
    'A': {'B': 10, 'C': 15},
    'B': {'A': 10, 'C': 5, 'D': 20},
    'C': {'A': 15, 'B': 5, 'D': 10},
    'D': {'B': 20, 'C': 10}
}

camino = ['A', 'B', 'D']  # Ejemplo de camino en el grafo

utilidad = utilidad_camino(grafo, camino)
print("Utilidad del camino:", utilidad)
#--------------------------HECHO POR----------------------------
# Hector Alejandro Ortega Garcia     grupo: 6E2  Registro: 21310248.

#-----------------TEORIA----------------------------------------
# El algoritmo de Forward Checking es una técnica utilizada en la resolución de problemas de Satisfacción de Restricciones 
# (CSP, por sus siglas en inglés) para realizar una verificación anticipada de las restricciones y reducir el espacio de búsqueda.
# Este algoritmo se utiliza comúnmente en problemas donde se deben asignar valores a un conjunto de variables, sujetas a ciertas restricciones,
# con el objetivo de satisfacer todas las restricciones impuestas.
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

# Función de comprobación hacia delante
def forward_checking(grafo, asignacion, variable, valor):
    # Copiar la asignación actual
    asignacion_temporal = asignacion.copy()
    # Asignar el valor a la variable en la asignación temporal
    asignacion_temporal[variable] = valor
    
    # Iterar sobre las variables vecinas
    for vecino in grafo[variable]:
        # Si el vecino no está asignado y no hay valores posibles para asignar
        if vecino not in asignacion_temporal and len(valores_posibles(grafo, asignacion_temporal, vecino)) == 0:
            return False  # Retornar False, ya que no hay valores posibles para asignar al vecino
    return True  # Retornar True si todas las comprobaciones son satisfactorias

# Función para obtener los valores posibles para una variable
def valores_posibles(grafo, asignacion, variable):
    # Suponemos valores del 1 al 4
    valores = [1, 2, 3, 4]
    # Iterar sobre los vecinos de la variable
    for vecino in grafo[variable]:
        # Si el vecino está asignado, remover su valor de los valores posibles
        if vecino in asignacion:
            valor_vecino = asignacion[vecino]
            if valor_vecino in valores:
                valores.remove(valor_vecino)
    return valores


asignacion = {'A': 1}  # Asignación inicial
variable = 'B'
valor = 2
resultado = forward_checking(grafo, asignacion, variable, valor)
print("¿Es posible asignar el valor", valor, "a la variable", variable, "dada la asignación actual?", resultado)
